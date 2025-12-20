from openai import OpenAI

client = OpenAI()

def generate_weather_story(regional_data, alerts):
    prompt = f"""
You are a trending professional meteorologist.

Using the following regional forecasts and alerts,
write a concise national weather update suitable for Twitter.
Make it fun and trending.

Rules:
- 1–2 sentences max
- No emojis
- Neutral, factual tone
- Highlight significant or impactful weather
- Do not exceed 240 characters

Regional Forecasts:
{regional_data}

Active Alerts:
{alerts}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()
