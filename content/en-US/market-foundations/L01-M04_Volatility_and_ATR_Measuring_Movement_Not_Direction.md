# L01-M04 - Volatility and ATR: Measuring Movement, Not Direction

**Estimated time:** 26 minutes

## Objective
Use range and Average True Range as context for movement and risk without treating volatility as a directional forecast.

## Why it matters
Stops, targets, and expectations should account for how much an instrument normally moves. A fixed ten-point stop can be huge in one regime and insignificant in another.

## Core ideas
- Volatility describes the magnitude and variability of price movement.
- True range accounts for the current high-low range and gaps from the previous close.
- ATR averages true range over a selected lookback.
- ATR rises after larger ranges and falls after quieter ranges; it does not predict direction.
- ATR settings depend on timeframe, instrument, and purpose.

## Scenario
Two instruments both trade at 100. One has a daily ATR of 1; the other has a daily ATR of 8. The same two-point stop represents very different market breathing room.

## Practice
Record the current 14-period ATR for one instrument on Daily, 1H, and 5m. Compare your proposed stop distance to each ATR and explain the relevant comparison.

## Knowledge check
- **Does ATR indicate bullish or bearish direction?**
  - No.
- **What does rising ATR suggest?**
  - Recent ranges are expanding.
- **Should ATR be identical across timeframes?**
  - No.

## Common mistake
Buying because ATR rises or using ATR without a structural invalidation level.

## Evidence classification
Indicator definition plus risk-management practice

## Sources
- TradingView Help Center: https://www.tradingview.com/support/
