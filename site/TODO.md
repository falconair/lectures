# Online edition — outstanding work

Running list for the `online-book` branch. Nothing here blocks the build; it
all runs today via `./site/build.sh` and `python site/serve.py`.

---

## Needs a decision from you

### 1. Correct the book map
`site/books.yml` groups 81 of the 99 notebooks into four books. The grouping was
inferred from directory numbering and notebook titles, **not** from how the
courses were actually taught. Two calls most likely wrong:

- **`025_` was resequenced** into a teaching order (variables → numbers →
  strings → booleans → conditionals → loops → collections → functions →
  classes), ignoring the original `090`–`310` filename numbering. If that
  numbering reflects your delivery order, revert it.
- **`095-all_of_python_faster_basics`** was placed near the end of *Intro to
  Python* as an appendix. It is the "for experienced programmers" speedrun, so
  it may instead be the entry point for one of the courses.

No notebook currently appears in two books. Real courses overlap — duplicate
freely if that is truer.

### 2. Fix a Windows path in one notebook
`lectures/020_intro_to_jupyter/10 - Intro To Jupyter (not technical).ipynb`
references `images\python_repl.png` with a backslash. On macOS and Linux a
backslash is a filename character, not a separator, so **this image is broken
in local Jupyter today**, not only in the site. The build works around it by
normalising separators; the source is still wrong. One-character fix.

### 3. The 18 parked notebooks
Listed with reasons at the bottom of `site/books.yml`: `misc/` scratch files,
the two R notebooks, the untitled bytecode notebook, a TODO-marked one, and the
12-notebook taxi-trips series (needs 2.7GB of data that cannot ship).

---

## Deferred by choice

### 4. The reading skin
`apply_skin: false` in `site/books.yml`. Setting it to `true` hides the Jupyter
menubar, toolbar and cell prompts and re-typesets chapters as a reading column
(`site/assets/custom-book.css`). Parked until the structure settles.

Two things to resolve before turning it on:

- **No Run button.** The skin hides Jupyter's toolbar, so readers would need
  Shift+Enter with nothing telling them so. Needs a per-cell run affordance.
- **Dark mode is half-done.** The landing and book pages have a dark palette;
  the notebook skin does not. Switching between them in dark mode will jar.

### 5. Publish to GitHub Pages
Set `base_url: "/lectures/"` in `site/books.yml`, then a workflow that builds
and deploys `site/_site`. Watch: the 116MB LFS zip and the 2.7GB `datasets/`
tree must stay out (the build already excludes them), and the site is ~130MB.

### 6. Your content pass
Spelling, grammar, and clarity. Two typos already spotted, both of which are
also in filenames, so renaming touches `books.yml` too:

- "Conditonal statement" — `025_all_of_python_basics/220-conditonals_and_None.ipynb`
- "data-represntation" — `190_data_representation_overview/100-data-represntation-overview.ipynb`

---

## Known problems

### 7. Chapters that cannot fully run in the browser
19 of 81 chapters use something Pyodide cannot do. They render fine; the code
just cannot execute. No answer yet for what a reader should see instead — a
note, pre-computed output, or exclusion from the web edition.

| Cause | Chapters | Notes |
|---|---|---|
| Shell escapes `!cmd` | 10 | No subprocess in the browser |
| Ray | 5 | All of `130-distributed_python` |
| Docker | 2 | |
| MLflow server | 2 | |
| FastAPI / Flask | 2 | Cannot bind a port |
| PySpark | 1 | Needs a JVM |

Worst affected is **Machine Learning Engineering**: 17 of its 27 chapters.
That book may need a different treatment from the other three.

`%%writefile` (7 chapters) is fine — it writes to Pyodide's virtual
filesystem. It only breaks where a shell escape then runs the file.

### 8. Verify async and matplotlib chapters
- `025_all_of_python_basics/310-async.ipynb` — Pyodide already runs inside an
  event loop, so `asyncio.run()` typically raises. Untested.
- `025_all_of_python_basics/150-basic_plotting.ipynb` — matplotlib works in
  Pyodide but needs checking in this setup.

### 9. Run All halts on the first exception
Several notebooks deliberately raise exceptions to teach (`"Homer is " + 36`).
Jupyter's Run All stops there. Fine for readers going cell by cell; it rules
out ever pre-computing a whole notebook.

### 10. Page weight
The site is ~130MB. Heaviest assets:

- `045_intro_to_numpy/images/chicago.jpeg` — 7MB (plus 3MB and 1.9MB variants)
- `040_basic_computer_architecture/images/EBMotherboard.jpg` — 3.7MB
- `datasets/market_data/trades_...csv.gz` — 11MB, used by 4 chapters

Resizing the images is the easy win. `MAX_DATASET_BYTES` in
`site/scripts/build.py` caps dataset staging at 25MB.

---

## Smaller items

- **Search is substring-only** over titles and the first 400 words of prose
  (`site/scripts/pages.py`). No stemming, no ranking beyond title-before-body.
- **Chapter titles come from the first markdown heading.** Two notebooks have
  no heading and would fall back to a filename-derived title if ever added to
  a book.
- **`postcell.conf.bak`** is tracked and public. It is a template with a real
  `instructor_id` — deliberate, since students need it, but worth a conscious
  confirmation.
- **`datasets/market_data/.gitattributes`** contains a `../` LFS rule that
  matches nothing. Dead file, safe to delete.
- **Stale service workers.** Anyone who loaded a pre-`app/` build has a worker
  registered at the site root serving cached pages. Clear with the snippet in
  the commit log, or DevTools → Application → Service Workers → Unregister.
