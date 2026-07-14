# L03-M11 - Volume Profile Maps Activity by Price

**Estimated time:** 36 minutes

## Objective
Explain how a volume profile distributes recorded activity across price levels for a defined dataset and window without treating the profile as a forecast.

## Why it matters
Time-based volume bars show when activity occurred. A volume profile reorganizes the selected data to show where activity accumulated by price, giving a different descriptive view of the same market history.

## Core ideas
- A volume profile is a histogram of recorded activity at price levels across a selected symbol, data source, and window.
- The profile describes where activity occurred in the selected historical sample; it does not reveal participant intent or predict the next move.
- Rows, lower-timeframe inputs, session boundaries, and the platform's volume type can change the displayed distribution.
- Stocks may use trade volume while some indices, forex feeds, and CFDs use tick volume, so provenance must be checked before comparison.
- Profile features are contextual references, not guaranteed support, resistance, entries, stops, or targets.

## Scenario
Gold shows a broad concentration of activity near the middle of a completed session and little activity near its high. Record the distribution as an observation, then require fresh price and participation evidence before considering any plan.

## Practice
Build profiles for two completed sessions of the same instrument using identical settings. Record the window, session, data source, row settings, and observed concentrations. Finish with either a risk-defined hypothesis or a justified no-trade conclusion.

## Knowledge check
- **What does a volume profile organize?** Recorded activity by price for a defined dataset and window.
- **Does a high-activity price guarantee future support or resistance?** No.
- **Which settings must be documented?** Instrument, data source, window, session, volume type, and profile calculation settings.

## Common mistake
Treating a historical concentration of activity as proof of intent or a guaranteed future reaction.

## Risk note
Do not place an entry, stop, or target from a profile feature alone. Require current price evidence, define invalidation and controlled risk, and stand aside when the data or response is unclear.

## Evidence classification
Official platform calculation documentation

## Sources
- TradingView Help Center, Volume Profile Indicators: Basic Concepts: https://www.tradingview.com/support/solutions/43000502040-volume-profile-indicators-basic-concepts/
- CME Group, Position and Risk Management: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
