# Tk10. sinとcosを追加する

> **「斜めの棒の長さと角度は分かるのに、高さを計算できない！数字と計算記号のボタンも離れていて押しにくい！」**

この章の関数電卓は、四則演算に加え、入力した角度のsin（サイン）とcos（コサイン）を求める電卓です。数字・小数点・計算記号を一つの盤面に並べ、計算に使うボタンを近くに配置します。

## Tk10-1. 角度から高さや横の長さを求めたい

たとえば、長さ10メートルの棒を地面から30度傾けた時、棒の先端の高さは約5メートル、地面に沿った横の長さは約8.66メートルです。棒、地面、先端から地面までの垂直線で、角の一つが90度の三角形を考えます。棒は、90度の角の向かい側にある一番長い辺です。

- **sin（サイン）**は、棒の長さに対する高さの割合です。高さは「棒の長さ × sin（地面からの角度）」で求めます。
- **cos（コサイン）**は、棒の長さに対する横の長さの割合です。横の長さは「棒の長さ × cos（地面からの角度）」で求めます。

sinとcosをまとめて「三角関数」と呼びます。ボタンには、数学や関数電卓で使う名前の `sin` と `cos` を表示します。電卓画面の数字の入力欄へ角度の数字を入力し、高さの割合を求める場合は電卓画面の「sin」ボタン、横の長さの割合を求める場合は電卓画面の「cos」ボタンを押してください。棒の長さを掛ける時は、割合の答えから「*」ボタンで計算を続けられます。

この電卓では、90°のような角度の単位「度」を使います。入力欄には数字だけを入力してください。たとえば30度なら `30` を入力し、`°` は入力しないでください。

