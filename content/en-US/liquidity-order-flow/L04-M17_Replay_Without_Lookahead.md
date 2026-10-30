# L04-M17 - Replay Without Lookahead

## Objective
Evaluate replay without lookahead using reproducible observations and a conditional risk decision.

## Worked synthetic example
Pause at 09:35, record a plan, then reveal the 09:36 bar. The later high is unavailable at decision time.

## Interpretation and alternatives
- Save the decision timestamp, visible data window, settings and written conditional plan before revealing the outcome.
- A chart screenshot taken afterward can contain hindsight labels. Mark which evidence was genuinely available at the pause.
- Discard a trial if future bars or outcomes were seen before recording the decision.
- All numeric examples are synthetic and must not be interpreted as historical performance.

## Practice
Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.

## Answer rationale
- What does the worked case establish? Save the decision timestamp, visible data window, settings and written conditional plan before revealing the outcome.
- What cancels or limits the interpretation? Discard a trial if future bars or outcomes were seen before recording the decision.
- Does this example establish a profitable strategy? No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.

## Sources
- [Replay Chart - Sierra Chart](https://www.sierrachart.com/index.php?page=doc/ReplayChart.html)
