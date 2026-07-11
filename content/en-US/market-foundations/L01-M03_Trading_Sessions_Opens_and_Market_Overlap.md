# L01-M03 - Trading Sessions, Opens, and Market Overlap

**Estimated time:** 25 minutes

## Objective
Recognize how exchange hours, regional sessions, and overlaps influence liquidity and volatility.

## Why it matters
Participation is not evenly distributed across the day. A strategy tested during a liquid open may behave very differently during a quiet period or extended hours.

## Core ideas
- Cash equities trade around an exchange-defined regular session, with separate pre-market and after-hours conditions where available.
- Futures and foreign exchange may trade for longer hours, but liquidity still changes by time of day.
- Session opens can reprice markets as new participants and information arrive.
- Overlaps may increase activity, while off-hours can bring wider spreads and thinner depth.
- Daylight-saving changes can shift local clock times relative to another region.

## Scenario
A stock has a narrow spread during the main US session but a much wider spread after hours. The chart still prints prices, yet execution quality and available liquidity are different.

## Practice
Build a session table for your local timezone with London open, New York cash open, and the London-New York overlap. Add a daylight-saving reminder.

## Knowledge check
- **Is liquidity constant throughout the day?**
  - No.
- **Why can extended hours be riskier?**
  - Lower liquidity, wider spreads, and higher volatility can occur.
- **Do long trading hours guarantee deep liquidity at every moment?**
  - No.

## Common mistake
Backtesting at one session and trading the same rules at every hour.

## Evidence classification
Market fact plus risk-management practice

## Sources
- Extended-Hours Trading: Know the Risks - FINRA: https://www.finra.org/investors/insights/extended-hours-trading
- Trading Terms: Time Parameters and Qualifiers - FINRA: https://www.finra.org/investors/insights/time-parameters-qualifiers-stock-orders
