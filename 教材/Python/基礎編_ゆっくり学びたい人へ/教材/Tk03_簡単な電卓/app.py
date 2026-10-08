# 同じフォルダの calculator.py から電卓の CalculatorApp を読み込む
from calculator import CalculatorApp


# 電卓の起動処理を main にまとめる
def main():
    # app（アプリ）に CalculatorApp() で作った電卓を入れる
    app = CalculatorApp()
    # app のウィンドウを表示し、利用者の操作を待つ
    app.run()


# このファイルを直接実行したときだけ main() を呼び出す
if __name__ == "__main__":
    main()
