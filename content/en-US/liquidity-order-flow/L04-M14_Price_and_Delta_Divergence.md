# L04-M14 - Price and Delta Divergence

## Objective
Evaluate price and delta divergence using reproducible observations and a conditional risk decision.

## Worked synthetic example
Price highs move from 5000 to 5002 while comparable-window delta falls from +600 to +200.

## Interpretation and alternatives
- Price and delta are not obliged to move together. Passive liquidity and different volume distributions can explain divergence.
- Use the same contract, venue, session boundaries and classification method. Do not compare estimated spot/CFD delta with exchange futures delta as identical evidence.
- Accepted higher prices can invalidate a bearish interpretation despite divergence.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? Price and delta are not obliged to move together. Passive liquidity and different volume distributions can explain divergence.
- What cancels or limits the interpretation? Accepted higher prices can invalidate a bearish interpretation despite divergence.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Cumulative AskVolume and BidVolume Difference Bars - Sierra Chart Documentation](https://www.sierrachart.com/index.php?page=doc%2Fhelpdetails71.html)
- [Numbers Bars - Sierra Chart Documentation](https://www.sierrachart.com/index.php?page=doc%2FNumbersBars.php)
