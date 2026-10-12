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
# boss から Boss を読み込む
from boss import Boss
# collisions から hit_boss を読み込む
from collisions import hit_boss

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

        # enemy_bullets は通常の敵が撃った弾の一覧です。
        # self.enemy_bullets に [] を入れる
        self.enemy_bullets = []
        # font はフォント。文字の形と大きさを指定します。
        # self.font に pygame.font.Font(None, 36) を入れる
        self.font = pygame.font.Font(None, 36)

        # spawn_timer は前回の敵の出現からの更新回数です。
        # self.spawn_timer に 0 を入れる
        self.spawn_timer = 0
        # spawn_index は次に出す敵の番号。0が最初です。
        # self.spawn_index に 0 を入れる
        self.spawn_index = 0

        # boss はボス。通常の敵が全ていなくなった後に登場します。
        # self.boss に None を入れる
        self.boss = None

    # 押した知らせで弾を作る処理を、押している状態で移動する処理と混ぜないよう、handle_event（知らせへの対応）へ分けます。
    def handle_event(self, event):
        # eventは呼び出す側が指定した操作の知らせ1件、event.typeは知らせの種類、pygame.KEYDOWNはキーを押した知らせです。
        # andは左右の条件を両方満たす指定です。キーを押した知らせのときだけ、event.key（押したキー）がpygame.K_SPACE（スペースキー）か調べます。
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.player.shoot()が自機の位置から弾1発を作って返し、append（末尾へ追加）がその弾を自機の弾一覧self.bulletsへ加えます。
            # appendはself.bulletsに残っている以前の弾を置き換えません。弾の作成と一覧への追加だけでは、弾の移動や描画は行いません。
            self.bullets.append(self.player.shoot())

    # update の処理を定義する
    def update(self):
        # self.player.move(pygame.key.get_pressed()) を実行する
        self.player.move(pygame.key.get_pressed())

        # self.spawn_enemy() を実行する
        self.spawn_enemy()

        # self.move_bullets(self.bullets) を実行する
        self.move_bullets(self.bullets)

        # self.update_enemies() を実行する
        self.update_enemies()

        # self.move_bullets(self.enemy_bullets) を実行する
        self.move_bullets(self.enemy_bullets)

        # hit_enemies(self.bullets, self.enemies) を実行する
        hit_enemies(self.bullets, self.enemies)

        # self.update_boss() を実行する
        self.update_boss()

        # hit_player(self.enemy_bullets, self.player) を実行する
        hit_player(self.enemy_bullets, self.player)

    # is_game_over の処理を定義する
    def is_game_over(self):
        # self.player.hp <= 0 を返す
        return self.player.hp <= 0

    # is_clear の処理を定義する
    def is_clear(self):
        # self.boss is not None and self.boss.hp <= 0 を返す
        return self.boss is not None and self.boss.hp <= 0

    # 弾1発の移動と、弾一覧からの削除は別の役割なので、一覧を順に管理する処理をmove_bullets（弾を動かす）へ分けます。
    def move_bullets(self, bullets):
        # bulletsは呼び出す側が指定した弾一覧です。bullets[:]は一覧だけのコピーで、各要素は元の一覧と同じ弾を指します。
        # forはコピーの弾を順に1発ずつbulletへ選びます。元のbulletsから削除しても、コピーの次の弾を飛ばしません。
        for bullet in bullets[:]:
            # bullet.move()が、選んだ弾bulletに保存した移動量で位置を1回進めます。
            bullet.move()
            # bullet.is_off_screen()（選んだ弾が画面外か）がTrue（成り立つ）を返した場合だけ、bullets.remove(bullet)を実行します。
            if bullet.is_off_screen():
                # bullets.remove(bullet)が選んだ弾bulletを元の弾一覧bulletsから外します。弾一覧の削除は画面の絵を直接消す操作ではありません。
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

            # enemy.ready_to_fire() が成り立つなら
            elif enemy.ready_to_fire():
                # self.enemy_bullets.append(enemy.shoot()) を実行する
                self.enemy_bullets.append(enemy.shoot())

    # spawn_enemy の処理を定義する
    def spawn_enemy(self):
        # self.spawn_index >= len(settings.SPAWN_POSITIONS_X) が成り立つなら
        if self.spawn_index >= len(settings.SPAWN_POSITIONS_X):
            # この処理を終える
            return
        # self.spawn_timer に 1 を足す
        self.spawn_timer += 1
        # self.spawn_timer >= settings.SPAWN_INTERVAL が成り立つなら
        if self.spawn_timer >= settings.SPAWN_INTERVAL:
            # x は横位置。画面の左から右へ増えます。
            # x に settings.SPAWN_POSITIONS_X[self.spawn_index] を入れる
            x = settings.SPAWN_POSITIONS_X[self.spawn_index]

            # fire_interval は発射の間隔。単位は更新回数です。
            # fire_interval に settings.ENEMY_FIRE_INTERVALS[self.spawn_index] を入れる
            fire_interval = settings.ENEMY_FIRE_INTERVALS[self.spawn_index]
            # self.enemies.append(Enemy(x, -20, fire_interval)) を実行する
            self.enemies.append(Enemy(x, -20, fire_interval))

            # self.spawn_index に 1 を足す
            self.spawn_index += 1
            # spawn_timer は前回の敵の出現からの更新回数です。
            # self.spawn_timer に 0 を入れる
            self.spawn_timer = 0

    # update_boss の処理を定義する
    def update_boss(self):
        # self.boss is None が成り立つなら
        if self.boss is None:
            # self.spawn_index >= len(settings.SPAWN_POSITIONS_X) and (not self.enemies) が成り立つなら
            if self.spawn_index >= len(settings.SPAWN_POSITIONS_X) and not self.enemies:
                # boss はボス。通常の敵が全ていなくなった後に登場します。
                # self.boss に Boss() を入れる
                self.boss = Boss()

                # self.bullets.clear() を実行する
                self.bullets.clear()
            # この処理を終える
            return
        # hit_boss(self.bullets, self.boss) を実行する
        hit_boss(self.bullets, self.boss)

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

        # self.boss is not None が成り立つなら
        if self.boss is not None:
            # self.boss.draw(screen) を実行する
            self.boss.draw(screen)
            # self.draw_text(screen, f'BOSS HP: {self.boss.hp}', (220, 10)) を実行する
            self.draw_text(screen, f"BOSS HP: {self.boss.hp}", (220, 10))

    # 弾1発を描くBullet.drawと、弾一覧を順に描く役割を分けるため、draw_bullets（弾の描画）へ繰り返しをまとめます。
    def draw_bullets(self, screen, bullets):
        # screenは呼び出す側が指定した描画先、bulletsは指定した弾一覧です。forが一覧に残った弾を1発ずつbulletへ選びます。
        for bullet in bullets:
            # bullet.draw(screen)が、選んだ弾bulletに保存した位置・大きさ・色で描画先screenへ弾を描きます。弾を移動したり一覧へ追加したりはしません。
            bullet.draw(screen)

    # draw_text の処理を定義する
    def draw_text(self, screen, text, position):
        # image は画像。画面へ描く内容を持ちます。
        # image に self.font.render(text, True, (255, 255, 255)) を入れる
        image = self.font.render(text, True, (255, 255, 255))
        # screen.blit(image, position) を実行する
        screen.blit(image, position)
