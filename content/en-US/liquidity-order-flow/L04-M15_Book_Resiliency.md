# L04-M15 - Book Resiliency

## Objective
Evaluate book resiliency using reproducible observations and a conditional risk decision.

## Worked synthetic example
Displayed depth falls from 400 to 100 after a trade burst, then recovers to 300 after 500 milliseconds.

## Interpretation and alternatives
- The observed recovery is 200 contracts in 500 milliseconds; it does not show that the same participant replenished.
- Separate cancellations, additions and executions. Timestamp resolution and feed gaps can invalidate a recovery-time estimate.
- Avoid execution when spread and depth fail to recover within the predefined observation window.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? The observed recovery is 200 contracts in 500 milliseconds; it does not show that the same participant replenished.
- What cancels or limits the interpretation? Avoid execution when spread and depth fail to recover within the predefined observation window.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Market by Order (MBO) - CME Group](https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html)
