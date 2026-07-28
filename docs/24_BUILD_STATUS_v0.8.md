# Build Status v0.8.0

## Summary

The v0.8.0 build candidate begins the English-first Liquidity and Order Flow track and expands the canonical curriculum to 70 missions. It is a validated local candidate pending GitHub workflow verification. It is not tagged or published.

## Added

- Missions L04-M01 through L04-M10
- Liquidity dimensions: spread, depth, size-dependent cost, and execution conditions
- Limit-order-book, market-by-price, market-by-order, queue, and matching-algorithm foundations
- DOM as a time-sensitive displayed-order snapshot
- Observable versus inferred liquidity and stop-order limitations
- Sweep and breakout analysis based on post-event evidence rather than intent claims
- Footprint methodology, true bid/ask classification, and lower-timeframe estimates
- Delta and cumulative-delta interpretation with anchor and data-integrity controls
- Heatmap history, order changes, and spoofing interpretation boundaries
- Liquidity and Order Flow assessment
- Ten instructional diagrams, numbered 57 through 66
- Level-specific dataset: `data/liquidity_order_flow_missions_en-US.json`
- Canonical mission dataset: `data/missions_en-US_01_70.json`
- Cumulative handbook source: `handbooks/ITA_English_Handbook_Missions_01_70_v0.8.md`
- Dynamic handbook and validation scripts for future mission counts
- Corrected mission schema aligned to the actual canonical record format

## Educational safeguards

- Resting orders, executed trades, estimated classifications, and interpretation remain separate evidence categories.
- Displayed depth can change or cancel and is not guaranteed support, resistance, or executable size.
- Tool calculations depend on venue, feed, session, history, aggregation, and settings.
- Spoofing requires intent and cannot be diagnosed from a visual pattern alone.
- Every example includes structural invalidation, execution-risk awareness, and a valid no-trade outcome.

## English-first policy

English remains the canonical source language. Arabic authoring remains deferred until English v1.0.0 is reviewed and locked.

## Validation state

Local validation passes with 70 canonical English missions, 0 errors, and 0 warnings. The cumulative handbook was regenerated through mission 70, all ten new illustrations passed reference and dimension checks, and the package utility created `dist/institutional-trading-academy-v0.8.0.zip`. GitHub workflow verification remains pending the initial build-branch push.

## Repository handoff

The connected repository integration permitted inspection but rejected build-branch creation with `403 Resource not accessible by integration`. No remote repository state changed. The candidate includes `scripts/push_v0.8_candidate.ps1` and `release/v0.8.0/update_manifest.txt` for a guarded GitHub CLI push and draft pull request. Full handoff details are recorded in `docs/26_RELEASE_HANDOFF_v0.8.md`.

## Publication state

Unpublished candidate on `agent/ita-v0.8.0-master-build`. Packaging is not publication. Do not tag v0.8.0 or publish a GitHub release without separate authorization after the candidate passes branch and main validation.
