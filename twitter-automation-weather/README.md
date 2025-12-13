# Weather Twitter Bot Setup Guide

This guide will help you set up an automated Twitter bot that posts weather forecasts.

## What You Need Before Starting

1. A Twitter/X account (the one that will post weather)
2. Python installed on your computer
3. A text editor (Notepad works fine)
4. Twitter Developer Account (we'll create this together)

## File List - You Need 6 Files Total

1. `weather_bot.py` - The main bot program
2. `test_weather.py` - Test program to make sure it works
3. `.env` - YOUR secret credentials (you'll create this)
4. `.env.example` - Template showing what to put in .env
5. `requirements.txt` - List of tools Python needs to install
6. `.gitignore` - Protects your secrets from GitHub

## Step-by-Step Setup

### Part 1: Create Your Project Folder

**Option A - Using File Explorer (Easier):**
1. Open File Explorer (the folder icon on your taskbar)
2. Navigate to your Documents folder
3. Right-click in empty space
4. Click "New" → "Folder"
5. Name it: `weather-twitter-bot`
6. Double-click to open this new folder

**Option B - Using Command Prompt:**
1. Press `Windows Key + R`
2. Type: `cmd`
3. Press Enter
4. Type: `cd Documents`
5. Press Enter
6. Type: `mkdir weather-twitter-bot`
7. Press Enter
8. Type: `cd weather-twitter-bot`
9. Press Enter

### Part 2: Create the 6 Files

**You need to create 6 empty text files. Here's how:**

1. Open Notepad (search for "Notepad" in Windows search)
2. For EACH file below, do this:
   - In Notepad, click File → Save As
   - In "Save as type" dropdown, select "All Files (*.*)"
   - Type the exact filename (including the dot at the beginning if it has one)
   - Make sure you're saving in your `weather-twitter-bot` folder
   - Click Save

**Create these 6 files (exact names):**
- `weather_bot.py`
- `test_weather.py`
- `.env`
- `.env.example`
- `requirements.txt`
- `.gitignore`

**IMPORTANT:** The `.env` file starts with a dot. This is correct!

### Part 3: Copy Code Into Files

Now you'll copy the code I provided into each file:

1. Find the file in your folder
2. Right-click it
3. Click "Open with" → "Notepad"
4. Copy the code from my artifacts above
5. Paste into Notepad
6. Press `Ctrl + S` to save
7. Close Notepad

**Do this for all 6 files.**

### Part 4: Get Twitter Developer Access

1. Go to: https://developer.twitter.com
2. Click "Sign in" (top right)
3. Log in with your Twitter account
4. Click "Apply for a developer account"
5. Choose "Hobbyist" → "Making a bot"
6. Fill out the form with your name and country
7. Click through and accept terms

### Part 5: Get Your Twitter API Keys

1. In the Developer Portal, click "+ Create Project"
2. Project name: `weather-bot`
3. Use case: "Making a bot"
4. Description: `Automated weather forecasts`
5. App name: `weather-forecast-bot`

**YOU WILL NOW SEE YOUR KEYS - THIS IS CRITICAL:**

📋 **COPY THESE IMMEDIATELY** (you can't see them again):
- API Key
- API Key Secret  
- Bearer Token

**Save them in a temporary text file on your desktop!**

### Part 6: Set Up Permissions

1. In your app settings, find "User authentication settings"
2. Click "Set up"
3. Turn ON "OAuth 1.0a"
4. App permissions: Select "Read and write"
5. Callback URL: Type `http://localhost:3000`
6. Website: Type `https://twitter.com`
7. Click "Save"

### Part 7: Generate Access Tokens

1. Click the "Keys and tokens" tab
2. Scroll to "Access Token and Secret"
3. Click "Generate"
4. **COPY THESE IMMEDIATELY:**
   - Access Token
   - Access Token Secret

Now you have 4 credentials total.

### Part 8: Fill In Your .env File

1. Open your `.env` file (the one without .example)
2. You should see empty lines or placeholder text
3. Replace with your actual keys:

```
TWITTER_API_KEY=paste_your_api_key_here
TWITTER_API_SECRET=paste_your_api_secret_here
TWITTER_ACCESS_TOKEN=paste_your_access_token_here
TWITTER_ACCESS_SECRET=paste_your_access_secret_here
NWS_LATITUDE=43.0389
NWS_LONGITUDE=-87.9065
```

**NO SPACES around the = sign!**

4. Save the file (Ctrl + S)

### Part 9: Install Python Tools

1. Press `Windows Key + R`
2. Type: `cmd`
3. Press Enter
4. Type: `cd Documents\weather-twitter-bot`
5. Press Enter
6. Type: `pip install -r requirements.txt`
7. Press Enter
8. Wait for it to finish (you'll see text scrolling)

### Part 10: Test Everything

**Still in Command Prompt:**

1. Type: `python test_weather.py`
2. Press Enter
3. Read what it says - it will test each part
4. When it asks if you want to post a test tweet, type `yes`

**If you see ✅ checkmarks, you're good!**

### Part 11: Start the Automated Bot

**In Command Prompt:**

1. Type: `python weather_bot.py`
2. Press Enter

**The bot is now running!** It will:
- Post a weather tweet immediately
- Then post at 7 AM, 12 PM, and 6 PM every day
- Keep running until you close the Command Prompt window

**To stop it:** Press `Ctrl + C` in the Command Prompt window

## Troubleshooting

**"pip is not recognized"**
- Python isn't installed or not in PATH
- Reinstall Python and check "Add Python to PATH"

**"Twitter API error: 403"**
- App permissions need to be "Read and Write"
- Regenerate Access Tokens after changing permissions

**"Could not fetch weather data"**
- Change the latitude/longitude in .env
- NWS only works for USA locations

**"Missing credentials"**
- Check your .env file has all 4 Twitter credentials
- Make sure there are no extra spaces

## What Each File Does

- **weather_bot.py** - The main program that runs 24/7
- **test_weather.py** - Tests everything before you run the bot
- **.env** - Your secret Twitter keys (NEVER share this!)
- **.env.example** - Shows what the .env should look like
- **requirements.txt** - Tells pip what to install
- **.gitignore** - Protects your secrets if you use GitHub

## Questions?

If something doesn't work, check the `weather_bot.log` file that gets created. It shows what the bot is doing.
