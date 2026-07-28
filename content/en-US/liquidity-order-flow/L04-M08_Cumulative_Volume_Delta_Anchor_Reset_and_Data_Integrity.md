# L04-M08 - Cumulative Volume Delta: Anchor, Reset, and Data Integrity

**Estimated time:** 45 minutes

## Objective
Interpret cumulative volume delta only after verifying the underlying delta method, reset anchor, session, and historical data completeness.

## Why it matters
CVD converts a sequence of delta values into a running total. A different starting point, session template, or classification method can change the entire path and any apparent divergence.

## Core ideas
- CVD adds each bar or trade delta to a running total. The calculation may reset at the start of a trading day or another selected anchor period.
- A direct bid/ask implementation requires historical bid-volume and ask-volume data. Missing historical fields can produce incomplete or empty results.
- An estimated CVD may classify lower-timeframe volume from price movement. Lower intervals improve granularity but can reduce historical coverage.
- Price-CVD divergence is a descriptive disagreement between paths. It is not a stand-alone reversal or continuation signal and can persist.
- Compare CVD only when symbol, venue, contract, session, anchor, data source, bar construction, and calculation method are documented and equivalent.

## Scenario
One CVD chart resets at the cash-session open and uses bid/ask trades; another anchors weekly and estimates delta from one-minute intrabars. Their slopes disagree. The correct response is to stop the comparison until method and anchor are aligned.

## Practice
Recalculate one session using two reset anchors and, where available, two delta methods. Document how the path and any apparent divergence change, then state what evidence would be needed before using CVD in a plan.

## Knowledge check
- **What is CVD?** A running sum of volume delta over a defined period or session.
- **Why does the reset anchor matter?** Changing the starting point changes every subsequent cumulative value.
- **Does a price-CVD divergence guarantee reversal?** No. It is a contextual observation and can persist or disappear with different data and settings.

## Common mistake
Comparing CVD lines with different anchors or methods and treating any divergence as a guaranteed turning point.

## Risk note
CVD is sensitive to data completeness and settings. Choose no trade when the calculation cannot be reproduced or the structural invalidation is unclear.

## Evidence classification
Official direct and estimated cumulative-delta platform documentation

## Sources
- Cumulative AskVolume and BidVolume Difference Bars - Sierra Chart Documentation: https://www.sierrachart.com/index.php?page=doc%2Fhelpdetails71.html
- Cumulative Volume Delta - TradingView Help Center: https://www.tradingview.com/support/solutions/43000725058-cumulative-volume-delta/
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
