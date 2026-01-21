# Implementation Paths (How to Build Each Option)

This document lays out the concrete development steps for each usage option,
plus a testing strategy that does not depend on real client data.

## Shared foundations (all options)
These are the same no matter how the user interacts with the product:
- Finalize a stable input schema (columns, types, required fields).
- Implement the core pipeline (load -> clean -> validate -> SSOT -> report).
- Build a synthetic data generator to test end-to-end flows.

Core scripts to build:
- `src/run_pipeline.py`: orchestration entry point.
- `src/validate.py`: required-field checks, duplicates, invalid dates.
- `src/weekly_summary.py`: report generation and charts.
- `src/mock_data.py`: generates realistic demo data.

## Option A: Google Sheets + Apps Script
Goal: Pascal logs in Sheets, clicks a menu item, and receives a report.

Technical steps:
1) Build the core Python pipeline (shared foundations).
2) Define a Sheet template that matches the input schema.
3) Add Apps Script to the Sheet:
   - Export Sheet data to CSV.
   - Send CSV to a backend (or store in Drive).
4) Build a small backend service:
   - Accept CSV upload via HTTP.
   - Run the Python pipeline.
   - Return report as PDF/HTML and store output.
5) Wire the Apps Script menu to call the backend and display a link to the report.

Testing:
- Use the synthetic data generator to populate the Sheet.
- Validate that Apps Script exports the data correctly.
- Confirm the backend produces a report from the exported file.

Notes:
- Apps Script alone cannot run Python; it must call a backend.
- This is still low friction for the user.

## Option B: Upload Web App (Streamlit)
Goal: Pascal uploads a CSV and immediately gets a report.

Technical steps:
1) Build the core Python pipeline (shared foundations).
2) Create a Streamlit app:
   - File upload.
   - Run pipeline in-memory.
   - Show charts and provide downloads.
3) Host the app (Streamlit Cloud, VPS, or similar).
4) Add authentication if needed.

Testing:
- Use synthetic CSVs to test upload and report rendering.
- Test error paths (missing columns, invalid dates).
- Validate report outputs match expectations.

Notes:
- This is the cleanest UX.
- Requires hosting and light maintenance.

## Option C: Drop-Folder Automation
Goal: Pascal drops a file into a shared folder and a report appears automatically.

Technical steps:
1) Build the core Python pipeline (shared foundations).
2) Implement a watcher or scheduled job:
   - Poll a folder for new files.
   - Run the pipeline on the newest file.
   - Save report outputs to a shared location.
3) Add notifications (email or message) with a report link.

Testing:
- Use synthetic files dropped into the folder.
- Validate automatic detection, processing, and report output.
- Simulate missing or malformed files.

Notes:
- No user interface required.
- Requires a machine/server to run on a schedule.

## Option D: Lightweight Desktop App (optional)
Goal: Pascal runs a small app locally, uploads a file, gets a report.

Technical steps:
1) Build the core Python pipeline (shared foundations).
2) Wrap the pipeline in a simple UI (Tkinter or Electron + Python backend).
3) Package into a standalone installer.

Testing:
- Use synthetic data files.
- Validate cross-platform behavior (Mac/Windows).

Notes:
- More effort to distribute and maintain.
- Avoid unless hosting is impossible.

## Synthetic data strategy (for all options)
We do not wait for real data. We generate realistic test data to validate the system:
- A mock company list, contacts, and deals.
- Activities across a funnel with timestamps.
- Random missingness to test validation.
- Revenue values in realistic ranges.

Outputs of the generator:
- CSV files that match the final schema.
- A "golden" dataset for repeatable tests.

## Testing plan (end-to-end)
1) Generate synthetic data.
2) Run the pipeline and validate SSOT output.
3) Generate the weekly report and verify sections are present.
4) Validate error handling with incomplete or broken inputs.

## Decision later
We can build the pipeline once and swap the interface later.
That means we can start with Option B (upload app) or Option C (drop folder),
then move to Option A (Sheets) or vice versa depending on user preference.
