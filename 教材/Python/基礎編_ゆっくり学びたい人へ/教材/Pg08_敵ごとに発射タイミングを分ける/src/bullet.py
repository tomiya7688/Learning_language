# Pythonが、長方形の位置を管理し、描画先へ色を塗るpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから画面の高さHEIGHTなどの設定を読み込みます。
import settings

# Bullet は「弾」という意味です。弾1発の位置・動く量・色と、その弾の操作をまとめます。
# 自機から撃つ弾も敵が撃つ弾も Bullet から作ります。弾ごとに別の位置・色・移動量を持てます。
# __init__ は弾を作るとき、move は作った弾を動かすときの処理です。
# is_off_screen は弾が画面の外か調べ、draw は弾を画面へ描く処理です。
# Bullet が動かすのは弾1発です。自機の弾や敵の弾を並べて持つのは Battle の仕事です。
# 弾が何かに当たったかの判定や体力の変更は、別の collisions.py にあります。
class Bullet:
    # __init__ は、弾を作るときに中心位置・縦の移動量・大きさ・色を受け取ります。
    # x は中心の横位置、y は中心の縦位置、speed は縦の移動量、size は幅と高さ、color は色です。
    def __init__(self, x, y, speed, size, color):
        # self.rect は「この弾の長方形」です。弾の位置・幅・高さをまとめて持ちます。
        # size は「大きさ」です。size[0] は0番目の幅、size[1] は1番目の高さ。(6, 20)なら幅6、高さ20です。
        # self.rect に、左上を仮の(0, 0)、幅をsize[0]、高さをsize[1]にした長方形を入れます。
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        # self.rect.center に(x, y)を入れ、弾の大きさを保ったまま中心を指定された位置へ動かします。
        self.rect.center = (x, y)
        # speed は「縦の移動量」です。1回の更新で縦に何ピクセル動くかを表します。
        # self.speed にspeedを入れます。負なら上、正なら下、0なら移動しません。
        self.speed = speed
        # color は「色」です。赤・緑・青の強さを表すcolorを、この弾のself.colorに入れます。
        self.color = color

    # move は「動かす」という意味です。この弾を1回の更新分だけ上下へ動かします。
    def move(self):
        # self.rect.y は弾の上端の縦位置です。+= は今の値に右側の値を足す書き方です。
        # self.rect.y にself.speedを足します。上端を変えると中心と下端も同じ量だけ動きます。
        self.rect.y += self.speed

    # is_off_screen は「画面外か」という意味です。弾が画面の上または下に出たか調べます。
    # 判定結果だけを返します。弾を一覧から外すのは、結果を受け取る Battle の仕事です。
    def is_off_screen(self):
        # self.rect.bottom は弾の下端、self.rect.top は上端、settings.HEIGHT は画面の高さ（480）です。
        # 弾の下端が0より小さいか、弾の上端が画面の高さ480より大きいかを調べます。
        # or は「どちらか」です。どちらかが成り立てばTrue、両方とも成り立たなければFalseを返します。
        # 下端が0・上端が480と等しいときはFalseです。弾は縦にだけ動くので横は調べません。
        return self.rect.bottom < 0 or self.rect.top > settings.HEIGHT

    # draw は「描く」という意味です。この弾の今の位置・大きさ・色で画面へ描きます。
    def draw(self, screen):
        # screen は描く先の画面、self.color はこの弾の色、self.rect はこの弾の長方形です。
        # pygame.draw.rect にscreen・self.color・self.rectを渡し、指定した長方形の内側を塗ります。
        pygame.draw.rect(screen, self.color, self.rect)
