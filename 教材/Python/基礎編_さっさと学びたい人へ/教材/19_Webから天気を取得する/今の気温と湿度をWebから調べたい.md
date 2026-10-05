# 今の気温と湿度をWebから調べたい

Open-Meteoが提供する東京付近の現在の気温と湿度を取得し、ターミナルに表示します。値は天気モデルのデータから算出されています。

PythonとVS Codeをまだ使える状態にしていない場合は、先に準備します。

[進む：Pythonを書いて動かす準備をする](../../../基礎編_ゆっくり学びたい人へ/教材/01_環境構築/環境構築ガイド.md)

保存するフォルダを1つ選び、このページではその場所を「練習用フォルダ」と呼びます。

## コードを書く・保存する

VS Codeで新しいテキストファイルを開きます（Windows / Linuxは Ctrl + N、macOSは Command + N）。次のコード全体をそのファイルへコピーしてください。

```python
# requests は「要求」という意味
# 追加した Requests の処理を requests という名前で使えるようにする
import requests

# latitude は「緯度」という意味
# latitude に東京付近の緯度35.68を入れる
latitude = 35.68
# longitude は「経度」という意味
# longitude に東京付近の経度139.76を入れる
longitude = 139.76

# 下の処理を試し、通信やデータに問題があった場合は except の処理へ進む
try:
    # response は「応答」という意味
    # response に指定した緯度・経度の現在の気温と湿度を取得した応答を入れる
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": latitude, "longitude": longitude, "current": "temperature_2m,relative_humidity_2m"},
        timeout=10,
    )
    # response が表す応答がHTTPエラーなら、例外を発生させる
    response.raise_for_status()
    # data は「データ」という意味
    # data に response のJSONをPythonで扱える形に変換して入れる
    data = response.json()
    # 「気温:」と data の現在の気温と「℃」を表示する
    print("気温:", data["current"]["temperature_2m"], "℃")
    # 「湿度:」と data の現在の湿度と「%」を表示する
    print("湿度:", data["current"]["relative_humidity_2m"], "%")
# 通信に問題があるか、必要な項目がないか、データの形が合わない場合、下の行を実行する
except (requests.exceptions.RequestException, KeyError, TypeError):
    # 「天気を取得できませんでした。接続や取得先を確認してください」と表示する
    print("天気を取得できませんでした。接続や取得先を確認してください")
```

Windows / Linuxは Ctrl + S、macOSは Command + S を押し、練習用フォルダに `get_weather.py` という名前で保存します。ファイル名の最後は `.py` にします。

get は「取得する」、weather は「天気」という意味です。 `.py` はPythonのコードを書いたファイルの末尾に付けます。

[サンプルファイルを開く](./get_weather.py)

## 保存したファイルを実行する

コマンドは、コードを書いた欄ではなく、VS Codeのターミナルへ入力します。ターミナルは、文字で操作を入力し、プログラムの結果を見る場所です。表示されていなければ、**表示（View）→ ターミナル（Terminal）** を選びます。

### 保存先フォルダのパスをコピーする

`get_weather.py` を保存したフォルダの場所を、次の操作でコピーします。

- Windows：エクスプローラーで保存先フォルダを開き、上部のアドレス欄をクリックします。表示されたフォルダのパス全体を選び、Ctrl + C を押します。
- macOS：Finderで保存先フォルダを選択し、Option + Command + C を押して、そのフォルダのパスをコピーします。ファイルではなくフォルダを選びます。
- Linux（GNOMEの「ファイル」を使う場合）：保存先フォルダを開き、Ctrl + L で場所の入力欄を表示して、フォルダのパスを Ctrl + C でコピーします。

### ターミナルを保存先フォルダへ移動する

VS Codeのターミナルを開き、次の形で入力します。引用符の中は、上の操作でコピーした**フォルダのパス**に置き換えてください。Windowsは Ctrl + V、macOSは Command + V、Linuxは Ctrl + Shift + V で貼り付けます。入力し終えたら Enter キーを押します。

```text
cd "コピーした保存先フォルダのパス"
```

`cd` は、ターミナルで現在使っているフォルダを変える操作です。`PS C:\Users\...>` など、すでに表示されている文字は入力しません。

### Webのデータを読む道具を追加する

練習用フォルダの `.venv` に専用のPython実行環境を作り、Requestsを追加します。使うのはこのフォルダのPythonです。実行するPythonの場所をコマンドに書きます。インストールにはインターネット接続が必要です。

### Windows

まず専用の実行環境を作ります。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
python -m venv .venv
```

続けて、作った環境のPythonへRequestsを追加します。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.\.venv\Scripts\python.exe -m pip install requests
```

追加が終わったら、保存したファイルを実行します。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.\.venv\Scripts\python.exe get_weather.py
```

### macOS / Linux

まず専用の実行環境を作ります。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
python3 -m venv .venv
```

続けて、作った環境のPythonへRequestsを追加します。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.venv/bin/python -m pip install requests
```

追加が終わったら、保存したファイルを実行します。

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.venv/bin/python get_weather.py
```

