# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Enemy という型を定義する
class Enemy:
    # __init__ の処理を定義する
    def __init__(self, x, y):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (x, y) を入れる
        self.rect.center = (x, y)
        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
        # self.speed に settings.ENEMY_SPEED を入れる
        self.speed = settings.ENEMY_SPEED

    # move の処理を定義する
    def move(self):
        # self.rect.y に self.speed を足す
        self.rect.y += self.speed

    # is_off_screen の処理を定義する
    def is_off_screen(self):
        # self.rect.top > settings.HEIGHT を返す
        return self.rect.top > settings.HEIGHT

    # shoot の処理を定義する
    def shoot(self):
        # Bullet(self.rect.centerx, self.rect.bottom, settings.ENEMY_BULLET_SPEED, (8, 16), (255, 100, 180)) を返す
        return Bullet(self.rect.centerx, self.rect.bottom,
                      settings.ENEMY_BULLET_SPEED, (8, 16), (255, 100, 180))

    # draw の処理を定義する
    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 100, 100), self.rect) を実行する
        pygame.draw.rect(screen, (255, 100, 100), self.rect)
