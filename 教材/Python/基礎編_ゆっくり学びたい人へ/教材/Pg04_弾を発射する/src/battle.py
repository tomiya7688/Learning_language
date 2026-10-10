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

    # 発射・移動・描画を分けると、スペースキーを変えたいときはhandle_eventを探せます。
    # handle_event（操作を受け取る）は、game.pyが送ったevent（操作の知らせ）1件を調べる処理です。
    def handle_event(self, event):
        # typeは種類、KEYDOWNはキーを押した知らせ、keyは押したキー、K_SPACEはスペースキーです。
        # andは両方を満たす条件。まず種類を調べ、キーを押した知らせのときだけevent.keyを調べます。
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Player.shoot（発射）が弾1発を作って返し、append（末尾に追加）がその弾をself.bulletsへ加えます。
            # 以前撃った弾は一覧に残るので、飛んでいる弾があっても次の弾を加えられます。
            self.bullets.append(self.player.shoot())

    # update（状態を更新する）は、Game.runが1回の画面更新で実行する自機と弾の位置更新です。
    def update(self):
        # get_pressedは今押されている各キーの状態を調べます。押した瞬間の知らせとは別の情報です。
        # Player.moveへキーの状態を指定し、押し続けている矢印の方向へ毎回自機を動かします。
        self.player.move(pygame.key.get_pressed())

        # move_bullets（弾を動かす）へ、この戦闘の弾一覧を指定し、全弾の移動と画面外の弾の削除を行います。
        self.move_bullets(self.bullets)

    # 弾1発ごとの移動・画面外の確認をmove_bulletsへ分け、updateから自機→弾の順を読めるようにします。
    # bulletsはupdateから指定したself.bulletsと同じ一覧です。別の弾一覧を新しく作る指定ではありません。
    def move_bullets(self, bullets):
        # 元の一覧を読みながら弾を削除すると、前へ詰まった次の弾を飛ばしてしまうことがあります。
        # [:]で読むための一覧をコピーします。弾自体は増やさず、コピーと元の一覧で同じ各弾を指します。
        for bullet in bullets[:]:
            # bulletは今確認する弾1発。Bullet.moveで、その弾の縦位置を更新します。
            bullet.move()
            # is_off_screen（画面外か）がTrueなら、弾全体が画面の上か下を越えています。
            if bullet.is_off_screen():
                # remove（取り除く）でその弾を元の一覧から外し、以後の移動と描画の対象から外します。
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

    # 弾1発ずつ描く処理をdraw_bulletsへ分け、drawから背景→自機→弾の順を読めるようにします。
    # screenはゲーム画面の描画先、bulletsはdrawから指定したself.bulletsと同じ弾一覧です。
    def draw_bullets(self, screen, bullets):
        # 現在の弾一覧からbullet（弾1発）を順に取り出します。弾が0発なら、このforの中は実行しません。
        for bullet in bullets:
            # Bullet.drawへ描画先screenを指定し、その弾の位置に黄色い長方形を描きます。
            # Battleは画面へ描くまでです。ウィンドウへ表示するのはgame.pyのpygame.display.flip()です。
            bullet.draw(screen)
