# L03-M05 - VWAP Foundations

**Estimated time:** 36 minutes

## Objective
Explain how VWAP combines price and volume and use it as a contextual reference rather than an automatic signal.

## Why it matters
VWAP is widely visible on intraday charts. Understanding its calculation, anchor, and lag helps learners avoid treating the line as guaranteed support or resistance.

## Core ideas
- VWAP is a cumulative average price weighted by volume over its anchor period.
- The result depends on the selected price source, volume data, and reset or anchor period.
- Price above or below VWAP describes location relative to the weighted average; it does not guarantee continuation or reversal.
- Because VWAP uses accumulated historical data, it is a lagging reference that should be combined with structure and risk controls.

## Scenario
US100 trades above session VWAP after the open but is approaching a higher-timeframe resistance zone. VWAP location supports context, not a blind long entry.

## Practice
Plot session VWAP on three completed sessions. Mark where price crossed it and explain which crosses mattered only after adding structure and session context.

## Knowledge check
- **What does VWAP weight price by?** Volume.
- **Why does the anchor matter?** It determines where the cumulative calculation starts or resets.
- **Is VWAP guaranteed support or resistance?** No.

## Common mistake
Buying every touch below VWAP or selling every touch above it without context.

## Risk note
VWAP is a computed reference, not fair value, guaranteed support or resistance, or permission to increase leverage.

## Evidence classification
Documented indicator calculation

## Sources
- TradingView Help Center, Volume Weighted Average Price (VWAP): https://www.tradingview.com/support/solutions/43000502018-volume-weighted-average-price-vwap/
