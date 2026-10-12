# 敵が3機いると、各敵の位置と、その敵を動かす・描く操作を対応させる必要があります。
# Enemy（敵）へ1機分の位置・大きさ・移動量と、その敵の操作をまとめます。
# ピクセルはゲーム画面の位置や大きさを数える単位です。画面の左上は横0・縦0で、縦の値は下へ増えます。
# pygameは、位置を長方形で管理し、ゲーム画面へ長方形を描く道具です。
import pygame
# 同じsrcフォルダのsettings.pyから、敵の移動量ENEMY_SPEEDと画面の高さHEIGHTを読み込みます。
import settings

# クラスは情報と操作をまとめる定義。Enemyは敵1機を作るための定義です。
class Enemy:
    # 敵を作る・動かす・画面外か調べる・描く処理を分けて、各操作を探しやすくします。
    # __init__はEnemy(...)で敵を作るときにPythonが実行する初期設定の処理です。
    # selfは今設定する敵1機。self.rectやself.speedのように、その敵の情報を保持します。
    # x（横）/y（縦）は敵の中心位置。画面左端から右へx、画面上端から下へyピクセルです。
    # battle.pyのBattle（戦闘）はEnemy(160, 80)、Enemy(320, 40)、Enemy(480, 100)で3機を作ります。
    def __init__(self, x, y):
        # rectはrectangle（長方形）の略。self.rectに敵の位置と幅・高さをまとめます。
        # pygame.Rectは左端・上端・幅・高さの順。幅40・高さ40で、まず左上を(0, 0)にします。
        # 長方形の情報を作るだけでは敵は描かれません。敵を描く操作は下のdrawです。
        self.rect = pygame.Rect(0, 0, 40, 40)
        # centerは長方形の中心。幅・高さを保ったまま、敵の中心を指定位置へ移します。
        # 中心が(160, 80)なら幅・高さの半分20を引き、敵の左上は(140, 60)になります。
        self.rect.center = (x, y)
        # speedは速さの指定。敵を作るときにENEMY_SPEEDをその敵のself.speedへ保持します。
        # 配布時のENEMY_SPEED=1なら、敵は更新1回で下へ1ピクセル進みます。
        # 起動中のゲームのウィンドウを閉じ、settings.pyを保存してからsrc/main.pyを再実行してください。敵は保存後の移動量で作り直されます。
        self.speed = settings.ENEMY_SPEED

    # move（動かす）は、Battle.update_enemiesが更新のたびに敵1機へ行う操作です。
    def move(self):
        # self.rect.yは敵の長方形の上端。+=は今の値に右側の値を足す書き方です。
        # 移動量1なら、上端60・中心80の敵は上端61・中心81へ進みます。横の位置は変えません。
        self.rect.y += self.speed

    # is_off_screen（画面外か）は、敵の上端が画面下端を越えたか調べる操作です。
    def is_off_screen(self):
        # topは敵の上端、HEIGHTは画面の高さ480。>は左の値が右の値より大きいか調べます。
        # returnは調べた結果を呼び出したBattleへ返す指定。481 > 480はTrue（当てはまる）です。
        # 高さ480・移動量1の設定では、上端480はFalse（当てはまらない）。敵は見えませんが一覧へ残り、次の更新で上端481になります。
        # Enemy.is_off_screenは敵を削除しません。self.rect.top > settings.HEIGHTがTrueなら、Battle.update_enemiesが判定対象の敵を一覧から外します。
        return self.rect.top > settings.HEIGHT

    # draw（描く）は、Battle.drawが一覧に残っている敵1機へ行う操作です。
    # screenはgame.pyが用意し、Battleから指定されたゲームの描画先です。
    def draw(self, screen):
        # pygame.draw.rectがself.rectの位置・大きさで、塗りつぶした赤い長方形をscreenへ描きます。
        # 色の組は赤・緑・青の強さを0〜255で指定します。(255, 100, 100)は赤を強くした色です。
        # 描いた画面を表示するのはgame.pyのpygame.display.flip()です。
        pygame.draw.rect(screen, (255, 100, 100), self.rect)
