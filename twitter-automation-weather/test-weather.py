"""
Test script to verify weather fetching and Twitter posting
Run this BEFORE starting the automated bot to ensure everything works
"""

import tweepy
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
NWS_LATITUDE = os.getenv('NWS_LATITUDE', '37.774929')
NWS_LONGITUDE = os.getenv('NWS_LONGITUDE', '-122.419418')

def test_credentials():
    """Test if credentials are loaded"""
    print("=" * 50)
    print("STEP 1: Checking credentials...")
    print("=" * 50)
    
    if not all([TWITTER_API_KEY, TWITTER_API_SECRET, 
                TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]):
        print("❌ FAILED: Missing credentials in .env file!")
        print("   Please ensure all Twitter credentials are set.")
        return False
    
    print("✅ All credentials found in .env file")
    print(f"   API Key: {TWITTER_API_KEY[:10]}...")
    print(f"   Location: {NWS_LATITUDE}, {NWS_LONGITUDE}")
    return True

def test_twitter_connection():
    """Test Twitter API connection"""
    print("\n" + "=" * 50)
    print("STEP 2: Testing Twitter API connection...")
    print("=" * 50)
    
    try:
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_SECRET
        )
        
        # Try to get authenticated user
        me = client.get_me()
        print(f"✅ Connected to Twitter successfully!")
        print(f"   Account: @{me.data.username}")
        print(f"   Name: {me.data.name}")
        return client
        
    except tweepy.TweepyException as e:
        print(f"❌ FAILED: Twitter API error: {e}")
        print("\n   Common fixes:")
        print("   - Ensure app has 'Read and Write' permissions")
        print("   - Regenerate Access Tokens after changing permissions")
        print("   - Check that all 4 credentials are correct")
        return None
    except Exception as e:
        print(f"❌ FAILED: {e}")
        return None

def test_weather_api():
    """Test National Weather Service API"""
    print("\n" + "=" * 50)
    print("STEP 3: Testing NWS weather API...")
    print("=" * 50)
    
    try:
        # Get grid endpoint
        points_url = f"https://api.weather.gov/points/{NWS_LATITUDE},{NWS_LONGITUDE}"
        headers = {'User-Agent': 'WeatherBot/1.0 (test)'}
        
        points_response = requests.get(points_url, headers=headers, timeout=10)
        points_response.raise_for_status()
        points_data = points_response.json()
        
        city = points_data['properties']['relativeLocation']['properties']['city']
        state = points_data['properties']['relativeLocation']['properties']['state']
        
        print(f"✅ Location identified: {city}, {state}")
        
        # Get forecast
        forecast_url = points_data['properties']['forecast']
        forecast_response = requests.get(forecast_url, headers=headers, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()
        
        periods = forecast_data['properties']['periods']
        current = periods[0]
        
        print(f"✅ Weather data retrieved successfully!")
        print(f"\n   Current forecast:")
        print(f"   {current['name']}: {current['shortForecast']}")
        print(f"   Temperature: {current['temperature']}°{current['temperatureUnit']}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED: Could not fetch weather data: {e}")
        print("\n   Common fixes:")
        print("   - Ensure coordinates are valid US locations")
        print("   - Check internet connection")
        print("   - NWS API only works for US territories")
        return False
    except Exception as e:
        print(f"❌ FAILED: {e}")
        return False

def test_post_tweet(client):
    """Test posting a tweet"""
    print("\n" + "=" * 50)
    print("STEP 4: Testing tweet posting...")
    print("=" * 50)
    
    response = input("\nDo you want to post a TEST TWEET now? (yes/no): ")
    
    if response.lower() != 'yes':
        print("⏭️  Skipping test tweet")
        return True
    
    try:
        test_message = "🤖 Weather bot test tweet - If you see this, the bot is working! This is a test."
        tweet_response = client.create_tweet(text=test_message)
        
        print(f"✅ Test tweet posted successfully!")
        print(f"   Tweet ID: {tweet_response.data['id']}")
        print(f"   Message: {test_message}")
        return True
        
    except tweepy.TweepyException as e:
        print(f"❌ FAILED: Could not post tweet: {e}")
        return False
    except Exception as e:
        print(f"❌ FAILED: {e}")
        return False

def main():
    """Run all tests"""
    print("\n" + "🌤️ " * 15)
    print("   WEATHER TWITTER BOT - SETUP TEST")
    print("🌤️ " * 15 + "\n")
    
    # Test 1: Credentials
    if not test_credentials():
        print("\n❌ Setup incomplete. Please fix credentials and try again.")
        return
    
    # Test 2: Twitter connection
    client = test_twitter_connection()
    if not client:
        print("\n❌ Setup incomplete. Please fix Twitter API setup and try again.")
        return
    
    # Test 3: Weather API
    if not test_weather_api():
        print("\n❌ Setup incomplete. Please fix location coordinates and try again.")
        return
    
    # Test 4: Post tweet
    test_post_tweet(client)
    
    # Final summary
    print("\n" + "=" * 50)
    print("✅ ALL TESTS PASSED!")
    print("=" * 50)
    print("\nYour bot is ready to run automatically!")
    print("\nNext steps:")
    print("1. Run: python weather_bot.py")
    print("2. The bot will post immediately and then at scheduled times")
    print("3. Check weather_bot.log for activity logs")
    print("\nPress Ctrl+C to stop the bot at any time.")

if __name__ == "__main__":
    main()
