# 弾を何発も撃つと、各弾の位置と移動する処理を対応させる必要があります。
# Bullet（弾）へ1発分の位置・縦方向の移動量・色と、その弾の操作をまとめます。
# ピクセルは、ゲーム画面の位置や大きさを数える単位です。
# pygame はゲーム画面へ長方形を描く道具です。
import pygame
# settings は同じsrcフォルダのsettings.py。HEIGHTに画面の高さ480ピクセルがあります。
import settings

# クラスは情報と操作をまとめる定義です。Bulletは弾1発を作るための定義です。
class Bullet:
    # 弾を作る処理、動かす処理、画面外か調べる処理、描く処理を分けて探しやすくします。
    # __init__ は、Bullet(...)で弾を作るときにPythonが実行する初期設定の処理です。
    # selfは設定する弾1発を表す名前です。self.rectのように、その弾の情報を保存します。
    # x（横）/y（縦）は弾の中心位置。画面左端から右へx、画面上端から下へyピクセルです。
    # speed（速さの指定）は1回の更新で縦に進む量（ピクセル）。負なら上、正なら下へ進みます。
    # size（大きさ）は幅と高さの組、color（色）は赤・緑・青の強さを0〜255で指定した組です。
    # 配布時の設定で自機が初期位置なら、player.pyはBullet(320, 380, -8, (6, 20), (255, 240, 100))を作ります。
    def __init__(self, x, y, speed, size, color):
        # rectはrectangle（長方形）の略。self.rectに弾の位置と大きさをまとめます。
        # pygame.Rectは左端・上端・幅・高さの順で指定します。まず左上を(0, 0)にします。
        # size[0]は組の最初の値で幅、size[1]は2番目の値で高さです。この章は6と20ピクセルです。
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        # centerは長方形の中心。幅・高さを保ったまま、弾の中心を指定位置へ移します。
        # 中心が(320, 380)なら、幅6・高さ20の弾の左上は(317, 370)になります。
        self.rect.center = (x, y)
        # 縦方向の移動量speedをその弾のself.speedへ保存し、moveで毎回使います。
        self.speed = speed
        # color（色）をその弾のself.colorへ保存し、drawで黄色い弾を描くときに使います。
        self.color = color

    # move（動かす）は、battle.pyが画面を1回更新するたびに弾1発へ行う操作です。
    def move(self):
        # yは弾の長方形の上端。画面上端が0なので、yを減らすと弾が上へ進みます。
        # +=は現在の値に足して保存する指定。speed=-8なら上端が370から362へ変わります。
        self.rect.y += self.speed

    # 画面外の弾まで動かし続けないよう、弾が上下のどちらへ抜けたかを調べます。
    # is_off_screen（画面外か）は、弾全体が上下の端を越えたか調べる操作です。
    def is_off_screen(self):
        # bottomは弾の下端、topは弾の上端。HEIGHTはsettings.pyにある画面の高さ480です。
        # 下端が0より小さければ弾全体が上側、上端が480より大きければ弾全体が下側です。
        # orはどちらかを満たすか調べる指定。この章の上向きの弾にはbottom < 0が当てはまります。
        # returnは結果を返す指定。条件を満たすTrueなら、battle.pyが弾を一覧から外します。
        # 条件を満たさないFalseなら、battle.pyは弾を一覧に残します。
        return self.rect.bottom < 0 or self.rect.top > settings.HEIGHT

    # draw（描く）は弾1発を描く操作。screen（画面）はgame.pyで用意したゲーム画面の描画先です。
    def draw(self, screen):
        # pygame.draw.rectは、描画先・色・長方形の順で指定して、その範囲を塗ります。
        # この章ではself.colorに黄色の(255, 240, 100)、self.rectに幅6・高さ20の弾を持ちます。
        # 画面への表示はgame.pyのpygame.display.flip()が行います。
        pygame.draw.rect(screen, self.color, self.rect)
