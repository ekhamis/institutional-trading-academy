# L04-M19 - Advanced No-Trade Conditions

## Objective
Evaluate advanced no-trade conditions using reproducible observations and a conditional risk decision.

## Worked synthetic example
A depth feed is 2 seconds stale during a burst while the price feed updates every 100 milliseconds.

## Interpretation and alternatives
- A stale depth snapshot and current price are not a synchronized order-flow view. Restore and verify timestamps before interpreting.
- No trade is justified for missing history, inconsistent sessions, unsuitable venue comparisons, late confirmation or unbounded execution cost.
- Resume observation only after the original data and risk conditions can be verified again.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? A stale depth snapshot and current price are not a synchronized order-flow view. Restore and verify timestamps before interpreting.
- What cancels or limits the interpretation? Resume observation only after the original data and risk conditions can be verified again.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Market by Order (MBO) - CME Group](https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html)
- [Position and Risk Management - CME Group](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management)
