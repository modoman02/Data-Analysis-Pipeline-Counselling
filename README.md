# Friend Agency Analytics — Starter Repo

This repo is a structured starter to analyze and improve a small marketing/video agency’s pipeline and operations.

## Folder structure
- `data_raw/`    : original exports (never edit)
- `data_clean/`  : cleaned standardized tables (generated)
- `src/`         : pipeline scripts
- `notebooks/`   : exploratory analysis
- `reports/`     : written reports + figures
- `docs/`        : project brief, metric dictionary, notes

## Quickstart
1) Create venv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Put current CSV exports into `data_raw/`.

3) Run the starter pipeline (to be implemented):
```bash
python -m src.load_data
python -m src.clean
python -m src.build_ssot
```

4) Open `notebooks/eda.ipynb` and iterate.

## What we’re optimizing for
- Reliable definitions (metric dictionary)
- Low-friction logging/tracking
- Reproducible data build
- Descriptive insights that translate into business decisions

See `docs/project_brief.md` and `docs/codex_prompt.md`.
