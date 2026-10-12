# pygame を読み込む
import pygame
# settings を読み込む
import settings

# Background という型を定義する
class Background:
    # __init__ の処理を定義する
    def __init__(self):
        # stars は星の位置の一覧です。
        # self.stars に [[40, 30], [120, 90], [210, 40], [300, 160], [390, 70], [480, 210], [570, 130], [80, 260], [170, 350], [260, 290], [350, 430], [440, 330], [530, 400], [620, 250], [30, 440], [145, 190], [235, 10], [325, 240], [415, 150], [555, 20]] を入れる
        self.stars = [[40, 30], [120, 90], [210, 40], [300, 160], [390, 70], [480, 210], [570, 130], [80, 260], [170, 350], [260, 290], [350, 430], [440, 330], [530, 400], [620, 250], [30, 440], [145, 190], [235, 10], [325, 240], [415, 150], [555, 20]]

    # update の処理を定義する
    def update(self):
        # self.stars から star を1つずつ取り出して繰り返す
        for star in self.stars:
            # star[1] に (star[1] + settings.BACKGROUND_SPEED) % settings.HEIGHT を入れる
            star[1] = (star[1] + settings.BACKGROUND_SPEED) % settings.HEIGHT

    # draw の処理を定義する
    def draw(self, screen):
        # screen.fill((10, 10, 30)) を実行する
        screen.fill((10, 10, 30))
        # self.stars から star を1つずつ取り出して繰り返す
        for star in self.stars:
            # pygame.draw.circle(screen, (220, 220, 255), star, 2) を実行する
            pygame.draw.circle(screen, (220, 220, 255), star, 2)
