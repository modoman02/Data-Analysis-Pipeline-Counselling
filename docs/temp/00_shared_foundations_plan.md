# Shared Foundations Plan

This plan covers the core system every option depends on: data schema, pipeline,
validation, reporting, and test data. Each interface option plugs into this base.

## Goals
- A stable input schema that is easy to fill and easy to validate.
- A repeatable pipeline that builds a single source of truth (SSOT).
- A weekly report output that is consistent even with sparse data.
- A synthetic data generator to test end-to-end without client data.

## Architecture (modules)
- `src/schema.py`: schema definition (required columns, types, allowed values).
- `src/load_data.py`: load CSV/Excel/Sheet exports.
- `src/clean.py`: normalize columns, parse dates, numeric parsing.
- `src/validate.py`: data quality checks and clear error messages.
- `src/build_ssot.py`: merge into SSOT catalog.
- `src/weekly_summary.py`: compute metrics and render report.
- `src/mock_data.py`: generate synthetic data for testing.
- `src/run_pipeline.py`: orchestrate full flow and output artifacts.

## Input schema (v1)
Minimum columns (one row = one activity):
- `activity_id` (unique)
- `contact_id` or `company_name`
- `activity_type` (call, dm, email, meeting)
- `activity_date` (YYYY-MM-DD)
- `stage` (funnel stage)
- `owner` (who did it)
- `result` (optional)
- `deal_value_eur` (optional)
- `source_channel` (optional)

## SSOT outputs
- `data_clean/activities_clean.csv`
- `data_clean/ssot_catalog.csv`
- `reports/01_weekly_summary.md`
- `reports/figures/*.png`

## Validation rules
- Required columns present.
- Unique `activity_id`.
- Valid date formats.
- Stage values in allowed list.
- Warn if missing contact/company identifiers.

## Report contents (weekly)
- Activity volume by type and stage.
- Funnel counts by stage.
- Stage aging summary (if timestamps exist).
- Pace vs targets (if targets provided).
- Data quality section (missingness, invalids).

## Synthetic data plan
- Generate contacts, activities, and a basic funnel path.
- Include realistic sparsity and missing fields.
- Seeded random generation for repeatable tests.

## Test strategy
- Unit tests for parsing and validation.
- End-to-end run with synthetic data.
- Snapshot a "golden" report output for regression checks.

## Documentation
- `docs/product_deliverable.md`
- `docs/usage_options.md`
- `docs/implementation_paths.md`
