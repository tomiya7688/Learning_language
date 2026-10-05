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
