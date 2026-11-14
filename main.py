"""Generate a cited user persona from a Reddit profile.

Examples:
    python main.py https://www.reddit.com/user/kojied/
    python main.py kojied --posts 30 --comments 80
"""
import argparse

from persona_builder import build_persona
from reddit_loader import load_reddit_data, username_from_input
from utils import save_persona


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("profile", nargs="?", help="Reddit username or profile URL")
    parser.add_argument("--posts", type=int, default=25, help="How many recent posts to read (default 25)")
    parser.add_argument("--comments", type=int, default=50, help="How many recent comments to read (default 50)")
    parser.add_argument("--output", default="output", help="Output folder (default: output)")
    args = parser.parse_args()

    profile = args.profile or input("Reddit username or profile URL: ")
    username = username_from_input(profile)

    print(f"Fetching activity for u/{username} ...")
    posts, comments = load_reddit_data(username, args.posts, args.comments)
    print(f"  {len(posts)} posts, {len(comments)} comments")

    print("Building persona ...")
    persona = build_persona(username, posts, comments)

    for path in save_persona(username, persona, posts, comments, args.output):
        print(f"  saved {path}")


if __name__ == "__main__":
    main()
