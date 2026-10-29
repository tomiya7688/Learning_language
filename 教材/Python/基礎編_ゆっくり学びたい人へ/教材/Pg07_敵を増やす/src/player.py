# pygame を読み込む
import pygame
# settings を読み込む
import settings
# bullet から Bullet を読み込む
from bullet import Bullet

# Player という型を宣言する
class Player:
    # __init__ の処理を宣言する
    def __init__(self):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (settings.PLAYER_X, settings.PLAYER_Y) を入れる
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
        # self.speed に settings.PLAYER_SPEED を入れる
        self.speed = settings.PLAYER_SPEED

        # hp はhit points（体力）。攻撃1回で1減り、0で倒されます。
        # self.hp に settings.PLAYER_HP を入れる
        self.hp = settings.PLAYER_HP

    # 自機の位置を変える処理と弾を作る処理を混ぜないよう、move（移動）へキーの確認と位置変更をまとめます。
    def move(self, keys):
        # keysは、呼び出す側がpygame.key.get_pressed()で調べた、今押しているキーの状態です。
        # keys[pygame.K_LEFT]がTrue（左矢印キーを押している）なら、ifの下の字下げした位置変更を行います。
        if keys[pygame.K_LEFT]:
            # self.rect.xは自機の左端。-=は引いた結果を同じ場所へ保存する指定で、左端をself.speedだけ減らし、自機全体を左へ動かします。
            self.rect.x -= self.speed
        # keys[pygame.K_RIGHT]がTrue（右矢印キーを押している）なら、右へ動かす位置変更を行います。
        if keys[pygame.K_RIGHT]:
            # +=は足した結果を同じ場所へ保存する指定で、左端self.rect.xをself.speedだけ増やし、自機全体を右へ動かします。
            self.rect.x += self.speed
        # keys[pygame.K_UP]がTrue（上矢印キーを押している）なら、上へ動かす位置変更を行います。
        if keys[pygame.K_UP]:
            # self.rect.yは自機の上端。上端をself.speedだけ減らし、自機全体を上へ動かします。
            self.rect.y -= self.speed
        # keys[pygame.K_DOWN]がTrue（下矢印キーを押している）なら、下へ動かす位置変更を行います。
        if keys[pygame.K_DOWN]:
            # 上端self.rect.yをself.speedだけ増やし、自機全体を下へ動かします。
            self.rect.y += self.speed
        # 4つのifは左・右・上・下を別々に調べます。各キーがFalse（押していない）なら、そのキーの位置変更は行いません。
        # Player.moveは逆向きの矢印を両方押した場合も2回の位置変更を行い、同じ軸の座標変化は差し引き0になります。右と上なら横・縦をそれぞれself.speedだけ変えて斜めに動きます。
        # pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT)が、左上(0, 0)から画面全体の幅・高さを持つ長方形を用意します。
        # clamp_ipは位置を範囲内に収める操作で、ipはin place（その場で）の略。元のself.rectの位置を変え、幅・高さは変えません。
        # Player.moveが4方向の位置変更を終えた後に、自機の長方形が画面から出た分だけ位置を戻します。画面端では実際の移動量が小さくなります。
        self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

    # 自機の位置から弾1発を作る処理と、弾一覧へ加える処理を分けるため、shoot（発射）へ弾の作成をまとめます。
    def shoot(self):
        # self.rect.centerxは自機の横の中心、self.rect.topは上端。Bulletが作る弾の中心へ、この2つの位置を指定します。
        # -settings.BULLET_SPEEDが弾の縦方向の移動量です。画面では縦の位置が下へ増えるので、負の値を足す弾は上へ動きます。
        # (6, 20)は弾の幅6・高さ20ピクセル、(255, 240, 100)は赤・緑・青の強さを0〜255で指定した黄色です。
        # returnが新しい弾1発を呼び出す側へ返します。戦闘が持つ自機の弾一覧へ追加するのはBattle.handle_eventです。
        return Bullet(self.rect.centerx, self.rect.top, -settings.BULLET_SPEED,
                      (6, 20), (255, 240, 100))

    # take_damage の処理を宣言する
    def take_damage(self):
        # self.hp から 1 を引く
        self.hp -= 1

    # 位置の情報を用意するだけでは自機の絵が出ないため、draw（描画）へ現在の位置に自機を描く処理を分けます。
    def draw(self, screen):
        # screenは呼び出す側が指定した描画先です。points（点の一覧）は現在の自機の三角形を結ぶ3つの位置です。
        # self.rect.midtopは上辺の真ん中、self.rect.bottomleftは左下、self.rect.bottomrightは右下で、pointsへその順に入れます。
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # polygon（多角形）は点を順に結ぶ図形。pygame.draw.polygonへ描画先screen・水色(100, 200, 255)・3点の一覧pointsを指定します。
        # 太さの指定がないので三角形の内側を塗ります。self.rectの長方形を描く操作や、ウィンドウの表示を更新する操作ではありません。
        pygame.draw.polygon(screen, (100, 200, 255), points)
