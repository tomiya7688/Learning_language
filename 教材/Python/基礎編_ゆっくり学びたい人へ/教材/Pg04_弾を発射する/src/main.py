# 起動と終了の順序をゲームの移動処理へ混ぜると、準備や片付けの場所を探しにくくなります。
# 弾の移動量はsettings.pyのBULLET_SPEED、位置を変える計算はbullet.pyのmoveで変更します。起動はmain.pyです。
# main（開始する処理）へPygameの準備・ゲームの実行・終了後の片付けをまとめます。
# Pythonがゲーム画面・キー入力・描画を扱う道具pygameを読み込みます。
import pygame
# Pythonが同じsrcフォルダのgame.pyから、画面と進行をまとめるGame（ゲーム全体）の定義を読み込みます。
from game import Game

# defは名前を付けた処理の定義。main()と書くと、Pythonがmainの字下げした処理を実行します。
def main():
    # pygame.init()がPygameの各機能を使う準備をします。ゲームのウィンドウはGame()で作ります。
    pygame.init()
    # Pythonは、このtry内のGame()とgame.run()が正常に終わった場合も、エラーで中断した場合もfinallyへ進みます。
    try:
        # PythonがGame()でゲーム画面と進行に必要な情報を作り、変数gameから使えるようにします。
        game = Game()
        # game.run()が操作の確認と画面更新を繰り返します。閉じる操作でrunが終わると、Pythonはfinallyへ進みます。
        game.run()
    finally:
        # pygame.quit()が使用中のPygameの機能を片付け、開いていたゲームのウィンドウを閉じます。
        # Game()やgame.run()のエラーはfinallyでは解決されず、片付けの後にPythonがエラーを表示します。
        pygame.quit()

# __name__はPythonが付ける名前。main.pyを直接実行したとき、Pythonは__name__を"__main__"にします。
# ==は等しいか調べる記号。main.pyを読み込んだだけの場合、Pythonは次のmain()を実行しません。
if __name__ == "__main__":
    # Pythonがmain()を実行し、Pygameの準備からゲームの実行・終了後の片付けまでを開始します。
    main()
