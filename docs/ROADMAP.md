# Project Roadmap — Status as of 2026-10-20

| Phase | Deliverable | Verified status | Remaining validation |
|---|---|---|---|
| 1 — Privacy | Drive sync reads only allowlisted public folder; automatic publication disabled | **Implemented in code** | Real Drive end-to-end audit and privacy verification still pending |
| 2 — Three Sages | Ten hypothetical illustrative decisions and prompt roles | **Documentation complete** | Independent scoring and false-positive tests pending |
| 3 — Benefit Comparison | Twenty hypothetical decisions, paired aggregate scores and a written methodology | **Documentation complete; descriptive dataset audited** | No independent/blinded/time-matched evaluation or real-user outcome study |
| 4 — Accessible Guides | Quick start, no-GitHub workflow, four-language examples and global guide | **Documentation published** | No evidence yet of outside-user adoption, retention, or public website launch |

## Descriptive Phase 3 figures
Recomputed from the supplied 20-row dataset: traditional review **2.4/10**, sages review **8.6/10**, paired difference **+6.2 points**. The narrative report claims 2.5, 8.6 and +6.1; the discrepancy is preserved and documented in [PHASE3-RESULTS](PHASE3-RESULTS.md). These scores are not evidence of real-world regret prevention.

## Phase 4 audience test (not yet conducted)
Recruit 10 people unfamiliar with the project. Ask whether they can use the four-line method without assistance; collect anonymous feedback without personal decision content; assess use in 3+ languages, 2+ domains, and a seven-day return rate above 30%. Do not claim success before these outcomes are measured.

## Privacy boundary
The Drive source is restricted in code to the designated public folder. The GitHub workflow's daily schedule and automatic push remain disabled pending owner-approved live testing. Do not sync private journals. A past synthetic security test is not a proof of production Drive privacy.

## Next
Conduct an independently scored, reproducible, time-matched study, then a privacy-preserving usability pilot. A separate one-page public site is proposed but not deployed.
