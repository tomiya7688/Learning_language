# tkinterを、このプログラムで使えるようにする
import tkinter


# 入力された名前で挨拶を表示する show_greeting を定義する
def show_greeting():
    # name に name_entry に入力された文字列を入れる
    name = name_entry.get()
    # result_label の表示を「こんにちは 」と name をつなげた文字列に変える
    result_label.config(text=f"こんにちは {name}")


# window に tkinterのTkクラスから作ったウィンドウを入れる
window = tkinter.Tk()
# window のタイトルを「挨拶アプリ」にする
window.title("挨拶アプリ")
# window の大きさを横400、縦220にする
window.geometry("400x220")

# name_label に window 内で「名前を入力してください」と表示するラベルを入れる
name_label = tkinter.Label(window, text="名前を入力してください")
# name_label を window 内に配置する
name_label.pack()

# name_entry に window 内の1行の入力欄を入れる
name_entry = tkinter.Entry(window)
# name_entry を window 内に配置する
name_entry.pack()

# greet_button に window 内で「挨拶する」と表示し、押すと show_greeting を呼ぶボタンを入れる
greet_button = tkinter.Button(window, text="挨拶する", command=show_greeting)
# greet_button を window 内に配置する
greet_button.pack()

# result_label に window 内で空の文字列を表示するラベルを入れる
result_label = tkinter.Label(window, text="")
# result_label を window 内に配置する
result_label.pack()

# window の画面を表示し、操作を待ち続ける
window.mainloop()
