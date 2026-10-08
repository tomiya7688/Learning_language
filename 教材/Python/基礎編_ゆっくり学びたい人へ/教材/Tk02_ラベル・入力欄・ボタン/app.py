# tkinterを、このプログラムで使えるようにする
import tkinter


# 名前入力欄と挨拶表示をまとめる GreetingApp クラスを定義する
class GreetingApp:
    # GreetingApp の画面と部品を用意する __init__ を定義する
    def __init__(self):
        # self.window に tkinter.Tk() で作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「挨拶アプリ」にする
        self.window.title("挨拶アプリ")
        # self.window の大きさを横400、縦220にする
        self.window.geometry("400x220")

        # self.name_label に名前の入力を案内するLabelを入れる
        self.name_label = tkinter.Label(self.window, text="名前を入力してください")
        # self.name_label を self.window 内に配置する
        self.name_label.pack()

        # self.name_entry に1行の名前入力欄を入れる
        self.name_entry = tkinter.Entry(self.window)
        # self.name_entry を self.window 内に配置する
        self.name_entry.pack()

        # self.greet_button に挨拶を表示するボタンを入れる
        self.greet_button = tkinter.Button(
            self.window,
            text="挨拶する",
            # ボタンを押したときに呼ぶ処理として self.show_greeting を登録する
            command=self.show_greeting,
        )
        # self.greet_button を self.window 内に配置する
        self.greet_button.pack()

        # self.result_label に空の文字列を表示するLabelを入れる
        self.result_label = tkinter.Label(self.window, text="")
        # self.result_label を self.window 内に配置する
        self.result_label.pack()

    # 入力された名前で挨拶する show_greeting を定義する
    def show_greeting(self):
        # name に self.name_entry から取り出した文字列を入れる
        name = self.name_entry.get()
        # self.result_label の表示を「こんにちは 」と name をつないだ文字列に変える
        self.result_label.config(text=f"こんにちは {name}")

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()


# アプリの起動処理を main にまとめる
def main():
    # app に GreetingApp() で作ったアプリを入れる
    app = GreetingApp()
    # app のウィンドウを表示し、利用者の操作を待つ
    app.run()


# このファイルを直接実行したときだけ main() を呼び出す
if __name__ == "__main__":
    main()
