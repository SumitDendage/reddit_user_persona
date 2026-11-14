"""Save personas as Markdown, plain text and a standalone HTML page."""
import html
import os
import re

OUTPUT_DIR = "output"


def _sources_section(posts, comments):
    lines = ["", "---", "", "## Sources", ""]
    for item in posts + comments:
        lines.append(f"- [{item['id']}] r/{item['subreddit']}: {item['url']}")
    return "\n".join(lines)


def save_persona(username, persona_md, posts, comments, output_dir=OUTPUT_DIR):
    """Write <username>_persona.md, .txt and .html; return the paths."""
    os.makedirs(output_dir, exist_ok=True)
    full = persona_md.rstrip() + "\n" + _sources_section(posts, comments) + "\n"

    base = os.path.join(output_dir, f"{username}_persona")
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(full)
    with open(base + ".txt", "w", encoding="utf-8") as f:
        f.write(full)
    with open(base + ".html", "w", encoding="utf-8") as f:
        f.write(to_html(username, full))
    return [base + ".md", base + ".txt", base + ".html"]


def to_html(username, markdown_text):
    """Very small Markdown-to-HTML conversion (headings, bullets, bold, links)."""
    body = []
    in_list = False
    for raw in markdown_text.splitlines():
        line = html.escape(raw)
        line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
        line = re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', line)
        if line.startswith(("- ", "* ")):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{line[2:]}</li>")
            continue
        if in_list:
            body.append("</ul>")
            in_list = False
        if line.startswith("### "):
            body.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            body.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            body.append(f"<h1>{line[2:]}</h1>")
        elif line.strip() == "---":
            body.append("<hr>")
        elif line.strip():
            body.append(f"<p>{line}</p>")
    if in_list:
        body.append("</ul>")

    name = html.escape(username)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>User persona: u/{name}</title>
<style>
  body {{ font-family: system-ui, -apple-system, "Segoe UI", sans-serif; background: #f4f5f7; color: #222; margin: 0; padding: 40px 16px; }}
  main {{ max-width: 860px; margin: auto; background: #fff; padding: 32px 40px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,.08); }}
  h1 {{ margin-top: 0; }} h2 {{ border-bottom: 1px solid #eee; padding-bottom: 6px; margin-top: 28px; }}
  li, p {{ line-height: 1.6; }} a {{ color: #0b63ce; word-break: break-all; }}
</style>
</head>
<body>
<main>
<h1>User persona: u/{name}</h1>
{chr(10).join(body)}
</main>
</body>
</html>
"""
