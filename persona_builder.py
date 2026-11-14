"""Turn a user's Reddit activity into a cited persona with an LLM."""
import os

from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a user-research analyst. You write evidence-based user personas from a person's public Reddit activity.
Rules:
- Use only the activity provided. Do not invent facts, quotes or demographics.
- Every characteristic must cite at least one item by its ID, e.g. [P2] or [C14], and quote a short supporting phrase.
- If something (age, job, location, ...) is not evident, write "Not evident from activity"."""

PERSONA_TEMPLATE = """Build a user persona for Reddit user u/{username}.

Return Markdown with these sections:
## Summary
## Interests
## Personality traits
## Writing style and tone
## Most active communities
## Motivations and frustrations
## Demographics (only if evident)

Activity (most recent first):

### Posts
{posts}

### Comments
{comments}
"""

MAX_ITEM_CHARS = 600


def _format_items(items):
    if not items:
        return "(none)"
    lines = []
    for item in items:
        text = " ".join(item["text"].split())[:MAX_ITEM_CHARS]
        lines.append(f"[{item['id']}] r/{item['subreddit']}: {text}")
    return "\n".join(lines)


def build_prompt(username, posts, comments):
    return PERSONA_TEMPLATE.format(
        username=username,
        posts=_format_items(posts),
        comments=_format_items(comments),
    )


def build_persona(username, posts, comments, client=None, model=None):
    """Ask an OpenAI-compatible chat model for the persona and return Markdown."""
    if not posts and not comments:
        return f"# u/{username}\n\nNo public posts or comments were found for this user."

    if client is None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("Set OPENAI_API_KEY in your .env file (see .env.example).")
        from openai import OpenAI
        client = OpenAI()  # also honours OPENAI_BASE_URL for compatible providers

    response = client.chat.completions.create(
        model=model or os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(username, posts, comments)},
        ],
    )
    return response.choices[0].message.content.strip()
