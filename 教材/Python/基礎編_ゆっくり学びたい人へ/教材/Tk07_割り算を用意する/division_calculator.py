import tkinter


calculation_parts = []


def add_operator(operator):
    number_text = number_entry.get()

    if number_text == "":
        result_label.config(text="次の数字を入力してください")
        return

    calculation_parts.append(float(number_text))
    calculation_parts.append(operator)

    expression_label.config(
        text="計算式: " + " ".join(str(part) for part in calculation_parts)
    )

    number_entry.delete(0, tkinter.END)
    result_label.config(text="答え:")


def select_addition():
    add_operator("+")


def select_subtraction():
    add_operator("-")


def select_multiplication():
    add_operator("*")


def select_division():
    add_operator("/")


def calculate():
    number_text = number_entry.get()

    if number_text == "":
        result_label.config(text="最後の数字を入力してください")
        return

    calculation_parts.append(float(number_text))

    # 掛け算と割り算を先に計算する
    addition_and_subtraction_parts = [calculation_parts[0]]

    for index in range(1, len(calculation_parts), 2):
        operator = calculation_parts[index]
        number = calculation_parts[index + 1]

        if operator == "*":
            addition_and_subtraction_parts[-1] = (
                addition_and_subtraction_parts[-1] * number
            )
        elif operator == "/":
            if number == 0:
                result_label.config(text="0では割れません")
                calculation_parts.clear()
                return

            addition_and_subtraction_parts[-1] = (
                addition_and_subtraction_parts[-1] / number
            )
        else:
            addition_and_subtraction_parts.append(operator)
            addition_and_subtraction_parts.append(number)

    # 残った足し算と引き算を左から計算する
    answer = addition_and_subtraction_parts[0]

    for index in range(1, len(addition_and_subtraction_parts), 2):
        operator = addition_and_subtraction_parts[index]
        number = addition_and_subtraction_parts[index + 1]

        if operator == "+":
            answer = answer + number
        else:
            answer = answer - number

    expression_label.config(
        text=(
            "計算式: "
            + " ".join(str(part) for part in calculation_parts)
            + f" = {answer}"
        )
    )
    result_label.config(text=f"答え: {answer}")

    calculation_parts.clear()
    number_entry.delete(0, tkinter.END)
    number_entry.insert(0, str(answer))


window = tkinter.Tk()
window.title("割り算を用意する")
window.geometry("420x400")

number_label = tkinter.Label(window, text="数字")
number_label.pack()

number_entry = tkinter.Entry(window)
number_entry.pack()

expression_label = tkinter.Label(window, text="計算式:")
expression_label.pack()

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

multiplication_button = tkinter.Button(
    window,
    text="*",
    command=select_multiplication
)
multiplication_button.pack()

division_button = tkinter.Button(
    window,
    text="/",
    command=select_division
)
division_button.pack()

equals_button = tkinter.Button(
    window,
    text="=",
    command=calculate
)
equals_button.pack()

result_label = tkinter.Label(window, text="答え:")
result_label.pack()

window.mainloop()
