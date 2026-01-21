# Project Brief — Agency Funnel & Ops Analytics (Friend Consulting)

**Date created:** 2026-01-15**Owner:** Moritz (analyst) + ChatGPT (planning/analysis) + Codex in VS Code (implementation)

## Context

You are providing pro-bono data science/analytics consulting for a friend who runs a small, local online marketing / video production agency.He produces short- and mid-length videos for local businesses and also operates his own Instagram channel as a protagonist/brand.

Goal: turn the business from “amateur tracking + gut feel” into a **measurable, analyzable system**:

-   clearer pipeline / CRM discipline
-   consistent metrics
-   descriptive + exploratory analytics
-   actionable weekly decision-making
-   optional future automation or a small internal “pipeline app”

## What we have so far

We currently have:

-   A weekly planning/protocol document (targets, weekly activity goals, basic templates)
-   Three CSV exports from an “Anfragen Dashboard”:
    -   Jahresübersicht (mostly target numbers; sparse actuals)
    -   Januar Anfragen (daily log; very sparse entries)
    -   Zielliste (small list of target companies; mostly empty detail fields)

### First-pass diagnosis (from ChatGPT)

-   The documents describe an **intended operating system** (targets + weekly cadence).
-   Actual tracked data is **too sparse and inconsistent** for meaningful inferential statistics.
-   Biggest leverage: **instrumentation + definitions + single source of truth** before doing “real stats”.

## What “success” looks like

Short term (1–2 weeks once access exists):

-   A “single source of truth” dataset that is re-buildable with one command
-   A simple weekly dashboard: funnel rates, stage aging, activity vs results, pace vs targets

Medium term (1–2 months):

-   Segmentation insights (by industry/service/channel)
-   Operational bottleneck diagnosis (cycle time by stage, rework, delays)
-   A repeatable report for the friend (executive + appendix)

Long term:

-   Lightweight internal tooling/automation (e.g., clean data exports, automated weekly report)
-   Optional “pipeline app” (only if needed and data is stable)

## Philosophy

-   Keep it **practical**: only analyses that translate to decisions.
-   Prefer **clean definitions + reliable logging** over fancy models.
-   Build minimal friction processes: tracking should be effortless or it won’t happen.

## Note 21.01.

-   need further conversation with Pascal, need further data and focus.
-   Ask, what he wants. If i turn this into a big ass pipeline thing, then this should not be unasked for. Then i could also get paid for it, or at least i can propose it to him as a freelance kinda thing.
-   I need more information, i need more ideas about the whole project. I dont even know what he tracks. I should figure out most i can and propose a plan and build the first steps into this direction and then schedule a meeting with him presenting this and proposing my idea but also furthermore asking for more data or focus of what he wants.
-   Need to figure out a way to turn the worker (Sascha, etc.) Notes into actionable and profitable insights or build something for that. right now im not really focusing on that.