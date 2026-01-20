# 00 — First View (from current documents)

**Date:** 2026-01-15

## What the documents show
- A weekly operating template exists with ambitious targets and an intended funnel cadence.
- Current tracking exports contain targets and very sparse January entries.
- A small target-company list exists but is mostly empty beyond names.

## Key gap
The current logs are too sparse/inconsistent to support meaningful statistics beyond basic descriptive summaries.
Biggest leverage is instrumentation: definitions + consistent logging + a single source of truth dataset.

## Immediate recommendations
1) Define metrics (Erstkontakt, Lead, Termin gelegt, Angebot, Zusage, Close, Abo vs Einmalauftrag).
2) Export CRM data (preferably Pipedrive): deals + activities + contacts weekly.
3) Tie revenue (invoices/payments) and marketing (social + ads) to leads/deals with identifiers.

## What we can do with what we have (now)
- Build a clean repo structure and data pipeline skeleton.
- Produce an initial descriptive snapshot (counts, days with activity, missingness).
- Draft the metric dictionary + “what to track next” list for the friend.

## Next data request (minimum viable)
One of the following is enough to start a real funnel analysis:
- Pipedrive deals export (with stages, created, closed, value, owner)
- Pipedrive activities export (calls/DMs/meetings with timestamps)
- list of closed clients last 6–12 months: date, service, price, acquisition channel

