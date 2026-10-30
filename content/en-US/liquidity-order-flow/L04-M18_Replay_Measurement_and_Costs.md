# L04-M18 - Replay Measurement and Costs

## Objective
Evaluate replay measurement and costs using reproducible observations and a conditional risk decision.

## Worked synthetic example
A synthetic trade earns 10 gross ticks; fees equal 2 ticks and modeled slippage is 3 ticks.

## Interpretation and alternatives
- Net result is 5 ticks. Cost assumptions must match size, instrument and execution conditions; a replay fill is not proof of a live fill.
- Select sessions before viewing outcomes, retain losses and no-trades, separate development from held-out evaluation, and report sample size and uncertainty.
- Stop evaluation if fills are modeled from unavailable depth or if the test set influenced parameter selection.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? Net result is 5 ticks. Cost assumptions must match size, instrument and execution conditions; a replay fill is not proof of a live fill.
- What cancels or limits the interpretation? Stop evaluation if fills are modeled from unavailable depth or if the test set influenced parameter selection.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Replay Chart - Sierra Chart](https://www.sierrachart.com/index.php?page=doc/ReplayChart.html)
- [Position and Risk Management - CME Group](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management)
