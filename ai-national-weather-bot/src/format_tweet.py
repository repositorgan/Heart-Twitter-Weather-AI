def clean_tweet(text):
    text = text.replace("\n", " ").strip()
    if len(text) > 280:
        text = text[:277] + "..."
    return text
