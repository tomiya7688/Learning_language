# pygame を読み込む
import pygame
# settings を読み込む
import settings
# player から Player を読み込む
from player import Player

# Battle という型を定義する
class Battle:
    # __init__ の処理を定義する
    def __init__(self):
        # player はプレイヤー。ここでは操作する自機です。
        # self.player に Player() を入れる
        self.player = Player()

        # bullets は弾の一覧。ここでは自機が撃った弾を並べます。
        # self.bullets に [] を入れる
        self.bullets = []

    # handle_event の処理を定義する
    def handle_event(self, event):
        # event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE が成り立つなら
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.bullets.append(self.player.shoot()) を実行する
            self.bullets.append(self.player.shoot())

    # update の処理を定義する
    def update(self):
        # self.player.move(pygame.key.get_pressed()) を実行する
        self.player.move(pygame.key.get_pressed())

        # self.move_bullets(self.bullets) を実行する
        self.move_bullets(self.bullets)

    # move_bullets の処理を定義する
    def move_bullets(self, bullets):
        # bullets[:] から bullet を1つずつ取り出して繰り返す
        for bullet in bullets[:]:
            # bullet.move() を実行する
            bullet.move()
            # bullet.is_off_screen() が成り立つなら
            if bullet.is_off_screen():
                # bullets.remove(bullet) を実行する
                bullets.remove(bullet)

    # draw の処理を定義する
    def draw(self, screen):
        # screen.fill((10, 10, 30)) を実行する
        screen.fill((10, 10, 30))

        # self.player.draw(screen) を実行する
        self.player.draw(screen)
        # self.draw_bullets(screen, self.bullets) を実行する
        self.draw_bullets(screen, self.bullets)

    # draw_bullets の処理を定義する
    def draw_bullets(self, screen, bullets):
        # bullets から bullet を1つずつ取り出して繰り返す
        for bullet in bullets:
            # bullet.draw(screen) を実行する
            bullet.draw(screen)
