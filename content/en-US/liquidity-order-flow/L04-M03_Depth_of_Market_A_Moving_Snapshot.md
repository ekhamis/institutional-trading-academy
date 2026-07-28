# L04-M03 - Depth of Market: A Moving Snapshot

**Estimated time:** 38 minutes

## Objective
Read a depth-of-market ladder as a time-sensitive display of bids and asks while documenting feed, venue, refresh, and aggregation limitations.

## Why it matters
DOM numbers change continuously. A single screenshot can be useful for observation, but it cannot prove that displayed liquidity will remain, execute, or predict the next move.

## Core ideas
- A DOM displays bid and ask quantities at multiple prices. The visible data comes from a broker, venue, or data provider and may differ from the chart feed.
- Top-of-book shows the best bid and ask; deeper levels show additional displayed quantity. The number of levels and aggregation method depend on the subscription and feed.
- Orders can be added, modified, executed, or cancelled between updates. Read changes over time rather than treating one large number as permanent support or resistance.
- Compare displayed depth with actual trades and subsequent price response. Resting quantity and executed volume are different datasets.
- Stale updates, dropped packets, delayed subscriptions, provider mismatches, and fast markets can make the DOM unsuitable for a controlled decision.

## Scenario
A large offer appears three ticks above price, then repeatedly reduces before price reaches it. Record the additions and cancellations, but do not claim the participant intent. Wait for execution and price-response evidence or choose no trade.

## Practice
Record a 60-second DOM observation at normal speed and around a scheduled event. Note best bid/ask, five-level depth, additions, reductions, trades, and feed status. Explain which conclusions remain unsupported.

## Knowledge check
- **What does the DOM primarily show?** Displayed bid and ask quantities at different prices from the connected data source.
- **Does a large displayed order guarantee that price will stop there?** No. It can execute, change, or cancel.
- **Why compare the DOM with trades?** Because resting orders and executed volume describe different parts of market activity.

## Common mistake
Freezing one DOM snapshot and converting the largest displayed quantity into a guaranteed barrier or directional signal.

## Risk note
Do not execute from stale, delayed, or mismatched depth data. Fast book changes can increase slippage before a manual decision can be acted upon.

## Evidence classification
Official DOM, exchange order-book, and liquidity methodology documentation

## Sources
- Depth of Market (DOM) - TradingView Help Center: https://www.tradingview.com/support/solutions/43000516459-depth-of-market-dom-what-it-is-and-how-traders-can-use-it/
- Understanding the CME Liquidity Tool Methodology - CME Group: https://www.cmegroup.com/education/articles-and-reports/understanding-the-cme-liquidity-tool-methodology
- Market by Order (MBO) - CME Group: https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html
