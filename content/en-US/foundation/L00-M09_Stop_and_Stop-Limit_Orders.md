# L00-M09 - Stop and Stop-Limit Orders

**Estimated time:** 22 minutes

## Objective
Distinguish a stop trigger from a guaranteed exit price.

## Why it matters
A stop defines when another order activates. It does not guarantee the exact execution price during a gap or rapid move.

## Core ideas
- A stop order generally becomes a market order after the trigger condition is met.
- A stop-limit becomes a limit order after activation.
- A stop may slip but prioritizes execution.
- A stop-limit controls price but can remain unfilled, leaving exposure open.
- Broker and venue rules must be checked because implementation details can differ.

## Scenario
A long position gaps below its stop. The stop activates and sells into the next available bids. A stop-limit might not execute if the market is already below its limit.

## Practice
For a long position, explain the difference between a stop at 98 and a stop-limit with trigger 98 and limit 97.80.

## Knowledge check
- What does a stop order become after activation?
- What does a stop-limit become?
- Which can remain unfilled after activation?

## Common mistake
Calling the stop trigger a guaranteed exit price.

## Evidence classification
Market fact

## Sources
- Stop, Stop-Limit, and Trailing Stop Orders - Investor.gov: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15
- Stop Orders During Volatile Markets - FINRA: https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets
- Futures Order Types - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types