Pythonの `math` は、sinやcosなどの計算をまとめた標準の道具です。`import math` で、その道具をコードから使えるようにします。`math.sin` と `math.cos` は、角度の別の単位「ラジアン」で指定された数値を使います。ラジアンは円周のうち角度に対応する部分の長さを半径で割った数で、角度を表す単位で、円の半周が180度、ラジアンではπ（約3.14）です。度の入力をそのまま指定すると違う角度の計算になるため、`math.radians` で度からラジアンへ変換してから計算します。[Python公式の角度変換と三角関数](https://docs.python.org/3/library/math.html#angular-conversion)

## Tk10-2. 画面を作る場所と、計算する場所を分ける

計算記号を数字から離れた場所へ縦に置くと、利用者は数字を押すたびに計算記号を探し直します。数字と計算記号を一つの `Frame`（部品をまとめる枠）に入れ、`grid`（行と列で部品を置く処理）で並べます。

ボタンの盤面は、左から次の配置です。「=」は最後の行の2列分を使うので、答えを出すボタンを大きくできます。

| 行 | 左端 | 左から2番目 | 左から3番目 | 右端 |
| --- | --- | --- | --- | --- |
| 一番上 | sin | cos | C | / |
| 2行目 | 7 | 8 | 9 | * |
| 3行目 | 4 | 5 | 6 | - |
| 4行目 | 1 | 2 | 3 | + |
| 一番下 | 0 | . | =（左から3・4列目を使う1個のボタン） | =（左から3・4列目を使う1個のボタン） |

表示欄とボタンの準備をすべて `__init__`（電卓を作った時の準備処理）へ書くと、入力欄を直す場所とボタンを直す場所が混ざります。表示欄の準備は `create_display`（表示欄を作る）、盤面の準備は `create_buttons`（ボタンを作る）へ分けます。`__init__` は、ウィンドウと計算用の情報を用意し、表示欄、盤面の順に作る処理です。

どのボタンも「表示する文字、位置、押した時の処理」を決めて作る点は同じです。ボタンを作るコードを毎回書くと、間隔を変える時に全ボタンを直すことになります。共通の作成処理を `create_button`（ボタンを一つ作る）へまとめ、数字や計算記号ごとの違いだけを一覧に書きます。`partial` は、ボタンを押す前に処理へ指定する数字や計算名を固定する道具です。たとえばsinボタンは、押した時に計算名 `"sin"` を指定して `apply_trigonometry` を実行します。

sinとcosで変わるのは、角度を計算する一行です。入力確認・角度変換・答えの表示を二重に書かず、`apply_trigonometry`（三角関数を適用する）へまとめ、押されたボタンの計算名でsinかcosを選びます。空欄や数字以外の入力を計算しないため、`read_number`（数値を読み取る）が使える数値を返した時だけ、角度を変換します。`None` は、この処理では数値を読めなかった状態を表し、数値の0とは区別します。

計算途中で `sin` を押す場合、入力中の角度だけをsinの値へ置き換え、入力済みの式は残します。たとえば `2 +` を保存した後に0度のsinを求めた場合、最後に「=」を押すと `2 + 0` の答えが出ます。sinの値を別の数字へ変える時に `2 +` まで消えると、式を最初から入力し直すことになります。数字と小数点の両方で同じ消去の判定をするため、`prepare_input`（次の入力を準備する）へまとめます。保存済みの式があれば入力中の値だけを消し、式がなければ前の計算全体を消します。

入力欄、保存済みの式、角度を計算する操作、表示欄は、同じ電卓に関する情報と操作です。角度を読む場所と答えを表示する場所を別々に置くと、どの電卓の入力をどの電卓へ戻すかが対応しにくくなります。`CalculatorApp`（電卓アプリ）というクラスに、同じ電卓の情報と操作をまとめます。クラスは、同じ対象の情報と操作をまとめて定義する仕組みです。

`CalculatorApp()` で作った個々の電卓を「インスタンス」と呼びます。クラス内の `self` は操作対象の電卓です。`self.calculation_parts` は保存済みの数値と計算記号の一覧、`self.replace_input` は次の数字ボタンか小数点ボタンで入力を置き換えるかを覚える情報です。sin/cos、数字入力、表示の処理は同じ `self` を使うので、操作する電卓がそろいます。クラス内で定義する関数を「メソッド」と呼びます。

計算記号を押した時の保存は `add_operator`（演算子を追加する）、四則演算の答えは `calculate`（計算する）、入力と式の消去は `clear`（消す）が担当します。演算子は「+」「-」「*」「/」など計算の種類を示す記号です。`select_addition` などのメソッドは、ボタンを押した時に対応する記号を `add_operator` へ指定します。

画面の準備と操作を待つ処理は実行するタイミングが違うため、操作待ちは `run`（実行する）へ分けます。`app.py` の `main`（起動時の中心の処理）は、電卓を作って `run` を実行する処理です。電卓の機能を変更するファイルは `calculator.py`（電卓）、起動するファイルは `app.py`（アプリ）のままです。

## Tk10-3. 関数電卓の2ファイルを保存する

PythonとVS Codeで保存して実行する準備がまだなら、[Pythonを書いて動かす準備](../01_環境構築/環境構築ガイド.md)を済ませ、この章へ戻ってください。画面を作る道具には、PythonのTkinter（ティーケーインター）を使います。

Tk10用の新しいフォルダを作り、`calculator.py` と `app.py` を両方保存してください。配布ファイルを使う場合は、次のリンクをそれぞれ開いてコード全体を保存してください。自分で書く場合は、VS Codeで新しいファイルを2つ作り、それぞれの全体コードを書いてください。両方とも同じTk10用フォルダに、末尾の `.py` まで含めた名前で保存してください。

| ファイル | 担当 |
| --- | --- |
| [`calculator.py`](./calculator.py) | 表示欄、数字と計算記号の配置、入力確認、四則演算、sin/cosの処理を定義します。機能を変更するファイルです。 |
| [`app.py`](./app.py) | 同じフォルダから `CalculatorApp` を読み込み、電卓を起動します。ターミナルで実行するファイルです。 |

### calculator.py：関数電卓の画面と計算

元ファイル：[`calculator.py` 全体](./calculator.py)。

```python
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
        # self.number_entry（数字の入力欄）に self.window 内の1行の入力欄を入れる
        self.number_entry = tkinter.Entry(self.window)
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
            # self.expression_label に、保存した式の各値を空白でつないだ文字列を表示する
            self.expression_label.config(
                text="計算式: " + " ".join(str(part) for part in self.calculation_parts)
            )
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

        # part（式の部品）として self.calculation_parts の値を順に取り出し、str(part) で文字列に変換する
        # self.expression_label の表示を「計算式: 」に、self.calculation_parts の各値を文字列にして空白でつないだものを付けた文字列に変える
        self.expression_label.config(
            text="計算式: " + " ".join(str(part) for part in self.calculation_parts)
        )

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
            # self.replace_input に True を入れる
            self.replace_input = True
            # calculate の処理をここで終える
            return

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
        # self.replace_input に True を入れる
        self.replace_input = True

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
        # operation_text（角度の計算表示）に計算名・度の角度・度の記号を含む文字列を入れる
        operation_text = f"{function_name}({angle_degrees}°)"
        # self.calculation_parts に式が残っていれば、次の処理を実行する
        if self.calculation_parts:
            # self.expression_label に、保存した式と operation_text を表示する
            self.expression_label.config(
                text="計算式: "
                + " ".join(str(part) for part in self.calculation_parts)
                + " " + operation_text
            )
        # self.calculation_parts に式が残っていなければ、次の処理を実行する
        else:
            # self.expression_label に、operation_text と answer を表示する
            self.expression_label.config(text=f"計算式: {operation_text} = {answer}")
        # self.result_label の表示を「答え: 」と answer の値を含む文字列に変える
        self.result_label.config(text=f"答え: {answer}")
        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.number_entry の先頭に answer を文字列にした値を挿入する
        self.number_entry.insert(0, str(answer))
        # self.replace_input に True を入れる
        self.replace_input = True

    # ウィンドウを表示する run を定義する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
```

### app.py：電卓を起動する

元ファイル：[`app.py` 全体](./app.py)。

```python
# 同じフォルダの calculator.py から電卓の CalculatorApp を読み込む
from calculator import CalculatorApp


# 電卓の起動処理を main にまとめる
def main():
    # app（アプリ）に CalculatorApp() で作った電卓を入れる
    app = CalculatorApp()
    # app のウィンドウを表示し、利用者の操作を待つ
    app.run()


# このファイルを直接実行したときだけ main() を呼び出す
if __name__ == "__main__":
    main()
```

## Tk10-4. 保存したapp.pyを実行する

1. `calculator.py` と `app.py` を保存したTk10のフォルダを開き、フォルダの場所を表す文字列（パス）をコピーしてください。Windowsはエクスプローラー上部のアドレスバーをクリックしてCtrl + C、macOSはFinderでフォルダを選択してOption + Command + C、Linux（GNOMEの「ファイル」）はフォルダを開いてCtrl + Lで場所欄を表示しCtrl + Cを押してください。
2. VS Codeの **表示（View）→ ターミナル（Terminal）** を選び、文字で操作を入力するターミナルを開いてください。ターミナルへ次のコマンドを入力し、引用符の中を、手順1のエクスプローラーのアドレスバー、Finderのフォルダ選択、Linuxの場所欄でコピーしたTk10のフォルダのパスに置き換えてください。Enterキーを押すと、ターミナルの現在のフォルダがTk10のフォルダに変わります。

   ```text
   cd "コピーしたTk10のフォルダのパス"
   ```

3. VS Codeの **表示（View）→ ターミナル（Terminal）** を選び、Tk10のフォルダへ移動したターミナルを表示してください。Windowsは次のコマンドを入力してEnterキーを押してください。macOS / Linuxは `python3 app.py` と入力してEnterキーを押してください。「関数電卓」というタイトルの画面に、数字の入力欄、計算記号、数字・C・小数点・sin・cosのボタンが表示されます。

   ```text
   python app.py
   ```

   Windowsで `python` が見つからない場合は、VS Codeの **表示（View）→ ターミナル（Terminal）** で同じターミナルを表示し、`py app.py` と入力してEnterキーを押してください。同じ電卓が起動します。

`PS C:\...>` や `$` など、すでにターミナルに表示されている入力待ちの文字は入力しないでください。電卓が開いている間はTkinterが操作を待つため、起動に使ったターミナルへ次のコマンドを入力できません。

## Tk10-5. 1.5 + 2.5 を計算する

小数点ボタンの「.」は、Pythonで小数を書く記号に合わせています。電卓画面の「.」ボタンを数字より先に押すと `0.` が入り、2個目の点を押しても追加されません。

足し算・引き算・答えを出すボタンは、電卓で使う記号の「+」「-」「=」に合わせています。掛け算と割り算のボタンには、Pythonで計算式を書くときの記号「*」「/」を使います。

1. 電卓画面の「C」ボタンで入力と式を消し、電卓画面の「1」「.」「5」の各ボタンを順に押してください。「数字（sin・cosは角度を度で入力）」の入力欄に `1.5`、式の欄に `計算式:`、結果の欄に `答え:` と表示されます。
2. 電卓画面の「+」ボタンをクリックしてください。式の欄に `計算式: 1.5 +` と表示され、入力欄が空になります。
3. 電卓画面の「2」「.」「5」の各ボタンを順に押してください。数字の入力欄に `2.5` と表示され、式の欄は `計算式: 1.5 +` のままです。
4. 電卓画面の「=」ボタンを押してください。式の欄に `計算式: 1.5 + 2.5 = 4.0`、結果の欄に `答え: 4.0` と表示され、入力欄にも答えの `4.0` が入ります。`.0` は小数部分が0であることを表します。

「-」は引き算、「*」は掛け算、「/」は割り算のボタンです。正常な計算の答えの `4.0` が入力欄にある状態で、電卓画面の計算記号ボタンを押すと、その答えを使って計算を続けられます。新しい計算を始める場合は、電卓画面の数字ボタンか小数点ボタンを押してください。前の答えと式が消え、数字ボタンなら押した数字、小数点ボタンなら `0.` が入力欄へ入ります。

「C」はClear（消去）の頭文字です。入力や式を最初からやり直すためのボタンです。途中の入力を間違えた場合に電卓画面の「C」ボタンを押すと、入力欄と保存した式が消え、式の欄は `計算式:`、結果の欄は `答え:` に戻ります。

## Tk10-6. 入力を間違えた時に直す

### キーボードで点を2個入力した場合

1. 電卓画面の「C」ボタンを押し、電卓画面の「1」「.」「5」「+」の各ボタンを順に押してください。式の欄は `計算式: 1.5 +`、入力欄は空、結果の欄は `答え:` になります。
2. 電卓画面の数字の入力欄をクリックし、キーボードで `1.2.3` と入力してください。入力欄は `1.2.3`、式の欄は `計算式: 1.5 +` のままです。
3. 電卓画面の「=」ボタンを押してください。結果の欄に「数字を入力してください（例: 1.5）」と表示されます。入力欄は `1.2.3`、式の欄は `計算式: 1.5 +` のままです。
4. 電卓画面の入力欄で、`1.2.3` の先頭から末尾までマウスの左ボタンを押したまま動かして全体を選択し、Windows / LinuxはBackspaceキー、macOSはDeleteキーで削除してください。空になった入力欄へキーボードで `2.5` と入力してください。入力欄は `2.5`、式の欄は `計算式: 1.5 +` のままで、入力ミスの案内は次の計算まで残ります。
5. 電卓画面の「=」ボタンを押してください。式の欄は `計算式: 1.5 + 2.5 = 4.0`、結果の欄は `答え: 4.0`、入力欄は `4.0` に変わります。

キーボードで新しい計算を始める場合は、最初に電卓画面の「C」ボタンを押してください。キーボードの入力は、数字ボタンのように前の答えを自動では消しません。

### 0で割る入力の場合

電卓画面の「C」ボタンを押して入力と式を消し、電卓画面の「1」「.」「5」「/」「0」「=」の各ボタンを順に押してください。結果の欄は「0では割れません」、式の欄は `計算式: 1.5 /`、入力欄は `0` になります。保存した式は空になります。

0で割った後には答えがなく、入力欄に残る `0` は割る数として入力した数字です。その後に電卓画面の数字ボタンをクリックすると、残った `0` と前の式を消して、その数字から新しい入力を始めます。電卓画面の小数点ボタンなら `0.` から新しく入力します。電卓画面の計算記号ボタンを押した場合は、残る `0` を新しい計算の最初の数字として使います。

## Tk10-7. sin・cosを使う

### sinとcosだけを計算する

1. 電卓画面の「C」「0」「sin」の各ボタンを順に押してください。式の欄は `計算式: sin(0.0°) = 0.0`、結果の欄は `答え: 0.0`、入力欄は `0.0` になります。角度が0度なら、棒を地面に寝かせた状態なので高さの割合は0です。
2. 電卓画面の「C」「0」「cos」の各ボタンを順に押してください。式の欄は `計算式: cos(0.0°) = 1.0`、結果の欄は `答え: 1.0`、入力欄は `1.0` になります。角度が0度なら、棒の横の長さは棒の長さと同じなので割合は1です。
3. 入力欄にcosの答え `1.0` がある状態で、電卓画面の「*」「1」「0」「=」の各ボタンを順に押してください。式の欄は `計算式: 1.0 * 10.0 = 10.0`、結果の欄は `答え: 10.0`、入力欄は `10.0` になります。長さ10メートルの棒が0度なら、横の長さも10メートルです。

30度のsinを試す場合は、電卓画面の「C」「3」「0」「sin」の各ボタンを順に押してください。結果の欄には、約0.5を表す `答え: 0.49999999999999994` など、0.5に近い小数が表示されます。入力欄にもその数値が入り、式の欄には `sin(30.0°)` と答えが表示されます。Pythonの `float`（小数も扱える数値）は、計算した値を近い数で表すことがあるため、末尾の桁は実行環境によって異なる場合があります。

入力欄に30度のsinの答えがある状態で、電卓画面の「*」「1」「0」「=」の各ボタンを順に押してください。結果の欄には約5の数値、入力欄には同じ数値、式の欄にはsinの数値に `* 10.0` を続けた計算と答えが表示されます。長さ10メートルの棒の高さが約5メートルと分かります。この章では、余分な桁を丸める処理は追加しません。

### 保存済みの式へsinの値を使う

1. 電卓画面の「C」「2」「+」「0」「sin」の各ボタンを順に押してください。式の欄は `計算式: 2.0 + sin(0.0°)`、結果の欄は `答え: 0.0`、入力欄は `0.0` になります。結果の欄の0.0はsinだけの答えで、`2 +` の計算はまだ終わっていません。
2. 電卓画面の「=」ボタンを押してください。プログラムは保存済みの `2 +` にsinの値 `0.0` を使います。式の欄は `計算式: 2.0 + 0.0 = 2.0`、結果の欄は `答え: 2.0`、入力欄は `2.0` になります。式の欄のsinという表示は、四則演算に使った数値へ変わります。

sinの値を使わず入力し直す場合は、電卓画面の「C」「2」「+」「0」「sin」「3」の各ボタンを順に押してください。sinの答えだけが消え、式の欄は `計算式: 2.0 +`、入力欄は `3`、結果の欄は `答え:` に変わります。電卓画面の「=」ボタンを押すと、式の欄は `計算式: 2.0 + 3.0 = 5.0`、結果の欄は `答え: 5.0`、入力欄は `5.0` になります。小数点ボタンでも、保存済みの式を残して `0.` から入力し直せます。

### 保存済みの式へsinの値と計算記号を続ける

1. 電卓画面の「C」「2」「+」「0」「sin」の各ボタンを順に押してください。式の欄は `計算式: 2.0 + sin(0.0°)`、結果の欄は `答え: 0.0`、入力欄は `0.0` になります。0.0はsinだけの答えです。
2. 電卓画面の「*」ボタンを押してください。プログラムはsinの値 `0.0` と「*」を保存済みの `2.0 +` へ追加します。式の欄は `計算式: 2.0 + 0.0 *`、入力欄は空、結果の欄は `答え:` になります。sinという表示は四則演算に使う数値へ変わり、掛ける数字の入力を待ちます。
3. 電卓画面の「3」「=」の各ボタンを順に押してください。掛け算を足し算より先に計算するため、式の欄は `計算式: 2.0 + 0.0 * 3.0 = 2.0`、結果の欄は `答え: 2.0`、入力欄は `2.0` になります。

### 角度を間違えて入力した場合

電卓画面の「C」「2」「+」の各ボタンを順に押し、数字の入力欄をクリックしてキーボードで `30°` と入力し、電卓画面の「sin」ボタンを押してください。結果の欄は「数字を入力してください（例: 1.5）」、式の欄は `計算式: 2.0 +`、入力欄は `30°` のままです。

電卓画面の入力欄で `30°` 全体をマウスで選択し、Windows / LinuxはBackspaceキー、macOSはDeleteキーで消してください。空になった入力欄へキーボードで `0` を入力し、電卓画面の「sin」「=」の各ボタンを順に押してください。保存済みの式を使い、式の欄は `計算式: 2.0 + 0.0 = 2.0`、結果の欄は `答え: 2.0`、入力欄は `2.0` に変わります。

sin・cosボタンは、押すたびに入力欄にある数値を度の角度として計算します。たとえばcosの答え `1.0` の直後にsinを押すと、0度のsinへ戻るのではなく、1度のsinを計算します。別の角度をキーボードで入力する場合は、先に電卓画面の「C」ボタンを押してください。計算途中の角度だけを直す場合は、Cで式を消さず、入力欄の文字列だけをマウスで選択して削除してください。

## Tk10-8. ボタンの配置を読む

`create_display` は入力欄・式・答えを、ウィンドウ内で `pack`（部品を順に配置する処理）を使って並べます。`create_buttons` は、その下へボタンの枠を `pack` で置きます。各ボタンは枠内で `grid` を使って行と列へ置くので、同じ親部品の中でpackとgridを混ぜません。

`fill="both"` と `expand=True` は、余った縦横の領域へ枠を広げる指定です。`columnconfigure` の `weight=1` は各列へ余った幅を同じ割合で配り、`uniform="buttons"` は4列の幅をそろえます。`rowconfigure` の `weight=1` は各行へ余った高さを同じ割合で配ります。ボタンの `sticky="nsew"` は、割り当てられたマスの上下左右へボタンを広げる指定です。[Tk公式のgrid配置](https://www.tcl-lang.org/man/tcl8.6/TkCmd/grid.htm)

配置の比較には、[Tk9の `create_digit_buttons`（98〜134行）](../Tk09_小数点を置く/calculator.py#L98-L134)と、[Tk10の `create_buttons`（53〜91行）](./calculator.py#L53-L91)を使ってください。Tk9は数字・C・小数点を一つの枠に置き、Tk10は計算記号とsin・cosも同じ枠へ置きます。Tk10の変更した全体は、[`calculator.py` 全体](./calculator.py)で確認してください。ボタンの作成処理を抜き出したものが次のコードです。

元ファイル：[`calculator.py` の93〜102行](./calculator.py#L93-L102)。

```python
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
```

`column_span` はボタンが使う列の数です。「=」だけ2を指定し、その他のボタンは1列分を使います。入力欄は横へ広げ、式と答えは幅380ピクセルで折り返します。画面の最小サイズは420×520ピクセルですが、OSや文字の大きさによって必要な領域は変わります。文字が窮屈なら、電卓のウィンドウの端をドラッグして広げてください。

## Tk10-9. 角度の計算を読む

`apply_trigonometry` は `read_number` で入力欄の数字を読み取り、`math.radians` で度からラジアンへ変換します。`math.sin` か `math.cos` が返した数値を、プログラムは答えの欄と入力欄へ表示します。保存済みの式があれば、その式へ角度の計算名を表示用として続け、数値のリスト自体は残します。

元ファイル：[`calculator.py` の352〜392行](./calculator.py#L352-L392)。

```python
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
        # operation_text（角度の計算表示）に計算名・度の角度・度の記号を含む文字列を入れる
        operation_text = f"{function_name}({angle_degrees}°)"
        # self.calculation_parts に式が残っていれば、次の処理を実行する
        if self.calculation_parts:
            # self.expression_label に、保存した式と operation_text を表示する
            self.expression_label.config(
                text="計算式: "
                + " ".join(str(part) for part in self.calculation_parts)
                + " " + operation_text
            )
        # self.calculation_parts に式が残っていなければ、次の処理を実行する
        else:
            # self.expression_label に、operation_text と answer を表示する
            self.expression_label.config(text=f"計算式: {operation_text} = {answer}")
        # self.result_label の表示を「答え: 」と answer の値を含む文字列に変える
        self.result_label.config(text=f"答え: {answer}")
        # self.number_entry の先頭から末尾までの文字列を削除する
        self.number_entry.delete(0, tkinter.END)
        # self.number_entry の先頭に answer を文字列にした値を挿入する
        self.number_entry.insert(0, str(answer))
        # self.replace_input に True を入れる
        self.replace_input = True
```

`prepare_input` は、数字ボタンと小数点ボタンから実行されます。`self.replace_input` がFalseなら現在の入力を消しません。Trueで保存済みの式があれば、角度の計算結果だけを消して式は残します。Trueで保存済みの式がなければ、`clear` で前の計算全体を消します。

元ファイル：[`calculator.py` の104〜123行](./calculator.py#L104-L123)。

```python
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
            # self.expression_label に、保存した式の各値を空白でつないだ文字列を表示する
            self.expression_label.config(
                text="計算式: " + " ".join(str(part) for part in self.calculation_parts)
            )
            # self.replace_input に False を入れる
            self.replace_input = False
        # self.calculation_parts に式が残っていなければ、次の処理を実行する
        else:
            # 同じ電卓の入力・計算式・結果表示を空にする self.clear を呼び出す
            self.clear()
```

## Tk10-10. 変更して再実行する

ウィンドウのタイトルを変える場合は、VS Codeで `calculator.py` を開き、検索欄（Windows / LinuxはCtrl + F、macOSはCommand + F）で `self.window.title` を検索してください。検索を使うと、長いファイルからタイトルを変える一行を見つけられます。次の2行を置き換えてください。

元ファイル：[`calculator.py` の19〜20行](./calculator.py#L19-L20)。

```python
        # self.window のタイトルを「関数電卓」にする
        self.window.title("関数電卓")
```

変更後の2行は、次の内容です。変更後の例は配布コードとは異なります。

```text
        # self.window のタイトルを「角度も計算できる電卓」にする
        self.window.title("角度も計算できる電卓")
```

起動中の電卓を閉じ、実行に使ったターミナルが文字を入力できる状態へ戻ったことを確認してください。VS Codeで変更した `calculator.py` を保存してください（Windows / LinuxはCtrl + S、macOSはCommand + S）。VS Codeの **表示（View）→ ターミナル（Terminal）** でTk10用フォルダへ移動済みのターミナルを開き、Windowsなら `python app.py`、macOS / Linuxなら `python3 app.py` と入力してEnterキーを押してください。ウィンドウのタイトルが「角度も計算できる電卓」に変わり、電卓の機能は同じままです。

## Tk10-11. 今回の内容

- 数字と計算記号は、同じ枠内の行と列へ配置します。
- sin・cosボタンは、入力欄の数値を度の角度として読み、ラジアンへ変換して計算します。
- 計算途中でsin・cosを押した場合、保存済みの式を残し、入力中の角度だけを計算した数値へ置き換えます。
- 新しい数字ボタンで角度の答えを置き換える場合、保存済みの式があればその式を残します。
- 電卓の機能は `calculator.py` に置き、起動は同じ `app.py` から行います。

この電卓は小数を丸めずに表示します。`0.1 + 0.2` の余分な桁やsin・cosの近似値の表示を整える教材は準備中です。[Python公式の小数計算の説明](https://docs.python.org/3/tutorial/floatingpoint.html)

---

[進む：完成した電卓を保存して動かす](../../../基礎編_さっさと学びたい人へ/教材/完成品の入口/電卓を動かす.md)

[戻る：Tk9. 小数点を置く](../Tk09_小数点を置く/小数点を置く.md)

[戻る：電卓ルートの目次](../../目次.md)
