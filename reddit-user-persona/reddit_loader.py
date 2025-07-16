# reddit_loader.py
import praw
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get credentials from .env
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")
user_agent = "script:Appsscrap:v1.0 (by u/Commando_sf)"

def load_reddit_data(target_username):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=user_agent
    )

    user = reddit.redditor(target_username)

    comments = [comment.body for comment in user.comments.new(limit=20)]
    posts = [post.title + "\n" + post.selftext for post in user.submissions.new(limit=10)]

    return posts, comments
