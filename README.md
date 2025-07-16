# reddit_user_persona

A Python-based command-line tool that analyzes Reddit user activity to generate a professional, citation-backed **User Persona** report. This project fulfills the criteria outlined in the internship assignment, including data scraping, content analysis, and persona generation with referenced source material.

---

## 📌 Overview

This tool takes a Reddit user’s profile URL, extracts their public posts and comments using the Reddit API (via `PRAW`), and generates a detailed **User Persona** profile. Each persona includes cited insights into the user’s personality traits, tone, interests, and writing style — mimicking the structure of real-world marketing personas.

---

## 🎯 Objectives

This project was developed in response to the following internship task:

- [x] Accept Reddit user profile URL as input.
- [x] Scrape posts and comments made by the user.
- [x] Build a **User Persona** from this activity.
- [x] Output the persona to a `.txt` file.
- [x] For every characteristic, **cite** the Reddit post or comment used.
- [x] Provide a professional and readable `README.md`.

---

## 🧠 What is a User Persona?

A **User Persona** is a detailed, fictional character representing real users, derived from behavioral data. In this case, we generate personas based on Reddit users' language, tone, content, and subreddit interests.

Each generated persona includes:
- Basic info (Reddit username)
- Key personality traits (with cited examples)
- Behavioral habits and subreddit activity
- Communication tone and writing style
- Interests and discussion topics

---

## 🛠️ Built With

- **Python 3.7+**
- [`PRAW`](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- `dotenv` for environment variable handling
- Standard libraries: `re`, `os`, `datetime`, `html`, etc.

---

## 🗂️ Project Structure

reddit_user_persona/
├── main.py # Entry point for execution
├── reddit_loader.py # Reddit API interactions (fetch user data)
├── persona_builder.py # Builds persona from comments/posts
├── utils.py # Helper functions (save to file, clean text)
├── .env.example # Template for API credentials
├── output/ # Stores generated persona .txt and .html files
└── README.md # This documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SumitDendage/reddit_user_persona.git
cd reddit_user_persona
2. Set Up a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Reddit API Access
Go to Reddit Apps.

Create a new app (script type) and obtain:

Client ID

Client Secret

User Agent

Copy .env.example to .env and fill in your credentials:

env
Copy code
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
🚀 Usage
Run the script via:

bash
Copy code
python main.py
When prompted, enter a Reddit profile URL:

ruby
Copy code
Enter Reddit user profile URL: https://www.reddit.com/user/kojied/
After analysis, persona files will be saved to:

bash
Copy code
output/kojied_persona.txt
output/kojied_persona.html
📝 Output Example (Simplified)
less
Copy code
Username: kojied

Top Personality Traits:
- Curious: Frequently participates in r/AskScience and r/TodayILearned
  → Cited Post: "Can someone explain how CRISPR works in layman terms?"
- Supportive: Responds empathetically in mental health communities.
  → Cited Comment: "You're not alone. I've been there and it's tough."

Writing Style:
- Semi-formal, thoughtful, emotionally aware

Frequent Subreddits:
- r/AskScience
- r/relationships
- r/books

Interests:
- Technology, psychology, mental health, fiction writing
📁 Sample Data
The output/ directory includes sample .txt and .html personas generated from public Reddit profiles such as:

kojied

Hungry-Move-6603

Each profile file includes cited comments/posts supporting the personality traits and behavioral insights.

