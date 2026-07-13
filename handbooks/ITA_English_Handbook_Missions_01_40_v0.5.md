# ITA English Handbook - Missions 01-40

Version 0.5.0

## L00-M01 - Why Markets Exist

**Objective:** Explain the economic purpose of financial markets before learning how to trade them.

**Why it matters:** A learner who sees a market only as a place to win money will misunderstand nearly every later concept. Markets help transfer ownership, allocate capital, manage risk, and discover prices.

**Core ideas:**
- Primary markets connect issuers with capital; secondary markets let existing claims change hands.
- Futures and derivatives can transfer price risk between participants with different needs.
- The displayed price is the latest result of interacting orders, not a promise about the future.

**Practice:** Write one sentence explaining how an airline, a pension fund, and a short-term trader might each use a financial market.

**Common mistake:** Treating the market as a machine designed to pay traders.

## L00-M02 - Investing, Trading, Speculation, and Gambling

**Objective:** Distinguish activities by decision process rather than by holding period or outcome.

**Why it matters:** A short holding period does not automatically make an activity gambling. The important differences are evidence, risk limits, repeatability, and whether the decision has a rational basis.

**Core ideas:**
- Investing usually seeks participation in longer-term economic value or cash flows.
- Trading seeks to manage a shorter-term opportunity with a defined thesis, invalidation, and risk.
- Speculation accepts uncertainty in pursuit of gain and can be disciplined or reckless.
- Gambling behavior appears when hope, excitement, or uncontrolled size replaces a tested process.

**Practice:** Classify three past market decisions as investment, disciplined trade, or gambling behavior. Explain each classification without referring to whether it made money.

**Common mistake:** Judging decision quality only by the profit or loss.

## L00-M03 - Who Participates in Markets?

**Objective:** Identify major participant groups and understand why their motives differ.

**Why it matters:** A hedge, an investment, a market-making action, and a speculative trade can produce similar transactions for very different reasons.

**Core ideas:**
- Hedgers seek to reduce an existing commercial or portfolio risk.
- Speculators intentionally accept price risk in pursuit of profit.
- Investors allocate capital according to longer-term objectives.
- Market makers quote prices and manage inventory risk.
- Brokers provide customer access and route or execute orders.
- Exchanges and clearing systems establish rules, matching, and post-trade obligations.

**Practice:** Create a two-column table: participant and likely objective. Include a bank, pension fund, airline, market maker, day trader, and central bank.

**Common mistake:** Assuming every large transaction is directional speculation.

## L00-M04 - Exchanges, Brokers, Clearing, and Settlement

**Objective:** Trace a transaction from the learner's instruction through execution and settlement.

**Why it matters:** A platform makes execution look instant, but legal relationships, routing, matching or dealer execution, clearing, and settlement sit behind a click.

**Core ideas:**
- A broker receives the client instruction and provides market access.
- An exchange or trading venue applies its rules and matches compatible orders.
- Clearing manages obligations and counterparty risk according to the market structure.
- Settlement completes the transfer of cash and the financial instrument.
- CFDs, exchange-traded futures, and shares can have materially different execution and legal structures.

**Practice:** Draw the transaction path for one exchange-traded share order and one OTC CFD order. Highlight where their structures differ.

**Common mistake:** Assuming all instruments and brokers use the same execution model.

## L00-M05 - Bid, Ask, and the Last Traded Price

**Objective:** Differentiate the last traded price from current executable quotations.

**Why it matters:** The last price shown on a chart is not automatically available for a new order.

**Core ideas:**
- The bid is the highest displayed price a buyer is currently willing to pay.
- The ask is the lowest displayed price a seller is currently willing to accept.
- The last price records a completed transaction and may no longer be available.
- Quotes can change before an order reaches the market.
- Different venues, data feeds, instruments, and brokers can display slightly different prices.

**Practice:** On a demo platform, record bid, ask, spread, and last price five times during an active session.

**Common mistake:** Using the last candle close as a guaranteed execution price.

## L00-M06 - The Bid-Ask Spread and Liquidity

**Objective:** Explain the spread as an immediate cost and a partial clue about liquidity.

**Why it matters:** An aggressive buyer crosses to the ask and an aggressive seller crosses to the bid. This matters especially in frequent trading and thin markets.

