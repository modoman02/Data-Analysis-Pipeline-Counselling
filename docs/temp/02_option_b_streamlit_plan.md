# Option B Plan: Upload Web App (Streamlit)

Goal: Pascal uploads a CSV and gets a report immediately.

## Scope
- A simple web UI for file upload.
- The app runs the pipeline and renders outputs.
- Download links for reports and cleaned data.

## Components
- Streamlit app (UI + pipeline call).
- Hosting environment.
- Basic authentication (optional).

## Detailed steps
1) Streamlit UI
   - File uploader for CSV/Excel.
   - Input preview and schema validation output.
   - "Run Report" action.

2) Pipeline integration
   - Load file in-memory.
   - Run cleaning, validation, SSOT build, and report generation.
   - Store outputs in a temp directory.

3) Output UX
   - Show summary metrics on the page.
   - Provide downloads for report and cleaned data.
   - Display validation errors inline.

4) Hosting
   - Deploy on Streamlit Cloud or a small VPS.
   - Add basic access control (password or shared token).

## Engineering details
- File size limits and validation.
- Error handling: missing columns, invalid dates.
- Cache results for repeatable runs.

## Testing plan
- Use synthetic CSVs to verify full flow.
- Run tests for malformed data.
- Validate charts and report formatting.

## Risks and mitigations
- Hosting cost and maintenance: keep app simple.
- Security: restrict access, avoid storing sensitive files long-term.
