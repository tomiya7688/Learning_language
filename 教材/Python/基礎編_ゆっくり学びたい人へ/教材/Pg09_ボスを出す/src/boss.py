# pygame を読み込む
import pygame
# settings を読み込む
import settings

# Boss という型を定義する
class Boss:
    # __init__ の処理を定義する
    def __init__(self):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 120, 80) を入れる
        self.rect = pygame.Rect(0, 0, 120, 80)
        # self.rect.center に (settings.BOSS_X, settings.BOSS_Y) を入れる
        self.rect.center = (settings.BOSS_X, settings.BOSS_Y)
        # hp はhit points（体力）。攻撃1回で1減り、0で倒されます。
        # self.hp に settings.BOSS_HP を入れる
        self.hp = settings.BOSS_HP

    # take_damage の処理を定義する
    def take_damage(self):
        # self.hp から 1 を引く
        self.hp -= 1

    # draw の処理を定義する
    def draw(self, screen):
        # pygame.draw.rect(screen, (180, 80, 255), self.rect) を実行する
        pygame.draw.rect(screen, (180, 80, 255), self.rect)
