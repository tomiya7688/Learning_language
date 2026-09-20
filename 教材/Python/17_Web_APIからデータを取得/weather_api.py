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