**Core ideas:**
- Spread equals best ask minus best bid.
- Tighter spreads often accompany liquid conditions, but top-of-book size alone does not fully describe liquidity.
- Spreads can widen around news, session changes, quiet hours, or stress.
- Total transaction cost may include spread, commission, fees, financing, and slippage.

**Practice:** Compare the spread of the same instrument during its primary session and during a quiet period. Record the difference and possible reason.

**Common mistake:** Backtesting without realistic spread and transaction-cost assumptions.

## L00-M07 - Market Orders: Execution First

**Objective:** Understand what a market order prioritizes and what it cannot guarantee.

**Why it matters:** Market orders seek execution against available liquidity. In fast or thin conditions, the actual average price can differ significantly from the expected price.

**Core ideas:**
- A market order seeks immediate execution against available opposite-side liquidity.
- It offers high execution certainty in normal conditions but no exact price guarantee.
- A large order can fill at several price levels.
- Slippage is the difference between a referenced or expected price and actual execution.

**Practice:** Use the order-book illustration to estimate how a small and a large market order could receive different average fills.

**Common mistake:** Using market orders around high-impact news without considering liquidity and slippage.

## L00-M08 - Limit Orders: Price First

**Objective:** Understand the trade-off between price control and execution uncertainty.

**Why it matters:** A limit order protects the permitted price but cannot force another participant to trade with you.

**Core ideas:**
- A buy limit can execute at the limit price or lower.
- A sell limit can execute at the limit price or higher.
- A limit order can partially fill, remain unfilled, or lose queue priority after modification.
- A historical price touch does not prove that every waiting order filled.

**Practice:** Define the execution condition for a buy limit at 99.50 and a sell limit at 101.20. Give one reason each might remain unfilled.

**Common mistake:** Treating every historical touch as a filled limit order in a backtest.

## L00-M09 - Stop and Stop-Limit Orders

**Objective:** Distinguish a stop trigger from a guaranteed exit price.

**Why it matters:** A stop defines when another order activates. It does not guarantee the exact execution price during a gap or rapid move.

**Core ideas:**
- A stop order generally becomes a market order after the trigger condition is met.
- A stop-limit becomes a limit order after activation.
- A stop may slip but prioritizes execution.
- A stop-limit controls price but can remain unfilled, leaving exposure open.
- Broker and venue rules must be checked because implementation details can differ.

**Practice:** For a long position, explain the difference between a stop at 98 and a stop-limit with trigger 98 and limit 97.80.

**Common mistake:** Calling the stop trigger a guaranteed exit price.

## L00-M10 - Risk, Leverage, and Survival

**Objective:** Explain why controlled exposure and survival come before strategy optimization.

**Why it matters:** A valid analysis can still produce a loss. Excessive size converts ordinary uncertainty into account-threatening damage.

**Core ideas:**
- Risk is uncertainty that can negatively affect capital or financial welfare.
- Leverage creates exposure larger than the cash committed.
- Margin is collateral, not the maximum possible loss.
- Position size should come from acceptable account risk and the distance to invalidation, not the maximum leverage offered.
- A professional plan sets per-trade and daily loss limits before considering targets.

**Practice:** For a EUR 10,000 account, calculate the cash amount represented by 0.25%, 0.5%, 1%, and 2%. Explain which is more appropriate for a novice simulation plan and why.

**Common mistake:** Choosing the position size first and forcing the stop to fit afterward.

## L01-M01 - Candlesticks and OHLC: What One Bar Actually Says

**Objective:** Read open, high, low, and close values without attaching unsupported stories to a candle shape.

**Why it matters:** Candles compress a period of trading into four prices. They are useful summaries, but a candle does not reveal every order, participant, or reason behind the move.

**Core ideas:**
- The open is the first recorded price for the selected interval; the close is the last recorded price for that interval.
- The high and low mark the interval extremes.
- A candle body shows the distance between open and close; wicks show prices traded beyond the body.
- The same market move appears differently when the timeframe changes.
- A single candle is evidence of price movement, not a complete trading signal.

**Practice:** Draw a candle for O=50, H=55, L=48, C=53. Then redraw the same values when C=49. Label every component.

**Common mistake:** Memorizing candle names while ignoring location, timeframe, and context.

## L01-M02 - Timeframes and Multi-Timeframe Context

**Objective:** Explain how higher and lower timeframes answer different questions without letting a small chart override broader context.

**Why it matters:** A market can be rising on the daily chart, correcting on the hourly chart, and rallying on the five-minute chart at the same time. These statements can all be true.

