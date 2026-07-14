# L03-M15 - High- and Low-Volume Nodes

**Estimated time:** 40 minutes

## Objective
Identify high- and low-volume nodes in a documented volume-profile sample and use them as descriptive context without treating either node type as a guaranteed trade level.

## Why it matters
Nodes show where a selected profile records relatively more or less activity by price. They can help describe the shape of that historical distribution, but their location depends on the sample and settings and does not predict future price behavior.

## Core ideas
- A high-volume node, or HVN, is a price region where the selected profile records relatively high activity compared with nearby rows. A low-volume node, or LVN, records relatively low activity compared with nearby rows.
- HVNs and LVNs are relative features of a particular distribution, not universal thresholds. The symbol, venue, provider, volume type, profile window, session, row size, and allocation method can change their shape and location.
- A node describes completed activity by price. It does not reveal participant intent or prove fair value, acceptance, rejection, support, resistance, a price magnet, or a fast-travel zone.
- Observe current price response and participation before forming a hypothesis. Similar-looking nodes can produce different outcomes in different structural and volatility contexts.
- If the node is poorly defined, the data is incomplete, settings are inconsistent, or current evidence is mixed, no trade is a valid conclusion.

## Scenario
A completed index-futures session profile contains one broad HVN and a thin LVN above it. During the next session, price approaches the LVN. Record the node and the current price-and-volume response without assuming that price must accelerate, reverse, or return to the HVN. Require structural confirmation, predefined invalidation, and controlled risk before considering a plan.

## Practice
Mark the clearest HVN and LVN on three completed profiles of the same instrument using consistent settings. Document the provider, volume type, window, session, row size, and allocation method. For each sample, separate the historical node observation from any later interpretation, then finish with either a conditional, risk-defined hypothesis or a justified no-trade conclusion.

## Knowledge check
- **What distinguishes an HVN from an LVN?** An HVN records relatively high activity compared with nearby profile rows, while an LVN records relatively low activity in the selected sample.
- **Can changing the profile window or row size move the nodes?** Yes.
- **Does an LVN guarantee fast movement or an HVN guarantee support, resistance, or a return?** No.

## Common mistake
Converting a descriptive node into an automatic entry, stop, target, support, resistance, price magnet, or fast-travel prediction.

## Risk note
Do not derive a trade from an HVN or LVN alone. Verify the dataset and settings, require current price, participation, and structural evidence, define invalidation and controlled risk, and stand aside when the node or response is unclear.

## Evidence classification
Official platform calculation documentation

## Sources
- TradingView Help Center, Volume Profile Indicators: Basic Concepts: https://www.tradingview.com/support/solutions/43000502040-volume-profile-indicators-basic-concepts/
- CME Group, Position and Risk Management: https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/position-and-risk-management
