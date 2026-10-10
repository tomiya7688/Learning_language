# Pythonが、キーの状態を調べたり画面へ色を塗ったりするpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから画面の大きさなどの設定を読み込みます。
import settings
# Pythonが、同じsrcのplayer.pyから自機の情報と操作をまとめるPlayer（プレイヤー）の定義を読み込みます。
from player import Player
# Pythonが、同じsrcのenemy.pyから敵1機の情報と操作をまとめるEnemy（敵）の定義を読み込みます。
from enemy import Enemy
# Pythonが、同じsrcのcollisions.pyから弾と敵の命中を調べて一覧を変更するhit_enemies（敵への命中）の定義を読み込みます。
from collisions import hit_enemies

# 自機・弾・敵の情報を別々に置くと、どの一覧を移動・命中・描画に使うか追いにくくなります。
# Battle（戦闘）へ自機と2つの一覧、その情報を使う操作をまとめます。ウィンドウの管理と表示はGameへ任せます。
class Battle:
    # 毎回の移動で自機や敵を作り直すと位置が戻るため、開始時にだけ用意する情報は__init__（作成時の準備）へ分けます。
    # selfは、今作っている戦闘1つ分の情報です。Game.start_gameがBattle()と書くと、Pythonが__init__を実行します。
    def __init__(self):
        # playerはプレイヤー。Player()が自機1機の位置などを用意し、self.playerから同じ自機を後の移動・発射・描画で使います。
        self.player = Player()

        # bulletsは弾。self.bulletsはこの戦闘の自機が撃った弾の一覧で、[]はまだ弾がない空の一覧です。
        # Battle.handle_eventが弾を追加し、Battle.updateとBattle.drawが一覧に残っている弾を使います。
        self.bullets = []

        # enemiesは敵。self.enemiesはこの戦闘の敵の一覧で、最初に[]で空の一覧を作ります。
        self.enemies = []
        # Enemy(160, 80)が中心を画面左から160・上から80ピクセルに置く敵1機を作り、append（末尾へ追加）が敵一覧へ加えます。
        self.enemies.append(Enemy(160, 80))
        # Enemy(320, 40)が中心を画面左から320・上から40ピクセルに置く敵1機を作り、self.enemiesへ加えます。
        self.enemies.append(Enemy(320, 40))
        # Enemy(480, 100)が中心を画面左から480・上から100ピクセルに置く敵1機を作り、self.enemiesへ加えます。開始時の敵は合計3機です。
        self.enemies.append(Enemy(480, 100))

    # 押した知らせで弾を作る処理を、押している状態で移動する処理と混ぜないよう、handle_event（知らせへの対応）へ分けます。
    def handle_event(self, event):
        # eventは呼び出す側が指定した操作の知らせ1件、event.typeは知らせの種類、pygame.KEYDOWNはキーを押した知らせです。
        # andは左右の条件を両方満たす指定です。キーを押した知らせのときだけ、event.key（押したキー）がpygame.K_SPACE（スペースキー）か調べます。
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.player.shoot()が自機の位置から弾1発を作って返し、append（末尾へ追加）がその弾を自機の弾一覧self.bulletsへ加えます。
            # appendはself.bulletsに残っている以前の弾を置き換えません。弾の作成と一覧への追加だけでは、弾の移動や描画は行いません。
            self.bullets.append(self.player.shoot())

    # 移動と命中の処理が各所に分かれると、移動の前と後のどちらで判定するか追いにくいため、update（状態の更新）へ順序をまとめます。
    def update(self):
        # Game.runから依頼されたBattle.updateがget_pressed（押しているキーの状態）を調べ、Player.moveへ指定して自機を動かします。
        # スペースキーを押した知らせへの対応は、別のBattle.handle_eventが行います。
        self.player.move(pygame.key.get_pressed())

        # Battle.updateが自機の弾一覧self.bulletsをmove_bulletsへ指定し、弾の移動と画面外の弾の削除を依頼します。
        self.move_bullets(self.bullets)

        # Battle.updateがupdate_enemiesへ、敵の移動と画面外の敵の削除を依頼します。
        self.update_enemies()

        # hit_enemiesが、移動後に残った自機の弾と敵の重なりを調べ、命中した弾と敵を元のself.bullets/self.enemiesから外します。
        # Battle.updateは命中の戻り値を使わず、一覧の変更をhit_enemiesへ任せます。
        hit_enemies(self.bullets, self.enemies)

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

    # 敵1機を動かすEnemy.moveと、敵一覧を管理する処理を分けるため、update_enemies（敵の更新）へ繰り返しと削除をまとめます。
    def update_enemies(self):
        # self.enemies[:]は敵一覧だけのコピーで、各要素は同じ敵を指します。forがコピーからenemy（敵1機）を順に選びます。
        # 元のself.enemiesから敵を外しても、コピーの次の敵を飛ばしません。
        for enemy in self.enemies[:]:
            # 選んだ敵のEnemy.moveが、その敵に保存した移動量で位置を下へ1回進めます。
            enemy.move()
            # Enemy.is_off_screenがTrueを返すのは、移動後の敵の上端が画面の高さsettings.HEIGHTより下へ出た場合です。
            if enemy.is_off_screen():
                # Battle.update_enemiesが選んだ敵を元のself.enemiesから外し、以後の更新・描画の対象から外します。
                self.enemies.remove(enemy)

    # 一覧の変更と画面へ絵を描く処理を混ぜないよう、draw（描画）へ背景・自機・弾・敵を描く順序をまとめます。
    def draw(self, screen):
        # screenはGame.runが指定した描画先です。fill（塗る）が全体を暗い青に塗り、前に描いた絵を塗りつぶします。
        # (10, 10, 30)は赤・緑・青の強さの順で各値は0〜255です。fillは物体の位置や一覧を変更しません。
        screen.fill((10, 10, 30))

        # Battle.drawがPlayer.drawへ同じ描画先screenを指定し、現在の自機の位置に水色の三角形を描くよう依頼します。
        self.player.draw(screen)
        # Battle.drawがdraw_bulletsへ描画先screenと自機の弾一覧self.bulletsを指定し、残った弾の描画を依頼します。
        self.draw_bullets(screen, self.bullets)

        # forが、移動や命中の確認後に元の敵一覧self.enemiesへ残った敵を1機ずつenemyへ選びます。
        for enemy in self.enemies:
            # 選んだ敵のEnemy.drawが、同じ描画先screenへ現在の敵の位置に赤い長方形を描きます。
            enemy.draw(screen)

    # 弾1発を描くBullet.drawと、弾一覧を順に描く役割を分けるため、draw_bullets（弾の描画）へ繰り返しをまとめます。
    def draw_bullets(self, screen, bullets):
        # screenは呼び出す側が指定した描画先、bulletsは指定した弾一覧です。forが一覧に残った弾を1発ずつbulletへ選びます。
        for bullet in bullets:
            # bullet.draw(screen)が、選んだ弾bulletに保存した位置・大きさ・色で描画先screenへ弾を描きます。弾を移動したり一覧へ追加したりはしません。
            bullet.draw(screen)
