# main（開始する処理）へ、Pygameの準備・ゲームの実行・終了後の片付けをまとめます。
# 弾の移動を変えるときはbattle.pyやbullet.pyを編集し、起動するファイルはmain.pyに保ちます。
# pygameは、ゲーム画面・キー入力・描画を扱う道具です。
import pygame
# 同じsrcフォルダのgame.pyから、画面とゲームの進行をまとめたGame（ゲーム）を読み込みます。
from game import Game

# defは名前を付けた処理の定義。main()と書くと、Pythonが下の字下げした処理を実行します。
def main():
    # Pygameが画面やキー入力を使うための準備をします。ウィンドウを作るのは次のGame()です。
    pygame.init()
    # ゲームが終わった場合も、このtry内でエラーが起きた場合も、finallyでPygameを片付けます。
    try:
        # gameはゲーム全体。Game()がウィンドウと戦闘を作り、gameという名前であとから使います。
        game = Game()
        # Gameのrun（動かす）が操作の確認・位置更新・描画・表示を繰り返し、閉じる操作で終わります。
        game.run()
    finally:
        # pygame.quit()はPygameを終了し、開いたゲームのウィンドウも閉じます。
        # try内のエラーを無かったことにはせず、片付けの後にPythonがエラーを表示します。
        pygame.quit()

# __name__はPythonが付ける名前。main.pyを直接実行したときは"__main__"になります。
# ==は同じか調べる書き方。別ファイルからmain.pyを読み込んだだけのときは下の処理を実行しません。
if __name__ == "__main__":
    # 直接実行したmain.pyから、上で定義したmainの準備・実行・片付けを開始します。
    main()
