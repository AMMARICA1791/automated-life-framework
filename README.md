# Automated Life Framework

## ⚡ Prevent Regret in 5 Minutes — No App, No GitHub, No Signup

Write four lines anywhere (paper, private notes, or an AI chat):

1. **What will I do?** One sentence.
2. **Why now?** The real reason.
3. **What is the worst outcome I can tolerate?**
4. **What did I say opposite a month ago?** Leave blank if unknown.

Copy this into your AI assistant:

> Analyze my four-line decision using three distinct lenses: **Facts** (which claims have reliable sources and dates, and which are unverified?), **Evidence** (which assumptions can be tested or quantified, without inventing numbers?), and **Contradiction** (what past commitment conflicts, and what new evidence might justify changing my mind?). Give each analysis separately, identify uncertainties, and suggest one practical next step. Do not make the decision for me.

- [Start in 5 minutes](docs/QUICK-START.md)
- [Examples in English, Portuguese, Arabic and Spanish](docs/EXAMPLES.md)
- [Full public guide](docs/PHASE4-GLOBAL-GUIDE.md)

**Privacy:** Do not paste confidential journals or sensitive personal information into public channels. This framework does not require submitting decisions to this repository.

**Evidence note:** The reported +6.2-point difference is a descriptive comparison of 20 authored hypothetical examples, **not** verified improvement in real-world decisions or reduced regret. [See audit](docs/PHASE3-RESULTS.md).

---

## For Developers — Repository Details Below

Observer-Only Regret Prevention System

> Not a tool that brings news faster, but a mirror that prevents regret slowly.  
> **Time is like a sword.**

## The Problem
We make stupid decisions not because we lack information, but because we contradict ourselves.

## The Solution - 4 Lines Observer-Only
1. Fill 4 lines in templates/decision-template.md
2. Paste them anywhere
3. The 3 Sages analyze and reveal contradiction
4. System archives automatically

**You write 4 lines. System does the rest.**

## The 4-Line Template
1. What will I do? [one sentence]
2. Why now? [real reason]
3. What is worst outcome?
4. What did I say opposite a month ago?

See full version in Drive.

## 🔒 Phase 1 Privacy Hardening - Allowlist Mode

The Google Drive synchronization source is restricted to one explicitly designated `public/` folder. Files outside that folder, including `journal/` and `journal/private/`, are not read by the synchronization script. Name-based exclusion remains an additional safeguard, not the primary privacy boundary.

**Publication is disabled pending owner review.** The daily schedule is disabled, and the workflow's Git push step is disabled. No private decision journal should be published to this public repository.

The public folder in Drive must be reviewed before any automatic publishing is enabled. The independent security test validates the path checks, but does not verify actual Drive content.

An analytical report was described in the Phase 1 handoff, but its source contents have not yet been retrieved or published.

## Phase 2: Three Sages — Illustrative Tests Documented

Ten hypothetical decisions are available for review:
- [Narrative examples](docs/PHASE2-SAGES-TEST.md)
- [Structured CSV](templates/decisions-test-10.csv)
- [Results and methodological limitations](docs/PHASE2-RESULTS.md)

The examples illustrate distinct fact-checking, evidence, and contradiction questions. The source report's 90% claim is **not an independently validated accuracy rate**. A controlled comparison with a simple review is still needed. Automatic Drive sync and publication remain disabled.

## Phase 3: Hypothetical Comparison — Data Reviewed (Validation Pending)

- [20-decision dataset](templates/decisions-20-controlled.csv)
- [Verified calculations and methodological limitations](docs/PHASE3-RESULTS.md)
- [Controlled-test source document status](docs/PHASE3-CONTROLLED-TEST.md)

The supplied 20 hypothetical decisions show a traditional-review mean of **2.4/10**, a three-sage mean of **8.6/10**, and a **+6.2-point descriptive difference**. These numbers are from the provided dataset, not independently validated evidence of effectiveness. Full scoring rubrics, paired review outputs, blinded independent evaluation, and real-world outcomes remain pending. The original detailed controlled-test document was not attached. Daily Drive sync and automatic GitHub publication remain disabled.
