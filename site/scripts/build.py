#!/usr/bin/env python3
"""Build the JupyterLite site for the online edition of the lecture notes.

Staging mirrors the repository's directory layout inside the JupyterLite
virtual filesystem, so notebook-relative paths like
`../../datasets/deaths-in-gameofthrones/...` resolve unchanged and the source
notebooks never have to be rewritten.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SITE = REPO / "site"
BUILD = SITE / "_build"          # staged contents handed to jupyter lite
OUT = SITE / "_site"             # rendered site

# Page-weight guard, not a technical limit: Pyodide will happily read a file of
# any size the browser can fetch. This exists so the 2.7GB taxi-trip corpus and
# the 116MB LFS zip never end up in the published site. Raise it freely if a
# chapter needs a bigger file — 25MB comfortably covers every dataset the books
# currently reference.
MAX_DATASET_BYTES = 25 * 1024 * 1024

DATASET_RE = re.compile(r'["\']([^"\']*datasets/[^"\']+)["\']')

# Markdown/HTML image references: ![alt](path) and <img src="path">
IMAGE_RE = re.compile(r'(!\[[^\]]*\]\()([^)]+)(\))|(<img[^>]+src=["\'])([^"\']+)(["\'])')


def rewrite_image_paths(nb: dict, nb_dir_rel: str, base_url: str = "/") -> int:
    """Point relative image references at JupyterLite's /files/ endpoint.

    JupyterLite does not resolve relative markdown image paths against the
    notebook's own directory. A bare `images/foo.png` is resolved against the
    app URL (/notebooks/) and 404s; a `../files/...` path sends JupyterLab's
    markdown renderer to the contents API, which fails and blanks the src.
    An absolute URL is left alone and served directly.

    base_url makes the site relocatable: "/" locally, "/lectures/" when
    published to GitHub Pages under a repository path.

    Applied to the staged copy only; source notebooks are never modified.
    """
    changed = 0

    def sub(m):
        nonlocal changed
        prefix, ref, suffix = (m.group(1), m.group(2), m.group(3)) if m.group(1) \
            else (m.group(4), m.group(5), m.group(6))
        if ref.startswith(("http://", "https://", "data:", "/", "attachment:", "#")):
            return m.group(0)
        changed += 1
        return f"{prefix}{base_url}files/{nb_dir_rel}/{ref}{suffix}"

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = "".join(cell.get("source", []))
        new = IMAGE_RE.sub(sub, src)
        if new != src:
            cell["source"] = new.splitlines(keepends=True)
    return changed


def load_books():
    with open(SITE / "books.yml") as fh:
        return yaml.safe_load(fh)


def notebook_datasets(nb_path: Path):
    """Dataset paths referenced from a notebook's code cells."""
    try:
        nb = json.loads(nb_path.read_text())
    except Exception:
        return set()
    found = set()
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        for m in DATASET_RE.finditer(src):
            found.add(m.group(1))
    return found


def stage(config):
    if BUILD.exists():
        shutil.rmtree(BUILD)
    contents = BUILD / "contents"
    contents.mkdir(parents=True)

    base_url = config.get("base_url", "/")
    if not base_url.endswith("/"):
        base_url += "/"

    staged_dirs = set()
    chapters = []
    image_refs = 0
    for book in config["books"]:
        for rel in book["chapters"]:
            src = REPO / rel
            if not src.exists():
                sys.exit(f"ERROR: {book['id']} lists a missing notebook: {rel}")
            dst = contents / rel
            dst.parent.mkdir(parents=True, exist_ok=True)

            nb = json.loads(src.read_text())
            image_refs += rewrite_image_paths(nb, str(Path(rel).parent), base_url)
            dst.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")

            staged_dirs.add(src.parent)
            chapters.append((book["id"], rel, src))

    # images/ directories that sit alongside the staged notebooks
    for d in staged_dirs:
        img = d / "images"
        if img.is_dir():
            shutil.copytree(img, contents / img.relative_to(REPO), dirs_exist_ok=True)

    # the postcell shim must be importable from each notebook's own directory
    shim = SITE / "shim" / "postcell.py"
    for d in staged_dirs:
        shutil.copy2(shim, contents / d.relative_to(REPO) / "postcell.py")

    # only the datasets the staged notebooks actually reference, and only small ones
    wanted, skipped = set(), set()
    for _, rel, src in chapters:
        for ref in notebook_datasets(src):
            resolved = (src.parent / ref).resolve()
            if not resolved.exists() or not resolved.is_file():
                continue
            if resolved.stat().st_size > MAX_DATASET_BYTES:
                skipped.add(resolved)
                continue
            wanted.add(resolved)

    for f in wanted:
        try:
            rel = f.relative_to(REPO)
        except ValueError:
            continue
        dst = contents / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst)

    return {
        "notebooks": len(chapters),
        "image_refs": image_refs,
        "dirs": len(staged_dirs),
        "datasets": len(wanted),
        "datasets_skipped": sorted(p.name for p in skipped),
    }


def build_site():
    cfg = {"LiteBuildConfig": {"contents": [str(BUILD / "contents")],
                               "output_dir": str(OUT)}}
    (BUILD / "jupyter_lite_config.json").write_text(json.dumps(cfg, indent=2))
    subprocess.run(["jupyter", "lite", "build"], cwd=BUILD, check=True)


def inject_css():
    """Link the book skin into each JupyterLite app shell."""
    css_src = SITE / "assets" / "custom-book.css"
    shutil.copy2(css_src, OUT / "custom-book.css")
    patched = []
    for app in ("notebooks", "lab", "tree", "edit", "consoles", "repl"):
        shell = OUT / app / "index.html"
        if not shell.exists():
            continue
        html = shell.read_text()
        if "custom-book.css" in html:
            continue
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="../custom-book.css">\n</head>', 1)
        shell.write_text(html)
        patched.append(app)
    return patched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-build", action="store_true",
                    help="stage contents only; do not run jupyter lite")
    args = ap.parse_args()

    config = load_books()
    stats = stage(config)
    print(f"staged {stats['notebooks']} notebooks across {stats['dirs']} directories")
    print(f"rewrote {stats['image_refs']} relative image references to /files/")
    print(f"staged {stats['datasets']} dataset files")
    if stats["datasets_skipped"]:
        print(f"skipped {len(stats['datasets_skipped'])} oversized datasets: "
              f"{', '.join(stats['datasets_skipped'])}")

    if args.skip_build:
        return
    build_site()
    print("patched app shells with book skin:", ", ".join(inject_css()))
    print(f"\nsite built at {OUT}")


if __name__ == "__main__":
    main()
