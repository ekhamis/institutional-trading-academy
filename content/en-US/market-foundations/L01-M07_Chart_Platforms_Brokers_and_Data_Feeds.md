# L01-M07 - Chart Platforms, Brokers, and Data Feeds

**Estimated time:** 25 minutes

## Objective
Describe the path from venue and data vendor to chart platform and broker execution.

## Why it matters
The chart, broker, and underlying exchange can be separate systems. Small differences in symbols, feeds, sessions, and aggregation can produce different candles and indicator values.

## Core ideas
- A charting platform displays data obtained from one or more providers.
- A broker routes or internalizes orders according to its execution model and product.
- The same market can have multiple symbols, contract months, composite feeds, or broker-specific prices.
- Session settings and adjusted data can change historical candles.
- Platform tools should support analysis; they do not guarantee execution quality.

## Scenario
Two learners compare a gold CFD chart with COMEX gold futures. The broad direction is similar, but exact highs, lows, spreads, and session behavior differ because the instruments and feeds are not identical.

## Practice
For one instrument, record platform, symbol, exchange or broker, data status, timezone, session setting, and whether the series is adjusted or continuous.

## Knowledge check
- **Can two legitimate feeds print slightly different candles?**
  - Yes.
- **Is a chart platform always the executing broker?**
  - No.
- **Why document the exact symbol?**
  - To make analysis and review reproducible.

## Common mistake
Assuming every symbol with the same nickname is the same product.

## Evidence classification
Platform and market-data practice

## Sources
- TradingView Help Center: https://www.tradingview.com/support/
