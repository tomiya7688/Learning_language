# ゲームのウィンドウを閉じる処理と弾1発の移動を混ぜると、ゲーム全体が終わる場所を探しにくくなります。
# Game（ゲーム全体）へ画面と進行をまとめ、自機・敵・弾の管理はbattle.pyのBattle（戦闘）へ任せます。
# Pythonがウィンドウ・キー入力・描画・表示を扱う道具pygameを読み込みます。
import pygame
# Pythonが同じsrcのsettings.pyから、画面の幅WIDTH・高さHEIGHT・更新回数の上限FPSを読み込みます。
import settings
# Pythonが同じsrcのbattle.pyから、自機・敵・弾の情報と操作をまとめるBattle（戦闘）の定義を読み込みます。
from battle import Battle

# クラスは情報と操作をまとめた定義。Gameはゲーム画面と、画面更新を始めて終える操作をまとめます。
class Game:
    # __init__はGame()を作る際にPythonが実行する準備です。ウィンドウと、更新に使う情報を1回用意します。
    # selfは今作っているゲーム自身。self.screenのように、同じゲームへ情報を持たせます。
    def __init__(self):
        # pygame.display.set_modeが、幅settings.WIDTH・高さsettings.HEIGHTのウィンドウを作ります。
        # Gameはウィンドウに色や図形を描くための場所を、screen（画面）という名前のself.screenに保存します。
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_captionが、ゲームのウィンドウのタイトルを「敵を実装する」にします。
        pygame.display.set_caption('敵を実装する')

        # pygame.time.Clock()が更新の間隔を測る道具を作り、Gameはclock（時計）という名前のself.clockへ保存します。
        # Game.runはself.clock.tick(settings.FPS)で、画面更新が速くなりすぎないように待ちます。
        self.clock = pygame.time.Clock()
        # Gameはrunning（動作中）という名前のself.runningをTrue（続ける）にし、runが画面更新を始められるようにします。
        self.running = True

        # Game.__init__がstart_game（ゲームを始める）を実行して、自機1機・敵3機・空の弾一覧を持つ戦闘を用意します。
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

            # Game.runが今の戦闘self.battleのupdate（状態を更新する）へ、自機・敵・弾の移動、画面外の弾と敵の削除、弾と敵の命中の確認を依頼します。
            self.battle.update()

            # Game.runが今の戦闘self.battleのdraw（描く）へ、描画先self.screenに背景・自機・残っている弾と敵を描くよう依頼します。
            self.battle.draw(self.screen)

            # pygame.display.flip()が、self.screenへ描画済みの背景・自機・残っている弾と敵をゲームのウィンドウへ表示します。
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