これらの `-m venv` は専用の環境を作り、`-m pip install requests` はその環境へRequestsを追加します。作成や追加に失敗した場合は表示されたエラーを確認し、プログラムの実行へ進む前に、ページ上部の準備手順でPythonを確認してください。

## 実行結果

次は表示例です。実際の数字は取得した時点と場所で変わります。インターネットへ接続して実行してください。

```text
気温: 25.0 ℃
湿度: 60 %
```

## このコードの読み方

緯度と経度は、地図上の場所を数字で指定するものです。東京付近の `35.68` と `139.76` を使っています。`latitude` など、値を使うための名前を **変数** と呼びます。

`import requests` は追加したRequestsの処理を使えるようにします。`requests.get(...)` は、指定したURL（取得先のアドレス）へデータを求めます。`params` は取得の条件で、`latitude` が緯度、`longitude` が経度、`current` が現在の項目です。`temperature_2m` は地上2mの気温、`relative_humidity_2m` は地上2mの相対湿度を指定します。

こうして、決められたアドレスと条件で外部のサービスからデータを受け取る仕組みを **Web API** と呼びます。Open-Meteoのこの例は学習のための取得で、APIキーを指定せずに使います。

`timeout=10` は、接続やデータの受信を待ち続けないための指定です。通信全体を必ず10秒で終えるという意味ではありません。`response.raise_for_status()` はHTTPエラーの応答を例外にします。

`response.json()` は受け取ったJSON（名前付きの情報を記録する書き方）をPythonで扱える形に変換します。ここでは辞書という、項目と値を組にしたものになります。`data["current"]["temperature_2m"]` は、「現在の情報」の中から「気温」を取り出す指定です。

`print(...)` はターミナルに表示します。引用符で囲んだ値は **文字列**（文字の並び）です。名前の後ろに `()` を付けて呼び出す処理を **関数** と呼びます。`try:` の下の処理で通信などの問題が起きたら、`except` の下で案内を表示します。実行中の問題を **例外** と呼び、`requests.exceptions.RequestException` は通信などの問題、`KeyError` は必要な項目がない問題、`TypeError` はこの例ではデータの形が合わない問題を扱います。

行頭の空白でまとまりを示す書き方を **インデント** と呼び、`try` や `except` の中は空白4つです。`requests.get(` から `)` までは、1つの呼び出しを読みやすく改行して書いています。取得に失敗したときは、インターネット接続とURLの書き間違いを確認してから再実行します。

コードの `#` から行末までに書いた説明を **コメント** と呼びます。コメントは実行されません。

## どこを変えるか

表示する気温の前に、場所の名前を付けます。行頭の空白4つも残してください。

VS Codeで `get_weather.py` を開き、**27行目**を探します。行番号は、最初のコードをコメントと空行も含めてそのまま保存した場合の番号です。

Windows / Linuxは Ctrl + F、macOSは Command + F を押します。検索欄に次の文字を入力して、対象の行を探します。

```text
print("気温:"
```

対象の行と、その直上の処理コメントを、次のように置き換えます。

変更前：

```python
    # 「気温:」と data の現在の気温と「℃」を表示する
    print("気温:", data["current"]["temperature_2m"], "℃")
```

変更後：

```python
    # 「東京付近の気温:」と data の現在の気温と「℃」を表示する
    print("東京付近の気温:", data["current"]["temperature_2m"], "℃")
```

## 保存してもう一度実行する

VS Codeで `get_weather.py` を保存します。Windows / Linuxは Ctrl + S、macOSは Command + S を押します。

最初の実行と同じターミナルを使えます。

コマンドは、コードを書いた欄ではなく、VS Codeのターミナルへ入力します。ターミナルは、文字で操作を入力し、プログラムの結果を見る場所です。表示されていなければ、**表示（View）→ ターミナル（Terminal）** を選びます。

保存先フォルダへ移動済みなら、次の実行コマンドへ進みます。別のフォルダに移動した場合は、最初の実行の手順でコピーした保存先フォルダのパスを使い、ターミナルへ `cd "コピーした保存先フォルダのパス"` と入力して Enter キーを押します。

### Windows

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.\.venv\Scripts\python.exe get_weather.py
```

### macOS / Linux

1. VS Codeのターミナルを開き、次のコマンドを入力します。
2. Enter キーを押します。

```text
.venv/bin/python get_weather.py
```

次は変更後の表示例です。数字は再取得した時点で変わります。

```text
東京付近の気温: 25.0 ℃
湿度: 60 %
```

## 公式資料

[Open-Meteoの取得条件とデータの公式説明](https://open-meteo.com/en/docs)

[Requestsの取得・タイムアウト・エラーの公式説明](https://requests.readthedocs.io/en/latest/user/quickstart/)

---

[進む：通常基礎編で詳しく読む](../../../基礎編_ゆっくり学びたい人へ/教材/17_Web_APIからデータを取得/Web_APIからデータを取得.md)

[戻る：作りたいもの・試したいことから選ぶ目次](../../目次.md)
