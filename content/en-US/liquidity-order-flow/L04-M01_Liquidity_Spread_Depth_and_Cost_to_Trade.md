# L04-M01 - Liquidity: Spread, Depth, and Cost to Trade

**Estimated time:** 35 minutes

## Objective
Distinguish liquidity from trading volume and assess spread, displayed depth, order size, and expected execution cost as separate evidence.

## Why it matters
A market can print substantial volume yet still be expensive or difficult to enter and exit at a particular moment. Liquidity must be assessed relative to order size, venue, time, and current conditions.

## Core ideas
- Liquidity is multi-dimensional. Common observable measures include the bid-ask spread, available quantity at price levels, the cost to trade a stated size, and how quickly the book changes after orders and trades.
- Depth is size-specific: a book that can absorb a small order near the best price may still produce material price impact for a larger order.
- Volume records completed trading activity, while displayed depth records resting interest that is currently shown in the order book. They answer different questions.
- Compare liquidity only across equivalent instruments, venues, session windows, data feeds, and order sizes. A raw depth number without these conditions is not decision-grade.
- Displayed liquidity can be added, reduced, executed, or cancelled. Treat it as a current state, not as a promise that the quantity will remain available.

## Scenario
An index future shows a one-tick spread and substantial quantity at the best bid and ask during the main session. Ten minutes before a scheduled release, the spread widens and nearby depth falls. The earlier volume total does not remove the new execution risk.

## Practice
Compare three snapshots of the same instrument: normal session, thin session, and scheduled-event conditions. Record spread, depth within five levels, hypothetical cost to trade two different sizes, and whether the evidence supports participation or no trade.

## Knowledge check
- **Is high traded volume the same as deep current liquidity?** No. Volume is completed activity; depth is displayed resting quantity and can change.
- **Why must order size be stated when assessing liquidity?** Because the expected price impact and cost depend on how much quantity must be executed.
- **What makes two liquidity observations comparable?** The instrument, venue, session, feed, measurement method, and order size should be equivalent.

## Common mistake
Calling a market liquid from the daily volume total while ignoring the current spread, nearby depth, order size, and event conditions.

## Risk note
Wider spreads, thin depth, and unstable books increase slippage and execution uncertainty. Reduce size or choose no trade when risk cannot be bounded.

## Evidence classification
Exchange liquidity methodology and exchange risk education

## Sources
- Understanding the CME Liquidity Tool Methodology - CME Group: https://www.cmegroup.com/education/articles-and-reports/understanding-the-cme-liquidity-tool-methodology
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
