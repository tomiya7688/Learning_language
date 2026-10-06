# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Player という型を定義する
class Player:
    # __init__ の処理を定義する
    def __init__(self):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (settings.PLAYER_X, settings.PLAYER_Y) を入れる
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
        # self.speed に settings.PLAYER_SPEED を入れる
        self.speed = settings.PLAYER_SPEED

    # move の処理を定義する
    def move(self, keys):
        # keys[pygame.K_LEFT] が成り立つなら
        if keys[pygame.K_LEFT]:
            # self.rect.x から self.speed を引く
            self.rect.x -= self.speed
        # keys[pygame.K_RIGHT] が成り立つなら
        if keys[pygame.K_RIGHT]:
            # self.rect.x に self.speed を足す
            self.rect.x += self.speed
        # keys[pygame.K_UP] が成り立つなら
        if keys[pygame.K_UP]:
            # self.rect.y から self.speed を引く
            self.rect.y -= self.speed
        # keys[pygame.K_DOWN] が成り立つなら
        if keys[pygame.K_DOWN]:
            # self.rect.y に self.speed を足す
            self.rect.y += self.speed
        # self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT)) を実行する
        self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

    # shoot の処理を定義する
    def shoot(self):
        # Bullet(self.rect.centerx, self.rect.top, -settings.BULLET_SPEED, (6, 20), (255, 240, 100)) を返す
        return Bullet(self.rect.centerx, self.rect.top, -settings.BULLET_SPEED,
                      (6, 20), (255, 240, 100))

    # draw の処理を定義する
    def draw(self, screen):
        # points は自機の三角形を結ぶ3点の一覧です。
        # points に [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright] を入れる
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # pygame.draw.polygon(screen, (100, 200, 255), points) を実行する
        pygame.draw.polygon(screen, (100, 200, 255), points)
