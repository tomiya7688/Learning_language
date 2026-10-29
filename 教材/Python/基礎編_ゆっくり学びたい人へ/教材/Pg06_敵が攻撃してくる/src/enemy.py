# Pythonが、敵の位置を長方形で管理し、描画先へ色を塗るpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから敵の移動量・画面の高さ・敵弾の移動量を読み込みます。
import settings
# Pythonが、同じsrcのbullet.pyから弾1発の情報と操作をまとめたBullet（弾）の宣言を読み込みます。
from bullet import Bullet

# Enemy（敵）は、敵ごとに異なる位置と、その敵を動かす・撃たせる・描く操作を対応させるため、敵1機の情報と操作をまとめるクラスです。
# Battle.__init__が敵を作り、Battleの敵一覧self.enemiesへ追加します。
# Battle.update_enemiesが敵を動かして画面外の敵を一覧から外し、発射の更新では残った敵のshootを呼び出します。
class Enemy:
    # Enemyは、毎回の移動で開始位置へ戻さないよう、情報の準備を__init__、位置変更をmoveに分けて宣言します。
    # selfは作成する敵1機。PythonがEnemy(x, y)を実行すると、__init__が指定された中心位置でその敵の情報を用意します。
    def __init__(self, x, y):
        # rectはrectangle（長方形）の略。pygame.Rectへ左端・上端・幅・高さを指定し、敵の位置と大きさをself.rectへ保存します。
        self.rect = pygame.Rect(0, 0, 40, 40)
        # center（中心）へ(x, y)を指定し、敵の幅40・高さ40を保って中心を指定位置へ移します。ピクセルは画面の位置や大きさを数える単位です。
        self.rect.center = (x, y)
        # speedは速さの指定。settings.ENEMY_SPEEDは更新1回で敵が下へ進む量で、作成時の値を敵のself.speedへ保存します。
        self.speed = settings.ENEMY_SPEED

    # Enemyは、作成時の準備と作成後の位置変更の実行時点が違うため、更新ごとの位置変更をmove（移動）へまとめます。
    def move(self):
        # self.rect.yは敵の上端。+=は足した結果を同じ場所へ保存する書き方で、上端へ保存済みの移動量self.speedを足します。
        # Enemy.moveは敵の横位置と大きさを変えず、中心と下端も上端と同じ量だけ縦へ移します。
        self.rect.y += self.speed

    # Enemyは、敵1機の位置の比較へ戦闘の一覧変更まで混ぜないよう、判定をis_off_screen、一覧からの除外をBattle.update_enemiesへ分けます。
    def is_off_screen(self):
        # Enemy.is_off_screenは敵の上端self.rect.topがゲーム画面の高さsettings.HEIGHTより大きいかを調べ、結果をBattle.update_enemiesへ返します。
        # 上端が高さと等しい場合はFalse（成り立たない）、大きい場合はTrue（成り立つ）です。敵の位置や一覧は変更しません。
        return self.rect.top > settings.HEIGHT

    # Enemyは、敵の位置から弾を作る処理へ戦闘の一覧変更まで混ぜないよう、作成をshoot（発射）へまとめ、追加はBattle.update_enemiesへ任せます。
    def shoot(self):
        # Enemy.shootは敵の横の中心self.rect.centerxと下端self.rect.bottomを、新しい弾の中心位置としてBulletへ指定します。
        # settings.ENEMY_BULLET_SPEEDは下への移動量（ピクセル/回）、(8, 16)は幅・高さ、(255, 100, 180)は赤・緑・青の強さを指定したピンクです。
        # returnが作成した弾1発をBattle.update_enemiesへ返します。Enemy.shoot自体は一覧への追加・弾の移動・描画を行いません。
        return Bullet(self.rect.centerx, self.rect.bottom,
                      settings.ENEMY_BULLET_SPEED, (8, 16), (255, 100, 180))

    # Enemyは、位置の情報だけでは敵の絵が出ないため、位置変更をmove、描画先へ色を塗る処理をdraw（描画）に分けて宣言します。
    def draw(self, screen):
        # screenはBattle.drawが指定した描画先。pygame.draw.rectへ描画先・赤系の色・敵の位置と大きさを持つself.rectを指定します。
        # pygame.draw.rectは太さを指定しない場合、長方形の内側を塗ります。敵の位置変更やウィンドウの表示更新は行いません。
        pygame.draw.rect(screen, (255, 100, 100), self.rect)
