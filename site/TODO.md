# Online edition — outstanding work

Running list for the online edition. Nothing here blocks the build; it all runs
today via `./site/build.sh` and `python site/serve.py`.

---

## Start here

Sequenced. Everything below this section is detail for these.

1. **Switch Pages on and publish.** Settings → Pages → Source = GitHub Actions,
   then push to `main` or dispatch the workflow by hand. Until Pages is
   switched on the deploy job fails while the build job passes. (item 5)
2. **Decide about `postcell.conf.bak`** before anyone is pointed at the site.
   Tracked, public, real `instructor_id`. (Smaller items)
3. **Look at chapters with rich output.** The skin has only been checked on
   four chapters. (item 11)
4. **Correct the book map.** The grouping was inferred, not taken from how you
   taught. Wrong order is the most visible thing a reader meets. (item 1)
5. **Decide what Machine Learning Engineering should be.** 17 of its 27
   chapters cannot execute in the browser. (item 7)
6. **Your content pass** — spelling, grammar, two known typos that are also
   filenames. (item 6)

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

### 2. Broken image references in source notebooks
All of these are broken in local Jupyter too, not only in the site.

**A Windows path.** `lectures/020_intro_to_jupyter/10 - Intro To Jupyter (not
technical).ipynb` references `images\python_repl.png` with a backslash. On
macOS and Linux a backslash is a filename character, not a separator. The build
works around it by normalising separators; the source is still wrong.
One-character fix.

**Five images that do not exist anywhere in the repo**, referenced seven times.
They 404 in the browser and show as broken in Jupyter:

| Missing file | Referenced by |
|---|---|
| `030_intro_to_pandas/images/dataframes.jpg` | `110-…-series`, `120-…-dataframes`, `160-pandas-index` |
| `030_intro_to_pandas/images/series.jpg` | `110-pandas-overview-series` |
| `030_intro_to_pandas/images/splitapplycombine.png` | `150-pandas-groupby` |
| `140-algorithms_datastructs/images/binary_tree.svg` | `100-data_structures` |
| `lectures/sklearn_diff.png` | `Data Science in Python` |

There is no `images/` directory in `030_intro_to_pandas` at all. Either the
files were never committed or they were removed; check your working copies
before recreating them.

To re-check after fixing, the build's staged output can be scanned for
`/app/files/` references whose target is absent.

### 3. The 18 parked notebooks
Listed with reasons at the bottom of `site/books.yml`: `misc/` scratch files,
the two R notebooks, the untitled bytecode notebook, a TODO-marked one, and the
12-notebook taxi-trips series (needs 2.7GB of data that cannot ship).

---

## Deferred by choice

### 4. Cell affordances and shortcut teaching
The reading skin is **on** (`apply_skin: true`). It restyles the Jupyter
menubar and toolbar rather than hiding them, so every affordance — Run, Insert
Cell, Restart, every keyboard shortcut — keeps working. That retires the old
"No Run button" blocker. Dark mode is also settled: `site/assets/tokens.css`
carries a warm paper light and a warm dark, shared by the book pages and the
chapter skin, so the two can no longer drift.

What was deliberately deferred, in rough priority order:

- **A per-cell run control.** The gutter currently shows Jupyter's execution
  count (`[4]`) as margin notation — it marks a cell as executable and records
  what ran, but is not itself a button. Making it hover-to-run needs
  `window.jupyterapp`, which requires `exposeAppInBrowser: true` in the
  JupyterLite page config. That is a documented option in the shipped schema
  (`app/jupyterlite.schema.v0.json`), not a private internal. The command is
  `notebook:run-cell-and-select-next`.
- **An insert-cell affordance.** A hairline with a ⊕ appearing between cells on
  hover, for a student who wants somewhere to experiment without reaching for
  the menu. `notebook:insert-cell-below`. Same prerequisite.
- **Tooltips that teach shortcuts.** Jupyter's own toolbar tooltips read
  "Run this cell and advance" and never name the key. `app.commands.keyBindings`
  holds the real binding for every command, so tooltips can be generated from
  what is actually bound rather than hardcoded — they cannot drift out of date.

