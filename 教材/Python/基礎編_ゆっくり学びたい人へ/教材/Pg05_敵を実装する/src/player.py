# Pythonが、自機の位置を長方形で扱い、画面へ図形を描くpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから画面の大きさ、自機の開始位置と移動量、弾の移動量を読み込みます。
import settings
# Pythonが、同じsrcのbullet.pyから弾1発の情報と操作をまとめるBullet（弾）の定義を読み込みます。
from bullet import Bullet

# 自機の位置と、移動・発射・描画する操作を別々に置くと、どの自機の位置を使うか追いにくくなります。
# Player（プレイヤー）へ、操作する自機1機の情報と、その自機を操作する処理をまとめます。
class Player:
    # 移動のたびに位置を初期値へ戻さないよう、__init__（作成時の準備）へ開始位置と移動量の保存を分けます。
    # selfは今用意している自機1機です。PythonがBattle.__init__内のPlayer()を実行すると、Player.__init__が情報を用意します。
    def __init__(self):
        # rectはrectangle（長方形）の略。self.rectが自機の位置・大きさを持ち、移動・発射・描画で同じ位置を使います。
        # pygame.Rectへ左端・上端・幅・高さをピクセル（画面の位置や大きさの単位）で指定し、左上(0, 0)・幅40・高さ40を用意します。
        self.rect = pygame.Rect(0, 0, 40, 40)
        # centerは中心。self.rect.centerへsettings.PLAYER_X（横の中心）とsettings.PLAYER_Y（縦の中心）を指定して位置を変えます。
        # 配布時の中心は(320, 400)なので、幅・高さ40の自機の左上は(300, 380)です。中心の設定は幅・高さを変えません。
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # speedは速さの指定。self.speedは、自機が更新1回で横・縦それぞれに進む量（ピクセル）です。
        # Player.__init__がsettings.PLAYER_SPEEDをself.speedへ保存し、Player.moveが後の更新で同じ保存値を使います。
        self.speed = settings.PLAYER_SPEED

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
        # 同じ軸の逆向きの矢印は相殺され、右と上なら横・縦をそれぞれself.speedだけ変えて斜めに動きます。
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

    # 位置の情報を用意するだけでは自機の絵が出ないため、draw（描画）へ現在の位置に自機を描く処理を分けます。
    def draw(self, screen):
        # screenは呼び出す側が指定した描画先です。points（点の一覧）は現在の自機の三角形を結ぶ3つの位置です。
        # self.rect.midtopは上辺の真ん中、self.rect.bottomleftは左下、self.rect.bottomrightは右下で、pointsへその順に入れます。
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # polygon（多角形）は点を順に結ぶ図形。pygame.draw.polygonへ描画先screen・水色(100, 200, 255)・3点の一覧pointsを指定します。
        # 太さの指定がないので三角形の内側を塗ります。self.rectの長方形を描く操作や、ウィンドウの表示を更新する操作ではありません。
        pygame.draw.polygon(screen, (100, 200, 255), points)
