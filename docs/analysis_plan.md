# Action Plan (Consultant Mode)

## Phase 1 — Data audit & metric definitions (must-have)
Deliverables:
1) Metric Dictionary (strict definitions)
2) Funnel Schema (what “one row” represents)
3) Source-of-truth map (Pipedrive + revenue + socials + ads)

Output: a short document you can hand to the friend to align on definitions.

## Phase 2 — Build the single source of truth (SSOT)
If possible, export from Pipedrive (or other CRM) weekly:
- deals
- activities
- contacts
Optionally: invoices / payment export, social analytics export, ad platform export.

Then create:
- /data_raw: untouched exports
- /data_clean: standardized cleaned tables
- /src: a pipeline script that produces merged dataset (CSV/Parquet)
- /reports: charts + written summary

## Phase 3 — Descriptive & exploratory analysis (high leverage)
- Funnel conversion rates:
  - contact → meeting
  - meeting → offer
  - offer → close
- Stage aging (time stuck in each stage)
- Cycle time (first contact → close)
- Deal size distribution & revenue concentration
- Segment comparisons (industry/service/channel)
- “Activity quality”: volume vs conversion

## Phase 4 — Recommendations & operating rhythm
- weekly dashboard + 15-min review ritual
- bottleneck focus: pick the single constraint each week
- simple experiments: scripts + outreach templates + content formats
- instrumentation upgrades (required fields, automation, error-proof logging)
