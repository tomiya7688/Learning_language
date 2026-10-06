# pygame を読み込む
import pygame

# Player という型を定義する
class Player:
    # __init__ の処理を定義する
    def __init__(self):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(0, 0, 40, 40) を入れる
        self.rect = pygame.Rect(0, 0, 40, 40)
        # self.rect.center に (320, 400) を入れる
        self.rect.center = (320, 400)

        # speed は速さ。1回の更新で動く距離で、単位はピクセルです。
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

# main の処理を定義する
def main():
    # pygame.init() を実行する
    pygame.init()
    # 終了時にfinallyの片付けが行われるように、ゲームを動かす
    try:
        # screen は画面。pygameが用意した描画先です。
        # screen に pygame.display.set_mode((640, 480)) を入れる
        screen = pygame.display.set_mode((640, 480))
        # pygame.display.set_caption('プレイヤーを操作する') を実行する
        pygame.display.set_caption('プレイヤーを操作する')

        # clock は時計。画面更新を最大60回/秒に調整します。
        # clock に pygame.time.Clock() を入れる
        clock = pygame.time.Clock()

        # player はプレイヤー。ここでは操作する自機です。
        # player に Player() を入れる
        player = Player()

        # running は実行中かどうか。Falseで繰り返しを終えます。
        # running に True を入れる
        running = True
        # running が成り立つ間、繰り返す
        while running:
            # pygame.event.get() から event を1つずつ取り出して繰り返す
            for event in pygame.event.get():
                # event.type == pygame.QUIT が成り立つなら
                if event.type == pygame.QUIT:
                    # running は実行中かどうか。Falseで繰り返しを終えます。
                    # running に False を入れる
                    running = False
            # not running が成り立つなら
            if not running:
                # この繰り返しを終える
                break

            # player.move(pygame.key.get_pressed()) を実行する
            player.move(pygame.key.get_pressed())

            # screen.fill((10, 10, 30)) を実行する
            screen.fill((10, 10, 30))

            # player.draw(screen) を実行する
            player.draw(screen)

            # pygame.display.flip() を実行する
            pygame.display.flip()
            # clock.tick(60) を実行する
            clock.tick(60)
    finally:
        # pygame.quit() を実行する
        pygame.quit()

# __name__ == '__main__' が成り立つなら
if __name__ == "__main__":
    # main() を実行する
    main()
