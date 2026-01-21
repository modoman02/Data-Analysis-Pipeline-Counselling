# Usage Options (Non-Technical User)

This document describes realistic ways Pascal can use the product without coding or VS Code.
It focuses on practical UX, constraints, and tradeoffs.

## Option A: Google Sheet + Run Report action
How it works:
- Pascal logs data in a Google Sheet template.
- A custom menu item or a clickable Drawing runs an Apps Script.
- The script exports the data, runs the analysis, and outputs a report.

How the action works:
- Google Sheets does not have a native "button" widget.
- You can insert a Drawing and assign a script to it, which behaves like a button.
- Or add a custom menu item (e.g., "Analytics > Run Report").

Outputs:
- PDF/Doc report in Drive.
- CSV summary for downloads.

Pros:
- Lowest friction (he already uses Sheets).
- No file uploads.
- Easy to share and collaborate.

Cons:
- Apps Script limits and quotas.
- More fragile if the Sheet structure changes.

## Option B: Upload web app (Streamlit)
How it works:
- Pascal opens a URL.
- Uploads a CSV/Excel file exported from Sheets or CRM.
- The app runs the pipeline and shows the report.

Outputs:
- Downloadable PDF/HTML report.
- Cleaned data CSV.

Pros:
- Clean UX, very simple for non-technical users.
- Keeps the pipeline logic in one place.

Cons:
- Requires hosting.
- Ongoing maintenance for the server/app.

## Option C: Drop-folder automation (no UI)
How it works:
- Pascal drops a CSV into a shared folder (Drive/Dropbox).
- A scheduled job runs weekly and emails the report.

Outputs:
- Weekly report delivered automatically.
- Cleaned data saved in a folder.

Pros:
- No app or UI required.
- Fully automated once configured.

Cons:
- Setup is more technical.
- Needs a machine/server running on a schedule.

## Important constraint
Google Docs does not support clickable buttons that run scripts.
Only Google Sheets can attach scripts to drawings or custom menus.

## Considerations before choosing
- Data source: Sheet vs CRM export.
- Automation level: manual click vs scheduled job.
- Hosting: none (Apps Script) vs hosted app.
- Reliability: Sheets structure changes can break scripts.
- Security: where data is stored and who can access it.

## Suggested default
Start with Google Sheet + button (lowest friction), then move to an upload app if usage grows.

## Input formats that fit the system
Recommended (most practical):
- Google Sheet template (structured rows/columns).
- Google Form feeding a Sheet (lower friction, consistent inputs).
- CSV export (works with any tool, easy to ingest).

Possible but heavier:
- Airtable or Notion database (nice UI, but more setup).
- CRM export (best long-term if he already uses it consistently).

Not recommended for structured tracking:
- Google Docs (great for notes, poor for automation). If used, it must be manually converted to a Sheet or CSV.
