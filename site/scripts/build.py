#!/usr/bin/env python3
"""Build the online edition of the lecture notes.

Layout of the generated site:

    _site/                 the book: landing page, per-book indexes, search
    _site/app/             JupyterLite, exactly as it generates itself

Keeping JupyterLite entirely inside app/ means the build never edits or
replaces a file JupyterLite owns. An earlier version put the landing page at
the site root, which overwrote the index.html that JupyterLite reads its own
configuration back out of, and every notebook page failed to boot.

Staging mirrors the repository's directory layout inside the JupyterLite
virtual filesystem, so notebook-relative paths like
`../../datasets/deaths-in-gameofthrones/...` resolve unchanged and the source
notebooks are never modified.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pages  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SITE = REPO / "site"
BUILD = SITE / "_build"          # staged contents handed to jupyter lite
OUT = SITE / "_site"             # the published site
APP = OUT / "app"                # JupyterLite lives here, untouched

# Page-weight guard, not a technical limit: Pyodide will happily read a file of
# any size the browser can fetch. This exists so the 2.7GB taxi-trip corpus and
# the 116MB LFS zip never end up in the published site.
MAX_DATASET_BYTES = 25 * 1024 * 1024

DATASET_RE = re.compile(r'["\']([^"\']*datasets/[^"\']+)["\']')
IMAGE_RE = re.compile(r'(!\[[^\]]*\]\()([^)]+)(\))|(<img[^>]+src=["\'])([^"\']+)(["\'])')


def rewrite_image_paths(nb: dict, nb_dir_rel: str, files_base: str) -> int:
    """Point relative image references at JupyterLite's /files/ endpoint.

    JupyterLite does not resolve relative markdown image paths against the
    notebook's own directory. A bare `images/foo.png` resolves against the app
    URL and 404s; a `../files/...` path sends JupyterLab's markdown renderer to
    the contents API, which fails and blanks the src entirely. Only an absolute
    URL is left alone and served.

    Applied to the staged copy only; source notebooks keep the plain relative
    paths that work in local Jupyter.
    """
    changed = 0

    def sub(m):
        nonlocal changed
        prefix, ref, suffix = (m.group(1), m.group(2), m.group(3)) if m.group(1) \
            else (m.group(4), m.group(5), m.group(6))
        if ref.startswith(("http://", "https://", "data:", "/", "attachment:", "#")):
            return m.group(0)
        # One notebook was authored on Windows and carries `images\foo.png`.
        # A backslash is a legal filename character on POSIX, so it survives
        # into the URL as %5C and 404s. Normalise to a path separator.
        ref = ref.replace("\\", "/")
        changed += 1
        return f"{prefix}{files_base}{nb_dir_rel}/{ref}{suffix}"

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
        for m in DATASET_RE.finditer("".join(cell.get("source", []))):
            found.add(m.group(1))
    return found


def stage(config, files_base):
    if BUILD.exists():
        shutil.rmtree(BUILD)
    contents = BUILD / "contents"
    contents.mkdir(parents=True)

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
            image_refs += rewrite_image_paths(nb, str(Path(rel).parent), files_base)
            dst.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")

            staged_dirs.add(src.parent)
            chapters.append((book["id"], rel, src))

    for d in staged_dirs:
        img = d / "images"
        if img.is_dir():
            shutil.copytree(img, contents / img.relative_to(REPO), dirs_exist_ok=True)

    # the postcell shim must be importable from each notebook's own directory
    shim = SITE / "shim" / "postcell.py"
    for d in staged_dirs:
        shutil.copy2(shim, contents / d.relative_to(REPO) / "postcell.py")

    wanted, skipped = set(), set()
    for _, rel, src in chapters:
        for ref in notebook_datasets(src):
            resolved = (src.parent / ref).resolve()
            if not resolved.exists() or not resolved.is_file():
                continue
            (skipped if resolved.stat().st_size > MAX_DATASET_BYTES else wanted).add(resolved)

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


def build_app():
    """Run JupyterLite into _site/app/. Nothing else writes into that tree."""
    cfg = {"LiteBuildConfig": {"contents": [str(BUILD / "contents")],
                               "output_dir": str(APP)}}
    (BUILD / "jupyter_lite_config.json").write_text(json.dumps(cfg, indent=2))
    subprocess.run(["jupyter", "lite", "build"], cwd=BUILD, check=True)


def inject_into_apps(base_url, apply_skin):
    """Add the chapter nav bar (and optionally the reading skin) to app shells.

    This edits JupyterLite's generated HTML in place, which is the one place we
    have to. It only ever appends <link>/<script> tags before </head>.
    """
    for asset in ("book-nav.js", "book-nav.css", "custom-book.css"):
        shutil.copy2(SITE / "assets" / asset, APP / asset)

    tags = (f'  <link rel="stylesheet" href="{base_url}app/book-nav.css">\n'
            f'  <script>window.__BOOK_BASE__="{base_url}";</script>\n'
            f'  <script defer src="{base_url}app/book-nav.js"></script>\n')
    if apply_skin:
        tags = f'  <link rel="stylesheet" href="{base_url}app/custom-book.css">\n' + tags

    patched = []
    for app in ("notebooks", "lab"):
        shell = APP / app / "index.html"
        if not shell.exists() or "book-nav.js" in shell.read_text():
            continue
        shell.write_text(shell.read_text().replace("</head>", tags + "</head>", 1))
        patched.append(app)
    return patched


def write_book_layer(config, base_url):
    """Landing page, per-book indexes, nav lookup and search index."""
    books = pages.collect(config, REPO)

    (OUT / "book-nav.json").write_text(json.dumps(pages.nav_json(books)))
    (OUT / "search.json").write_text(
        json.dumps(pages.search_index(books, REPO), ensure_ascii=False))
    for asset in ("site.css", "search.js"):
        shutil.copy2(SITE / "assets" / asset, OUT / asset)

    (OUT / "index.html").write_text(pages.render_index(config, books, base="./"))
    bookdir = OUT / "books"
    bookdir.mkdir(exist_ok=True)
    for b in books:
        (bookdir / f"{b['id']}.html").write_text(pages.render_book(config, b, base="../"))
    return books


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-app", action="store_true",
                    help="regenerate the book layer only; leave app/ alone")
    args = ap.parse_args()

    config = load_books()
    base_url = config.get("base_url", "/")
    if not base_url.endswith("/"):
        base_url += "/"
    apply_skin = bool(config.get("apply_skin", False))
    files_base = f"{base_url}app/files/"

    if not args.skip_app:
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)
        stats = stage(config, files_base)
        print(f"staged {stats['notebooks']} notebooks across {stats['dirs']} directories")
        print(f"rewrote {stats['image_refs']} relative image references to {files_base}")
        print(f"staged {stats['datasets']} dataset files")
        if stats["datasets_skipped"]:
            print(f"skipped {len(stats['datasets_skipped'])} oversized datasets: "
                  f"{', '.join(stats['datasets_skipped'])}")
        build_app()
        print("patched app shells:", ", ".join(inject_into_apps(base_url, apply_skin)),
              f"(reading skin {'ON' if apply_skin else 'OFF'})")

    books = write_book_layer(config, base_url)
    print(f"generated landing page and {len(books)} book indexes")
    print(f"\nsite built at {OUT}")


if __name__ == "__main__":
    main()
