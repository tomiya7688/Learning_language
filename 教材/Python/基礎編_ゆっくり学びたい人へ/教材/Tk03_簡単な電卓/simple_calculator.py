# tkinterを、このプログラムで使えるようにする
import tkinter


# 入力された2つの数字を足して答えを表示する calculate を定義する
def calculate():
    # number1_text に number1_entry に入力された文字列を入れる
    number1_text = number1_entry.get()
    # number2_text に number2_entry に入力された文字列を入れる
    number2_text = number2_entry.get()

    # number1_text または number2_text が空の文字列なら、次の処理を実行する
    if number1_text == "" or number2_text == "":
        # result_label の表示を「数字を2つ入力してください」に変える
        result_label.config(text="数字を2つ入力してください")
        # calculate の処理をここで終える
        return

    # number1 に number1_text を float で数値に変換した値を入れる
    number1 = float(number1_text)
    # number2 に number2_text を float で数値に変換した値を入れる
    number2 = float(number2_text)

    # answer に number1 と number2 を足した値を入れる
    answer = number1 + number2

    # result_label の表示を「答え: 」と answer の値を含む文字列に変える
    result_label.config(text=f"答え: {answer}")


# window に tkinterのTkクラスから作ったウィンドウを入れる
window = tkinter.Tk()
# window のタイトルを「簡単な電卓」にする
window.title("簡単な電卓")
# window の大きさを横400、縦260にする
window.geometry("400x260")

# number1_label に window 内で「1つ目の数字」と表示するラベルを入れる
number1_label = tkinter.Label(window, text="1つ目の数字")
# number1_label を window 内に配置する
number1_label.pack()

# number1_entry に window 内の1行の入力欄を入れる
number1_entry = tkinter.Entry(window)
# number1_entry を window 内に配置する
number1_entry.pack()

# number2_label に window 内で「2つ目の数字」と表示するラベルを入れる
number2_label = tkinter.Label(window, text="2つ目の数字")
# number2_label を window 内に配置する
number2_label.pack()

# number2_entry に window 内の1行の入力欄を入れる
number2_entry = tkinter.Entry(window)
# number2_entry を window 内に配置する
number2_entry.pack()

# 計算する
# calculate_button に window 内で「計算する」と表示し、押すと calculate を呼ぶボタンを入れる
calculate_button = tkinter.Button(
    window,
    text="計算する",
    command=calculate
)
# calculate_button を window 内に配置する
calculate_button.pack()

# result_label に window 内で「答え:」と表示するラベルを入れる
result_label = tkinter.Label(window, text="答え:")
# result_label を window 内に配置する
result_label.pack()

# window の画面を表示し、操作を待ち続ける
window.mainloop()
