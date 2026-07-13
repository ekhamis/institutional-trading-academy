# L03-M03 - Relative Volume and the Comparison Baseline

**Estimated time:** 34 minutes

## Objective
Use relative volume to compare current activity with an explicit historical baseline.

## Why it matters
An absolute volume number is difficult to judge without context. Relative volume makes the comparison visible, but the chosen lookback and session rules still matter.

## Core ideas
- A common relative-volume calculation divides current volume by average volume over a defined lookback.
- A value above one means current activity exceeds that calculation's average; it does not mean price must rise.
- Relative volume at time compares activity with similar historical time points to account for intraday seasonality.
- Lookback length, session selection, incomplete bars, and provider rules can change the result.

## Scenario
A stock shows relative volume of 1.8 shortly after the open. That confirms activity above the selected baseline, but earnings news and opening volatility still shape the risk.

## Practice
Calculate a simple ten-period relative-volume ratio for three completed bars, then note how the answer changes when the lookback changes.

## Knowledge check
- **What does relative volume compare?** Current volume with an average defined by the calculation.
- **Does relative volume above one predict direction?** No.
- **Why compare the same time of day?** Intraday activity often follows a time-dependent pattern.

## Common mistake
Quoting relative volume without knowing its lookback, session, or incomplete-bar treatment.

## Risk note
Relative volume identifies unusual participation, not a complete trade setup.

## Evidence classification
Documented indicator calculation

## Sources
- TradingView Help Center, Relative Volume calculation: https://www.tradingview.com/support/solutions/43000635874-how-do-we-calculate-relative-volume-and-relative-volume-at-time/
