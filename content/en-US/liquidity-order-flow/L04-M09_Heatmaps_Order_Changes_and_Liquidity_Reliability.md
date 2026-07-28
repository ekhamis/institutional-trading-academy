# L04-M09 - Heatmaps, Order Changes, and Liquidity Reliability

**Estimated time:** 45 minutes

## Objective
Use an order-book heatmap to observe displayed liquidity through time while avoiding unsupported conclusions about permanence, intent, or spoofing.

## Why it matters
A heatmap preserves the history of visible order-book changes that a single DOM snapshot loses. It still shows displayed orders, not private intent, and the result depends on feed depth, latency, and aggregation.

## Core ideas
- An order-book heatmap maps displayed quantity by price and time. Greater visual intensity normally represents more displayed resting liquidity in the chosen feed.
- Because the display retains history, the learner can observe where quantity was added, reduced, cancelled, executed against, or left untouched as price approached.
- An order cancellation is not automatically deceptive. Legitimate orders are routinely modified or cancelled as conditions change.
- Spoofing is a legal and intent-based concept: bidding or offering with the intent to cancel before execution. A chart pattern alone does not establish that intent.
- Feed depth, aggregation, hidden orders, venue coverage, latency, and replay reconstruction can make heatmaps incomparable. Validate settings and combine them with trades and price response.

## Scenario
A bright offer band appears, moves away twice, and disappears before price reaches it. The heatmap proves displayed changes in the chosen feed, but not why they occurred. Record the sequence and avoid accusing a participant or predicting direction.

## Practice
Replay five heatmap events. Separate displayed additions, reductions, executions, and price response; document feed limitations; and write one neutral interpretation plus one reason to choose no trade.

## Knowledge check
- **What does heatmap intensity normally represent?** The amount of displayed resting liquidity at a price in the selected feed.
- **Is every cancelled order spoofing?** No. Spoofing depends on intent to cancel before execution and broader facts and circumstances.
- **What should accompany a heatmap observation?** Feed and setting documentation, executed trades, price response, structure, and risk.

## Common mistake
Calling every disappearing order spoofing or treating every bright band as guaranteed support or resistance.

## Risk note
Displayed liquidity can vanish faster than a manual response. Do not rely on a heatmap band as the sole exit or invalidation mechanism.

## Evidence classification
Official heatmap explanation, exchange order-book documentation, and CFTC spoofing guidance

## Sources
- Heatmap in Trading: Market Depth Visualization - Bookmap: https://bookmap.com/blog/heatmap-in-trading-the-complete-guide-to-market-depth-visualization
- Market by Order (MBO) - CME Group: https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html
- CFTC Interpretive Guidance on Disruptive Practices and Spoofing: https://www.cftc.gov/LawRegulation/FederalRegister/FinalRules/2013-12365.html
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
