# 自機と何発もの弾を別々の場所で管理すると、どの弾を動かして描くか追いにくくなります。
# Battle（戦闘）へ自機1機・弾の一覧と、その一覧を更新する操作をまとめます。この章には敵はいません。
# pygameはキーの状態を調べ、ゲーム画面を塗る道具です。
import pygame
# 同じsrcフォルダのsettings.pyを読み込みます。このファイル内では設定値を直接使っていません。
import settings
# 同じsrcフォルダのplayer.pyから、自機1機の位置・移動・発射・描画をまとめたPlayerを読み込みます。
from player import Player

# クラスは情報と操作をまとめた定義です。Battleは1回の戦闘に使う自機と弾を管理します。
class Battle:
    # __init__は、game.pyがBattle()を作るときにPythonが実行する初期設定です。
    # selfは今作る戦闘。self.playerやself.bulletsに、その戦闘が使う自機と弾一覧を持たせます。
    def __init__(self):
        # player（プレイヤー）に操作する自機1機を作ります。位置と描く形はplayer.pyのPlayerが決めます。
        self.player = Player()

        # bulletsは弾の一覧。[]は空の一覧で、まだ1発も撃っていない状態です。
        self.bullets = []

    # 押した知らせで弾を作る処理を、押している状態で移動する処理と混ぜないよう、handle_event（知らせへの対応）へ分けます。
    def handle_event(self, event):
        # eventは呼び出す側が指定した操作の知らせ1件、event.typeは知らせの種類、pygame.KEYDOWNはキーを押した知らせです。
        # andは左右の条件を両方満たす指定です。キーを押した知らせのときだけ、event.key（押したキー）がpygame.K_SPACE（スペースキー）か調べます。
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.player.shoot()が自機の位置から弾1発を作って返し、append（末尾へ追加）がその弾を自機の弾一覧self.bulletsへ加えます。
            # appendはself.bulletsに残っている以前の弾を置き換えません。弾の作成と一覧への追加だけでは、弾の移動や描画は行いません。
            self.bullets.append(self.player.shoot())

    # update（状態を更新する）は、Game.runが1回の画面更新で実行する自機と弾の位置更新です。
    def update(self):
        # get_pressedは今押されている各キーの状態を調べます。押した瞬間の知らせとは別の情報です。
        # Player.moveへキーの状態を指定し、押し続けている矢印の方向へ毎回自機を動かします。
        self.player.move(pygame.key.get_pressed())

        # move_bullets（弾を動かす）へ、この戦闘の弾一覧を指定し、全弾の移動と画面外の弾の削除を行います。
        self.move_bullets(self.bullets)

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

    # draw（描く）は、Game.runから指定されたscreen（ゲーム画面の描画先）へ背景・自機・弾を描きます。
    def draw(self, screen):
        # fill（塗る）で画面全体を暗い青へ塗り、前の更新で描いた自機や弾の絵を消します。
        # (10, 10, 30)は赤・緑・青の強さの順。各値は0〜255で、位置や弾一覧を変更する指定ではありません。
        screen.fill((10, 10, 30))

        # Player.drawへ描画先screenを指定し、現在の自機の位置に水色の三角形を描きます。
        self.player.draw(screen)
        # draw_bullets（弾を描く）へ描画先と現在の弾一覧を指定し、一覧に残った全弾を描きます。
        self.draw_bullets(screen, self.bullets)

    # 弾1発を描くBullet.drawと、弾一覧を順に描く役割を分けるため、draw_bullets（弾の描画）へ繰り返しをまとめます。
    def draw_bullets(self, screen, bullets):
        # screenは呼び出す側が指定した描画先、bulletsは指定した弾一覧です。forが一覧に残った弾を1発ずつbulletへ選びます。
        for bullet in bullets:
            # bullet.draw(screen)が、選んだ弾bulletに保存した位置・大きさ・色で描画先screenへ弾を描きます。弾を移動したり一覧へ追加したりはしません。
            bullet.draw(screen)
