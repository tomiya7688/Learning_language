# pygame を読み込む
import pygame

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # screen はゲーム画面を描く場所です。
        # self.screen に pygame.display.set_mode((640, 480)) を入れる
        self.screen = pygame.display.set_mode((640, 480))
        # pygame.display.set_caption("最初のゲーム画面") を実行する
        pygame.display.set_caption("最初のゲーム画面")
        # self.clock に pygame.time.Clock() を入れる
        self.clock = pygame.time.Clock()
        # self.running に True を入れる
        self.running = True

    # run の処理を定義する
    def run(self):
        # self.running が成り立つ間、繰り返す
        while self.running:
            # pygame.event.get() から event を1つずつ取り出して繰り返す
            for event in pygame.event.get():
                # event.type == pygame.QUIT が成り立つなら
                if event.type == pygame.QUIT:
                    # self.running に False を入れる
                    self.running = False

            # self.running が False なら
            if not self.running:
                # この繰り返しを終える
                break

            # self.screen.fill((10, 10, 30)) を実行する
            self.screen.fill((10, 10, 30))
            # pygame.display.flip() を実行する
            pygame.display.flip()
            # self.clock.tick(60) を実行する
            self.clock.tick(60)
