# L04-M07 - Delta: Aggressive Trade Imbalance Without Certainty

**Estimated time:** 42 minutes

## Objective
Calculate and interpret volume delta as a difference between classified buy-side and sell-side activity without treating its sign as a price forecast.

## Why it matters
Positive or negative delta describes how a platform classified executed activity. Price can advance, stall, or reverse under the same delta sign, so the response matters more than the number alone.

## Core ideas
- In bid/ask trade data, delta is commonly calculated as ask volume minus bid volume for a price level, bar, or period.
- In estimated implementations, lower-timeframe price movement can be used to assign volume to positive or negative categories. This is not equivalent to direct exchange bid/ask classification.
- Positive delta means the classified buy-side volume exceeded the classified sell-side volume for the selected calculation. It does not guarantee a higher close or future rise.
- Compare delta with price progress, location, volatility, and structure. Large delta with limited progress is an observation that may justify further testing, not proof of absorption.
- Normalize expectations by instrument, session, bar type, and feed. Raw delta values from different markets or settings are not directly comparable.

## Scenario
A footprint bar shows strongly positive delta at a prior range high, but price makes little progress and closes inside the range. Record the aggressive buy-side imbalance and weak price result separately; do not assume either immediate reversal or continuation.

## Practice
Collect twenty bars with extreme positive or negative delta. Classify the price result as progress, stall, rejection, or unresolved, then test whether context improves the interpretation over delta sign alone.

## Knowledge check
- **How is bid/ask volume delta commonly calculated?** Ask volume minus bid volume.
- **Does positive delta guarantee a rising price?** No. It describes classified executed activity, not the next price move.
- **Why can delta differ between platforms?** The trade data, classification algorithm, intrabar precision, bar type, and session settings can differ.

## Common mistake
Buying every positive-delta bar or selling every negative-delta bar without considering methodology, price response, structure, and risk.

## Risk note
Delta can change rapidly and may be estimated. Never size a trade from delta magnitude alone; use predefined invalidation and a valid no-trade option.

## Evidence classification
Official bid/ask numbers-bars and estimated volume-delta documentation

## Sources
- Numbers Bars - Sierra Chart Documentation: https://www.sierrachart.com/index.php?page=doc%2FNumbersBars.php
- Volume Delta - TradingView Help Center: https://www.tradingview.com/support/solutions/43000725057-volume-delta/
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
