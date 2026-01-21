# Option A Plan: Google Sheets + Apps Script

Goal: Pascal logs data in a Sheet and triggers report generation without coding.

## Scope
- User input lives in a Google Sheet template.
- A menu action triggers an Apps Script.
- Apps Script exports data and sends it to a backend.
- Backend runs the Python pipeline and returns report output.

## Components
- Google Sheet template (tabs, columns, data validation).
- Apps Script project (menu, export, HTTP request).
- Backend service (API endpoint that runs pipeline).
- Report storage (Drive or backend storage).

## Detailed steps
1) Sheet template
   - Create a single input tab with required columns.
   - Add data validation lists for stages and activity types.
   - Lock header row and add usage notes.

2) Apps Script
   - Add a custom menu: `Analytics > Run Report`.
   - Export the input tab to CSV.
   - POST the CSV to a backend endpoint.
   - Display a link to the output report.

3) Backend service
   - Minimal API endpoint: `POST /run-report`.
   - Save upload to a temp folder.
   - Run `src/run_pipeline.py` with the uploaded file.
   - Return report URLs (PDF/HTML + CSV outputs).

4) Report delivery
   - Save to Drive or a hosted folder.
   - Optional: email the report to Pascal.

## Engineering details
- Auth: use a shared secret token for the POST request.
- Storage: local disk or cloud bucket.
- Error handling: return clear error messages for missing columns.

## Testing plan
- Generate synthetic data and import into the Sheet.
- Confirm Apps Script export format and encoding.
- Validate that the backend generates a report.
- Test error states (missing columns, invalid dates).

## Risks and mitigations
- Apps Script quotas and timeouts: keep pipeline lightweight.
- Sheet structure changes: lock headers and validate schema.
- Backend hosting: pick a simple host (Render, Fly, or VPS).
