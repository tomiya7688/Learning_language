# pygame を読み込む
import pygame
# game から Game を読み込む
from game import Game

# main の処理を定義する
def main():
    # pygame.init() を実行する
    pygame.init()
    # Pythonは try: の処理が終わったときもエラーで中断したときも、finally: の下の pygame.quit() を実行する
    try:
        # game はゲーム全体を表し、ゲーム画面や実行状態を持ちます。
        # game に Game() を入れる
        game = Game()
        # game.run() を実行する
        game.run()
    finally:
        # pygameを終了する
        pygame.quit()

# このファイルを直接実行したときだけ main() を実行する
if __name__ == "__main__":
    # main() を実行する
    main()