**Core ideas:**
- Higher timeframes compress more trading and usually define broader structure.
- Lower timeframes reveal execution detail but contain more noise.
- Analysis should assign a purpose to each timeframe: context, setup, or trigger.
- A lower-timeframe reversal may be only a pullback inside a higher-timeframe trend.
- Timeframe selection should match the expected holding period and risk plan.

**Practice:** Create a three-row plan using Daily for context, 1H for setup, and 5m for execution. Write one question each timeframe must answer.

**Common mistake:** Changing timeframe until a preferred trade appears.

## L01-M03 - Trading Sessions, Opens, and Market Overlap

**Objective:** Recognize how exchange hours, regional sessions, and overlaps influence liquidity and volatility.

**Why it matters:** Participation is not evenly distributed across the day. A strategy tested during a liquid open may behave very differently during a quiet period or extended hours.

**Core ideas:**
- Cash equities trade around an exchange-defined regular session, with separate pre-market and after-hours conditions where available.
- Futures and foreign exchange may trade for longer hours, but liquidity still changes by time of day.
- Session opens can reprice markets as new participants and information arrive.
- Overlaps may increase activity, while off-hours can bring wider spreads and thinner depth.
- Daylight-saving changes can shift local clock times relative to another region.

**Practice:** Build a session table for your local timezone with London open, New York cash open, and the London-New York overlap. Add a daylight-saving reminder.

**Common mistake:** Backtesting at one session and trading the same rules at every hour.

## L01-M04 - Volatility and ATR: Measuring Movement, Not Direction

**Objective:** Use range and Average True Range as context for movement and risk without treating volatility as a directional forecast.

**Why it matters:** Stops, targets, and expectations should account for how much an instrument normally moves. A fixed ten-point stop can be huge in one regime and insignificant in another.

**Core ideas:**
- Volatility describes the magnitude and variability of price movement.
- True range accounts for the current high-low range and gaps from the previous close.
- ATR averages true range over a selected lookback.
- ATR rises after larger ranges and falls after quieter ranges; it does not predict direction.
- ATR settings depend on timeframe, instrument, and purpose.

**Practice:** Record the current 14-period ATR for one instrument on Daily, 1H, and 5m. Compare your proposed stop distance to each ATR and explain the relevant comparison.

**Common mistake:** Buying because ATR rises or using ATR without a structural invalidation level.

## L01-M05 - Gaps, Repricing, and the Market Open

**Objective:** Identify a gap and distinguish the observation from assumptions about whether it must fill.

**Why it matters:** A gap can reflect new information or a discontinuity between sessions. Traders often turn the visible space into a rule that price must return, but no such guarantee exists.

**Core ideas:**
- A gap appears when the next traded range does not overlap a prior reference range.
- Stocks commonly gap after earnings or news outside the regular session.
- Futures can show weekend or session gaps depending on chart settings and trading hours.
- A gap may fill, partially fill, or remain open.
- The opening auction and early liquidity can produce rapid repricing and slippage.

**Practice:** Find three historical gaps. Label the catalyst if known, initial direction, maximum extension, whether the gap filled, and how long that took.

**Common mistake:** Trading against every gap because “all gaps fill.”

## L01-M06 - Stocks, ETFs, Futures, Forex, and CFDs

**Objective:** Compare major instrument types by ownership, contract structure, trading venue, leverage, expiry, and counterparty risk.

**Why it matters:** A symbol that tracks the S&P 500 may represent an ETF share, a futures contract, a CFD, or another derivative. Similar-looking charts do not mean identical rights, costs, or risks.

**Core ideas:**
- A stock represents an ownership interest in a company.
- An ETF is a pooled product whose shares trade on an exchange and may track a basket or strategy.
- A futures contract is a standardized agreement with defined terms and an expiry or settlement process.
- Retail forex commonly involves leveraged over-the-counter trading through a dealer or broker.
- A CFD is a broker-provided derivative in permitted jurisdictions; the learner must understand local regulation and counterparty terms.

**Practice:** Create a comparison matrix for SPY, ES futures, and one broker’s index CFD. Include ownership, expiry, minimum size, spread/commission, financing, market hours, and regulator.

**Common mistake:** Choosing an instrument only because its chart looks familiar.

## L01-M07 - Chart Platforms, Brokers, and Data Feeds

**Objective:** Describe the path from venue and data vendor to chart platform and broker execution.

