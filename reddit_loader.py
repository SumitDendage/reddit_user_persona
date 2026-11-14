"""Fetch a Reddit user's recent public posts and comments with PRAW."""
import os

import praw
from dotenv import load_dotenv

load_dotenv()


def get_client():
    """Create a read-only Reddit client from environment variables."""
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError("Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in your .env file (see .env.example).")
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=os.getenv("REDDIT_USER_AGENT", "reddit-user-persona/1.0"),
    )
    reddit.read_only = True
    return reddit


def username_from_input(value):
    """Accept 'name', 'u/name' or a profile URL and return the bare username."""
    value = value.strip().rstrip("/")
    if "reddit.com" in value:
        parts = [p for p in value.split("/") if p]
        for marker in ("user", "u"):
            if marker in parts and parts.index(marker) + 1 < len(parts):
                return parts[parts.index(marker) + 1]
        return parts[-1]
    return value.removeprefix("u/").removeprefix("/u/")


def load_reddit_data(username, post_limit=25, comment_limit=50, reddit=None):
    """Return (posts, comments) as lists of dicts with id, subreddit, text and permalink."""
    reddit = reddit or get_client()
    user = reddit.redditor(username)

    posts = []
    for post in user.submissions.new(limit=post_limit):
        text = (post.title + "\n" + (post.selftext or "")).strip()
        posts.append({
            "id": f"P{len(posts) + 1}",
            "subreddit": str(post.subreddit),
            "text": text,
            "url": f"https://www.reddit.com{post.permalink}",
        })

    comments = []
    for comment in user.comments.new(limit=comment_limit):
        comments.append({
            "id": f"C{len(comments) + 1}",
            "subreddit": str(comment.subreddit),
            "text": comment.body.strip(),
            "url": f"https://www.reddit.com{comment.permalink}",
        })

    return posts, comments
