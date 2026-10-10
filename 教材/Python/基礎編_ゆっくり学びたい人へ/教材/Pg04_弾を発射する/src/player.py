# 自機の位置と、その自機を動かす・弾を撃つ・描く操作を別々に置くと対応を探しにくくなります。
# Player（プレイヤー）へ、操作する自機1機の情報と操作をまとめます。
# ピクセルはゲーム画面の位置や大きさを数える単位。ゲーム画面の左上が横0・縦0で、ゲーム画面の横・縦の位置の値は右・下へ進むほど増えます。
# pygame はキーの状態を調べ、長方形で位置を扱い、画面へ図形を描く道具です。
import pygame
# settings は同じsrcフォルダのsettings.py。画面の大きさ、自機の初期位置、移動量を読み込みます。
import settings
# 同じsrcフォルダのbullet.pyから、弾1発の情報と操作をまとめたBullet（弾）を読み込みます。
from bullet import Bullet

# クラスは情報と操作をまとめた定義です。Playerは操作する自機1機を作るための定義です。
class Player:
    # 初期設定・移動・発射・描画を分けると、弾を出す位置や大きさを変えたいときはshootを探せます。
    # __init__は、battle.pyがPlayer()で自機を作るときにPythonが実行する初期設定です。
    # selfは今設定する自機1機を表す名前。self.rectのように、その自機の情報を持たせます。
    def __init__(self):
        # rectはrectangle（長方形）の略。self.rectに自機の位置と幅・高さをまとめます。
        # pygame.Rectは左端・上端・幅・高さの順。左上(0, 0)、幅40・高さ40で作ります。
        self.rect = pygame.Rect(0, 0, 40, 40)
        # centerは中心。settings.pyのPLAYER_X（横の中心）320、PLAYER_Y（縦の中心）400へ移します。
        # 幅・高さ40を保つので、自機の長方形の左上は(300, 380)になります。
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # speedは速さの指定。この自機が1回の更新で横・縦それぞれに進む量（ピクセル）です。
        # settings.pyのPLAYER_SPEED=5を自機のself.speedへ入れ、moveで毎回使います。
        self.speed = settings.PLAYER_SPEED

    # move（動かす）は、battle.pyが画面を1回更新するたびに自機へ行う操作です。
    # keys（キーの状態）は、pygame.key.get_pressed()で調べた、各キーが押されているかの情報です。
    # ifは条件を満たすとき、その下の字下げした行を実行する書き方です。
    def move(self, keys):
        # K_LEFTは左矢印。keys[pygame.K_LEFT]がTrue（押されている）なら左へ動かします。
        if keys[pygame.K_LEFT]:
            # xは長方形の左端。-=は引いた値を同じ場所へ入れる指定で、初期位置300なら295になります。
            self.rect.x -= self.speed
        # K_RIGHTは右矢印。押されていれば左端の値を増やし、自機全体を右へ動かします。
        if keys[pygame.K_RIGHT]:
            # +=は足した値を同じ場所へ入れる指定。右だけを押した更新なら、初期位置300が305になります。
            self.rect.x += self.speed
        # K_UPは上矢印。押されていれば上端の値を減らし、自機全体を上へ動かします。
        if keys[pygame.K_UP]:
            # yは長方形の上端。初期位置380から移動量5を引くと375になります。
            self.rect.y -= self.speed
        # K_DOWNは下矢印。押されていれば上端の値を増やし、自機全体を下へ動かします。
        if keys[pygame.K_DOWN]:
            # 下だけを押した更新なら、初期位置380に移動量5を足して385にします。
            self.rect.y += self.speed
        # 4つのifはそれぞれ調べます。右と上なら横へ+5・縦へ-5進み、同じ軸の両矢印なら相殺します。
        # キーがFalse（押されていない）なら、そのキーのif内の位置変更は行いません。
        # 自機が画面から出ないよう、clamp（範囲内に収める）で自機の長方形の位置を戻します。
        # ipはin place（その場で）の略。新しい長方形を返さず、自機のself.rect自体を変更します。
        # settings.pyのWIDTH=640・HEIGHT=480で画面全体の長方形を指定します。
        # 自機は40x40なので左端は0〜600、上端は0〜440。右端へ進んで左端が605なら600へ戻します。
        self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

    # shoot（発射）は、battle.pyがスペースキーを押した知らせを受けたときに実行する操作です。
    def shoot(self):
        # centerxは自機の横の中心、topは上端。初期位置なら(320, 380)を弾の中心へ指定します。
        # settings.pyのBULLET_SPEEDを負にして、新しい弾が更新1回で上へ進む量として指定します。
        # (6, 20)は弾の幅6・高さ20。色は赤・緑・青の強さを0〜255で指定し、黄色にします。
        # returnは作った弾を呼び出したbattle.pyへ返す指定。Battleが弾の一覧へ加えます。
        return Bullet(self.rect.centerx, self.rect.top, -settings.BULLET_SPEED,
                      (6, 20), (255, 240, 100))

    # draw（描く）は、battle.pyが自機を描くときに実行する操作です。
    # screen（画面）は、game.pyが用意したゲーム画面の描画先です。
    def draw(self, screen):
        # points（点の一覧）に、自機の上辺の真ん中・左下・右下を、この順で入れます。
        # midtop、bottomleft、bottomrightは長方形の辺や角の位置。初期位置なら(320,380)、(300,420)、(340,420)。
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # polygon（多角形）は点を順に結ぶ図形。pygame.draw.polygonは描画先・色・点の一覧を指定します。
        # 赤100・緑200・青255で3点の内側を水色に塗り、上向きの三角形で自機を描きます。
        # self.rectの長方形自体は描きません。描いた画面を表示するのはgame.pyのpygame.display.flip()です。
        pygame.draw.polygon(screen, (100, 200, 255), points)
