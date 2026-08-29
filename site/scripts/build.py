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

# Datasets above this size are assumed to be class-time downloads, not things
# a reader should pull over the wire. The taxi-trip corpus (2.7GB) is the
# reason this limit exists.
MAX_DATASET_BYTES = 5 * 1024 * 1024

DATASET_RE = re.compile(r'["\']([^"\']*datasets/[^"\']+)["\']')


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

    staged_dirs = set()
    chapters = []
    for book in config["books"]:
        for rel in book["chapters"]:
            src = REPO / rel
            if not src.exists():
                sys.exit(f"ERROR: {book['id']} lists a missing notebook: {rel}")
            dst = contents / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
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
