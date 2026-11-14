# Reddit User Persona Generator

A command-line tool that reads a Reddit user's public posts and comments and turns them into an evidence-based **user persona** — interests, personality, writing style, communities and motivations — where **every claim cites the post or comment it came from**.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![PRAW](https://img.shields.io/badge/Reddit%20API-PRAW-FF4500?logo=reddit&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-OpenAI--compatible-412991?logo=openai&logoColor=white)

## How it works

```text
profile URL ─> PRAW (read-only) ─> recent posts [P1..] + comments [C1..] ─> LLM prompt ─> persona.md / .txt / .html
```

1. **Collect** – the user's latest posts and comments are fetched with the official Reddit API through [PRAW](https://praw.readthedocs.io/), in read-only mode.
2. **Label** – every item gets an ID (`P1`, `C7`, …) with its subreddit, so the model can cite it.
3. **Analyse** – an OpenAI-compatible chat model writes the persona under strict rules: use only the supplied activity, cite an ID and a short quote for each trait, and say "Not evident" rather than guess demographics.
4. **Export** – the persona is saved as Markdown, plain text and a styled HTML page, followed by a **Sources** list linking every cited item back to Reddit.

## Getting started

```bash
git clone https://github.com/SumitDendage/reddit_user_persona.git
cd reddit_user_persona
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env`:

| Variable | Where to get it |
|---|---|
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | Create a **script** app at <https://www.reddit.com/prefs/apps> |
| `REDDIT_USER_AGENT` | Any descriptive string, e.g. `reddit-user-persona/1.0 (by u/you)` |
| `OPENAI_API_KEY` | Your LLM provider's API key |
| `OPENAI_MODEL` | Optional, defaults to `gpt-4o-mini` |
| `OPENAI_BASE_URL` | Optional, to use another OpenAI-compatible provider |

## Usage

```bash
python main.py https://www.reddit.com/user/kojied/
python main.py kojied --posts 30 --comments 80 --output personas
```

Output:

```text
output/kojied_persona.md
output/kojied_persona.txt
output/kojied_persona.html
```

Example of the format (illustrative):

```markdown
## Interests
- **Local LLMs and fine-tuning** — experiments with small open models. [P3] "fine-tuned a 7B model on my own notes"

## Most active communities
- r/LocalLLaMA, r/MachineLearning [P3] [C12]
```

## Project structure

```text
├── main.py             # CLI: parse the profile, run the pipeline, save files
├── reddit_loader.py    # PRAW client, username parsing, post/comment collection
├── persona_builder.py  # prompt construction and LLM call
├── utils.py            # Markdown / text / HTML export with a sources list
├── requirements.txt
└── .env.example
```

## Responsible use

The tool only reads public activity, but a persona is still a profile of a real person. Use it for research or product work on aggregated insights, respect Reddit's API terms, and don't publish personas of private individuals.

## Author

**Sumit Dendage** · [GitHub](https://github.com/SumitDendage) · [LinkedIn](https://www.linkedin.com/in/sumit-dendage-636a50201) · [Medium](https://dendagesumitbalkrishna123.medium.com)
