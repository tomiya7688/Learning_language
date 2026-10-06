# pygame を読み込む
import pygame
# settings を読み込む
import settings
# player から Player を読み込む
from player import Player
# enemy から Enemy を読み込む
from enemy import Enemy
# collisions から hit_enemies を読み込む
from collisions import hit_enemies
# collisions から hit_player を読み込む
from collisions import hit_player

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

        # enemies は通常の敵の一覧。各要素はEnemyです。
        # self.enemies に [] を入れる
        self.enemies = []
        # self.enemies.append(Enemy(160, 80)) を実行する
        self.enemies.append(Enemy(160, 80))
        # self.enemies.append(Enemy(320, 40)) を実行する
        self.enemies.append(Enemy(320, 40))
        # self.enemies.append(Enemy(480, 100)) を実行する
        self.enemies.append(Enemy(480, 100))

        # enemy_bullets は通常の敵が撃った弾の一覧です。
        # self.enemy_bullets に [] を入れる
        self.enemy_bullets = []
        # font はフォント。文字の形と大きさを指定します。
        # self.font に pygame.font.Font(None, 36) を入れる
        self.font = pygame.font.Font(None, 36)

        # fire_timer は前回の発射から何回更新したかを数える値です。
        # self.fire_timer に 0 を入れる
        self.fire_timer = 0

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

        # self.update_enemies() を実行する
        self.update_enemies()

        # self.move_bullets(self.enemy_bullets) を実行する
        self.move_bullets(self.enemy_bullets)

        # hit_enemies(self.bullets, self.enemies) を実行する
        hit_enemies(self.bullets, self.enemies)

        # hit_player(self.enemy_bullets, self.player) を実行する
        hit_player(self.enemy_bullets, self.player)

    # is_game_over の処理を定義する
    def is_game_over(self):
        # self.player.hp <= 0 を返す
        return self.player.hp <= 0

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

    # update_enemies の処理を定義する
    def update_enemies(self):
        # self.enemies[:] から enemy を1つずつ取り出して繰り返す
        for enemy in self.enemies[:]:
            # enemy.move() を実行する
            enemy.move()
            # enemy.is_off_screen() が成り立つなら
            if enemy.is_off_screen():
                # self.enemies.remove(enemy) を実行する
                self.enemies.remove(enemy)

        # self.fire_timer に 1 を足す
        self.fire_timer += 1
        # self.fire_timer >= settings.ENEMY_FIRE_INTERVAL が成り立つなら
        if self.fire_timer >= settings.ENEMY_FIRE_INTERVAL:
            # fire_timer は前回の発射から何回更新したかを数える値です。
            # self.fire_timer に 0 を入れる
            self.fire_timer = 0
            # self.enemies から enemy を1つずつ取り出して繰り返す
            for enemy in self.enemies:
                # self.enemy_bullets.append(enemy.shoot()) を実行する
                self.enemy_bullets.append(enemy.shoot())

    # draw の処理を定義する
    def draw(self, screen):
        # screen.fill((10, 10, 30)) を実行する
        screen.fill((10, 10, 30))

        # self.player.draw(screen) を実行する
        self.player.draw(screen)
        # self.draw_bullets(screen, self.bullets) を実行する
        self.draw_bullets(screen, self.bullets)

        # self.enemies から enemy を1つずつ取り出して繰り返す
        for enemy in self.enemies:
            # enemy.draw(screen) を実行する
            enemy.draw(screen)

        # self.draw_bullets(screen, self.enemy_bullets) を実行する
        self.draw_bullets(screen, self.enemy_bullets)
        # self.draw_text(screen, f'HP: {self.player.hp}', (10, 10)) を実行する
        self.draw_text(screen, f"HP: {self.player.hp}", (10, 10))

    # draw_bullets の処理を定義する
    def draw_bullets(self, screen, bullets):
        # bullets から bullet を1つずつ取り出して繰り返す
        for bullet in bullets:
            # bullet.draw(screen) を実行する
            bullet.draw(screen)

    # draw_text の処理を定義する
    def draw_text(self, screen, text, position):
        # image は画像。画面へ描く内容を持ちます。
        # image に self.font.render(text, True, (255, 255, 255)) を入れる
        image = self.font.render(text, True, (255, 255, 255))
        # screen.blit(image, position) を実行する
        screen.blit(image, position)
