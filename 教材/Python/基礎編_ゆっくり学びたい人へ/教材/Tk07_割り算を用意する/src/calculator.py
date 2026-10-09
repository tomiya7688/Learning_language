# tkinterを、このプログラムで使えるようにする
import tkinter


# 電卓の入力欄・計算途中の式・結果表示・計算処理をまとめる CalculatorApp クラスを定義する
class CalculatorApp:
    # CalculatorApp の画面と部品を用意する __init__ を定義する
    def __init__(self):
        # self.calculation_parts（計算式の部品）に空のリストを入れる
        self.calculation_parts = []

        # self.window（ウィンドウ）に tkinterのTkクラスから作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「割り算を用意する」にする
        self.window.title("割り算を用意する")
        # self.window の大きさを横420、縦400にする
        self.window.geometry("420x400")

        # self.number_label（数字の案内）に self.window 内で「数字」と表示するラベルを入れる
        self.number_label = tkinter.Label(self.window, text="数字")
        # self.number_label を self.window 内に配置する
        self.number_label.pack()

        # self.number_entry（数字の入力欄）に self.window 内の1行の入力欄を入れる
        self.number_entry = tkinter.Entry(self.window)
        # self.number_entry を self.window 内に配置する
        self.number_entry.pack()

        # self.expression_label（計算式の表示）に self.window 内で「計算式:」と表示するラベルを入れる
        self.expression_label = tkinter.Label(self.window, text="計算式:")
        # self.expression_label を self.window 内に配置する
        self.expression_label.pack()

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

        # self.multiplication_button（掛け算ボタン）に self.window 内で「*」と表示し、押すと self.select_multiplication を呼ぶボタンを入れる
        self.multiplication_button = tkinter.Button(
            self.window,
            text="*",
            # ボタンを押したときに呼ぶ処理として self.select_multiplication を登録する
            command=self.select_multiplication,
        )
        # self.multiplication_button を self.window 内に配置する
        self.multiplication_button.pack()

        # self.division_button（割り算ボタン）に self.window 内で「/」と表示し、押すと self.select_division を呼ぶボタンを入れる
        self.division_button = tkinter.Button(
            self.window,
            text="/",
            # ボタンを押したときに呼ぶ処理として self.select_division を登録する
            command=self.select_division,
        )
        # self.division_button を self.window 内に配置する
        self.division_button.pack()

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

    # 入力された数字と operator を計算式に追加する add_operator を定義する
    def add_operator(self, operator):
        # operator（演算子）には、この電卓のボタン処理が指定した計算記号が入る
        # number_text（入力文字列）に self.number_entry に入力された文字列を入れる
        number_text = self.number_entry.get()

        # number_text が空の文字列なら、次の処理を実行する
        if number_text == "":
            # self.result_label の表示を「次の数字を入力してください」に変える
            self.result_label.config(text="次の数字を入力してください")
            # add_operator の処理をここで終える
            return

        # self.calculation_parts の末尾に number_text を float で数値に変換した値を追加する
        self.calculation_parts.append(float(number_text))
        # self.calculation_parts の末尾に operator を追加する
        self.calculation_parts.append(operator)

        # part（式の部品）として self.calculation_parts の値を順に取り出し、str(part) で文字列に変換する
        # self.expression_label の表示を「計算式: 」に、self.calculation_parts の各値を文字列にして空白でつないだものを付けた文字列に変える
        self.expression_label.config(
            text="計算式: " + " ".join(str(part) for part in self.calculation_parts)
        )

        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.result_label の表示を「答え:」に変える
        self.result_label.config(text="答え:")

    # 入力された数字と「+」を計算式に追加する select_addition を定義する
    def select_addition(self):
        # 「+」を指定して self.add_operator を呼び出す
        self.add_operator("+")

    # 入力された数字と「-」を計算式に追加する select_subtraction を定義する
    def select_subtraction(self):
        # 「-」を指定して self.add_operator を呼び出す
        self.add_operator("-")

    # 入力された数字と「*」を計算式に追加する select_multiplication を定義する
    def select_multiplication(self):
        # 「*」を指定して self.add_operator を呼び出す
        self.add_operator("*")

    # 入力された数字と「/」を計算式に追加する select_division を定義する
    def select_division(self):
        # 「/」を指定して self.add_operator を呼び出す
        self.add_operator("/")

    # 計算式に最後の数字を追加し、掛け算と割り算を先に計算して答えを表示する calculate を定義する
    def calculate(self):
        # number_text（入力文字列）に self.number_entry に入力された文字列を入れる
        number_text = self.number_entry.get()

        # number_text が空の文字列なら、次の処理を実行する
        if number_text == "":
            # self.result_label の表示を「最後の数字を入力してください」に変える
            self.result_label.config(text="最後の数字を入力してください")
            # calculate の処理をここで終える
            return

        # self.calculation_parts の末尾に number_text を float で数値に変換した値を追加する
        self.calculation_parts.append(float(number_text))

        # 掛け算と割り算を先に計算する
        # addition_and_subtraction_parts（足し算と引き算の部品）に self.calculation_parts の先頭の値を入れたリストを入れる
        addition_and_subtraction_parts = [self.calculation_parts[0]]

        # index（一覧の番号）に1から self.calculation_parts の要素数未満までの番号を2ずつ増やして入れ、次の処理を繰り返す
        for index in range(1, len(self.calculation_parts), 2):
            # operator（演算子）に self.calculation_parts の番号 index にある値を入れる
            operator = self.calculation_parts[index]
            # number（次の数値）に self.calculation_parts の番号 index + 1 にある値を入れる
            number = self.calculation_parts[index + 1]

            # operator が「*」なら、次の処理を実行する
            if operator == "*":
                # addition_and_subtraction_parts の末尾の要素に、その値と number を掛けた値を入れる
                addition_and_subtraction_parts[-1] = (
                    addition_and_subtraction_parts[-1] * number
                )
            # operator が「*」ではなく「/」なら、次の処理を実行する
            elif operator == "/":
                # number が0なら、次の処理を実行する
                if number == 0:
                    # self.result_label の表示を「0では割れません」に変える
                    self.result_label.config(text="0では割れません")
                    # self.calculation_parts の要素をすべて削除する
                    self.calculation_parts.clear()
                    # calculate の処理をここで終える
                    return

                # addition_and_subtraction_parts の末尾の要素に、その値を number で割った値を入れる
                addition_and_subtraction_parts[-1] = (
                    addition_and_subtraction_parts[-1] / number
                )
            # operator が「*」でも「/」でもなければ、次の処理を実行する
            else:
                # addition_and_subtraction_parts の末尾に operator を追加する
                addition_and_subtraction_parts.append(operator)
                # addition_and_subtraction_parts の末尾に number を追加する
                addition_and_subtraction_parts.append(number)

        # 残った足し算と引き算を左から計算する
        # answer（答え）に addition_and_subtraction_parts の先頭の値を入れる
        answer = addition_and_subtraction_parts[0]

        # index に1から addition_and_subtraction_parts の要素数未満までの番号を2ずつ増やして入れ、次の処理を繰り返す
        for index in range(1, len(addition_and_subtraction_parts), 2):
            # operator に addition_and_subtraction_parts の番号 index にある値を入れる
            operator = addition_and_subtraction_parts[index]
            # number に addition_and_subtraction_parts の番号 index + 1 にある値を入れる
            number = addition_and_subtraction_parts[index + 1]

            # operator が「+」なら、次の処理を実行する
            if operator == "+":
                # answer に answer と number を足した値を入れる
                answer = answer + number
            # operator が「+」でなければ、次の処理を実行する
            else:
                # answer に answer から number を引いた値を入れる
                answer = answer - number

        # part（式の部品）として self.calculation_parts の値を順に取り出し、str(part) で文字列に変換する
        # self.expression_label の表示を「計算式: 」に、self.calculation_parts の各値を文字列にして空白でつないだものと「 = 」と answer の値を付けた文字列に変える
        self.expression_label.config(
            text=(
                "計算式: "
                + " ".join(str(part) for part in self.calculation_parts)
                + f" = {answer}"
            )
        )
        # self.result_label の表示を「答え: 」と answer の値を含む文字列に変える
        self.result_label.config(text=f"答え: {answer}")

        # self.calculation_parts の要素をすべて削除する
        self.calculation_parts.clear()
        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.number_entry の先頭に answer を文字列にした値を挿入する
        self.number_entry.insert(0, str(answer))

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