**Why it matters:** The chart, broker, and underlying exchange can be separate systems. Small differences in symbols, feeds, sessions, and aggregation can produce different candles and indicator values.

**Core ideas:**
- A charting platform displays data obtained from one or more providers.
- A broker routes or internalizes orders according to its execution model and product.
- The same market can have multiple symbols, contract months, composite feeds, or broker-specific prices.
- Session settings and adjusted data can change historical candles.
- Platform tools should support analysis; they do not guarantee execution quality.

**Practice:** For one instrument, record platform, symbol, exchange or broker, data status, timezone, session setting, and whether the series is adjusted or continuous.

**Common mistake:** Assuming every symbol with the same nickname is the same product.

## L01-M08 - Real-Time, Delayed, and Historical Data

**Objective:** Verify whether a chart is real-time, delayed, replayed, or historical before making a time-sensitive decision.

**Why it matters:** A clean chart is not necessarily current. Exchanges may require separate market-data permissions, and platforms can display delayed or vendor-dependent information.

**Core ideas:**
- Real-time data is delivered with minimal distribution delay under the relevant entitlement.
- Delayed data can be suitable for education but unsuitable for live execution decisions.
- Historical and replay modes deliberately show past data.
- Bid/ask data, last-trade data, and indicative prices are different information types.
- Data quality checks belong in every trading checklist.

**Practice:** Audit five symbols on your platform. Record feed source, delay indicator, exchange entitlement, last-trade time, and comparison with your execution venue.

**Common mistake:** Assuming a moving screen equals exchange-grade real-time data.

## L01-M09 - Economic Calendars, Scheduled Risk, and News

**Objective:** Use official release schedules to identify event risk without pretending to know the market reaction in advance.

**Why it matters:** Employment, inflation, growth, and central-bank decisions can sharply change volatility, spreads, and liquidity. The release time is knowable; the size and direction of the reaction are not.

**Core ideas:**
- An economic calendar lists scheduled releases and events.
- Official statistical agencies and central banks are primary sources for timing and published data.
- Consensus forecasts are estimates, not facts.
- A release can cause slippage, spread expansion, and rapid two-way movement.
- The correct response may be reduced size, wider planned risk, waiting, or no trade.

**Practice:** Build tomorrow’s event-risk sheet using official sources. Include release time, affected markets, expected volatility window, and your rule for trading or standing aside.

**Common mistake:** Treating the “high impact” label as a guaranteed direction.

## L01-M10 - Foundation Assessment: Read the Market Screen

**Objective:** Demonstrate that you can identify what is on a trading screen before analyzing direction or placing a trade.

**Why it matters:** Most avoidable beginner errors occur before strategy: wrong symbol, wrong session, wrong timeframe, delayed data, misunderstood product, or unrecognized event risk.

**Core ideas:**
- Identify the instrument and legal product.
- Confirm venue or broker, contract month if relevant, and price currency.
- Confirm timeframe, timezone, session, and data status.
- Read OHLC and current volatility context.
- Check scheduled event risk and define a no-trade condition.

**Practice:** Complete the Market Screen Verification Checklist for three instruments: SPY, a DAX futures contract, and a gold CFD. Then explain which comparisons are valid and which are not.

**Common mistake:** Starting with pattern recognition before confirming the screen itself.

## L02-M01 - Swing Highs and Swing Lows

**Objective:** Identify swing highs and swing lows without forcing structure onto every candle.

**Why it matters:** Market structure starts with objective turning points. If a learner cannot mark meaningful swings, every later concept such as trend, pullback, BOS, and CHoCH becomes subjective.

**Core ideas:**
- A swing high is a local turning point where buying failed to continue and price rotated lower.
- A swing low is a local turning point where selling failed to continue and price rotated higher.
- Not every minor candle wiggle deserves a structural label.
- Useful swing points should be visible enough to influence future decisions.

**Practice:** Open one clean trending chart and one choppy chart. Mark only the swing points that would matter for a trading decision, then explain why you ignored the rest.

**Common mistake:** Marking every candle fluctuation as structure.

## L02-M02 - Trend Structure

**Objective:** Read trend through structural progression rather than through a single indicator line.

**Why it matters:** Beginners often call a market bullish because one candle is green. Professional trend reading asks whether buyers or sellers keep defending increasingly favorable prices.

