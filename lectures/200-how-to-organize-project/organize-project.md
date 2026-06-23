# How to organize your project

See https://cookiecutter-data-science.drivendata.org/ for details
Also see Kdro (from Mckinsey): https://kedro.org/blog/customise-a-new-kedro-project-with-tools



Your code must be reproducible. This means that you should be able to re-run your code and get the same results. To do this, you should use a version control system (like git) and a package manager (like pip or conda) to manage your dependencies.

### You should use a standard directory structure

(from https://cookiecutter-data-science.drivendata.org/)
```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.                              <<===== IMPORTANT
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details                  <<===== IMPORTANT
|
├── presentations      <- Slide decks and presentations related to the project                      <<===== IMPORTANT
│
├── models             <- Trained and serialized models, model predictions, or model summaries      <<===== IMPORTANT
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),          <<===== IMPORTANT
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.          <<===== IMPORTANT
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.     <<===== IMPORTANT
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations   
```

### You should use standardize file name

Current CCDD suggestions `0.01-pjb-data-source-1.ipynb`, but my suggestion: 
- `100-sac-aggregates-data.ipynb`
- `110-sac-removes-outliers.ipynb`
- `120-sac-exploration-do-basic-counts.ipynb`
- `130-sac-exploration-do-visualizations.ipynb`
- `140-sac-exploration-do-something-else.ipynb`
- `150-sac-build-model.ipynb`
- `160-sac-evaluate-model.ipynb`

(Lecturer note: see private repo example from ML Engineering course)

Note that my file names are verbs. If you don't need a file anymore, don't delete it: `XXX-100-sac-aggregates-data.ipynb`

### You should provide a README.md file

We are all trained to look for a "README" file which describes the project. This file should contain enough information to get new users acclimated to your project.

Examples:
- https://github.com/sidneycadot/oeis#readme
- https://github.com/falconair/fix.js
- https://github.com/falconair/sklearn-embeddings

