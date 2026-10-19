# Automated Life Framework
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
