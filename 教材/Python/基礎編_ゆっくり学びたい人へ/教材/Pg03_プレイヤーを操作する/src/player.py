# pygame を読み込む
import pygame

# Player という型を宣言する
class Player:
    # __init__ の処理を宣言する
    def __init__(self):
        # rect はrectangle（長方形）の略。自機の位置・大きさに使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (320, 400) を入れる
        self.rect.center = (320, 400)
        # self.speed に 5 を入れる
        self.speed = 5

    # move の処理を宣言する
    def move(self, keys):
        # keys[pygame.K_LEFT] が成り立つなら
        if keys[pygame.K_LEFT]:
            # self.rect.x から self.speed を引く
            self.rect.x -= self.speed
        # keys[pygame.K_RIGHT] が成り立つなら
        if keys[pygame.K_RIGHT]:
            # self.rect.x に self.speed を足す
            self.rect.x += self.speed
        # keys[pygame.K_UP] が成り立つなら
        if keys[pygame.K_UP]:
            # self.rect.y から self.speed を引く
            self.rect.y -= self.speed
        # keys[pygame.K_DOWN] が成り立つなら
        if keys[pygame.K_DOWN]:
            # self.rect.y に self.speed を足す
            self.rect.y += self.speed
        # self.rect.clamp_ip(pygame.Rect(0, 0, 640, 480)) を実行する
        self.rect.clamp_ip(pygame.Rect(0, 0, 640, 480))

    # 位置の情報を用意するだけでは自機の絵が出ないため、draw（描画）へ現在の位置に自機を描く処理を分けます。
    def draw(self, screen):
        # screenは呼び出す側が指定した描画先です。points（点の一覧）は現在の自機の三角形を結ぶ3つの位置です。
        # self.rect.midtopは上辺の真ん中、self.rect.bottomleftは左下、self.rect.bottomrightは右下で、pointsへその順に入れます。
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # polygon（多角形）は点を順に結ぶ図形。pygame.draw.polygonへ描画先screen・水色(100, 200, 255)・3点の一覧pointsを指定します。
        # 太さの指定がないので三角形の内側を塗ります。self.rectの長方形を描く操作や、ウィンドウの表示を更新する操作ではありません。
        pygame.draw.polygon(screen, (100, 200, 255), points)
