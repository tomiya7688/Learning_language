# tkinterを、このプログラムで使えるようにする
import tkinter


# 電卓の入力欄・結果表示・計算処理をまとめる CalculatorApp クラスを定義する
class CalculatorApp:
    # CalculatorApp の画面と部品を用意する __init__ を定義する
    def __init__(self):
        # self.window（ウィンドウ）に tkinterのTkクラスから作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「簡単な電卓」にする
        self.window.title("簡単な電卓")
        # self.window の大きさを横400、縦260にする
        self.window.geometry("400x260")

        # self.number1_label（1つ目の数字の案内）に self.window 内で「1つ目の数字」と表示するラベルを入れる
        self.number1_label = tkinter.Label(self.window, text="1つ目の数字")
        # self.number1_label を self.window 内に配置する
        self.number1_label.pack()

        # self.number1_entry（1つ目の数字の入力欄）に self.window 内の1行の入力欄を入れる
        self.number1_entry = tkinter.Entry(self.window)
        # self.number1_entry を self.window 内に配置する
        self.number1_entry.pack()

        # self.number2_label（2つ目の数字の案内）に self.window 内で「2つ目の数字」と表示するラベルを入れる
        self.number2_label = tkinter.Label(self.window, text="2つ目の数字")
        # self.number2_label を self.window 内に配置する
        self.number2_label.pack()

        # self.number2_entry（2つ目の数字の入力欄）に self.window 内の1行の入力欄を入れる
        self.number2_entry = tkinter.Entry(self.window)
        # self.number2_entry を self.window 内に配置する
        self.number2_entry.pack()

        # self.calculate_button（計算ボタン）に self.window 内で「計算する」と表示し、押すと self.calculate を呼ぶボタンを入れる
        self.calculate_button = tkinter.Button(
            self.window,
            text="計算する",
            # ボタンを押したときに呼ぶ処理として self.calculate を登録する
            command=self.calculate,
        )
        # self.calculate_button を self.window 内に配置する
        self.calculate_button.pack()

        # self.result_label（結果表示）に self.window 内で「答え:」と表示するラベルを入れる
        self.result_label = tkinter.Label(self.window, text="答え:")
        # self.result_label を self.window 内に配置する
        self.result_label.pack()

    # 入力された2つの数字を足して答えを表示する calculate を定義する
    def calculate(self):
        # number1_text（1つ目の入力文字列）に self.number1_entry に入力された文字列を入れる
        number1_text = self.number1_entry.get()
        # number2_text（2つ目の入力文字列）に self.number2_entry に入力された文字列を入れる
        number2_text = self.number2_entry.get()

        # number1_text または number2_text が空の文字列なら、次の処理を実行する
        if number1_text == "" or number2_text == "":
            # self.result_label の表示を「数字を2つ入力してください」に変える
            self.result_label.config(text="数字を2つ入力してください")
            # calculate の処理をここで終える
            return

        # number1（1つ目の数値）に number1_text を float で数値に変換した値を入れる
        number1 = float(number1_text)
        # number2（2つ目の数値）に number2_text を float で数値に変換した値を入れる
        number2 = float(number2_text)

        # answer（答え）に number1 と number2 を足した値を入れる
        answer = number1 + number2

        # self.result_label の表示を「答え: 」と answer の値を含む文字列に変える
        self.result_label.config(text=f"答え: {answer}")

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
