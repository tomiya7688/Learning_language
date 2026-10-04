# tkinterを、このプログラムで使えるようにする
import tkinter


# calculation_parts に空のリストを入れる
calculation_parts = []


# 入力された数字と operator を計算式に追加する add_operator を定義する
def add_operator(operator):
    # number_text に number_entry に入力された文字列を入れる
    number_text = number_entry.get()

    # number_text が空の文字列なら、次の処理を実行する
    if number_text == "":
        # result_label の表示を「次の数字を入力してください」に変える
        result_label.config(text="次の数字を入力してください")
        # add_operator の処理をここで終える
        return

    # calculation_parts の末尾に number_text を float で数値に変換した値を追加する
    calculation_parts.append(float(number_text))
    # calculation_parts の末尾に operator を追加する
    calculation_parts.append(operator)

    # expression_label の表示を「計算式: 」に、calculation_parts の各値を文字列にして空白でつないだものを付けた文字列に変える
    expression_label.config(
        text="計算式: " + " ".join(str(part) for part in calculation_parts)
    )

    # number_entry の先頭から末尾までの文字列を削除する
    number_entry.delete(0, tkinter.END)
    # result_label の表示を「答え:」に変える
    result_label.config(text="答え:")


# 入力された数字と「+」を計算式に追加する select_addition を定義する
def select_addition():
    # 「+」を指定して add_operator を呼び出す
    add_operator("+")


# 入力された数字と「-」を計算式に追加する select_subtraction を定義する
def select_subtraction():
    # 「-」を指定して add_operator を呼び出す
    add_operator("-")


# 計算式に最後の数字を追加し、順に計算して答えを表示する calculate を定義する
def calculate():
    # number_text に number_entry に入力された文字列を入れる
    number_text = number_entry.get()

    # number_text が空の文字列なら、次の処理を実行する
    if number_text == "":
        # result_label の表示を「最後の数字を入力してください」に変える
        result_label.config(text="最後の数字を入力してください")
        # calculate の処理をここで終える
        return

    # calculation_parts の末尾に number_text を float で数値に変換した値を追加する
    calculation_parts.append(float(number_text))

    # answer に calculation_parts の先頭の値を入れる
    answer = calculation_parts[0]

    # index に1から calculation_parts の要素数未満までの番号を2ずつ増やして入れ、次の処理を繰り返す
    for index in range(1, len(calculation_parts), 2):
        # operator に calculation_parts の番号 index にある値を入れる
        operator = calculation_parts[index]
        # number に calculation_parts の番号 index + 1 にある値を入れる
        number = calculation_parts[index + 1]

        # operator が「+」なら、次の処理を実行する
        if operator == "+":
            # answer に answer と number を足した値を入れる
            answer = answer + number
        # operator が「+」でなければ、次の処理を実行する
        else:
            # answer に answer から number を引いた値を入れる
            answer = answer - number

    # expression_label の表示を「計算式: 」に、calculation_parts の各値を文字列にして空白でつないだものと「 = 」と answer の値を付けた文字列に変える
    expression_label.config(
        text=(
            "計算式: "
            + " ".join(str(part) for part in calculation_parts)
            + f" = {answer}"
        )
    )
    # result_label の表示を「答え: 」と answer の値を含む文字列に変える
    result_label.config(text=f"答え: {answer}")

    # calculation_parts の要素をすべて削除する
    calculation_parts.clear()
    # number_entry の先頭から末尾までの文字列を削除する
    number_entry.delete(0, tkinter.END)
    # number_entry の先頭に answer を文字列にした値を挿入する
    number_entry.insert(0, str(answer))


# window に tkinterのTkクラスから作ったウィンドウを入れる
window = tkinter.Tk()
# window のタイトルを「複数の数字を計算できる」にする
window.title("複数の数字を計算できる")
# window の大きさを横420、縦320にする
window.geometry("420x320")

# number_label に window 内で「数字」と表示するラベルを入れる
number_label = tkinter.Label(window, text="数字")
# number_label を window 内に配置する
number_label.pack()

# number_entry に window 内の1行の入力欄を入れる
number_entry = tkinter.Entry(window)
# number_entry を window 内に配置する
number_entry.pack()

# expression_label に window 内で「計算式:」と表示するラベルを入れる
expression_label = tkinter.Label(window, text="計算式:")
# expression_label を window 内に配置する
expression_label.pack()

# 足し算
# addition_button に window 内で「+」と表示し、押すと select_addition を呼ぶボタンを入れる
addition_button = tkinter.Button(
    window,
    text="+",
    command=select_addition
)
# addition_button を window 内に配置する
addition_button.pack()

# 引き算
# subtraction_button に window 内で「-」と表示し、押すと select_subtraction を呼ぶボタンを入れる
subtraction_button = tkinter.Button(
    window,
    text="-",
    command=select_subtraction
)
# subtraction_button を window 内に配置する
subtraction_button.pack()

# 計算する
# equals_button に window 内で「=」と表示し、押すと calculate を呼ぶボタンを入れる
equals_button = tkinter.Button(
    window,
    text="=",
    command=calculate
)
# equals_button を window 内に配置する
equals_button.pack()

# result_label に window 内で「答え:」と表示するラベルを入れる
result_label = tkinter.Label(window, text="答え:")
# result_label を window 内に配置する
result_label.pack()

# window の画面を表示し、操作を待ち続ける
window.mainloop()
