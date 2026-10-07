# pygame を読み込む
import pygame
# game から Game を読み込む
from game import Game

# main の処理を定義する
def main():
    # pygame.init() を実行する
    pygame.init()
    # 終了時にfinallyの片付けが行われるように、ゲームを動かす
    try:
        # game はゲーム全体。起動・繰り返し・画面切り替えを担当します。
        # game に Game() を入れる
        game = Game()
        # game.run() を実行する
        game.run()
    finally:
        # pygame.quit() を実行する
        pygame.quit()

# このファイルを直接実行したときだけ main() を実行する
if __name__ == "__main__":
    # main() を実行する
    main()
