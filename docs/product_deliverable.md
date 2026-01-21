# Product Deliverable (End Goal)

## What this product is
A small, self-running analytics system for a local agency that turns raw activity data
into a consistent weekly decision report with minimal manual work.

## Core capabilities
- Ingests raw inputs (CSV/Sheets/CRM exports).
- Cleans and standardizes data into a single source of truth dataset.
- Applies fixed funnel definitions and stage rules.
- Generates a weekly summary report and simple charts.
- Flags data quality issues (missing fields, duplicates, broken dates).

## What the user experiences
- A single command (or automated schedule) produces the report.
- The report is consistent week to week, even with sparse data.
- The system makes it obvious what is missing or inconsistent.

## Outputs
- Cleaned tables in `data_clean/`.
- A merged SSOT dataset (catalog).
- A weekly summary in `reports/` with charts and a short decision focus.

## Constraints and principles
- Simple and reliable over complex and fragile.
- Minimal friction for logging and maintenance.
- Clear definitions that do not change week to week.
- Extensible for future data sources (CRM, invoices, socials, ads).
