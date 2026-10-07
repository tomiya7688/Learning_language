# pygame を読み込む
import pygame

# Player という型を定義する
class Player:
    # __init__ の処理を定義する
    def __init__(self):
        # rect はrectangle（長方形）の略。自機の位置・大きさに使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (320, 400) を入れる
        self.rect.center = (320, 400)
        # self.speed に 5 を入れる
        self.speed = 5

    # move の処理を定義する
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

    # draw の処理を定義する
    def draw(self, screen):
        # points は自機の三角形を結ぶ3点の一覧です。
        # points に [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright] を入れる
        points = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
        # pygame.draw.polygon(screen, (100, 200, 255), points) を実行する
        pygame.draw.polygon(screen, (100, 200, 255), points)
