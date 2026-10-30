# L04-M13 - Stacked Imbalances

## Objective
Evaluate stacked imbalances using reproducible observations and a conditional risk decision.

## Worked synthetic example
Three consecutive diagonal ask/bid comparisons are 120/30, 150/40 and 90/20. The test ratio is 3 and minimum numerator is 80.

## Interpretation and alternatives
- The ratios are 4, 3.75 and 4.5, so all three satisfy this explicitly defined synthetic rule.
- Platform diagonal conventions, zero handling, tick grouping and minimum-volume filters change results. A stack describes a calculation, not a profitable entry.
- Require contextual acceptance; cancel if price returns through the tested area or the settings cannot be reproduced.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? The ratios are 4, 3.75 and 4.5, so all three satisfy this explicitly defined synthetic rule.
- What cancels or limits the interpretation? Require contextual acceptance; cancel if price returns through the tested area or the settings cannot be reproduced.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Numbers Bars - Sierra Chart Documentation](https://www.sierrachart.com/index.php?page=doc%2FNumbersBars.php)
