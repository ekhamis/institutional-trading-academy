# L04-M04 - Liquidity Zones, Stop Orders, and Hidden Information

**Estimated time:** 40 minutes

## Objective
Separate observable liquidity from inferred chart zones and explain why stop orders, hidden size, and cross-venue interest cannot be read directly from a normal price chart.

## Why it matters
Traders often label prior highs, lows, or range edges as liquidity pools. These locations may attract activity, but the chart does not reveal the exact quantity, ownership, order type, or intent waiting there.

## Core ideas
- Observable liquidity includes displayed bids and offers from a specified order-book feed. Executed trades are observed separately in trade or volume data.
- A chart-based liquidity zone is an inference that orders may cluster near a visible reference such as a prior high, low, range boundary, or round price. The quantity is unknown unless a suitable feed shows it.
- Stop orders are conditional. In the equity example described by Investor.gov, a stop becomes a market order when the stop price is reached; broker and venue policies can differ.
- Hidden, iceberg, synthetic, implied, and cross-venue orders mean the displayed book may not contain all available interest.
- Use precise language: observed displayed depth, observed executions, or inferred potential order concentration. Do not merge these categories.

## Scenario
Price approaches a prior session high that many analysts call a buy-stop pool. The chart confirms the reference but not the stop quantity. A DOM shows some offers, while hidden and off-venue interest remain unknown. Plan only around observable response and controlled invalidation.

## Practice
Mark six commonly cited liquidity zones on historical charts. For each, list what is directly observed, what is inferred, what data would be needed to strengthen the claim, and what would justify no trade.

## Knowledge check
- **Can a price chart show the exact quantity of stop orders above a prior high?** No. The location may be inferred, but the quantity and ownership are not visible on a normal chart.
- **Is displayed depth the complete market interest?** Not necessarily. Hidden, iceberg, synthetic, implied, and other-venue interest can be absent.
- **What language should distinguish evidence quality?** Label displayed orders and executions as observed, and potential order concentrations as inferred.

## Common mistake
Presenting every prior high or low as a measured pool of stop orders and describing unknown participants or intent as fact.

## Risk note
An inferred zone is not an exit guarantee. Fast triggering of conditional orders can widen spreads and create slippage; define risk outside the scenario or stand aside.

## Evidence classification
Official order-type and exchange order-book documentation

## Sources
- Stop, Stop-Limit, and Trailing Stop Orders - Investor.gov: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15
- Market by Order (MBO) - CME Group: https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
