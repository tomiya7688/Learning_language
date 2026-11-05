# 8. 完成した関数電卓のsin・cosと操作待ちを読む

> **「30度を入力してsinを押すと、どうして0.5が出るの？」**

[7章](./07_四則演算を読む.md)までで四則演算の処理を読みました。ここでは`calculator.py`の398〜439行を、**実際のPythonコードを1行ずつ**読んでいきます。ここで`calculator.py`の最後まで到達します。

## 398〜416行：入力された角度からsin・cosを求める

数字を読み、度をラジアンへ変換してから、押したボタンに対応する計算をします。

実ファイルのPythonコード：[ `calculator.py` の398〜416行](./src/calculator.py#L398-L416)

```python
    # 入力欄の角度からsinかcosを求める apply_trigonometry を宣言する
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
```

**元ファイルの行番号順**に、右側の計算と呼び出す処理を確認してください。

- **399行目：`def apply_trigonometry(self, function_name):`** — `apply_trigonometry`は「三角比の計算を適用する」という意味のメソッドです。`function_name`（関数名）に、ボタンから渡された文字列`"sin"`または`"cos"`が入ります。

- **402行目：`angle_degrees = self.read_number("角度を度で入力してください（例: 30）")`** — 右側の`self.read_number("角度を度で入力してください（例: 30）")`が入力欄を読み、数値か`None`を返します。括弧の文字列は空欄の際の案内。左側の`angle_degrees`（度で表した角度）へ入れます。

- **404行目：`if angle_degrees is None:`** — 右側の`angle_degrees is None`は入力の数値が読めなかったかどうかです。数値の0度とは違います。

- **406行目：`return`** — `return`で角度の計算だけを終了します。数値がなければ、sin・cosの計算へ進みません。

- **408行目：`angle_radians = math.radians(angle_degrees)`** — 右側の`math.radians(angle_degrees)`が度の角度をラジアンへ変換し、左側の`angle_radians`（ラジアンの角度）へ入れます。30度なら約0.5236ラジアンです。`radians`はラジアンという意味です。

- **410行目：`if function_name == "sin":`** — `if function_name == "sin":`は指定された計算名が文字列`"sin"`かを調べます。`==`は左右が等しいか確認する記号です。

- **412行目：`answer = math.sin(angle_radians)`** — 右側の`math.sin(angle_radians)`はラジアンの角度からsinを求めます。30度のsinは約0.5。その結果を左側の`answer`（答え）へ保存します。

- **414行目：`else:`** — `else`は指定された計算名が`"sin"`ではなかった場合。ボタンの指定が`"sin"`と`"cos"`だけなので、ここではcosです。

- **416行目：`answer = math.cos(angle_radians)`** — 右側の`math.cos(angle_radians)`でcosを求め、左側の`answer`へ保存します。0度のcosは1です。

## 417〜434行：sin・cosの式と答えを表示する

途中の式が残っているかで表示の形が変わります。答えを入力欄へ表示し、元の数値も残します。

実ファイルのPythonコード：[ `calculator.py` の417〜434行](./src/calculator.py#L417-L434)

```python
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
```

**元ファイルの行番号順**に、右側の計算と呼び出す処理を確認してください。

- **418行目：`operation_text = f"{function_name}({self.format_number(angle_degrees)}°)"`** — 左側の`operation_text`は「角度計算の表示文字列」。右側の`f"{function_name}({self.format_number(angle_degrees)}°)"`は`f`を付けた文字列の`{...}`へ値を組み込みます。sinと30度なら`"sin(30°)"`です。`format_number`は角度の表示を整えます。

- **420行目：`if self.calculation_parts:`** — `self.calculation_parts`は保存された計算式の部品の一覧です。空でなければ式の途中なので、次の表示を使います。

- **422行目：`self.expression_label.config(`** — `self.expression_label.config(`で、計算式を表示する欄の文字を更新する呼び出しを始めます。次の行で`text=`の中身を作ります。

- **423行目：`text="計算式: "`** — 右側の`"計算式: "`は、式の表示の先頭に付ける文字列です。

- **424行目：`+ self.format_expression()`** — 右側の`self.format_expression()`が現在保存されている式の部品を文字列につなぎ、先頭の`"計算式: "`の後ろへ追加します。

- **425行目：`+ " " + operation_text`** — 右側の`" " + operation_text`は空白とsinなどの計算名・角度の表示を追加します。例では`"計算式: 2 + sin(30°)"`です。

- **426行目：`)`** — `)`で式の表示欄へ文字列を設定する処理を閉じます。計算途中の式はこの時点では消していません。

- **428行目：`else:`** — `else`は`self.calculation_parts`が空、つまり途中の式がない場合です。

- **430行目：`self.expression_label.config(`** — 式の表示欄の文字を更新する呼び出しを始めます。

- **431行目：`text="計算式: " + operation_text + " = " + self.format_number(answer)`** — 右側の`"計算式: " + operation_text + " = " + self.format_number(answer)`をつなげます。sin30度なら`"計算式: sin(30°) = 0.5"`になります。`format_number`が答えの表示桁を整えます。

- **432行目：`)`** — `)`で、表示欄へ文字を設定する呼び出しを閉じます。

- **434行目：`self.show_answer(answer)`** — `self.show_answer(answer)`へ数値の答えを渡し、答え欄と入力欄へ文字列を表示します。同時に、次の計算のために表示前の元の数値も保存します。

## 436〜439行：ウィンドウが操作を待つ

ここまでで電卓本体の最後の行です。起動ファイルから呼ばれる`run`の動きを確認します。

実ファイルのPythonコード：[ `calculator.py` の436〜439行](./src/calculator.py#L436-L439)

```python
    # ウィンドウを表示する run を宣言する
    def run(self):
        # self.window を表示し、利用者の操作を待ち続ける
        self.window.mainloop()
```

**元ファイルの行番号順**に、右側の計算と呼び出す処理を確認してください。

- **437行目：`def run(self):`** — `run`は「実行する」という意味のメソッドです。ここではウィンドウの操作待ちを始める処理を宣言します。クラスに書いた段階ではまだ動きません。

- **439行目：`self.window.mainloop()`** — `self.window.mainloop()`は、作った電卓のウィンドウを表示して、ボタンやキー入力などの操作を受け取り続けます。`main`は「主な」、`loop`は「繰り返す」。ウィンドウを閉じると操作待ちを終えます。


## 電卓を作ってから操作するまで

起動ファイルの`app.py`では、最初に`CalculatorApp()`で電卓を作ります。その準備中に`create_display`と`create_buttons`が呼ばれ、sin・cosなどのボタンへ処理が登録されます。次に`app.run()`が呼ばれ、`mainloop()`で操作を待ちます。

この時点でボタンの処理を「登録しただけ」と「利用者が押してから呼び出される」に分けてください。sinボタンは、押されたときに`apply_trigonometry("sin")`が呼ばれます。`calculate()`の四則演算とは別のメソッドですが、`show_answer`で答えを表示・保存する部分は共通です。

## 変更せずに確かめる：角度で答えが変わる

1. 電卓を開いたまま「C」「0」「cos」を押してください。結果の欄が `答え: 1` になることを確認してください。
2. 続けて「C」「9」「0」「sin」を押してください。`答え: 1` と表示されます。
3. `calculator_practice/src/calculator.py` の `def apply_trigonometry(self, function_name):` を検索して、`math.radians`、`math.sin`、`math.cos`、`self.show_answer(answer)` が呼ばれる順番と比較してください。

次は、ここまで読んだコードを使って、電卓へ自分の変更を加えます。

---

[次へ：9. 電卓を改造してみる](./09_電卓を改造する.md)

[戻る：関数電卓のコードを読む目次](./電卓のコードを読む.md)
