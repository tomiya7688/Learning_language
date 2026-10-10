# pygame を読み込む
import pygame
# settings を読み込む
import settings
# resources から load_image を読み込む
from resources import load_image

# Background という型を定義する
class Background:
    # __init__ の処理を定義する
    def __init__(self):
        # image は画像。画面へ描く内容を持ちます。
        # self.image に load_image('space_background.png', (settings.WIDTH, settings.HEIGHT)) を入れる
        self.image = load_image("space_background.png", (settings.WIDTH, settings.HEIGHT))
        # y1 は1枚目の背景の上端の位置です。
        # self.y1 に 0 を入れる
        self.y1 = 0
        # y2 は2枚目の背景の上端の位置です。
        # self.y2 に -settings.HEIGHT を入れる
        self.y2 = -settings.HEIGHT

    # update の処理を定義する
    def update(self):
        # self.y1 に settings.BACKGROUND_SPEED を足す
        self.y1 += settings.BACKGROUND_SPEED
        # self.y2 に settings.BACKGROUND_SPEED を足す
        self.y2 += settings.BACKGROUND_SPEED
        # self.y1 >= settings.HEIGHT が成り立つなら
        if self.y1 >= settings.HEIGHT:
            # y1 は1枚目の背景の上端の位置です。
            # self.y1 に self.y2 - settings.HEIGHT を入れる
            self.y1 = self.y2 - settings.HEIGHT
        # self.y2 >= settings.HEIGHT が成り立つなら
        if self.y2 >= settings.HEIGHT:
            # y2 は2枚目の背景の上端の位置です。
            # self.y2 に self.y1 - settings.HEIGHT を入れる
            self.y2 = self.y1 - settings.HEIGHT

    # draw の処理を定義する
    def draw(self, screen):
        # screen.blit(self.image, (0, self.y1)) を実行する
        screen.blit(self.image, (0, self.y1))
        # screen.blit(self.image, (0, self.y2)) を実行する
        screen.blit(self.image, (0, self.y2))