**Core ideas:**
- An uptrend is generally a sequence of higher highs and higher lows.
- A downtrend is generally a sequence of lower lows and lower highs.
- Healthy trends show continuation and controlled pullbacks.
- A trend is weakened when the side in control fails to defend the prior structural point.

**Practice:** Mark the last three major highs and lows on US30, DAX40, and Gold. Classify each as uptrend, downtrend, or unclear.

**Common mistake:** Calling one strong candle a trend.

## L02-M03 - Ranges and Balance

**Objective:** Recognize when price is rotating inside a range instead of trending.

**Why it matters:** Many losses come from applying trend tactics inside balanced markets. A range requires different expectations: fade extremes, wait for acceptance, or do nothing.

**Core ideas:**
- A range forms when neither side can sustain continuation.
- Range highs and lows often collect liquidity because many traders place stops beyond obvious extremes.
- The middle of a range usually offers poor reward-to-risk for directional trades.
- A breakout is not confirmed by crossing a line; it needs acceptance or follow-through.

**Practice:** Find one chart that is clearly ranging. Mark the range high, range low, midpoint, and two areas where false breaks could trap traders.

**Common mistake:** Trading the middle of a range as if it were a fresh trend.

## L02-M04 - Support and Resistance Zones

**Objective:** Draw support and resistance as decision zones rather than fragile exact lines.

**Why it matters:** Real markets do not always respect a single pixel-perfect price. Zones help learners account for spread, volatility, liquidity sweeps, and different market venues.

**Core ideas:**
- Support is an area where demand previously overcame supply strongly enough to rotate price higher.
- Resistance is an area where supply previously overcame demand strongly enough to rotate price lower.
- Zones are more practical than exact lines when volatility is meaningful.
- A level is stronger when it aligns with structure, session context, and visible reaction.

**Practice:** Replace three exact horizontal lines on a chart with zones. Explain what evidence justifies each zone.

**Common mistake:** Making zones so wide that they no longer support a clear risk decision.

## L02-M05 - Impulse and Pullback

**Objective:** Distinguish directional expansion from corrective movement.

**Why it matters:** A trader who enters during exhaustion often buys after the opportunity has already moved. Understanding impulse and pullback helps students wait for better location.

**Core ideas:**
- An impulse is a stronger directional movement that expands price away from a prior area.
- A pullback is a counter-move that tests whether the trend side can defend structure.
- Healthy pullbacks are usually smaller and less aggressive than the prior impulse.
- Deep or violent pullbacks warn that the trend may be losing quality.

**Practice:** On a trending chart, label three impulses and three pullbacks. Note which pullback was healthiest and why.

**Common mistake:** Chasing the impulse after reward-to-risk has already deteriorated.

## L02-M06 - Break of Structure

**Objective:** Define a break of structure as a meaningful continuation event, not a random wick through a level.

**Why it matters:** BOS is powerful only when used precisely. If every minor break becomes confirmation, the learner will overtrade and confuse liquidity grabs with continuation.

**Core ideas:**
- A bullish BOS occurs when price breaks a meaningful prior structural high in an existing bullish context.
- A bearish BOS occurs when price breaks a meaningful prior structural low in an existing bearish context.
- The broken level must be structurally relevant, not a random candle high or low.
- A better BOS shows displacement, acceptance, or follow-through.

**Practice:** Find two apparent structure breaks. Label one high-quality BOS and one weak break. Explain the difference.

**Common mistake:** Treating a liquidity sweep as automatic continuation confirmation.

## L02-M07 - Change of Character

**Objective:** Use change of character as an early warning that the current structural behavior may be shifting.

**Why it matters:** Reversals rarely become obvious at the best price. CHoCH helps learners notice when a trend is no longer behaving like the prior trend.

**Core ideas:**
- A CHoCH is an early structural shift against the prior behavior.
- It is not a guaranteed reversal signal.
- A higher-quality CHoCH appears near meaningful liquidity, support, resistance, or session context.
- A CHoCH often needs additional confirmation before execution.

**Practice:** Mark one possible bullish CHoCH and one possible bearish CHoCH. Write what would confirm or invalidate each idea.

**Common mistake:** Entering every CHoCH as if it were a completed reversal.

## L02-M08 - Breakout Acceptance and Failure

**Objective:** Separate accepted breakouts from failed breakouts.

**Why it matters:** Breakout traders and reversal traders often fight around the same level. The professional skill is not predicting every break, but reading whether price is accepted beyond the level.

