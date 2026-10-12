import requests

# データを取得するAPIのURLを url に保存します。
url = "https://api.open-meteo.com/v1/forecast"

# APIへ渡す条件を params にまとめます。
params = {
    "latitude": 35.68,
    "longitude": 139.76,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Tokyo"
}

try:
    # APIから返ってきた応答を response に保存します。
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    # 応答のJSONをPythonで使える形にして data に保存します。
    data = response.json()
    # data の現在値部分を current に保存します。
    current = data["current"]

    print("現在の気温:", current["temperature_2m"], "℃")
    print("現在の湿度:", current["relative_humidity_2m"], "%")

except requests.RequestException as error:
    print("APIの取得に失敗しました:", error)
