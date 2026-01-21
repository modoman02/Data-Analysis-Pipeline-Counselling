# Option C Plan: Drop-Folder Automation

Goal: Pascal drops a CSV into a shared folder and a report appears automatically.

## Scope
- Shared folder for inputs (Drive, Dropbox, or local).
- Scheduled job watches for new files.
- Pipeline runs and writes outputs to a shared report folder.

## Components
- Folder watcher or scheduled cron job.
- Pipeline runner script.
- Report storage location.
- Optional email notification.

## Detailed steps
1) Shared folder setup
   - Define input folder structure (e.g., `incoming/`).
   - Define output folder structure (e.g., `reports/`).

2) Scheduler
   - Cron job or scheduled task runs daily/weekly.
   - Detect newest file and skip already processed ones.

3) Pipeline execution
   - Copy file to temp and run `src/run_pipeline.py`.
   - Save outputs to `reports/` and `data_clean/`.

4) Notifications (optional)
   - Email report link or attach PDF.

## Engineering details
- File naming conventions and timestamps.
- Logging for audit trail.
- Error handling with retries.

## Testing plan
- Drop synthetic CSVs into the folder.
- Confirm detection and output generation.
- Test missing or invalid inputs.

## Risks and mitigations
- Needs a machine/server running reliably.
- Users must follow file naming and placement rules.
