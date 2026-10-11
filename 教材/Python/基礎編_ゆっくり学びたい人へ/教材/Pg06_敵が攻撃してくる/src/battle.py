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

        # Battleのself.fire_timerは、開始時または前回の発射タイミングからの更新回数。Enemyごとのタイマーではなく、戦闘で1つを共有します。
        # Battle.__init__が0を保存し、Battle.update_enemiesが更新ごとに1を足します。
        self.fire_timer = 0

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

        # self.move_bullets(self.bullets) を実行する
        self.move_bullets(self.bullets)

        # Battle.updateが敵の移動・画面外除外・一斉発射を行うupdate_enemiesを呼び出します。
        self.update_enemies()

        # Battle.updateが敵弾一覧self.enemy_bulletsをmove_bulletsへ指定し、今作った敵弾も同じ更新で1回動かします。
        self.move_bullets(self.enemy_bullets)

        # hit_enemiesが自機の弾と敵の重なりを調べ、命中した自機の弾をBattleのself.bullets、敵をBattleのself.enemiesから直接外します。敵の発射より後の判定です。
        hit_enemies(self.bullets, self.enemies)

        # hit_playerが移動後の敵弾と自機の重なりを調べ、命中した敵弾をBattleのself.enemy_bulletsから直接外し、Battleの自機self.playerへダメージを与えます。
        hit_player(self.enemy_bullets, self.player)

    # is_game_over の処理を定義する
    def is_game_over(self):
        # self.player.hp <= 0 を返す
        return self.player.hp <= 0

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

    # Battleは、敵1機の移動・弾の作成へ一覧の変更まで混ぜないよう、敵一覧の更新と一斉発射の間隔をupdate_enemiesへまとめます。
    # Battle.updateがupdate_enemiesを1回呼び、Enemy.move・is_off_screen・shootへ敵1機ずつの操作を任せます。
    def update_enemies(self):
        # self.enemies[:]はBattleの敵一覧だけのコピー。forは元のself.enemiesと同じ敵をenemy（選んだ敵）へ1機ずつ選びます。
        # Battle.update_enemiesが元のself.enemiesから敵を外しても、コピーを読むforは次の敵を飛ばしません。
        for enemy in self.enemies[:]:
            # Enemy.moveが選んだ敵の保存済みの移動量で位置を1回進めます。発射位置を使う前に敵を移動します。
            enemy.move()
            # Enemy.is_off_screenが敵の上端と画面の高さを比較し、Trueの場合だけBattle.update_enemiesが除外を行います。
            if enemy.is_off_screen():
                # removeが選んだ敵を元の敵一覧self.enemiesから外します。除外された敵は、この後の発射対象へ入りません。
                self.enemies.remove(enemy)

        # Battle.update_enemiesが、戦闘で共有する更新回数self.fire_timerへ1を足します。敵が0機でもこの回数は進みます。
        self.fire_timer += 1
        # >=は以上か調べる比較。数えた回数がsettings.ENEMY_FIRE_INTERVALに届くと、残った敵を一斉に発射させます。
        if self.fire_timer >= settings.ENEMY_FIRE_INTERVAL:
            # Battle.update_enemiesが回数を0へ戻し、次の発射タイミングまで再び更新を数えます。残った敵が0機でも0へ戻します。
            self.fire_timer = 0
            # forが元の敵一覧self.enemiesに残った敵だけを、enemyへ1機ずつ選びます。
            for enemy in self.enemies:
                # Enemy.shootが選んだ敵の移動後の位置で作った弾を返し、appendがBattleの敵弾一覧self.enemy_bulletsへ加えます。
                # appendは以前の敵弾を置き換えません。Battle.updateが、この呼び出しの後に敵弾の移動と命中判定を行います。
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
