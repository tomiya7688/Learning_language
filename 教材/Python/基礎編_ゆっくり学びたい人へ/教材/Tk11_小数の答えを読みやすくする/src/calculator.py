# tkinterを、このプログラムで使えるようにする
import tkinter
# math を、このプログラムで使えるようにする
import math
# functools から、処理に指定する値を先に固定する partial を読み込む
from functools import partial


# 電卓の入力欄・計算途中の式・結果表示・計算処理をまとめる CalculatorApp クラスを定義する
class CalculatorApp:
    # CalculatorApp の画面と部品を用意する __init__ を定義する
    def __init__(self):
        # self.calculation_parts（計算式の部品）に空のリストを入れる
        self.calculation_parts = []
        # self.replace_input（次の数字ボタンか小数点ボタンで入力を置き換えるか）に False を入れる
        self.replace_input = False
        # self.answer_value（表示する前の答え）に、答えがないことを表す None を入れる
        self.answer_value = None
        # self.window（ウィンドウ）に tkinterのTkクラスから作ったウィンドウを入れる
        self.window = tkinter.Tk()
        # self.window のタイトルを「関数電卓」にする
        self.window.title("関数電卓")
        # self.window の大きさを横420、縦520にする
        self.window.geometry("420x520")
        # self.window の最小の大きさを横420、縦520にする
        self.window.minsize(420, 520)
        # 入力欄・式・答えを配置する self.create_display を呼び出す
        self.create_display()
        # 数字と計算記号のボタンを配置する self.create_buttons を呼び出す
        self.create_buttons()

    # 入力欄・式・答えを配置する create_display を定義する
    def create_display(self):
        # self.number_label（数字の案内）に self.window 内の「数字（sin・cosは角度を度で入力）」というラベルを入れる
        self.number_label = tkinter.Label(
            self.window, text="数字（sin・cosは角度を度で入力）"
        )
        # self.number_label を self.window 内に配置し、上下に6ピクセルずつ間を空ける
        self.number_label.pack(pady=6)
        # self.input_text（入力欄の文字列）に self.window で使う、文字列を保持する変数を入れる
        self.input_text = tkinter.StringVar(master=self.window)
        # self.input_text へ書き込まれた時の処理として self.forget_answer を登録する
        self.input_text.trace_add("write", self.forget_answer)
        # self.number_entry（数字の入力欄）に、文字列を self.input_text とつなぐ1行の入力欄を入れる
        self.number_entry = tkinter.Entry(self.window, textvariable=self.input_text)
        # self.number_entry を横へ広げ、左右に16ピクセルずつ間を空ける
        self.number_entry.pack(fill="x", padx=16)
        # self.expression_label（計算式の表示）に「計算式:」を表示し、380ピクセルで折り返すラベルを入れる
        self.expression_label = tkinter.Label(
            self.window, text="計算式:", wraplength=380
        )
        # self.expression_label を横へ広げ、上下に6ピクセルずつ間を空ける
        self.expression_label.pack(fill="x", pady=6)
        # self.result_label（答えの表示）に「答え:」を表示し、380ピクセルで折り返すラベルを入れる
        self.result_label = tkinter.Label(self.window, text="答え:", wraplength=380)
        # self.result_label を横へ広げ、上下に6ピクセルずつ間を空ける
        self.result_label.pack(fill="x", pady=6)

    # 数字と計算記号のボタンを配置する create_buttons を定義する
    def create_buttons(self):
        # self.buttons_frame（ボタンの枠）に self.window 内の部品をまとめる枠を入れる
        self.buttons_frame = tkinter.Frame(self.window)
        # self.buttons_frame を縦横へ広げ、左右と上下に12ピクセルずつ間を空ける
        self.buttons_frame.pack(fill="both", expand=True, padx=12, pady=12)
        # column（列番号）に0から3までの番号を入れ、次の処理を繰り返す
        for column in range(4):
            # self.buttons_frame の column 列へ、余った幅を同じ割合で配分する
            self.buttons_frame.columnconfigure(column, weight=1, uniform="buttons")
        # row（行番号）に0から4までの番号を入れ、次の処理を繰り返す
        for row in range(5):
            # self.buttons_frame の row 行へ、余った高さを同じ割合で配分する
            self.buttons_frame.rowconfigure(row, weight=1)
        # digit_positions（数字と配置位置）に、数字の文字列・行番号・列番号の組を並べたリストを入れる
        digit_positions = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 0),
        ]
        # digit（数字）・row（行）・column（列）に digit_positions の各組の値を入れ、次の処理を繰り返す
        for digit, row, column in digit_positions:
            # digit を指定した self.append_digit の処理を、指定した行と列のボタンへ登録する
            self.create_button(digit, row, column, partial(self.append_digit, digit))
        # operation_positions（計算ボタンと配置位置）に、表示文字列・行・列・押した時の処理の組を入れる
        operation_positions = [
            ("sin", 0, 0, partial(self.apply_trigonometry, "sin")),
            ("cos", 0, 1, partial(self.apply_trigonometry, "cos")),
            ("C", 0, 2, self.clear), ("/", 0, 3, self.select_division),
            ("*", 1, 3, self.select_multiplication),
            ("-", 2, 3, self.select_subtraction),
            ("+", 3, 3, self.select_addition),
            (".", 4, 1, self.append_decimal_point), ("=", 4, 2, self.calculate),
        ]
        # text（表示文字列）・row・column・command（押した時の処理）に各組の値を入れて繰り返す
        for text, row, column, command in operation_positions:
            # 「=」なら2列分、それ以外なら1列分の幅を指定して self.create_button を呼び出す
            self.create_button(text, row, column, command, 2 if text == "=" else 1)

    # 指定した文字と処理のボタンを配置する create_button を定義する
    def create_button(self, text, row, column, command, column_span=1):
        # column_span（使う列数）には、ボタンを広げる列の数が入り、省略した場合は1になる
        # button（ボタン）に text を表示し、押すと command を実行するボタンを入れる
        button = tkinter.Button(self.buttons_frame, text=text, command=command)
        # button を row 行・column 列から column_span 列分へ広げ、周囲に4ピクセルずつ間を空ける
        button.grid(
            row=row, column=column, columnspan=column_span,
            sticky="nsew", padx=4, pady=4
        )

    # 数値を表示用の文字列にする format_number を定義する
    def format_number(self, number):
        # number（表示する数値）が0なら、次の処理を実行する
        if number == 0:
            # 文字列の「0」を返す
            return "0"
        # number を有効数字12桁の表示へ変換した文字列を返す
        return format(number, ".12g")

    # 保存済みの式を表示用の文字列にする format_expression を定義する
    def format_expression(self):
        # parts_text（表示する式の部品）に空のリストを入れる
        parts_text = []
        # part（式の部品）に self.calculation_parts の値を順に入れて繰り返す
        for part in self.calculation_parts:
            # part が文字列なら、次の処理を実行する
            if isinstance(part, str):
                # parts_text の末尾に part を追加する
                parts_text.append(part)
            # part が文字列でなければ、次の処理を実行する
            else:
                # parts_text の末尾に part を表示用の文字列にした値を追加する
                parts_text.append(self.format_number(part))
        # parts_text の文字列を空白でつないだ文字列を返す
        return " ".join(parts_text)

    # 入力欄へ書き込まれた時に答えを忘れる forget_answer を定義する
    def forget_answer(self, variable_name, index, operation):
        # variable_name（変数名）・index（添字）・operation（操作の種類）には、Tkinterが指定した変更情報が入る
        # self.answer_value に、保存した答えがないことを表す None を入れる
        self.answer_value = None
        # self.replace_input に False を入れる
        self.replace_input = False

    # 答えを表示し、次の計算用の数値を保存する show_answer を定義する
    def show_answer(self, answer):
        # answer_text（答えの表示文字列）に answer を表示用に変換した文字列を入れる
        answer_text = self.format_number(answer)
        # self.result_label の表示を「答え: 」と answer_text をつないだ文字列に変える
        self.result_label.config(text="答え: " + answer_text)
        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.number_entry の先頭に answer_text を挿入する
        self.number_entry.insert(0, answer_text)
        # self.answer_value に、表示する前の数値 answer を入れる
        self.answer_value = answer
        # self.replace_input に True を入れる
        self.replace_input = True

    # 次の数字入力のために前の値を消す prepare_input を定義する
    def prepare_input(self):
        # self.replace_input が False なら、次の処理を実行する
        if not self.replace_input:
            # prepare_input の処理をここで終える
            return
        # self.calculation_parts に式が残っていれば、次の処理を実行する
        if self.calculation_parts:
            # self.number_entry の先頭から末尾までの文字列を削除する
            self.number_entry.delete(0, tkinter.END)
            # self.expression_label に、保存した式を表示用に変換した文字列を表示する
            self.expression_label.config(text="計算式: " + self.format_expression())
            # self.replace_input に False を入れる
            self.replace_input = False
        # self.calculation_parts に式が残っていなければ、次の処理を実行する
        else:
            # 同じ電卓の入力・計算式・結果表示を空にする self.clear を呼び出す
            self.clear()

    # 入力欄へ数字を追加する append_digit を定義する
    def append_digit(self, digit):
        # digit（追加する数字）には、押された数字ボタンの文字列が入る
        # 次の数字入力のために前の値を消す self.prepare_input を呼び出す
        self.prepare_input()
        # self.number_entry の末尾へ digit を挿入する
        self.number_entry.insert(tkinter.END, digit)
        # self.result_label の表示を「答え:」に変える
        self.result_label.config(text="答え:")

    # 入力欄へ小数点を追加する append_decimal_point を定義する
    def append_decimal_point(self):
        # 次の数字入力のために前の値を消す self.prepare_input を呼び出す
        self.prepare_input()
        # number_text（入力文字列）に self.number_entry に入力された文字列を入れる
        number_text = self.number_entry.get()
        # number_text に小数点が含まれていれば、次の処理を実行する
        if "." in number_text:
            # self.result_label の表示を「小数点は1つの数字に1個だけ入力できます」に変える
            self.result_label.config(text="小数点は1つの数字に1個だけ入力できます")
            # append_decimal_point の処理をここで終える
            return
        # number_text が空の文字列なら、次の処理を実行する
        if number_text == "":
            # self.number_entry の末尾へ「0」を挿入する
            self.number_entry.insert(tkinter.END, "0")
        # self.number_entry の末尾へ「.」を挿入する
        self.number_entry.insert(tkinter.END, ".")
        # self.result_label の表示を「答え:」に変える
        self.result_label.config(text="答え:")

    # 入力・計算式・結果表示を空にする clear を定義する
    def clear(self):
        # self.calculation_parts の要素をすべて削除する
        self.calculation_parts.clear()
        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.expression_label の表示を「計算式:」に変える
        self.expression_label.config(text="計算式:")
        # self.result_label の表示を「答え:」に変える
        self.result_label.config(text="答え:")
        # self.replace_input に False を入れる
        self.replace_input = False

    # 入力欄を数値へ変換し、使えない入力を結果の欄で知らせる read_number を定義する
    def read_number(self, empty_message):
        # empty_message（空欄の案内）には、入力欄が空の場合に表示する文字列が入る
        # number_text（入力文字列）に self.number_entry の文字列から前後の空白を取り除いた文字列を入れる
        number_text = self.number_entry.get().strip()
        # number_text が空の文字列なら、次の処理を実行する
        if number_text == "":
            # self.result_label の表示を empty_message に変える
            self.result_label.config(text=empty_message)
            # 数値を読み取れなかったことを表す None を返す
            return None
        # self.answer_value に答えの数値が保存されていれば、次の処理を実行する
        if self.answer_value is not None:
            # 表示する前の答え self.answer_value を返す
            return self.answer_value
        # 次の数値変換で ValueError が起きるかを確認する
        try:
            # number（読み取った数値）に number_text を float で数値に変換した値を入れる
            number = float(number_text)
        # 数値へ変換できず ValueError が起きた場合は、次の処理を実行する
        except ValueError:
            # self.result_label の表示を「数字を入力してください（例: 1.5）」に変える
            self.result_label.config(text="数字を入力してください（例: 1.5）")
            # 数値を読み取れなかったことを表す None を返す
            return None
        # number が無限大でも非数でもない数値でなければ、次の処理を実行する
        if not math.isfinite(number):
            # self.result_label の表示を「有限の数字を入力してください」に変える
            self.result_label.config(text="有限の数字を入力してください")
            # 数値を読み取れなかったことを表す None を返す
            return None
        # 読み取った数値 number を返す
        return number

    # 入力された数字と operator を計算式に追加する add_operator を定義する
    def add_operator(self, operator):
        # operator（演算子）には、この電卓のボタン処理が指定した計算記号が入る
        # number（読み取った数値）に、空欄の案内「次の数字を入力してください」を指定して self.read_number が返す値を入れる
        number = self.read_number("次の数字を入力してください")
        # number が None なら、次の処理を実行する
        if number is None:
            # add_operator の処理をここで終える
            return

        # self.calculation_parts の末尾に number を追加する
        self.calculation_parts.append(number)
        # self.calculation_parts の末尾に operator を追加する
        self.calculation_parts.append(operator)

        # self.expression_label に、保存した式を表示用に変換した文字列を表示する
        self.expression_label.config(text="計算式: " + self.format_expression())

        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.result_label の表示を「答え:」に変える
        self.result_label.config(text="答え:")
        # self.replace_input に False を入れる
        self.replace_input = False

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
        # number（読み取った数値）に、空欄の案内「最後の数字を入力してください」を指定して self.read_number が返す値を入れる
        number = self.read_number("最後の数字を入力してください")
        # number が None なら、次の処理を実行する
        if number is None:
            # calculate の処理をここで終える
            return

        # self.calculation_parts の末尾に number を追加する
        self.calculation_parts.append(number)

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
                    # self.answer_value に、答えがないことを表す None を入れる
                    self.answer_value = None
                    # self.replace_input に True を入れる
                    self.replace_input = True
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

        # answer が無限大でも非数でもない数値でなければ、次の処理を実行する
        if not math.isfinite(answer):
            # self.result_label の表示を「計算結果が大きすぎます。Cで消してやり直してください」に変える
            self.result_label.config(text="計算結果が大きすぎます。Cで消してやり直してください")
            # self.calculation_parts の要素をすべて削除する
            self.calculation_parts.clear()
            # self.answer_value に、答えがないことを表す None を入れる
            self.answer_value = None
            # self.replace_input に True を入れる
            self.replace_input = True
            # calculate の処理をここで終える
            return

        # self.expression_label に、表示用の式と表示用の答えをつないだ文字列を表示する
        self.expression_label.config(
            text="計算式: " + self.format_expression() + " = " + self.format_number(answer)
        )
        # self.calculation_parts の要素をすべて削除する
        self.calculation_parts.clear()
        # answer を指定して、答えを表示して保存する self.show_answer を呼び出す
        self.show_answer(answer)

    # 入力欄の角度からsinかcosを求める apply_trigonometry を定義する
    def apply_trigonometry(self, function_name):
        # function_name（計算名）には、ボタンが指定した「sin」か「cos」が入る
        # angle_degrees（度の角度）に、空欄の案内を指定して self.read_number が返す値を入れる
        angle_degrees = self.read_number("角度を度で入力してください（例: 30）")
        # angle_degrees が None なら、次の処理を実行する
        if angle_degrees is None:
            # apply_trigonometry の処理をここで終える
            return
        # angle_radians（ラジアンの角度）に、angle_degrees をラジアンへ変換した値を入れる
        angle_radians = math.radians(angle_degrees)
        # function_name が「sin」なら、次の処理を実行する
        if function_name == "sin":
            # answer（答え）に angle_radians のsinを求めた値を入れる
            answer = math.sin(angle_radians)
        # function_name が「sin」でなければ、次の処理を実行する
        else:
            # answer に angle_radians のcosを求めた値を入れる
            answer = math.cos(angle_radians)
        # operation_text（角度の計算表示）に計算名・表示用の度の角度・度の記号を含む文字列を入れる
        operation_text = f"{function_name}({self.format_number(angle_degrees)}°)"
        # self.calculation_parts に式が残っていれば、次の処理を実行する
        if self.calculation_parts:
            # self.expression_label に、保存した式と operation_text を表示する
            self.expression_label.config(
                text="計算式: "
                + self.format_expression()
                + " " + operation_text
            )
        # self.calculation_parts に式が残っていなければ、次の処理を実行する
        else:
            # self.expression_label に、operation_text と表示用の答えを表示する
            self.expression_label.config(
                text="計算式: " + operation_text + " = " + self.format_number(answer)
            )
        # answer を指定して、答えを表示して保存する self.show_answer を呼び出す
        self.show_answer(answer)

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
