# 17. Web APIからデータを取得

この章では、**インターネット上にあるデータをPythonから取得する方法**を学びます。

今回作るのは、公開されている天気APIから現在の気温と湿度を取得して表示するプログラムです。

この章の本質はこれです。

> **毎回ブラウザ開いて、人間がコピペしてたら日が暮れるわ！**

人間が画面を見て写すのではなく、Pythonから直接データを取りに行きます。

---

## 17-1. 今回作るもの

[weather_api.py](./weather_api.py) を開いてください。

`weather` は「天気」、`api` はAPIという意味です。

実行すると、たとえば次のように表示されます。

```text
現在の気温: 26.4 ℃
現在の湿度: 71 %
```

値はそのときのデータによって変わります。

---

## 17-2. なぜWeb APIが必要なの？

天気を知りたいだけなら、ブラウザで天気サイトを開けば済みます。

でも、プログラムで、

- 天気を自動取得したい
- 毎時間記録したい
- 気温によって処理を変えたい
- GUIへ表示したい
- 複数地点をまとめて確認したい

となると、人間が毎回ブラウザを開いて数字をコピーするのは大変です。

> **「毎回そこ人間がやるんかい！」**

となります。

そこで、プログラムから直接データを受け取れる入口を使います。

それが **Web API** です。

---

## 17-3. APIとは

APIは、ざっくり言えば、

> **別のプログラムが使うために用意された入口**

です。

今回なら、

```text
自分のPython
    ↓
Open-MeteoのAPI
    ↓
天気データ
    ↓
自分のPython
```

という流れになります。

画面を人間が読む代わりに、Python同士でデータをやり取りします。

---

## 17-4. 今回使うAPI

この教材では **Open-Meteo** のForecast APIを使います。

公式ドキュメント:

