import tkinter


def calculate():
    number1_text = number1_entry.get()
    number2_text = number2_entry.get()

    if number1_text == "" or number2_text == "":
        result_label.config(text="数字を2つ入力してください")
        return

    number1 = float(number1_text)
    number2 = float(number2_text)

    answer = number1 + number2

    result_label.config(text=f"答え: {answer}")


window = tkinter.Tk()
window.title("簡単な電卓")
window.geometry("400x260")

number1_label = tkinter.Label(window, text="1つ目の数字")
number1_label.pack()

number1_entry = tkinter.Entry(window)
number1_entry.pack()

number2_label = tkinter.Label(window, text="2つ目の数字")
number2_label.pack()

number2_entry = tkinter.Entry(window)
number2_entry.pack()

calculate_button = tkinter.Button(
    window,
    text="計算する",
    command=calculate
)
calculate_button.pack()

result_label = tkinter.Label(window, text="答え:")
result_label.pack()

window.mainloop()
