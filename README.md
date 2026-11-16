# Why did my portfolio move today?

Each evening after Indian market close, this tool explains a user's portfolio move.

**Core principle:** math decides what happened; the LLM only narrates, from retrieved sources, with citations.

## What it does (planned)
1. Splits the day's portfolio return into market, sector and stock-specific effects.
2. For stocks with unusually large stock-specific moves, retrieves news/filings and writes a short cited explanation, or says "no clear news driver".
3. Emails a digest and collects ratings to measure quality.

## Status
Phase 0: project setup. Not yet functional.

## Disclaimer
Explains past price moves only. Not investment advice, not a recommendation to buy or sell. Rules may change; verify current SEBI requirements.

## Structure
- `src/` code, `tests/` tests, `data/` local data (not committed), `docs/` documentation