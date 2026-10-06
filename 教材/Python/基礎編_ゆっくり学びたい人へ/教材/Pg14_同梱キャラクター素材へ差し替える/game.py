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
        # screen は画面。pygameが用意した描画先です。
        # self.screen に pygame.display.set_mode((settings.WIDTH, settings.HEIGHT)) を入れる
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_caption('同梱キャラクター素材へ差し替える') を実行する
        pygame.display.set_caption('同梱キャラクター素材へ差し替える')

        # clock は時計。画面更新を最大60回/秒に調整します。
        # self.clock に pygame.time.Clock() を入れる
        self.clock = pygame.time.Clock()
        # running は実行中かどうか。Falseで繰り返しを終えます。
        # self.running に True を入れる
        self.running = True

        # self.start_game() を実行する
        self.start_game()

    # start_game の処理を定義する
    def start_game(self):
        # battle は戦闘。1回のゲームで使う自機と敵と弾の一覧を持ちます。
        # self.battle に Battle() を入れる
        self.battle = Battle()

    # run の処理を定義する
    def run(self):
        # self.running が成り立つ間、繰り返す
        while self.running:
            # self.handle_events() を実行する
            self.handle_events()
            # not self.running が成り立つなら
            if not self.running:
                # この繰り返しを終える
                break

            # self.battle.update() を実行する
            self.battle.update()

            # self.battle.is_game_over() が成り立つなら
            if self.battle.is_game_over():
                # print('GAME OVER') を実行する
                print("GAME OVER")
                # running は実行中かどうか。Falseで繰り返しを終えます。
                # self.running に False を入れる
                self.running = False

            # self.battle.is_clear() が成り立つなら
            elif self.battle.is_clear():
                # print('GAME CLEAR!') を実行する
                print("GAME CLEAR!")
                # running は実行中かどうか。Falseで繰り返しを終えます。
                # self.running に False を入れる
                self.running = False

            # self.battle.draw(self.screen) を実行する
            self.battle.draw(self.screen)

            # pygame.display.flip() を実行する
            pygame.display.flip()
            # self.clock.tick(settings.FPS) を実行する
            self.clock.tick(settings.FPS)

    # handle_events の処理を定義する
    def handle_events(self):
        # pygame.event.get() から event を1つずつ取り出して繰り返す
        for event in pygame.event.get():
            # event.type == pygame.QUIT が成り立つなら
            if event.type == pygame.QUIT:
                # running は実行中かどうか。Falseで繰り返しを終えます。
                # self.running に False を入れる
                self.running = False
                # この繰り返しを終える
                break

            # self.battle.handle_event(event) を実行する
            self.battle.handle_event(event)
