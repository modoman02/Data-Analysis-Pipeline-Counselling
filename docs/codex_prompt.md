# Codex Prompt — Agency Analytics Project (Paste into Codex)

You are working inside a VS Code project for an analytics consulting sprint for a small local marketing/video agency.

## Objective
Build a minimal, robust analytics pipeline and exploratory analysis using the available CSVs now, but design the codebase so we can plug in future exports from:
- Pipedrive (deals, activities, contacts)
- Invoices/payments (revenue)
- Social analytics (Instagram/TikTok/LinkedIn)
- Ads platforms (Meta/Google)

The first goal is NOT fancy modeling. The goal is:
1) data structure + definitions
2) reproducible dataset build
3) descriptive dashboard/report

## Constraints
- Assume current data is sparse/incomplete.
- Focus on creating an extensible structure and clean code.
- Produce a short written report draft and a few basic charts (even if sparse) to validate the pipeline.

## Tasks (start now)
1) Create a Python environment (requirements.txt) with:
   pandas, numpy, matplotlib, seaborn (optional), scipy, statsmodels, openpyxl, pyarrow (optional)
2) Implement `src/load_data.py` that loads all CSVs from `data_raw/` (UTF-8/semicolon issues likely) and prints a summary:
   - rows/cols
   - missingness
   - date range if possible
   - unique values for key categorical columns
3) Implement `src/clean.py` to standardize:
   - column names (snake_case)
   - date parsing
   - numeric parsing (German decimals)
4) Implement `src/build_ssot.py` to write:
   - cleaned versions into `data_clean/`
   - a merged “events” table if feasible
5) Create `notebooks/eda.ipynb` (or a script) that:
   - produces basic descriptive summaries
   - creates a few charts if possible (daily counts, totals, simple funnel counts)
6) Write `reports/00_first_view.md` summarizing:
   - what the data contains
   - what’s missing
   - what next exports are needed
   - recommended metric definitions and tracking improvements

## Notes
The business target document suggests:
- ambitious yearly target revenue and “active subscription customers”
- weekly activity goals: first contacts → meetings → offers → closings
But current tracking is too sparse for inferential stats. We need to build instrumentation first.

Proceed with implementation; keep code readable, minimal, and extendable.
