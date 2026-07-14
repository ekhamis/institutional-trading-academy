# L03-M12 - Building and Comparing Profile Windows

**Estimated time:** 38 minutes

## Objective
Build and compare volume profiles with explicit, consistent windows while explaining how window selection changes the distribution shown.

## Why it matters
A profile is inseparable from its selected sample. Comparing windows can reveal different historical distributions, but only when the instrument, data, session, and calculation settings are documented.

## Core ideas
- A profile window defines the bars or session whose recorded activity is distributed by price. Changing the window changes the sample and may change every profile feature.
- A fixed-range profile answers a question about a deliberately selected interval, while a session or visible-range profile follows a platform-defined or changing boundary.
- Comparisons are strongest when symbol, provider, volume type, session template, row settings, and calculation method remain consistent.
- Overlapping or unequal windows can answer different questions. Label each boundary and do not present their differences as evidence of participant intent.
- Use completed windows for baseline comparison where possible, then require current price and participation evidence before forming a risk-defined plan.

## Scenario
Two Gold profiles appear different: one covers the full regular session and the other starts after a major data release. Before interpreting the shapes, label the boundaries and rebuild both with a common session and identical settings. The remaining difference is a description of those samples, not proof of who traded or what price must do next.

## Practice
Create one completed-session profile and one fixed-range profile on the same instrument. Document the symbol, provider, volume type, timeframe, session, start and end points, row settings, and calculation method. State what each window can and cannot answer, then finish with either a conditional, risk-defined hypothesis or a justified no-trade conclusion.

## Knowledge check
- **Why can two profiles of the same instrument differ?** They may use different windows, sessions, data, volume types, or calculation settings.
- **What should remain consistent in a controlled comparison?** The symbol, provider, volume type, session template, row settings, and calculation method.
- **Does a chosen window prove participant intent?** No.

## Common mistake
Comparing unlabeled or mismatched profile windows and treating the resulting differences as a predictive signal.

## Risk note
Do not derive an entry, stop, or target from a profile comparison alone. Require current evidence, define invalidation and controlled risk, and stand aside when window selection or data provenance makes the comparison unclear.

## Evidence classification
Official platform calculation documentation

## Sources
- TradingView Help Center, Volume Profile Indicators: Basic Concepts: https://www.tradingview.com/support/solutions/43000502040-volume-profile-indicators-basic-concepts/
- CME Group, Position and Risk Management: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
