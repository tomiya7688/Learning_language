# ウィンドウの管理と弾1発ごとの処理を混ぜると、ゲーム全体の進む順序を探しにくくなります。
# Game（ゲーム）へ画面と進行をまとめ、自機と弾の管理はbattle.pyのBattle（戦闘）へ任せます。
# pygameは、ウィンドウを作り、キーや閉じる操作を調べ、描いた画面を表示する道具です。
import pygame
# 同じsrcフォルダのsettings.pyから、幅WIDTH=640、高さHEIGHT=480、更新回数の上限FPS=60を読み込みます。
import settings
# 同じsrcフォルダのbattle.pyから、自機1機と撃った弾の一覧を持つBattleを読み込みます。
from battle import Battle

# クラスは情報と操作をまとめた定義です。Gameはゲーム画面と、その画面を動かす操作をまとめます。
class Game:
    # __init__はmain.pyがGame()を作るときにPythonが実行する準備です。
    # selfは今作るゲーム全体。self.screenのように、そのゲームの情報を持たせます。
    def __init__(self):
        # screen（画面）に、幅640・高さ480ピクセルのウィンドウへ描くための場所を保存します。
        # ピクセルはゲーム画面の位置や大きさを数える単位。幅と高さはsettings.pyの値を使います。
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # captionはウィンドウのタイトル。ゲーム画面のタイトルを「弾を発射する」にします。
        pygame.display.set_caption('弾を発射する')

        # clock（時計）は更新の間隔を測る道具。runの最後でtickを使い、更新を速くしすぎないよう待ちます。
        self.clock = pygame.time.Clock()
        # running（動作中）がTrue（続ける）ならrunが更新を繰り返し、False（終える）なら繰り返しを終えます。
        self.running = True

        # start_game（ゲームを始める）で、今回の戦闘に使う自機1機と空の弾一覧を用意します。
        self.start_game()

    # ウィンドウの準備と戦闘の作成を分けると、start_game（ゲームを始める）から戦闘の作成場所を探せます。
    def start_game(self):
        # Battle（戦闘）が、自機や弾など、この章の戦闘で使う情報を作ります。
        # GameはBattle()で作った戦闘をself.battleへ保存し、後の更新と描画で同じ戦闘を使います。
        self.battle = Battle()

    # 1回の画面更新の順序をrun（動かす）へまとめると、操作確認から表示までの順を1か所で追えます。
    def run(self):
        # whileは条件が成り立つ間の繰り返し。Game.runはself.runningがTrueの間、画面更新を続けます。
        while self.running:
            # Game.runがhandle_events（操作を確認する）を実行し、届いたキーや閉じる操作の知らせを確認します。
            self.handle_events()
            # notはTrue/Falseを逆にする指定。self.runningがFalseならGame.runは次のbreakを実行します。
            if not self.running:
                # Game.runが画面更新のwhileを終えます。終了を確認した回の更新・描画・表示・待ち時間は省きます。
                break

            # Game.runが今の戦闘self.battleのupdate（状態を更新する）へ、自機と弾の移動、画面外の弾の削除を依頼します。
            self.battle.update()

            # Game.runが今の戦闘self.battleのdraw（描く）へ、描画先self.screenに背景・自機・残っている弾を描くよう依頼します。
            self.battle.draw(self.screen)

            # pygame.display.flip()が、self.screenへ描画済みの背景・自機・残っている弾をゲームのウィンドウへ表示します。
            pygame.display.flip()
            # Game.runがself.clock.tickで、更新回数の上限settings.FPSに合わせ、必要な時間だけ待ちます。
            # settings.pyのFPSはframes per second（毎秒の更新回数）。処理が遅い場合、実際の更新回数は上限より少なくなります。
            self.clock.tick(settings.FPS)

    # 操作ごとの分岐をhandle_events（操作を確認する）へ分けると、runから画面更新の順序を追えます。
    def handle_events(self):
        # Game.handle_eventsが、pygame.event.get()で取り出した操作の知らせの一覧をforで順番に確認します。
        # event（操作の知らせ）は、forが今回確認する1件の知らせを入れる名前です。
        for event in pygame.event.get():
            # Game.handle_eventsが知らせの種類event.typeを確認し、QUIT（終了）なら閉じる操作として扱います。
            if event.type == pygame.QUIT:
                # Game.handle_eventsがself.runningをFalse（続けない）にし、runが画面更新を終えるようにします。
                self.running = False
                # Game.handle_eventsが操作確認のforを終え、取り出した一覧の残りの知らせはBattleへ送りません。
                break

            # Game.handle_eventsが終了以外の知らせeventを今の戦闘self.battleへ渡し、Battleがキー入力を確認します。
            self.battle.handle_event(event)