- [Open-Meteo Weather Forecast API](https://open-meteo.com/en/docs)

今回は、APIキーなしで取得できる範囲を使います。

サンプルでは東京付近の緯度・経度を指定します。

```text
latitude  = 35.68
longitude = 139.76
```

---

## 17-5. URLとは

APIにもアクセス先があります。

今回の入口は、

```text
https://api.open-meteo.com/v1/forecast
```

です。

ブラウザのWebページと同じようにURLを使いますが、返ってくるものは人間向けの画面ではなく、プログラムが扱いやすいデータです。

---

## 17-6. requestsを使う

今回は外部ライブラリの **requests** を使います。

まだ入れていない場合は、ターミナルで、

Windows:

```text
python -m pip install requests
```

macOS / Linux:

```text
python3 -m pip install requests
```

と入力します。

15章で学んだ、

> 外部ライブラリをpipで入れる

をそのまま使います。

---

## 17-7. サンプルコード

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.68,
    "longitude": 139.76,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Tokyo"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

current = data["current"]

print("現在の気温:", current["temperature_2m"], "℃")
print("現在の湿度:", current["relative_humidity_2m"], "%")
```

---

## 17-8. `requests.get()`

```python
response = requests.get(url, params=params, timeout=10)
```

は、

> 指定したURLへデータを取りに行く

処理です。

今回使っているのはHTTPの **GET** です。

今は、

> GET = データをください

くらいに考えておけば十分です。

---

## 17-9. paramsは何を渡している？

```python
params = {
    "latitude": 35.68,
    "longitude": 139.76,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Tokyo"
}
```

ここでは辞書を使っています。

それぞれ、

```text
latitude
→ 緯度

longitude
→ 経度

current
→ 現在値として何が欲しいか

timezone
→ 時刻をどの地域に合わせるか
```

です。

11章で学んだ辞書が、そのままAPIでも使えます。

---

## 17-10. リクエストとレスポンス

APIへ送る側を **リクエスト** と呼びます。

返ってくる側を **レスポンス** と呼びます。

```text
Python
  │
  │ リクエスト
  ↓
API
  │
  │ レスポンス
  ↓
Python
```

です。

---

## 17-11. JSONで返ってくる

Open-MeteoからはJSON形式でデータが返ってきます。

```python
data = response.json()
```

とすると、JSONをPythonで使える辞書やリストの形へ変換できます。

16章でやったJSONがここでつながります。

---

## 17-12. 辞書として取り出す

返ってきたデータの中には、

```python
data["current"]
```

という現在値のまとまりがあります。

さらに、

```python
current["temperature_2m"]
```

で気温、

```python
current["relative_humidity_2m"]
```

で湿度を取り出せます。

つまり、

```text
JSON
↓
Pythonの辞書
↓
キーを指定して必要な値を取り出す
```

という流れです。

---

## 17-13. `raise_for_status()` は何？

通信に失敗したり、URLやパラメータがおかしかったりすると、正常なデータが返らないことがあります。

```python
response.raise_for_status()
```

は、

> HTTPでエラーが返っていたら、成功したふりをせず例外にする

ために使います。

13章の例外処理につながります。

---

## 17-14. 通信なので失敗することがある

Web APIは、自分のPCだけで完結しません。

そのため、

- インターネットにつながっていない
- API側が一時的に止まっている
- URLが変わった
- パラメータを間違えた
- 利用制限に引っかかった

などで失敗することがあります。

> **「ネットの向こう側まで自分の思い通りに動くと思うな！」**

ということです。

---

## 17-15. 例外処理を入れる

実際には、次のようにしておくと安全です。

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.68,
    "longitude": 139.76,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Tokyo"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    print("現在の気温:", current["temperature_2m"], "℃")
    print("現在の湿度:", current["relative_humidity_2m"], "%")

except requests.RequestException as error:
    print("APIの取得に失敗しました:", error)
```

今回のサンプルファイルも、この形にしています。

---

## 17-16. 地点を変えてみる

```python
"latitude": 35.68,
"longitude": 139.76,
```

を別の緯度・経度へ変えれば、別地点のデータを取得できます。

つまり、プログラム本体を大きく書き換えなくても、渡す値を変えるだけで取得対象を変えられます。

---

## 17-17. APIはサービスごとに違う

すべてのAPIが同じ形ではありません。

サービスによって、

- URL
- パラメータ
- 認証方法
- APIキー
- 返ってくるJSON
- 利用回数の制限
- 利用規約

が違います。

そのため、実際にAPIを使うときは **公式ドキュメントを読む** 必要があります。

---

## 17-18. APIキーとは

APIによっては、

> 誰が使っているのか

を区別するためにAPIキーが必要です。

今回使うOpen-Meteoの無料Forecast APIでは、この教材の範囲ではAPIキーを使いません。

ただし、別のAPIでは登録してキーを取得する場合があります。

APIキーはパスワードに近い扱いになることがあるため、公開リポジトリへそのまま書かないようにします。

---

## 17-19. Open-Meteoを使うときの注意

Open-Meteoの無料APIには利用条件があります。

この教材では学習用として少量のアクセスだけを行います。

大量アクセスしたり、商用サービスへそのまま組み込んだりする場合は、必ず最新の利用規約を確認してください。

また、Open-Meteoのデータを利用する場合は出典表記が必要です。

出典:

- [Open-Meteo](https://open-meteo.com/)
- [Open-Meteo Terms](https://open-meteo.com/en/terms)

---

## 17-20. ここまででつながったもの

ここまでの章がかなりつながっています。

```text
辞書
↓
APIへ渡すパラメータ

外部ライブラリ
↓
requests

JSON
↓
APIから返ってくるデータ

例外処理
↓
通信失敗への対応
```

Web APIは突然出てきた新世界ではなく、今まで学んだものを組み合わせたものです。

---

## 17-21. ここまでで覚えること

1. Web APIは別のプログラムが使うための入口
2. PythonからHTTPでデータを取得できる
3. GETは「データをください」と考えればよい
4. リクエストを送り、レスポンスを受け取る
5. APIではJSONがよく使われる
6. `response.json()` でJSONをPythonのデータとして扱える
7. 辞書のキーを使って必要な値を取り出せる
8. 外部APIは通信やサービス側の事情で失敗することがある
9. APIごとに公式ドキュメントと利用規約を確認する
10. APIキーは公開しない

---

## 前後のページ

← [16. CSV・JSON](../16_CSV・JSON/CSV・JSON.md)

[9. 進みたい方を選ぼうへ戻る](../09_進みたい方を選ぼう/進みたい方を選ぼう.md)
