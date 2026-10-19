Project Structure
This document explains the global-standard structure for contributors.

automated-life-framework/
├── README.md                 # Main global entry point
├── LICENSE                   # MIT
├── CONTRIBUTING.md           # How to contribute
├── CODE_OF_CONDUCT.md        # Community standards
├── SECURITY.md               # Security policy
├── GLOSSARY.md               # Arabic -> English glossary (historical)
├── .gitignore                # Protects secrets
├── prompts/                  # The 3 Sages (core value)
│   ├── 01-sage-of-facts.md
│   ├── 02-sage-of-evidence.md
│   └── 03-sage-of-contradiction.md
├── templates/
│   └── decision-template.md  # 4-line observer template
├── docs/
│   ├── OBSERVER-MODE.md      # How observer-only works
│   ├── SYNC-DRIVE-TO-GITHUB.md
│   ├── sync.py
│   └── workflow.yml
└── journal/
    └── 2026-10-19-decision-01...md  # Example decision log

Why this structure?
This follows the standard for global open-source prompt frameworks:
* prompts/ - Core intellectual property, easy to find
* templates/ - User-facing files
* docs/ - Technical documentation
* journal/ - Example usage, not required

All file names are 100% English, no transliteration.
For GitHub: When you push to GitHub, the structure is preserved. The github-en/ legacy folder is deprecated - use root structure now.
