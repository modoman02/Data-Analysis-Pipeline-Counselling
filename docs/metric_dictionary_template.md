# Metric Dictionary (Template)

**Goal:** stop ambiguity. Every metric must have a definition, inclusion rules, and a data source.

## Core entities

-   Contact: a person/business with identifiable contact info (name + phone/email + company).
-   Lead: a contact with an identified need + interest.
-   Deal: a potential engagement with value potential and a stage.
-   Activity: an action taken (call, DM, email, meeting, follow-up).

## Funnel stages (example — adjust to actual workflow)

1.  First contact (Erstkontakt)
2.  Qualified lead
3.  Meeting scheduled (Termin gelegt)
4.  Meeting held (Termin gehabt)
5.  Offer sent (Angebot)
6.  Verbal yes / commitment (Zusage)
7.  Closed won (Close)
8.  Delivered
9.  Retained / subscription (Abo)

## Definitions

### First contact (Erstkontakt)

Definition: first outbound or inbound touch where the agency and prospect directly interact.
Entry rule: activity is logged with channel and timestamp; contact info captured.
Exit rule: qualified lead or disqualified.
Field: first_contact_at
Source: CRM activity log or manual tracking sheet.Notes: includes DM, call, email, or form submission.

### Qualified lead

Definition: contact has confirmed need and potential fit (need, budget, timeline).
Entry rule: qualification questions answered and marked as qualified.
Exit rule: meeting scheduled or disqualified.
Timestamp field: qualified_at
Source: CRM deal stage change or qualification checklist.
Notes: disqualify if no fit, no budget, or no response after follow-ups.

### Meeting scheduled (Termin gelegt)

Definition: a discovery meeting time is agreed and scheduled.
Entry rule: calendar invite sent or meeting task created.
Exit rule: meeting held, no-show, or canceled.
Timestamp field: meeting_scheduled_at
Source: CRM activity type "meeting" or calendar log.
Notes: reschedules should update the scheduled timestamp only once.

### Meeting held (Termin gehabt)

Definition: the discovery meeting actually took place.E
ntry rule: meeting marked completed with notes.
Exit rule: offer sent, follow-up required, or disqualified.
Timestamp field: meeting_held_at
Source: CRM activity completion or meeting notes.
Notes: record key requirements and buying signals.

### Offer sent (Angebot)

Definition: proposal or quote delivered with scope and price.
Entry rule: proposal sent and logged.
Exit rule: verbal yes, lost, or expired.
Timestamp field: offer_sent_at
Source: CRM stage change or proposal system.
Notes: include price range and validity period.

### Verbal yes / commitment (Zusage)

Definition: prospect explicitly agrees to proceed pending contract/payment.
Entry rule: explicit confirmation received (email/DM/call notes).
Exit rule: contract signed (closed won) or lost.
Timestamp field: verbal_yes_at
Source: CRM note or status.
Notes: should include expected start date.

### Closed won (Close)

Definition: signed agreement and/or first payment received.
Entry rule: contract signed or invoice paid.
Exit rule: delivered or churned.
Timestamp field: closed_won_at
Source: CRM deal won plus invoice/payment record.
Notes: if payment arrives later, use contract date for funnel timing.

### Delivered

Definition: agreed deliverables completed and accepted by the client.
Entry rule: project marked completed with acceptance.
Exit rule: retained/subscription or end of engagement.
Timestamp field: delivered_at
Source: project tracker or client sign-off.
Notes: use a simple checklist to avoid ambiguity.

### Retained / subscription (Abo)

Definition: client commits to ongoing recurring service (retainer).
Entry rule: recurring invoice created or subscription contract signed.
Exit rule: cancellation or pause.
Timestamp field: retained_at
Source: billing system or CRM.
Notes: separate recurring vs one-off revenue.

## Financial metrics

-   Revenue (Netto): sum of invoiced amounts excluding VAT; currency EUR; period by invoice date; source invoices/payments.
-   MRR (if subscriptions): sum of active recurring contracts for the month; exclude one-off projects; source billing system.
-   Gross margin proxy: revenue minus paid media spend and contractor costs; period monthly; source invoices + ads + contractor invoices.

## Marketing metrics

-   Organic reach (by platform): total reach/impressions per week or month; source platform analytics.
-   Inbound leads: count of unique inbound contacts from DM, call, form, or email; dedupe by contact; source CRM/forms.
-   Paid spend, clicks, CPL: spend and clicks per platform; CPL = spend / qualified leads; period weekly or monthly.


### Note 21.01:
- Im pretty happy with this metric list until now: If this was well defined, then this would already be a big move forward for them.
