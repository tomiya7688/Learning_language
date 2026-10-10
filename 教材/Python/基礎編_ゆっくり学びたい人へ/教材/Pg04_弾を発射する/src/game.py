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

    # start_gameへ戦闘を作る処理を分け、ウィンドウを作る処理とは別に探せるようにします。
    def start_game(self):
        # battleは戦闘。Battle()が自機と弾一覧を作り、self.battleに保存します。この章には敵はいません。
        self.battle = Battle()

    # run（動かす）は、main.pyのgame.run()から始まるゲーム全体の繰り返しです。
    def run(self):
        # whileは条件を満たす間の繰り返し。self.runningがTrueの間、下の処理を順に実行します。
        while self.running:
            # handle_events（操作を確認する）で、届いたキーの操作とウィンドウを閉じる操作を確認します。
            self.handle_events()
            # notはTrue/Falseを逆にする指定。閉じる操作でself.runningがFalseになったら終了へ進みます。
            if not self.running:
                # breakでこのwhileを終えます。閉じる操作の後には位置更新・描画・表示を行いません。
                break

            # Battle.update（状態を更新する）へ、自機の移動と弾の移動・画面外の弾の削除を依頼します。
            self.battle.update()

            # Battle.draw（描く）へ、描画先self.screenの背景・自機・残っている弾を描くよう依頼します。
            self.battle.draw(self.screen)

            # flip（画面を切り替える）で、今回描いた背景・自機・弾をウィンドウへ表示します。
            pygame.display.flip()
            # FPSはframes per second（毎秒の更新回数）。settings.pyの60を上限に、必要な時間だけ待ちます。
            # tickは毎秒60回の達成を保証しません。処理に時間がかかると実際の更新回数は少なくなります。
            self.clock.tick(settings.FPS)

    # handle_eventsへ操作確認を分け、runからゲームが進む順序を読み取れるようにします。
    def handle_events(self):
        # event（操作の知らせ）を、pygame.event.get()が取り出した一覧から1つずつ確認します。
        # キーを押した知らせと、閉じる操作の知らせを、このfor（順に読む繰り返し）で受け取ります。
        for event in pygame.event.get():
            # typeは知らせの種類。QUIT（終了）なら、ウィンドウを閉じる操作の知らせです。
            if event.type == pygame.QUIT:
                # self.runningをFalseへ変え、runが位置更新をせずに繰り返しを終えるようにします。
                self.running = False
                # breakでこのforを終え、閉じる操作の後に残ったキーの知らせはBattleへ送りません。
                break

            # 閉じる操作以外の知らせをBattle.handle_eventへ送り、スペースキーを押した知らせなら弾を作ってもらいます。
            self.battle.handle_event(event)
