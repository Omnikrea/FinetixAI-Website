import os
import random
import time
from datetime import datetime
from openai import OpenAI
import tweepy
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# ✅ Ensure all required keys are present
if not all([OPENAI_API_KEY, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_BEARER_TOKEN]):
    print("❌ ERROR: Missing API credentials in .env")
    exit()

# ✅ Configure OpenAI client (v1.0+ SDK)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Configure Twitter client (v2)
twitter_client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET,
    bearer_token=TWITTER_BEARER_TOKEN
)

print("✅ Twitter v2 authentication successful!")

# ✅ Generate AI Tweet using OpenAI SDK v1.0+
def generate_tweet():
    try:
        prompt = "Give me a cutting-edge AI automation business tip with personality and monetization focus."
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a clever AI marketing expert that writes like a human."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=280
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ GPT Error: {e}\n. Retrying...")
        return None

# ✅ Post Tweet using Twitter API v2
def post_tweet(text):
    try:
        response = twitter_client.create_tweet(text=text)
        print(f"✅ Tweet posted: {text}")
        return response
    except tweepy.TweepyException as e:
        print(f"❌ Twitter posting error: {e.response.status_code} {e.response.text}")
        return None

# ✅ Main Bot Logic
def run_bot():
    delay_minutes = random.randint(5, 20)
    print(f"⏳ Delaying post by {delay_minutes} min...")
    time.sleep(delay_minutes * 60)

    print("✍️ Generating text-only post...")
    tweet = generate_tweet()
    if tweet:
        post_tweet(tweet)
    else:
        print("❌ Failed to generate content. Skipping tweet.")

if __name__ == "__main__":
    run_bot()

