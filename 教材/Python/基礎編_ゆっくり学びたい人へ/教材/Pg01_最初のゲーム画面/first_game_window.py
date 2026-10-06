# pygame を読み込む
import pygame

# main の処理を定義する
def main():
    # pygame.init() を実行する
    pygame.init()
    # 終了時にfinallyの片付けが行われるように、ゲームを動かす
    try:
        # screen は画面。pygameが用意した描画先です。
        # screen に pygame.display.set_mode((640, 480)) を入れる
        screen = pygame.display.set_mode((640, 480))
        # pygame.display.set_caption('最初のゲーム画面') を実行する
        pygame.display.set_caption('最初のゲーム画面')

        # clock は時計。画面更新を最大60回/秒に調整します。
        # clock に pygame.time.Clock() を入れる
        clock = pygame.time.Clock()

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

            # screen.fill((10, 10, 30)) を実行する
            screen.fill((10, 10, 30))

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
