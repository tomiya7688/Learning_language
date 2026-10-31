# Pythonが、長方形の位置を管理し、描画先へ色を塗るpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから画面の高さHEIGHTなどの設定を読み込みます。
import settings

# Bullet（弾）は、弾ごとの情報と操作を対応させるため、弾1発の位置・移動量・色と、その弾の操作をまとめるクラスです。
# Battle.handle_eventがself.player.shoot()で作った弾を、Battleの自機の弾一覧self.bulletsへ追加します。
# Battle.update_enemiesがenemy.shoot()で作った弾を、Battleの敵の弾一覧self.enemy_bulletsへ追加します。
# Battle.update_bossがself.boss.shoot()で作った弾を、Battleのボスの弾一覧self.boss_bulletsへ追加します。
# Battle.move_bulletsが、Battleの弾一覧self.bullets（自機の弾）・self.enemy_bullets（敵の弾）・self.boss_bullets（ボスの弾）から画面外の弾を外します。
# collisions.pyのhit_enemiesが、敵に命中した弾をBattleの自機の弾一覧self.bulletsから外します。
# collisions.pyのhit_playerが、自機に命中した弾をBattleの敵の弾一覧self.enemy_bulletsから外します。
# collisions.pyのhit_playerが、自機に命中した弾をBattleのボスの弾一覧self.boss_bulletsから外します。
# collisions.pyのhit_bossが、ボスに命中した弾をBattleの自機の弾一覧self.bulletsから外します。
# Battle.update_bossがボスを出すとき、Battleの自機の弾一覧self.bulletsをclear()で空にします。
class Bullet:
    # Bulletは、移動のたびに開始位置へ戻さないよう、作成時の情報の準備を__init__、毎回の位置変更をmoveに分けて宣言します。
    # selfは作成する弾1発。PythonがBullet(...)を実行すると、この弾の__init__へ指定した値を渡します。
    def __init__(self, x, y, speed, size, color):
        # x（横）・y（縦）は弾の中心位置で、ゲーム画面の左端・上端から右・下へ数えるピクセル数です。
        # size（大きさ）は幅・高さの組。size[0]は最初の値の幅、size[1]は2番目の値の高さです。
        # rectはrectangle（長方形）の略。pygame.Rectは左端・上端・幅・高さの順で指定し、self.rectへ弾の位置・大きさを保存します。
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        # center（中心）へ(x, y)を指定し、幅・高さを保って弾の中心を呼び出し側が指定した位置へ移します。
        self.rect.center = (x, y)
        # speed（速さの指定）は更新1回で縦に進む量。負なら上、正なら下、0なら縦の位置を変えません。
        # __init__が指定されたspeedを弾のself.speedへ保存し、Bullet.moveが後の更新でその保存値を使います。
        self.speed = speed
        # color（色）は赤・緑・青の強さを0〜255で指定した組。弾のself.colorへ保存し、Bullet.drawが描画に使います。
        self.color = color

    # Bulletは、弾の作成と毎回の位置変更の実行時点が違うため、更新ごとの位置変更をmove（移動）にまとめます。
    def move(self):
        # self.rect.yは弾の上端。+=は足した結果を同じ場所へ保存する指定で、上端をself.speedだけ変えて弾全体を縦へ動かします。
        # 幅・高さ・横の位置は変えません。中心と下端の縦の位置も、上端と同じ量だけ変わります。
        self.rect.y += self.speed

    # Bulletは、弾1発の位置の比較へ戦闘の一覧変更まで混ぜないよう、上下の判定をis_off_screenにまとめ、一覧からの除外はBattle.move_bulletsへ任せます。
    # is_off_screen（画面外か）は上下の位置を比較して結果だけを返します。Battle.move_bulletsが結果を受け取り、Trueの弾を指定された弾一覧から外します。
    def is_off_screen(self):
        # self.rect.bottomは弾の下端、self.rect.topは上端。settings.HEIGHTはゲーム画面の高さです。
        # 下端が画面の上端0より小さいか、上端が画面の高さより大きいかを、or（どちらかが成り立つか）で調べます。
        # returnがTrue（どちらかが成り立つ）かFalse（両方とも成り立たない）をBattle.move_bulletsへ返します。位置や一覧は変更しません。
        # 下端が0と同じなら上側の比較はFalse、上端が画面の高さと同じなら下側の比較はFalseです。横の位置は調べません。
        return self.rect.bottom < 0 or self.rect.top > settings.HEIGHT

    # Bulletは、位置の情報だけでは弾の絵が出ないため、位置変更をmove、描画先へ色を塗る処理をdrawに分けて宣言します。
    def draw(self, screen):
        # screenはBattle.draw_bulletsが指定した描画先。pygame.draw.rectへ描画先・弾の保存済みの色・位置と大きさを持つ長方形を指定します。
        # 太さを指定していないので、弾の長方形の内側を塗ります。弾の位置変更や、ウィンドウの表示更新は行いません。
        pygame.draw.rect(screen, self.color, self.rect)
