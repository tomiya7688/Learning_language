import tkinter


selected_operator = "+"


def select_addition():
    global selected_operator

    selected_operator = "+"
    operator_label.config(text="選択中: +")


def select_subtraction():
    global selected_operator

    selected_operator = "-"
    operator_label.config(text="選択中: -")


def calculate():
    number1_text = number1_entry.get()
    number2_text = number2_entry.get()

    if number1_text == "" or number2_text == "":
        result_label.config(text="数字を2つ入力してください")
        return

    number1 = float(number1_text)
    number2 = float(number2_text)

    if selected_operator == "+":
        answer = number1 + number2
    else:
        answer = number1 - number2

    result_label.config(text=f"答え: {answer}")


window = tkinter.Tk()
window.title("足し算と引き算を用意する")
window.geometry("400x340")

number1_label = tkinter.Label(window, text="1つ目の数字")
number1_label.pack()

number1_entry = tkinter.Entry(window)
number1_entry.pack()

number2_label = tkinter.Label(window, text="2つ目の数字")
number2_label.pack()

number2_entry = tkinter.Entry(window)
number2_entry.pack()

operator_label = tkinter.Label(window, text="選択中: +")
operator_label.pack()

addition_button = tkinter.Button(
    window,
    text="+",
    command=select_addition
)
addition_button.pack()

subtraction_button = tkinter.Button(
    window,
    text="-",
    command=select_subtraction
)
subtraction_button.pack()

equals_button = tkinter.Button(
    window,
    text="=",
    command=calculate
)
equals_button.pack()

result_label = tkinter.Label(window, text="答え:")
result_label.pack()

window.mainloop()
