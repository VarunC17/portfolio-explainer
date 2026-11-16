# Decisions

## D1: Python for the whole project
Why: dominant language for data/AI roles; strong libraries (pandas, statsmodels, FastAPI).

## D2: Separate src/, tests/, docs/, data/
Why: professional layout; keeps code, checks and docs apart as the project grows.

## D3: .gitignore from day one
Why: API keys and personal holdings must never reach GitHub; data files are large and local.

## D4: Terminal + git from the first session
Why: every real data/AI workflow uses them; history is part of the portfolio.

## D5: One virtual environment (.venv) per project
Why: isolates package versions between projects; .venv is never committed because it is large and rebuildable.

## D6: requirements.txt with pinned versions
Why: reproducible installs for me, for CI (GitHub Actions) and for deployment later.

## D7: Project lives outside OneDrive (C:\dev)
Why: cloud-sync tools lock files and sync thousands of package files, causing odd errors.

## D8: Public GitHub repo, no secrets ever committed
Why: it is the portfolio; secrets stay in .env, which is gitignored. Sign-in uses Git Credential Manager, never tokens in files.

## D9: Default branch is main
Why: matches GitHub's default and current convention.