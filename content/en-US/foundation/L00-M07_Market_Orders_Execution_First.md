# L00-M07 - Market Orders: Execution First

**Estimated time:** 20 minutes

## Objective
Understand what a market order prioritizes and what it cannot guarantee.

## Why it matters
Market orders seek execution against available liquidity. In fast or thin conditions, the actual average price can differ significantly from the expected price.

## Core ideas
- A market order seeks immediate execution against available opposite-side liquidity.
- It offers high execution certainty in normal conditions but no exact price guarantee.
- A large order can fill at several price levels.
- Slippage is the difference between a referenced or expected price and actual execution.

## Scenario
A large buy order enters a thin ask book. The first units fill near the best ask; the remainder consumes higher offers, producing a worse average price.

## Practice
Use the order-book illustration to estimate how a small and a large market order could receive different average fills.

## Knowledge check
- What does a market order prioritize?
- Does it guarantee an exact price?
- Can one order fill at multiple prices?

## Common mistake
Using market orders around high-impact news without considering liquidity and slippage.

## Evidence classification
Market fact

## Sources
- Types of Orders - Investor.gov: https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders
- Order Types - FINRA: https://www.finra.org/investors/investing/investment-products/stocks/order-types
- Futures Order Types - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types