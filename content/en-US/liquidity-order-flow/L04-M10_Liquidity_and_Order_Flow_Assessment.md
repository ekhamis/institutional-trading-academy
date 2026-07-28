# L04-M10 - Liquidity and Order Flow Assessment

**Estimated time:** 60 minutes

## Objective
Demonstrate a reproducible liquidity and order-flow review that separates resting orders, executed trades, estimates, interpretations, and risk decisions.

## Why it matters
Order-flow tools create dense and persuasive displays. A passing assessment must prove that the learner understands the data pipeline and can decline a trade when evidence or execution quality is insufficient.

## Core ideas
- Audit the instrument, venue, contract, session, feed, depth level, latency status, bar construction, footprint classification, delta method, CVD anchor, and heatmap settings before interpretation.
- Separate displayed resting orders, executed trades, estimated classifications, price structure, and narrative interpretation into distinct evidence categories.
- Use DOM and heatmap changes to describe displayed liquidity; use footprint, delta, and CVD to describe classified executions. Do not treat either dataset as participant identity or intent.
- A passing conditional plan states confirmation, structural invalidation, expected execution risk, maximum loss, and evidence that cancels the idea. Tool agreement is not a substitute for these controls.
- Choose no trade when feeds are stale or mismatched, methods are incomparable, visible liquidity is unstable, confirmation is late, or slippage and invalidation cannot be bounded.

## Scenario
You receive a futures DOM and heatmap, a true bid/ask footprint, an estimated CVD from another platform, and a CFD chart for the same underlying theme. The tools appear to agree directionally, but the venues and methods differ. Audit comparability before deciding whether any plan is valid.

## Practice
Complete two assessment cases. For each, submit a data-provenance sheet, observation-versus-interpretation table, liquidity and execution review, structure map, confirmation and invalidation plan, risk statement, and final conditional-trade or no-trade decision.

## Knowledge check
- **What is the first task in an order-flow assessment?** Audit the instrument, venue, feed, data method, session, and settings.
- **Can agreement among DOM, footprint, and CVD replace risk controls?** No. Confirmation, invalidation, execution risk, and maximum loss remain mandatory.
- **Can no trade receive a passing assessment?** Yes, when data, comparability, timing, liquidity, or risk limitations are correctly identified and justified.

## Common mistake
Passing the assessment by showing several colourful tools that appear aligned while ignoring data provenance, method differences, slippage, and invalidation.

## Risk note
Order-flow evidence does not remove loss risk. Protect capital when the data pipeline, execution conditions, or structural invalidation is not decision-grade.

## Evidence classification
Competency assessment based on official exchange, regulator, and platform documentation

## Sources
- Understanding the CME Liquidity Tool Methodology - CME Group: https://www.cmegroup.com/education/articles-and-reports/understanding-the-cme-liquidity-tool-methodology
- Market by Order (MBO) - CME Group: https://www.cmegroup.com/articles/faqs/market-by-order-mbo.html
- Volume Footprint Charts: A Complete Guide - TradingView Help Center: https://www.tradingview.com/support/solutions/43000726164-volume-footprint-charts-a-complete-guide/
- Cumulative AskVolume and BidVolume Difference Bars - Sierra Chart Documentation: https://www.sierrachart.com/index.php?page=doc%2Fhelpdetails71.html
- CFTC Interpretive Guidance on Disruptive Practices and Spoofing: https://www.cftc.gov/LawRegulation/FederalRegister/FinalRules/2013-12365.html
- Position and Risk Management - CME Group: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
