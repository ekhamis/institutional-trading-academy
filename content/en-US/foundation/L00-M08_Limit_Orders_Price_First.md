# L00-M08 - Limit Orders: Price First

**Estimated time:** 20 minutes

## Objective
Understand the trade-off between price control and execution uncertainty.

## Why it matters
A limit order protects the permitted price but cannot force another participant to trade with you.

## Core ideas
- A buy limit can execute at the limit price or lower.
- A sell limit can execute at the limit price or higher.
- A limit order can partially fill, remain unfilled, or lose queue priority after modification.
- A historical price touch does not prove that every waiting order filled.

## Scenario
Price touches a learner's buy limit and rises immediately. The learner assumes a fill, but insufficient sell volume reached the order after earlier orders in the queue.

## Practice
Define the execution condition for a buy limit at 99.50 and a sell limit at 101.20. Give one reason each might remain unfilled.

## Knowledge check
- What does a limit order control?
- Is execution guaranteed?
- Can a limit order partially fill?

## Common mistake
Treating every historical touch as a filled limit order in a backtest.

## Evidence classification
Market fact

## Sources
- Types of Orders - Investor.gov: https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders
- Order Types - FINRA: https://www.finra.org/investors/investing/investment-products/stocks/order-types
- Futures Order Types - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types