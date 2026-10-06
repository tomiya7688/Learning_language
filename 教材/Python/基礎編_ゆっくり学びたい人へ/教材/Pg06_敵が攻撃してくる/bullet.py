# pygame を読み込む
import pygame
# settings を読み込む
import settings

# Bullet という型を定義する
class Bullet:
    # __init__ の処理を定義する
    def __init__(self, x, y, speed, size, color):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, size[0], size[1]) を入れる
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        # self.rect.center に (x, y) を入れる
        self.rect.center = (x, y)
        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
        # self.speed に speed を入れる
        self.speed = speed
        # color は色。赤・緑・青の強さを0〜255で指定します。
        # self.color に color を入れる
        self.color = color

    # move の処理を定義する
    def move(self):
        # self.rect.y に self.speed を足す
        self.rect.y += self.speed

    # is_off_screen の処理を定義する
    def is_off_screen(self):
        # self.rect.bottom < 0 or self.rect.top > settings.HEIGHT を返す
        return self.rect.bottom < 0 or self.rect.top > settings.HEIGHT

    # draw の処理を定義する
    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, self.rect) を実行する
        pygame.draw.rect(screen, self.color, self.rect)
