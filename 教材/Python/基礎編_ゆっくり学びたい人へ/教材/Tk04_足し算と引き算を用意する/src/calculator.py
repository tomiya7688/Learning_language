# tkinterを、このプログラムで使えるようにする
import tkinter


# 電卓の入力欄・選択中の計算方法・結果表示・計算処理をまとめる CalculatorApp クラスを定義する
class CalculatorApp:
    # CalculatorApp の画面と部品を用意する __init__ を定義する
    def __init__(self):
        # self.selected_operator（選択中の演算子）に足し算を表す「+」を入れる
        self.selected_operator = "+"

        # self.window（ウィンドウ）に tkinterのTkクラスから作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「足し算と引き算を用意する」にする
        self.window.title("足し算と引き算を用意する")
        # self.window の大きさを横400、縦340にする
        self.window.geometry("400x340")

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

        # self.operator_label（選択中の演算子の表示）に self.window 内で「選択中: +」と表示するラベルを入れる
        self.operator_label = tkinter.Label(self.window, text="選択中: +")
        # self.operator_label を self.window 内に配置する
        self.operator_label.pack()

        # self.addition_button（足し算ボタン）に self.window 内で「+」と表示し、押すと self.select_addition を呼ぶボタンを入れる
        self.addition_button = tkinter.Button(
            self.window,
            text="+",
            # ボタンを押したときに呼ぶ処理として self.select_addition を登録する
            command=self.select_addition,
        )
        # self.addition_button を self.window 内に配置する
        self.addition_button.pack()

        # self.subtraction_button（引き算ボタン）に self.window 内で「-」と表示し、押すと self.select_subtraction を呼ぶボタンを入れる
        self.subtraction_button = tkinter.Button(
            self.window,
            text="-",
            # ボタンを押したときに呼ぶ処理として self.select_subtraction を登録する
            command=self.select_subtraction,
        )
        # self.subtraction_button を self.window 内に配置する
        self.subtraction_button.pack()

        # self.equals_button（計算を行うボタン）に self.window 内で「=」と表示し、押すと self.calculate を呼ぶボタンを入れる
        self.equals_button = tkinter.Button(
            self.window,
            text="=",
            # ボタンを押したときに呼ぶ処理として self.calculate を登録する
            command=self.calculate,
        )
        # self.equals_button を self.window 内に配置する
        self.equals_button.pack()

        # self.result_label（結果表示）に self.window 内で「答え:」と表示するラベルを入れる
        self.result_label = tkinter.Label(self.window, text="答え:")
        # self.result_label を self.window 内に配置する
        self.result_label.pack()

    # 足し算を選び、選択中の表示を更新する select_addition を定義する
    def select_addition(self):
        # self.selected_operator に足し算を表す「+」を入れる
        self.selected_operator = "+"
        # self.operator_label の表示を「選択中: +」に変える
        self.operator_label.config(text="選択中: +")

    # 引き算を選び、選択中の表示を更新する select_subtraction を定義する
    def select_subtraction(self):
        # self.selected_operator に引き算を表す「-」を入れる
        self.selected_operator = "-"
        # self.operator_label の表示を「選択中: -」に変える
        self.operator_label.config(text="選択中: -")

    # 入力された2つの数字を選択中の演算子で計算し、答えを表示する calculate を定義する
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

        # self.selected_operator が「+」なら、次の処理を実行する
        if self.selected_operator == "+":
            # answer（答え）に number1 と number2 を足した値を入れる
            answer = number1 + number2
        # self.selected_operator が「+」でなければ、次の処理を実行する
        else:
            # answer に number1 から number2 を引いた値を入れる
            answer = number1 - number2

        # self.result_label の表示を「答え: 」と answer の値を含む文字列に変える
        self.result_label.config(text=f"答え: {answer}")

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
