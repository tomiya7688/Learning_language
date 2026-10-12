# Pythonが、自機の位置を長方形で扱い、三角形を描くpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから自機の初期位置・移動量・体力と自機弾の移動量を読み込みます。
import settings
# Pythonが、同じsrcのbullet.pyから弾1発の位置・移動・描画をまとめるBullet（弾）の定義を読み込みます。
from bullet import Bullet

# Player（自機）は、自機の位置や体力と、それを変える操作が同じ機体のものだと分かるよう、情報と操作をまとめるクラスです。
class Player:
    # Playerは、毎回の移動で初期位置へ戻さないよう、作成時の準備を__init__、位置変更をmoveに分けます。selfは作成する自機1機を指します。
    def __init__(self):
        # rectはrectangle（長方形）の略。自機の位置・大きさと命中判定に使い、drawで三角形の3点を選ぶときも使います。
        # pygame.Rectへ左端0・上端0・幅40・高さ40ピクセルを指定します。次のcenterで自機の初期位置へ移します。
        self.rect = pygame.Rect(0, 0, 40, 40)
        # center（中心）へ(settings.PLAYER_X, settings.PLAYER_Y)を指定し、幅と高さを変えず中心を移します。初期値(320, 400)なら左端300・上端380です。
        self.rect.center = (settings.PLAYER_X, settings.PLAYER_Y)

        # speedは移動量。押した矢印の方向ごとに、更新1回で進むピクセル数です。
        # Playerは作成時のsettings.PLAYER_SPEEDをself.speedへ持ち、後のmoveで使います。初期値は方向ごとに5ピクセルです。
        self.speed = settings.PLAYER_SPEED

        # hpはhit points（体力）の略。Playerは自機の体力をself.hpへ持ち、take_damageで命中した敵弾1発ごとに1減らします。
        # Player.__init__がsettings.PLAYER_HPの作成時の値をself.hpへ保存します。同じ更新のBattle.updateが終わった後に、Game.runがBattle.is_game_overで自機のHPが0以下かを確認します。
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

    # Playerは、命中の位置判定と自機の体力変更を混ぜないよう、自機のHP変更をtake_damage（ダメージを受ける）へまとめ、位置判定はhit_playerへ任せます。
    def take_damage(self):
        # -=は引いた結果を同じ場所へ保存する書き方。Player.take_damageが自機のself.hpから1を引きます。HPを0で止める処理はありません。
        # Player.take_damageは画面の表示やゲームの終了を行いません。Battle.is_game_overが更新後の自機のHPが0以下かを調べて結果を返し、Game.runが終了を決めます。
        self.hp -= 1

    # 位置の情報を用意するだけでは自機の絵が出ないため、draw（描画）へ現在の位置に自機を描く処理を分けます。
    def draw(self, screen):
        # screenはBattle.drawが指定した描画先。points（点の一覧）は自機の三角形を結ぶ3点で、更新後のself.rectから選びます。
        # midtop（上辺の中央）・bottomleft（左下）・bottomright（右下）の順です。初期位置なら(320, 380)・(300, 420)・(340, 420)です。
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # polygon（多角形）は点を順に結ぶ図形。pygame.draw.polygonへ描画先screen・水色(100, 200, 255)・3点の一覧pointsを指定します。
        # 太さの指定がないので三角形の内側を塗ります。self.rectの長方形を描く操作や、ウィンドウの表示を更新する操作ではありません。
        pygame.draw.polygon(screen, (100, 200, 255), points)
