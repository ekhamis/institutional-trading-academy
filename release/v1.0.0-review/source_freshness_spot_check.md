# v1.0.0 Official-Source Freshness Spot-Check

Checked: 2026-10-30

## Scope

This pre-lock check covers the official, time-sensitive sources used by the
instrument-verification and scheduled-event missions. It records source
availability and identity; it does not turn examples into live trading
instructions. Contract terms, calendars, session hours, and trade dates must
still be checked at decision time.

## Results

| Registry IDs | Official source | Result |
| --- | --- | --- |
| `CME_ES_SPEC`, `CME_ES` | CME E-mini S&P 500 contract specifications | Current official product page resolved and identified ES as the E-mini S&P 500 futures product. |
| `CME_NQ_SPEC`, `CME_NQ` | CME E-mini Nasdaq-100 contract specifications | Current official product page resolved and identified NQ as the E-mini Nasdaq-100 futures product. |
| `CME_GC_SPEC`, `CME_GOLD` | CME Gold futures contract specifications | Current official product page resolved and exposed the contract-specification, expiration, rulebook, margin, and trading-hours resources. |
| `CME_MGC_SPEC` | CME Micro Gold futures contract specifications | Current official product page resolved for the Micro Gold product. |
| `FED_CALENDAR`, `FED_CAL` | Federal Reserve FOMC calendars | Current official calendar page resolved. Missions use it as a source to verify scheduled event risk, not to hard-code a release time. |
| `BLS_CALENDAR`, `BLS_CAL` | U.S. Bureau of Labor Statistics release calendar | Current official schedule page resolved. Missions require timezone/source verification and do not treat a remembered time as authoritative. |

## Curriculum review outcome

- `L01-M09` remains conditional and asks learners to verify the event, source,
  timezone, and release status rather than rely on the synthetic example time.
- `L06-M01` through `L06-M10` explicitly require current venue, symbol,
  expiry, multiplier, tick, session, and data-provenance checks. Their numeric
  cases are synthetic exercises and are regression-tested separately.
- No source URL correction or curriculum edit was indicated by this bounded
  spot-check.

## Gate status

Source freshness spot-check: **PASS for the v1.0.0 review candidate at the
date above**. Recheck official terms and calendars immediately before the
English lock if the lock occurs on a later date.

