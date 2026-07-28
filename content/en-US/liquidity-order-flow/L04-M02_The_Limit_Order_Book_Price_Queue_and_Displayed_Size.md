# L04-M02 - The Limit Order Book: Price, Queue, and Displayed Size

**Estimated time:** 38 minutes

## Objective
Explain how displayed limit orders are organized by price and priority, and distinguish price-level summaries from individual-order data.

## Why it matters
A depth ladder compresses a changing queue into numbers. Understanding what the feed contains prevents false claims about participant identity, queue position, or guaranteed execution.

## Core ideas
- A central limit order book organizes executable bids and offers by price. Orders at the same price are then handled according to the venue and product matching algorithm.
- Market-by-price data aggregates quantity and order count at each price level. Market-by-order data can expose anonymous individual orders, full depth, and queue information, but not customer identity.
- Price-time priority is common in some products, but matching rules can also include pro-rata, size-priority, or hybrid allocation. Never assume universal first-in-first-out behavior.
- Queue position affects the probability and timing of a resting order fill. A displayed quantity ahead of an order can execute, cancel, or change before the market reaches the price.
- Iceberg, synthetic, implied, hidden, and cross-venue interest can make the visible book an incomplete representation of total trading interest.

## Scenario
Two traders place limit buys at the same price. One feed shows only total quantity at that level; another provides anonymous order-level records. Even with order-level data, the product matching algorithm must be known before estimating priority.

## Practice
For one futures contract, document whether the feed is market-by-price or market-by-order, the number of levels shown, the matching algorithm, and what queue information is and is not available. Finish with three statements you are not entitled to make from the display.

## Knowledge check
- **Does market-by-price data show each individual order?** No. It normally aggregates quantity and order count by price level.
- **Is every electronic market matched strictly by price-time priority?** No. Matching algorithms vary by venue and product.
- **Does an anonymous order ID reveal the customer behind the order?** No. Order-level transparency does not provide customer identity.

## Common mistake
Treating the displayed quantity at a price as one participant, assuming FIFO without checking the product rules, or claiming a known fill from an estimated queue.

## Risk note
A resting order can remain unfilled, partially fill, or fill during fast movement. Plan for queue uncertainty and do not use displayed depth as a guaranteed exit.

## Evidence classification
Official exchange market-by-order and matching-algorithm documentation

## Sources
- Market by Order (MBO) - CME Group: https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html
- How CME Group Ag Markets Operate - Matching Algorithms: https://www.cmegroup.com/education/articles-and-reports/overview-what-makes-ags-markets-work
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
