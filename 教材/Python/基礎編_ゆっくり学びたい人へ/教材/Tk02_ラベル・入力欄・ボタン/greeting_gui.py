import tkinter


# ボタンが押されたときに実行する関数です。
def show_greeting():
    name = name_entry.get()
    result_label.config(text=f"こんにちは {name}")


# ウィンドウを作ります。
window = tkinter.Tk()
window.title("挨拶アプリ")
window.geometry("400x220")

# 説明を表示します。
name_label = tkinter.Label(window, text="名前を入力してください")
name_label.pack()

# 名前を入力する欄です。
name_entry = tkinter.Entry(window)
name_entry.pack()

# 押せるボタンです。
greet_button = tkinter.Button(window, text="挨拶する", command=show_greeting)
greet_button.pack()

# 結果を表示するラベルです。
result_label = tkinter.Label(window, text="")
result_label.pack()

# ウィンドウを表示し続けます。
window.mainloop()
