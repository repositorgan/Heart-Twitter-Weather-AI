def get_active_alerts():
    url = "https://api.weather.gov/alerts/active"
    data = requests.get(url, headers=HEADERS).json()
    return data["features"]
