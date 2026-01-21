# Option D Plan: Lightweight Desktop App

Goal: Pascal runs a small local app, uploads a file, and gets a report.

## Scope
- Local UI for file upload and report generation.
- Packaged as a standalone installer.

## Components
- UI layer (Tkinter or Electron).
- Python pipeline bundled with the app.
- Local storage for outputs.

## Detailed steps
1) UI prototype
   - File picker for CSV/Excel.
   - "Run Report" action.
   - Output preview and download location.

2) Pipeline integration
   - Run the pipeline on the selected file.
   - Write outputs to a local folder.

3) Packaging
   - Create a bundled app using PyInstaller or similar.
   - Test on Mac (and Windows if required).

## Engineering details
- Local file permissions.
- Clear error dialogs for invalid files.
- Versioning and update process.

## Testing plan
- Use synthetic files.
- Validate output generation on target OS.
- Confirm errors are user-friendly.

## Risks and mitigations
- Higher maintenance effort for packaging and updates.
- OS-specific issues and distribution overhead.
