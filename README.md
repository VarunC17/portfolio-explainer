# Why did my portfolio move today?

Each evening after Indian market close, this tool explains a user's portfolio move.

**Core principle:** math decides what happened; the LLM only narrates, from retrieved sources, with citations.

## What it does (planned)
1. Splits the day's portfolio return into market, sector and stock-specific effects.
2. For stocks with unusually large stock-specific moves, retrieves news/filings and writes a short cited explanation, or says "no clear news driver".
3. Emails a digest and collects ratings to measure quality.

## Status
Phase 0: environment and repository set up. Not yet functional.

## Setup
1. Install Python 3.12+ and git.
2. `python -m venv .venv`
3. Activate: Windows `.\.venv\Scripts\Activate.ps1`; Mac/Linux `source .venv/bin/activate`
4. `python -m pip install -r requirements.txt`
5. `python src/check_setup.py` to verify.

## Disclaimer
Explains past price moves only. Not investment advice, not a recommendation to buy or sell. Rules may change; verify current SEBI requirements.

## Structure
- `src/` code, `tests/` tests, `data/` local data (not committed), `docs/` documentation