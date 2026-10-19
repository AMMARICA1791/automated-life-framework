# Automated Life Framework - Public Folder (Allowlist)

This folder `public/` is the **ONLY** folder that gets published to public GitHub.

## Phase 1 - Privacy Hardening (Current)

Based on analytical review (docs/ANALYSIS.md), we moved from blocklist to allowlist:

**Old (insecure):** Download everything from Drive, then try to exclude private/
**New (secure):** Only download from public/ - everything else stays in Drive

### Structure:

```
Drive/automated-life-framework/
├── public/           <- ONLY this is synced to GitHub (this folder)
│   ├── README.md
│   ├── ANALYSIS.md
│   ├── prompts/      <- To be moved here
│   ├── templates/    <- To be moved here
│   └── docs/         <- To be moved here
├── journal/          <- Stays in Drive only (personal decisions)
│   ├── private/      <- Never synced (ID: 15yKzojvz6to-mvzEtBO72Xj9N9JTlwXN)
│   └── *.md          <- Personal logs, stays in Drive
├── docs/             <- Old location, will be migrated to public/
├── prompts/          <- Old location, will be migrated to public/
└── templates/        <- Old location, will be migrated to public/
```

### Security:

- `public/` ID: 1lwjUclr-Kecj87eoXConjkZslcEBFGZw
- `sync.py` now only syncs from public/ folder ID, not root
- Defense in depth: Even inside public/, private keywords still blocked
- Test run 39340196036 proved protection works in real GitHub Actions

### Next Steps (Phase 1):

1. Move public files from root into public/:
   - README.md -> public/README.md
   - prompts/ -> public/prompts/
   - templates/ -> public/templates/
   - docs/ -> public/docs/
   - SECURITY.md, CODE_OF_CONDUCT.md etc.

2. Keep journal/ and private/ outside public/ forever

3. Test allowlist sync with `public/` only

### Reference:

- Analytical Review: docs/ANALYSIS.md and public/ANALYSIS.md
- Security Test: https://github.com/AMMARICA1791/automated-life-framework/actions/runs/39340196036
- Private folder: journal/private/ (ID 15yKzojvz6to-mvzEtBO72Xj9N9JTlwXN) - stays in Drive only