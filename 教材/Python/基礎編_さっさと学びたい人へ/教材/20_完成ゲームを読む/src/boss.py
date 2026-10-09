# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Boss という型を定義する
class Boss:
    # __init__ の処理を定義する
    def __init__(self, image):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 120, 80) を入れる
        self.rect = pygame.Rect(0, 0, 120, 80)
        # self.rect.center に (settings.BOSS_X, settings.BOSS_Y) を入れる
        self.rect.center = (settings.BOSS_X, settings.BOSS_Y)
        # hp はhit points（体力）。攻撃1回で1減り、0で倒されます。
        # self.hp に settings.BOSS_HP を入れる
        self.hp = settings.BOSS_HP

        # image は画像。画面へ描く内容を持ちます。
        # self.image に image を入れる
        self.image = image
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に image.get_rect(center=self.rect.center) を入れる
        self.rect = image.get_rect(center=self.rect.center)

        # fire_timer は前回の発射から何回更新したかを数える値です。
        # self.fire_timer に 0 を入れる
        self.fire_timer = 0
        # fire_interval は発射の間隔。単位は更新回数です。
        # self.fire_interval に settings.BOSS_FIRE_INTERVAL を入れる
        self.fire_interval = settings.BOSS_FIRE_INTERVAL

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

    # shoot の処理を定義する
    def shoot(self):
        # Bullet(self.rect.centerx, self.rect.bottom, settings.BOSS_BULLET_SPEED, (settings.BOSS_BULLET_WIDTH, settings.BOSS_BULLET_HEIGHT), (255, 80, 80)) を返す
        return Bullet(self.rect.centerx, self.rect.bottom,
                      settings.BOSS_BULLET_SPEED,
                      (settings.BOSS_BULLET_WIDTH, settings.BOSS_BULLET_HEIGHT),
                      (255, 80, 80))

    # take_damage の処理を定義する
    def take_damage(self):
        # self.hp から 1 を引く
        self.hp -= 1

    # draw の処理を定義する
    def draw(self, screen):
        # screen.blit(self.image, self.rect) を実行する
        screen.blit(self.image, self.rect)
