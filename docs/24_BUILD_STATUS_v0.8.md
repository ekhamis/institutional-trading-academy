# Build Status v0.8.0

## Summary

The v0.8.0 release candidate begins the English-first Liquidity and Order Flow track and expands the canonical curriculum to 70 missions. Pull request #5 was squash-merged to `main` as commit `be51bd1a0a88dd44e444279ceffc868146b122b3`. The candidate is release-ready but is not yet tagged or published.

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
- Corrected mission schema aligned to the canonical record format

## Educational safeguards

- Resting orders, executed trades, estimated classifications, and interpretation remain separate evidence categories.
- Displayed depth can change or cancel and is not guaranteed support, resistance, or executable size.
- Tool calculations depend on venue, feed, session, history, aggregation, and settings.
- Spoofing requires intent and cannot be diagnosed from a visual pattern alone.
- Every example includes structural invalidation, execution-risk awareness, and a valid no-trade outcome.

## English-first policy

English remains the canonical source language. Arabic authoring remains deferred until English v1.0.0 is reviewed and locked.

## Validation state

- Local candidate validation: 70 canonical English missions, 0 errors, and 0 warnings.
- Candidate-branch workflow `Validate and package` #10: successful.
- Automatic `main` workflow #11 at merged commit `be51bd1`: successful.
- Manual `main` workflow #12: successful.
- Validation, versioned packaging, and artifact upload completed successfully on `main`.

## Repository state

- Candidate branch: `agent/ita-v0.8.0-master-build`
- Pull request: #5
- Pull request state: merged
- Main commit after squash merge: `be51bd1a0a88dd44e444279ceffc868146b122b3`
- Canonical version: `0.8.0`
- Canonical English missions: 70

## Release readiness

Release-ready on `main`, subject only to merging the metadata and workflow-runtime correction and confirming the final `main` workflow. The correction updates stale candidate wording and moves GitHub-maintained actions to Node.js 24-compatible major versions.

## Publication state

Unpublished. No `v0.8.0` tag or GitHub release should be created until the final release-readiness commit passes `Validate and package` and publication is explicitly authorized.
