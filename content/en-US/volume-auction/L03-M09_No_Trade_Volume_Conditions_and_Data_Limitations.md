# L03-M09 - No-Trade Volume Conditions and Data Limitations

**Estimated time:** 36 minutes

## Objective
Recognize when volume information is incomplete, incomparable, or too ambiguous to support a trade decision.

## Why it matters
A disciplined volume process includes conditions that stop analysis. Poor data, mismatched sessions, and unstable event conditions can make apparent precision misleading.

## Core ideas
- Volume availability and meaning vary across centralized exchanges, futures contracts, stocks, indices, CFDs, and foreign-exchange feeds.
- Provider changes, missing bars, contract rolls, extended-hours settings, and partial candles can break historical comparisons.
- Scheduled events, opening gaps, and thin liquidity can create extreme readings that need separate treatment.
- When the baseline or data provenance is unclear, the professional decision is to repair the comparison or stand aside.

## Scenario
A CFD chart shows a sudden volume spike after the provider reconnects, while the related futures chart does not. Until the feed and session settings are verified, the spike is not decision-grade evidence.

## Practice
Audit one chart's symbol, venue or provider, session settings, volume type, missing bars, and current-bar status. Write explicit conditions that would make you decline a trade.

## Knowledge check
- **Why can volume differ across feeds?** Venue, instrument, provider, and calculation rules can differ.
- **Should a partial bar be compared directly with completed bars?** Not without accounting for its incomplete state.
- **What is appropriate when data provenance is unclear?** Repair the comparison or stand aside.

## Common mistake
Treating every displayed volume series as complete, centralized, and directly comparable.

## Risk note
No trade is a valid outcome when data cannot support a defensible comparison or structural invalidation.

## Evidence classification
Platform documentation and risk controls

## Sources
- TradingView Help Center, Volume: https://www.tradingview.com/support/solutions/43000591617-volume/
- TradingView Help Center, Relative Volume: https://www.tradingview.com/support/solutions/43000635874-how-do-we-calculate-relative-volume-and-relative-volume-at-time/
- CME Group, Position and Risk Management: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
