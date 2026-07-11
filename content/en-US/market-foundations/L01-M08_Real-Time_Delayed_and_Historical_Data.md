# L01-M08 - Real-Time, Delayed, and Historical Data

**Estimated time:** 22 minutes

## Objective
Verify whether a chart is real-time, delayed, replayed, or historical before making a time-sensitive decision.

## Why it matters
A clean chart is not necessarily current. Exchanges may require separate market-data permissions, and platforms can display delayed or vendor-dependent information.

## Core ideas
- Real-time data is delivered with minimal distribution delay under the relevant entitlement.
- Delayed data can be suitable for education but unsuitable for live execution decisions.
- Historical and replay modes deliberately show past data.
- Bid/ask data, last-trade data, and indicative prices are different information types.
- Data quality checks belong in every trading checklist.

## Scenario
A learner sees a breakout on a delayed index feed and enters through a separate broker whose live price has already moved far beyond the planned level.

## Practice
Audit five symbols on your platform. Record feed source, delay indicator, exchange entitlement, last-trade time, and comparison with your execution venue.

## Knowledge check
- **Can delayed data look visually normal?**
  - Yes.
- **Should a live order be based on an unverified delayed feed?**
  - No.
- **Are bid/ask and last price identical concepts?**
  - No.

## Common mistake
Assuming a moving screen equals exchange-grade real-time data.

## Evidence classification
Data-quality practice

## Sources
- TradingView Help Center: https://www.tradingview.com/support/
