# L04-M06 - Footprint Charts: Traded Volume at Price

**Estimated time:** 45 minutes

## Objective
Explain what a footprint chart displays, distinguish executed volume from resting orders, and verify how the platform classifies bid and ask activity.

## Why it matters
Footprints add price-level detail inside each bar, but platforms can construct them from different data. Without checking the method, similar-looking cells can represent materially different evidence.

## Core ideas
- A footprint or numbers bar distributes traded activity across price levels within each chart bar. It may show bid volume, ask volume, total volume, delta, or comparison thresholds.
- Executed volume is not the same as displayed depth. A footprint records trades after they occur; a DOM or heatmap records resting orders before execution or cancellation.
- With suitable tick data, trades can be classified relative to the bid and ask. Some platforms instead estimate buy and sell categories from lower-timeframe price movement.
- Historical precision can change with the intrabar interval, available tick history, row size, aggregation, and session settings. Document these before comparison.
- Cell imbalance, POC, value area, and delta are descriptive calculations. They do not independently establish direction, support, resistance, or participant identity.

## Scenario
Two footprint platforms display different delta at the same bar. One uses historical bid/ask trade data; the other categorizes lower-timeframe volume by intrabar direction. The visual disagreement is a methodology difference, not automatically a data error.

## Practice
Build the same footprint view on two platforms or data settings. Document symbol, venue, session, tick or intrabar source, row size, buy/sell classification method, and resulting differences.

## Knowledge check
- **Does a footprint display resting limit orders?** No. It primarily displays executed volume at price; resting orders belong to depth data.
- **Can two platforms calculate different footprint values?** Yes. Data source, trade classification, intrabar precision, and row settings can differ.
- **Does a highlighted imbalance guarantee continuation?** No. It is a descriptive comparison that requires price, structure, and risk context.

## Common mistake
Assuming every footprint cell is true exchange bid/ask volume and treating a highlighted imbalance as a direct entry signal.

## Risk note
Do not trade a footprint whose data source or classification method is unknown. Require structural invalidation and controlled size independently of the cell display.

## Evidence classification
Official footprint and numbers-bars platform documentation

## Sources
- Volume Footprint Charts: A Complete Guide - TradingView Help Center: https://www.tradingview.com/support/solutions/43000726164-volume-footprint-charts-a-complete-guide/
- Numbers Bars - Sierra Chart Documentation: https://www.sierrachart.com/index.php?page=doc%2FNumbersBars.php
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
