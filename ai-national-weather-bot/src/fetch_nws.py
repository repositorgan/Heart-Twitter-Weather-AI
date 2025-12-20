import requests

HEADERS = {
    "User-Agent": "AIWeatherBot (contact: your@email.com)"
}

def get_forecast(lat, lon):
    point_url = f"https://api.weather.gov/points/{lat},{lon}"
    point_data = requests.get(point_url, headers=HEADERS).json()

    forecast_url = point_data["properties"]["forecast"]
    forecast = requests.get(forecast_url, headers=HEADERS).json()

    return forecast["properties"]["periods"]

