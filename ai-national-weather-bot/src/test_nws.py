from fetch_nws import get_forecast

forecast = get_forecast(40.7, -74.0)  # NYC
print(forecast[0]["name"])
print(forecast[0]["detailedForecast"])