**Core ideas:**
- Acceptance means price can hold beyond the broken area and continue doing business there.
- Failure means price breaks out but returns quickly into the prior range or structure.
- Failed breakouts can trap traders who entered late.
- Volume, volatility, session timing, and follow-through can help judge breakout quality.

**Practice:** Find one accepted breakout and one failed breakout. Mark the point where a professional would stop trusting the breakout.

**Common mistake:** Assuming a level break is enough without acceptance.

## L02-M09 - Internal and External Structure

**Objective:** Distinguish minor internal shifts from major external structure changes.

**Why it matters:** Many beginners reverse their bias because of a small lower-timeframe move while the higher-timeframe structure remains intact. This creates confusion and overtrading.

**Core ideas:**
- External structure is the major swing framework that defines broader direction.
- Internal structure is the smaller movement inside that broader framework.
- Internal shifts can provide early clues, but they do not always invalidate the larger structure.
- A trade idea should state which structure level it depends on.

**Practice:** On one chart, mark external structure in one color and internal structure in another. Write which one controls your bias.

**Common mistake:** Letting minor internal movement constantly flip the higher-timeframe bias.

## L02-M10 - Multi-Timeframe Structure Assessment

**Objective:** Demonstrate a complete structure read across higher, working, and execution timeframes.

**Why it matters:** The academy should not allow learners to advance because they recognize vocabulary. They must prove they can apply structure consistently to a real chart.

**Core ideas:**
- Start with the higher-timeframe bias.
- Use the working timeframe to define levels and active structure.
- Use the execution timeframe only after context is clear.
- A valid assessment includes invalidation and no-trade conditions.

**Practice:** Complete a structure assessment for one index and one gold chart. Include trend/range status, key swings, external structure, internal structure, and invalidation.

**Common mistake:** Using the lowest timeframe to invent a trade before context is understood.

## L02-M11 - Candlestick Context

**Objective:** Read candles inside market context instead of treating single candles as standalone signals.

**Why it matters:** A candle does not mean the same thing in every location. A strong bullish candle at range resistance may be late buying, while the same candle after a controlled pullback may show trend continuation.

**Core ideas:**
- Candles summarize open, high, low, and close for a selected period.
- A candle's meaning depends on location, prior structure, volatility, and session timing.
- Single-candle patterns are weaker without context.
- Professional reading asks what the candle changed, rejected, confirmed, or failed to do.

**Practice:** Find three large bullish candles. Label whether each is continuation, exhaustion, breakout, or unclear based on context.

**Common mistake:** Trading memorized candle patterns without context.

## L02-M12 - Candle Body and Commitment

**Objective:** Use candle bodies to judge directional commitment without confusing size with quality.

**Why it matters:** Large bodies show that price closed away from the open, but they can also appear at exhaustion points. The task is to decide whether the close improves or weakens the trade idea.

**Core ideas:**
- A large body shows directional progress during that candle period.
- A close near the candle extreme often shows stronger control than a close near the middle.
- Body size must be compared with recent volatility.
- A large candle after an extended move can be exhaustion rather than fresh opportunity.

**Practice:** Mark five large-body candles and classify each as useful commitment or possible exhaustion.

**Common mistake:** Assuming the biggest candle is the safest entry candle.

## L02-M13 - Wicks and Rejection

**Objective:** Interpret candle wicks as evidence of attempted price discovery and rejection.

**Why it matters:** Wicks often reveal that price tested an area and failed to maintain acceptance there. This is useful for reading liquidity sweeps, failed breakouts, and exhaustion.

**Core ideas:**
- A wick shows the distance price traveled but did not hold by the candle close.
- A long upper wick can indicate rejected higher prices.
- A long lower wick can indicate rejected lower prices.
- Wicks matter most when they occur at meaningful levels or liquidity areas.

**Practice:** Find two long upper wicks and two long lower wicks. Explain what area was tested and whether rejection was meaningful.

**Common mistake:** Calling every wick a reversal signal.

## L02-M14 - Inside Bars, Outside Bars, and Compression

**Objective:** Use candle range relationships to identify compression and expansion.

**Why it matters:** Markets alternate between compression and expansion. Recognizing this rhythm helps learners avoid forcing trades in low-quality areas and prepare for possible breakout conditions.

**Core ideas:**
- An inside bar stays within the prior candle's high-low range.
- An outside bar exceeds both the prior high and prior low.
- Several small overlapping candles can show compression.
- Compression often precedes expansion, but direction still requires context.

