# main.py
from reddit_loader import load_reddit_data
from persona_builder import build_persona
from utils import save_to_file
from utils import save_to_file, save_persona_as_html

def print_banner():
    print("=" * 60)
    print("REDDIT USER PERSONA GENERATOR")
    print("=" * 60)

def choose_user():
    print("\nSelect a Reddit user profile to analyze:")
    print("1. kojied")
    print("2. Hungry-Move-6603")
    print("3. Enter custom Reddit username")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        return "kojied"
    elif choice == "2":
        return "Hungry-Move-6603"
    elif choice == "3":
        url = input("Enter the Reddit user profile URL (e.g. https://www.reddit.com/user/example_user/): ").strip()
        return url.strip("/").split("/")[-1]  # Extract username from URL
    else:
        print(" Invalid choice. Please try again.")
        return choose_user()

if __name__ == "__main__":
    print_banner()
    username = choose_user()

    print(f"\n🔍 Scraping Reddit data for user: {username} ...")
    posts, comments = load_reddit_data(username)

    print(" Generating user persona...")
    persona = build_persona(posts, comments)

    save_to_file(username, persona)
    save_persona_as_html(username, persona)
    print(f"\n✅ User persona saved to: output/{username}_persona.txt\n")
