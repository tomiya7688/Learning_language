# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Enemy という型を定義する
class Enemy:
    # __init__ の処理を定義する
    def __init__(self, x, y, fire_interval, image):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (x, y) を入れる
        self.rect.center = (x, y)
        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
        # self.speed に settings.ENEMY_SPEED を入れる
        self.speed = settings.ENEMY_SPEED

        # image は画像。画面へ描く内容を持ちます。
        # self.image に image を入れる
        self.image = image
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に image.get_rect(center=self.rect.center) を入れる
        self.rect = image.get_rect(center=self.rect.center)

        # fire_interval は発射の間隔。単位は更新回数です。
        # self.fire_interval に fire_interval を入れる
        self.fire_interval = fire_interval
        # fire_timer は前回の発射から何回更新したかを数える値です。
        # self.fire_timer に 0 を入れる
        self.fire_timer = 0

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

    # ready_to_fire の処理を定義する
    def ready_to_fire(self):
        # self.fire_timer に 1 を足す
        self.fire_timer += 1
        # self.fire_timer >= self.fire_interval が成り立つなら
        if self.fire_timer >= self.fire_interval:
            # fire_timer は前回の発射から何回更新したかを数える値です。
            # self.fire_timer に 0 を入れる
            self.fire_timer = 0
            # True を返す
            return True
        # False を返す
        return False

    # draw の処理を定義する
    def draw(self, screen):
        # screen.blit(self.image, self.rect) を実行する
        screen.blit(self.image, self.rect)
