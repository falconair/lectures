#!/usr/bin/env bash
# Build the online edition. Requires the `jlite` conda environment:
#   conda create -n jlite -c conda-forge python=3.12 \
#       jupyterlite-core jupyterlite-pyodide-kernel jupyter_server pyyaml
set -euo pipefail
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate jlite
exec python "$(dirname "$0")/scripts/build.py" "$@"
