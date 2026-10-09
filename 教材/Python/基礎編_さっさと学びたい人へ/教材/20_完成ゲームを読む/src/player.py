# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Player という型を定義する
class Player:
    # __init__ の処理を定義する
    def __init__(self, image):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (settings.PLAYER_X, settings.PLAYER_Y) を入れる
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # image は画像。画面へ描く内容を持ちます。
        # self.image に image を入れる
        self.image = image
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に image.get_rect(center=self.rect.center) を入れる
        self.rect = image.get_rect(center=self.rect.center)

        # speed は速さ。1回の更新で、押した矢印の方向ごとに動く距離です。単位はピクセルです。
        # self.speed に settings.PLAYER_SPEED を入れる
        self.speed = settings.PLAYER_SPEED

        # hp はhit points（体力）。攻撃1回で1減り、0で倒されます。
        # self.hp に settings.PLAYER_HP を入れる
        self.hp = settings.PLAYER_HP

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

    # take_damage の処理を定義する
    def take_damage(self):
        # self.hp から 1 を引く
        self.hp -= 1

    # draw の処理を定義する
    def draw(self, screen):
        # screen.blit(self.image, self.rect) を実行する
        screen.blit(self.image, self.rect)