**Practice:** Mark one compression area and write bullish, bearish, and no-trade conditions for the next expansion.

**Common mistake:** Entering before expansion only because the chart became quiet.

## L02-M15 - Volatility-Adjusted Structure

**Objective:** Adjust structure expectations to the current volatility environment.

**Why it matters:** A pullback that is normal during high volatility may be abnormal during a quiet session. Structure cannot be read well without understanding the scale of recent movement.

**Core ideas:**
- Volatility describes movement size, not direction.
- Structural breaks in high volatility need more room and stricter confirmation.
- Quiet markets require patience because small breaks can be noise.
- A level's importance should be interpreted relative to recent range size.

**Practice:** Compare one quiet session and one high-volatility session. Note how swing size, wick size, and invalidation distance differ.

**Common mistake:** Using the same structural expectations in every volatility regime.

## L02-M16 - Session Transitions

**Objective:** Read how structure can change when a new trading session begins.

**Why it matters:** London, New York, and major cash opens can bring different participants and liquidity. A structure that looked stable before the open may be repriced quickly afterward.

**Core ideas:**
- Session opens can introduce new liquidity and volatility.
- Pre-session highs and lows often become reference points.
- A new session may accept prior prices, reject them, or expand away from them.
- The first move after an open can be informative, but it can also be a trap.

**Practice:** Mark Asia range, London open reaction, and New York open reaction on one chart. Explain what changed at each transition.

**Common mistake:** Ignoring session context when structure suddenly changes speed.

## L02-M17 - Trend Quality

**Objective:** Evaluate the quality of a trend rather than only naming its direction.

**Why it matters:** A trend can be technically bullish but poor to trade if it is extended, volatile, or losing momentum. Direction and quality are different judgments.

**Core ideas:**
- High-quality trends show clean continuation and controlled pullbacks.
- Weakening trends show overlap, failed continuation, deep pullbacks, or excessive wicks.
- Late-stage trends can still continue but may offer poor reward-to-risk.
- Trend quality should influence whether to enter, wait, reduce size, or avoid.

**Practice:** Rate three trends as high, medium, or low quality. Use structure, pullbacks, wicks, and volatility as evidence.

**Common mistake:** Entering every trend without judging whether the trend is still healthy.

## L02-M18 - Pullback Models

**Objective:** Classify pullbacks by depth, speed, and structure before planning continuation trades.

**Why it matters:** Not all pullbacks are equal. A shallow controlled pullback, a deep corrective pullback, and a violent reversal attempt require different decisions.

**Core ideas:**
- A shallow pullback can signal strong trend pressure but may offer limited entry location.
- A moderate pullback can offer better location if structure remains intact.
- A deep pullback may still continue, but it warns that the opposing side has gained influence.
- A pullback plan must define invalidation before entry.

**Practice:** Label three pullbacks as shallow, moderate, or deep. For each, define where the continuation idea becomes invalid.

**Common mistake:** Buying every dip without knowing which structural point must hold.

## L02-M19 - No-Trade Structure

**Objective:** Identify structure conditions where the professional decision is to avoid trading.

**Why it matters:** A strong academy must teach students when not to trade. Avoiding low-quality structure is a real skill, especially for beginners and funded-account traders.

**Core ideas:**
- No-trade is valid when structure is unclear.
- No-trade is valid when price is in the middle of a range.
- No-trade is valid when volatility makes risk unreadable.
- No-trade is valid before major news if the plan cannot control event risk.

**Practice:** Collect three screenshots where you intentionally would not trade. Write the exact structural reason for each.

**Common mistake:** Thinking progress requires taking more trades.

## L02-M20 - Structure and Volatility Assessment

**Objective:** Demonstrate an integrated read of candles, structure, volatility, sessions, and no-trade conditions.

**Why it matters:** Learners must prove they can combine concepts. The goal is not to predict the next candle; it is to produce a disciplined market read with clear evidence.

**Core ideas:**
- Start with higher-timeframe structure.
- Define whether the market is trending, ranging, or unclear.
- Judge candle behavior in context, not in isolation.
- Adjust invalidation to volatility and session conditions.
- State the best trade idea or explain why no trade is justified.

**Practice:** Complete a written assessment for two markets. Include bias, structure, candle evidence, volatility, session context, invalidation, and no-trade condition.

**Common mistake:** Turning every assessment into an entry hunt.
