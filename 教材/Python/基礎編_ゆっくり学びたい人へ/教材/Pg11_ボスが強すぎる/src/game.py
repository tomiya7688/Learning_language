# pygame を読み込む
import pygame
# settings を読み込む
import settings
# battle から Battle を読み込む
from battle import Battle

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # settings.pyで決めた幅と高さのウィンドウを開き、あとで色や絵を描く画面を self.screen に保存する
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_caption('ボスが強すぎる') を実行する
        pygame.display.set_caption('ボスが強すぎる')

        # self.clock.tick(settings.FPS) で、画面更新を1秒あたり最大 settings.FPS 回に抑える
        # pygame.time.Clock() で、画面更新の間隔を測る self.clock を作る
        self.clock = pygame.time.Clock()
        # self.running を True にして、ゲーム画面の繰り返しを続ける
        self.running = True

        # self.start_game() を実行する
        self.start_game()

    # ウィンドウの準備と戦闘の作成を分けると、start_game（ゲームを始める）から戦闘の作成場所を探せます。
    def start_game(self):
        # Battle（戦闘）が、自機や弾など、この章の戦闘で使う情報を作ります。
        # GameはBattle()で作った戦闘をself.battleへ保存し、後の更新と描画で同じ戦闘を使います。
        self.battle = Battle()

    # run の処理を定義する
    def run(self):
        # self.running が True の間、ゲーム画面を更新する
        while self.running:
            # self.handle_events() を実行する
            self.handle_events()
            # self.running が False なら、次の画面更新をせず繰り返しを終える
            if not self.running:
                # 画面更新を繰り返す while を終える
                break

            # self.battle.update() を実行する
            self.battle.update()

            # self.battle.is_game_over() が成り立つなら
            if self.battle.is_game_over():
                # print('GAME OVER') を実行する
                print("GAME OVER")
                # self.running を False にし、ゲーム画面の繰り返しを終える
                self.running = False

            # self.battle.is_clear() が成り立つなら
            elif self.battle.is_clear():
                # print('GAME CLEAR!') を実行する
                print("GAME CLEAR!")
                # self.running を False にし、ゲーム画面の繰り返しを終える
                self.running = False

            # self.battle.draw(self.screen) を実行する
            self.battle.draw(self.screen)

            # pygame.display.flip() を実行する
            pygame.display.flip()
            # settings.FPS 回/秒を上限にして、画面更新が速くなりすぎないよう待つ
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
