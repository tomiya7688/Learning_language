# pygame を読み込む
import pygame
# player から Player を読み込む
from player import Player

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # 横640、高さ480ピクセルのウィンドウを開き、あとで色や絵を描く画面を self.screen に保存する
        self.screen = pygame.display.set_mode((640, 480))
        # pygame.display.set_caption("プレイヤーを表示する") を実行する
        pygame.display.set_caption("プレイヤーを表示する")
        # pygame.time.Clock() で、画面更新の間隔を測る self.clock を作る
        self.clock = pygame.time.Clock()
        # self.player に Player() を入れる
        self.player = Player()
        # self.running を True にして、ゲーム画面の繰り返しを続ける
        self.running = True

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
            # self.draw() を実行する
            self.draw()
            # pygame.display.flip() を実行する
            pygame.display.flip()
            # 画面更新を1秒間に最大60回に抑える
            self.clock.tick(60)

    # handle_events の処理を定義する
    def handle_events(self):
        # Pygameに届いた操作の知らせを1つずつ取り出して確認する
        for event in pygame.event.get():
            # event.type が pygame.QUIT なら、ウィンドウを閉じる操作を受けています。
            if event.type == pygame.QUIT:
                # self.running を False にし、ゲーム画面の繰り返しを終える
                self.running = False
                # 残りの操作を確認せず、操作確認の繰り返しを終える
                break

    # draw の処理を定義する
    def draw(self):
        # self.screen.fill((10, 10, 30)) を実行する
        self.screen.fill((10, 10, 30))
        # self.player.draw(self.screen) を実行する
        self.player.draw(self.screen)
