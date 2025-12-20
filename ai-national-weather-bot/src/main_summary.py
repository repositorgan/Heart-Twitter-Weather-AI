from fetch_nws import get_forecast
from summarize_weather import generate_weather_story
from format_tweet import clean_tweet
from post_to_x import post_tweet
import json

def run():
    with open("config/regions.json") as f:
        regions = json.load(f)

    summaries = []
    for name, coords in regions.items():
        forecast = get_forecast(coords["lat"], coords["lon"])
        summaries.append(f"{name}: {forecast[0]['detailedForecast']}")

    story = generate_weather_story(
        regional_data="\n".join(summaries),
        alerts="See active alerts"
    )

    tweet = clean_tweet(story)
    post_tweet(tweet)

if __name__ == "__main__":
    run()
