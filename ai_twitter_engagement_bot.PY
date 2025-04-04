import os
import random
import time
import tweepy
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# ✅ Ensure all API keys are loaded
if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_BEARER_TOKEN]):
    print("❌ ERROR: Missing Twitter API credentials! Check .env file.")
    exit()

print("✅ API keys loaded successfully!")

# ✅ Authenticate using OAuth 1.0a (needed for posting replies)
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
api = tweepy.API(auth, wait_on_rate_limit=True)

# ✅ Authenticate using API v2 client (needed for reading/searching tweets)
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

print("✅ Twitter authentication successful!")

# ✅ Define keywords and hashtags for engagement
KEYWORDS = ["AI automation", "AI investing", "passive income", "crypto", "fintech", "machine learning"]

# ✅ Function to find tweets to engage with using v2 endpoint
def find_tweets():
    try:
        query = " OR ".join(KEYWORDS) + " -is:retweet lang:en"
        response = client.search_recent_tweets(
            query=query,
            max_results=10,
            tweet_fields=["author_id", "created_at", "text"]
        )
        return response.data if response.data else []
    except tweepy.TweepyException as e:
        print(f"❌ Error fetching tweets: {e}")
        return []

# ✅ Function to reply to tweets

def post_reply(tweet):
    try:
        reply_texts = [
            "Great insights! AI is truly revolutionizing the industry. #AI #Automation",
            "Couldn't agree more! The future of fintech is AI-driven. #Fintech #AI",
            "This is why AI is changing everything. Thoughts? #ML #AIInvesting",
            "Well said! AI is transforming business automation at an insane speed. #AI #Startup",
            "This aligns perfectly with AI-driven passive income strategies. #Automation #Finance"
        ]
        response = random.choice(reply_texts)
        api.update_status(status=response, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        print(f"✅ Replied to tweet: {tweet.text}")
        time.sleep(random.randint(20, 90))
    except tweepy.TweepyException as e:
        print(f"❌ Error replying: {e}")
        if "403" in str(e):
            print("🚨 Forbidden error detected! Sleeping for 15 minutes...")
            time.sleep(900)

# ✅ Main engagement loop
def run_engagement_bot():
    while True:
        print("🔄 Fetching tweets for engagement...")
        tweets = find_tweets()
        if tweets:
            for tweet in tweets:
                post_reply(tweet)
        else:
            print("⚠️ No relevant tweets found. Sleeping for 10 minutes.")
        time.sleep(600)

if __name__ == "__main__":
    run_engagement_bot()

