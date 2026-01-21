# Next Steps and Deliverables (Agency Analytics Project)

## Purpose
Define the actual product to build and the concrete development steps to get there.
This is not just a report. The product should run the analysis automatically.

## The product (what we build)
A small analytics system that turns raw exports into a weekly decision report with one command
or an automated schedule.

Core product behavior:
- Ingest raw inputs (CSV/Sheets/CRM exports).
- Validate and clean them.
- Build a single source of truth dataset.
- Generate a weekly summary report and charts.
- Surface issues (missing fields, duplicates, broken dates) automatically.

This can exist in two forms:
- Product v1 (CLI): a script-driven pipeline that produces clean data and a report when run.
- Product v2 (Automation): a scheduled job or a small web app that runs the pipeline and posts the report.

## What is actually delivered to him
You hand him a working system, not a slide deck:
- A repo with runnable scripts and templates.
- A documented workflow ("put exports here and run this").
- A repeatable weekly report output in `reports/`.
- A data model and definitions that remove ambiguity.
- Optional: a hosted or scheduled version so he does nothing except export.

## How it runs (who does what)
Product v1 (CLI):
- He (or you) drops exports into `data_raw/`.
- Run one command: `python -m src.run_pipeline`.
- Output appears in `data_clean/` and `reports/`.

Product v2 (Automated):
- Exports are pulled from a source (Sheets or CRM) on a schedule.
- A scheduler runs the pipeline weekly.
- The report is saved or sent (email/Notion/Slack).

## Development plan (what you will actually code)
Step 1: Define the data model and tracking template
- Decide "one row equals one activity" or "one row equals one deal."
- Build a CSV template with required columns and example rows.
- Wire the template into the pipeline.

Step 2: Build the pipeline entry point
- Create `src/run_pipeline.py` to orchestrate load, clean, build, and report.
- Add validation checks and a clear success/error summary.

Step 3: Build the SSOT and quality checks
- Output `data_clean/ssot_catalog.csv`.
- Add simple checks: missing required fields, duplicate IDs, invalid dates.

Step 4: Generate the weekly report
- Create `src/weekly_summary.py` to produce `reports/01_weekly_summary.md`.
- Add basic charts (funnel counts, stage aging, activity vs outcomes).

Step 5: Automation (optional, if he commits to usage)
- Add a scheduled job (cron) or a lightweight web app with upload + dashboard.
- Auto-run weekly and export to PDF or HTML.

## Success criteria
- He can run one command and get a usable weekly summary.
- The report is consistent even with sparse data.
- The system exposes what is missing so tracking improves over time.

## Decision needed now
Pick the product mode:
- Option A: CLI pipeline first (fastest, lowest cost).
- Option B: Automated pipeline (needs setup and data access).
