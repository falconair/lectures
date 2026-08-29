"""Generate the book layer: landing page, per-book indexes, and nav data.

JupyterLite has no concept of a book — it serves notebooks as isolated URLs.
Everything here exists to wrap those URLs in a reading structure: which books
exist, what order chapters go in, and what comes next.
"""

import html
import json
import re
import urllib.parse
from pathlib import Path

NOTEBOOK_URL = "app/notebooks/index.html?path={path}"


def notebook_url(rel: str) -> str:
    """URL for a chapter. The path must be percent-encoded: six notebooks have
    spaces or parentheses in their filenames, which otherwise produce links the
    browser and JupyterLite's query parser both mishandle."""
    return NOTEBOOK_URL.format(path=urllib.parse.quote(rel, safe="/"))

# Words that carry no signal in a search index for a Python course.
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "to", "of", "in", "is",
    "it", "we", "you", "this", "that", "for", "on", "as", "with", "be", "are",
    "can", "will", "at", "by", "from", "not", "have", "has", "do", "does",
}


def chapter_title(nb_path: Path) -> str:
    """First markdown heading in the notebook, else a title from the filename."""
    try:
        nb = json.loads(nb_path.read_text())
    except Exception:
        return nb_path.stem
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        m = re.search(r"^#{1,3}\s+(.+)$", "".join(cell.get("source", [])), re.M)
        if m:
            # strip inline markdown emphasis/code so titles read cleanly
            t = re.sub(r"[*`_]", "", m.group(1)).strip()
            if t:
                return t
    return re.sub(r"^[\d\-_ ]+", "", nb_path.stem).replace("_", " ").strip() or nb_path.stem


def chapter_text(nb_path: Path, limit: int = 400) -> str:
    """Prose from a notebook, for the search index."""
    try:
        nb = json.loads(nb_path.read_text())
    except Exception:
        return ""
    words = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = re.sub(r"[#*`_>\[\]()!]", " ", "".join(cell.get("source", [])))
        for w in text.split():
            lw = w.lower().strip(".,:;\"'")
            if len(lw) > 2 and lw not in STOPWORDS:
                words.append(lw)
            if len(words) >= limit:
                return " ".join(words)
    return " ".join(words)


def collect(config, repo: Path):
    """Resolve books.yml into books with chapter titles and neighbours."""
    books = []
    for b in config["books"]:
        chapters = []
        for rel in b["chapters"]:
            p = repo / rel
            chapters.append({
                "path": rel,
                "title": chapter_title(p),
                "url": notebook_url(rel),
            })
        books.append({
            "id": b["id"],
            "title": b["title"],
            "blurb": " ".join((b.get("blurb") or "").split()),
            "chapters": chapters,
        })
    return books


def nav_json(books):
    """Lookup used by the in-app nav bar: notebook path -> its place in a book."""
    index = {}
    for b in books:
        for i, ch in enumerate(b["chapters"]):
            index[ch["path"]] = {
                "book": b["title"],
                "bookId": b["id"],
                "n": i + 1,
                "of": len(b["chapters"]),
                "title": ch["title"],
                "prev": b["chapters"][i - 1] if i > 0 else None,
                "next": b["chapters"][i + 1] if i + 1 < len(b["chapters"]) else None,
            }
    return index


def search_index(books, repo: Path):
    return [
        {
            "t": ch["title"],
            "b": b["title"],
            "u": ch["url"],
            "x": chapter_text(repo / ch["path"]),
        }
        for b in books for ch in b["chapters"]
    ]


# --- HTML ------------------------------------------------------------------

def _shell(title, body, base, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{base}site.css">
{extra_head}
</head>
<body>
{body}
</body>
</html>
"""


LIVE_NOTE = """
<aside class="note">
  <strong>These are lecture notes, not a textbook.</strong>
  They were written to be delivered live, with me talking over them. Expect
  terse notes, deliberate gaps, and code that gets explained out loud rather
  than in writing. Reading them cold is not how they were meant to be used.
  <br><br>
  Every code cell runs in your browser — nothing is installed, nothing is sent
  anywhere. Edit them, break them, see what happens.
</aside>
"""


def render_index(config, books, base="./", extra_head=""):
    cards = []
    for b in books:
        cards.append(f"""
    <a class="card" href="{base}books/{b['id']}.html">
      <h2>{html.escape(b['title'])}</h2>
      <p>{html.escape(b['blurb'])}</p>
      <span class="count">{len(b['chapters'])} chapters</span>
    </a>""")
    body = f"""
<header class="site-head">
  <h1>{html.escape(config.get('site_title', 'Lecture notes'))}</h1>
  <p class="byline">{html.escape(config.get('author', ''))}</p>
</header>
<main class="wrap">
{LIVE_NOTE}
  <div class="search">
    <input id="q" type="search" placeholder="Search all chapters…" autocomplete="off">
    <ul id="results"></ul>
  </div>
  <div class="cards">{''.join(cards)}
  </div>
</main>
<script src="{base}search.js"></script>
"""
    return _shell(config.get("site_title", "Lecture notes"), body, base, extra_head)


def render_book(config, book, base="../"):
    items = []
    for i, ch in enumerate(book["chapters"], 1):
        items.append(f"""
      <li>
        <a href="{base}{ch['url']}">
          <span class="num">{i}</span>
          <span class="ch-title">{html.escape(ch['title'])}</span>
        </a>
      </li>""")
    body = f"""
<header class="site-head compact">
  <a class="back" href="{base}index.html">← all books</a>
  <h1>{html.escape(book['title'])}</h1>
  <p class="byline">{html.escape(book['blurb'])}</p>
</header>
<main class="wrap">
{LIVE_NOTE}
  <ol class="toc">{''.join(items)}
  </ol>
</main>
"""
    return _shell(book["title"], body, base)