Useful fact for all three: `windowingMode` defaults to `contentVisibility` in
this build, not `full`, so cell DOM stays in the document while scrolling.
Per-cell injection does not have to survive node recycling.

### 5. Publish to GitHub Pages
`.github/workflows/pages.yml` is written and committed but has never run. It
builds with `--base-url /lectures/` and deploys `site/_site` to
https://falconair.github.io/lectures/ on any push to `main` touching
`lectures/` or `site/`, and on manual dispatch.

Do NOT set `base_url: "/lectures/"` in `books.yml` as this item used to advise
— that breaks `python site/serve.py`, which needs `/`. The committed value
stays `/` and CI passes the flag.

Two steps remain, both yours:

1. Merge to `main`, then set **Settings → Pages → Source = GitHub Actions**.
   The workflow cannot enable Pages itself; until it is switched on, the deploy
   job fails.
2. Decide about `postcell.conf.bak` first (see Smaller items). It is tracked,
   public, and carries a real `instructor_id`. Publishing exposes nothing the
   public repo does not already, but a browsable site makes it findable.

Verified before committing: a cold build with no doit cache takes 4s and
produces 132MB — inside Pages' 1GB limit, largest single file 11MB against the
100MB per-file cap. LFS is not fetched by the workflow, so the 116MB taxi-trips
zip stays out; only 15MB of small datasets are staged.

Watch after the first deploy: Pages has a soft 100GB/month bandwidth limit and
Pyodide is a heavy first load per reader — including for the 19 chapters in
item 7 that cannot execute anyway.

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

### 11. The skin has only been seen on four chapters
The reading skin was checked against `140-strings`, `130-pandas-dataframes-
operations`, `linear_regression_with_numpy` and the two book pages — in light
and dark, at one window width. That leaves 77 chapters unseen.

The cases most likely to need work, none of them yet looked at:

- **Rendered dataframes.** Pandas emits its own `<table>` styling into the
  output area. Against the paper ground it may fight the typography or carry
  white backgrounds. Roughly half of `030_intro_to_pandas` is dataframe output.
- **Matplotlib figures.** Rendered on a white canvas, which will read as a
  bright rectangle in dark mode. `custom-book.css` sets a white background on
  output images deliberately, so figures stay legible — worth confirming that
  looks intentional rather than broken.
- **Wide images.** Several lectures carry screenshots wider than the 42rem
  code measure; they are capped at `max-width: 100%` but have not been seen.
- **Long error tracebacks.** Chapters that raise on purpose (item 9) put a
  stderr block in the output area with its own colouring.

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

- **The code measure is wider than the prose measure.** Prose sits at 34rem,
  code breaks out to 42rem (`--measure` / `--measure-code` in
  `site/assets/tokens.css`). At 34rem, 12.4% of the code lines in these
  lectures overflow into a horizontal scroll; at 42rem, 6.7%. Set the two
  equal for a single uniform column.
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
- **Three chapters read `postcell.conf`, which is not staged.**
  `245-functions-decorators`, `280-exceptions` and `290-context_managers` use
  `open('../../postcell.conf')` as a file-handling example. The build only
  stages files matched by the `datasets/` regex, so both `postcell.conf` and
  `postcell.conf.bak` 404 in the browser and those cells raise
  `FileNotFoundError`. Deliberate in `280-exceptions`, which is teaching
  exceptions; broken in the other two. Either stage the two files or point the
  examples at something that ships. Belongs with item 7.
- **Markdown cells show light-mode syntax colours while being edited, in dark
  mode.** Python code is themed correctly through `--jp-mirror-editor-*`, but
  CodeMirror themes markdown source separately and those variables do not reach
  it, so double-clicking a markdown cell in dark mode shows dark blue on near
  black. Only affects editing prose, not reading.
- **The postcell shim is now unused by the published site.**
  `site/scripts/build.py` strips every `%%postcell` magic and setup cell from
  the staged copies, so `site/shim/postcell.py` is still copied into 28
  directories but nothing imports it. Safe to stop copying; left in place as a
  net for any form the matcher misses.
- **Stale service workers.** Anyone who loaded a pre-`app/` build has a worker
  registered at the site root serving cached pages. Clear with the snippet in
  the commit log, or DevTools → Application → Service Workers → Unregister.
