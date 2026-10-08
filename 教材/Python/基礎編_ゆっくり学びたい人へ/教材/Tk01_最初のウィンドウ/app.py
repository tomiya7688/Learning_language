# tkinterを、このプログラムで使えるようにする
import tkinter


# ウィンドウと設定をまとめる App クラスを定義する
class App:
    # App の初期設定を行う __init__ を定義する
    def __init__(self):
        # self.window に tkinter.Tk() で作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「はじめてのGUI」にする
        self.window.title("はじめてのGUI")
        # self.window の大きさを横400、縦300にする
        self.window.geometry("400x300")

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()


# アプリの起動処理を main にまとめる
def main():
    # app に App() で作ったアプリを入れる
    app = App()
    # app のウィンドウを表示し、利用者の操作を待つ
    app.run()


# このファイルを直接実行したときだけ main() を呼び出す
if __name__ == "__main__":
    main()
