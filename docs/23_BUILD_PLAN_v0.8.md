# Build Plan v0.8.0

## Status

Authorized in the canonical Institutional Trading Academy development thread and built on `agent/ita-v0.8.0-master-build` from the verified v0.7.0 repository state. This candidate must pass local and GitHub workflow validation before it can be described as release-ready. Tagging and GitHub release publication remain separate operations.

## Goal

Begin Level 4 with an evidence-based introduction to liquidity and order flow. Learners must distinguish displayed resting orders, executed trades, platform estimates, and interpretation while keeping execution risk and no-trade judgment ahead of tool complexity.

## Scope boundary

This increment covers foundational liquidity and order-flow data literacy. Advanced absorption and exhaustion testing, stacked-imbalance frameworks, queue-model statistics, book resiliency measurement, cross-venue aggregation, and Level 4 completion remain deferred to the next increment.

## Mission sequence

1. L04-M01 - Liquidity: Spread, Depth, and Cost to Trade
2. L04-M02 - The Limit Order Book: Price, Queue, and Displayed Size
3. L04-M03 - Depth of Market: A Moving Snapshot
4. L04-M04 - Liquidity Zones, Stop Orders, and Hidden Information
5. L04-M05 - Sweeps, Breaks, and Post-Event Evidence
6. L04-M06 - Footprint Charts: Traded Volume at Price
7. L04-M07 - Delta: Aggressive Trade Imbalance Without Certainty
8. L04-M08 - Cumulative Volume Delta: Anchor, Reset, and Data Integrity
9. L04-M09 - Heatmaps, Order Changes, and Liquidity Reliability
10. L04-M10 - Liquidity and Order Flow Assessment

## Acceptance criteria

- Ten canonical English mission records and matching lesson files are complete for L04-M01 through L04-M10.
- Canonical data expands from 60 to 70 missions without duplicate IDs, broken prerequisites, or source-reference errors.
- Every factual claim is grounded in approved official exchange, regulator, or platform documentation.
- Every lesson separates resting orders, executed trades, estimates, and interpretation where relevant.
- Every mission has one 1600 x 900 numbered instructional PNG using the established dark academy system.
- Curriculum, knowledge graph, localization status, README, handbook source, schema, validator, roadmap, and build-status documentation agree on v0.8.0 and 70 missions.
- English remains the canonical source language; Arabic authoring remains deferred until English v1.0.0 lock.
- The validator discovers the current canonical dataset and release-status document dynamically rather than requiring future hard-coded mission counts.
- Local validation reports 70 canonical English missions, 0 errors, and 0 warnings.
- The handbook is regenerated from canonical data and contains exactly 70 mission headings.
- The v0.8.0 ZIP is generated only after validation passes.
- Publication remains separate from candidate packaging and requires explicit authorization.

## Educational and risk guardrails

- Displayed depth is a current feed state, not a promise that orders remain or execute.
- Executed volume, resting orders, and estimated classifications are distinct datasets.
- Prior highs, lows, and range edges may suggest potential order concentration but do not reveal exact stop quantity or intent.
- A sweep, delta divergence, imbalance, or heatmap band is not a guaranteed entry or directional signal.
- Spoofing is intent-based and cannot be established from a chart pattern alone.
- Every conditional plan requires data provenance, confirmation, structural invalidation, expected execution risk, maximum loss, and a valid no-trade outcome.

## Release discipline

Keep v0.8.0 work on the build branch until the complete candidate passes validation. A locally generated ZIP and a workflow artifact are build evidence, not a published release. Do not tag v0.8.0 or dispatch the release workflow without separate authorization.

## Exact next action

Use the guarded candidate push script to create `agent/ita-v0.8.0-master-build`, open a draft pull request, verify the `Validate and package` workflow, then record the workflow run and artifact in `docs/24_BUILD_STATUS_v0.8.md`.
