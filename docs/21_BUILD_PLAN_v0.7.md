# Build Plan v0.7.0

## Status

Release-ready on branch `build/v0.7.0`. Local validation and the branch workflow pass with 60 canonical English missions, 0 errors, and 0 warnings. Version `0.6.0` remains the latest published release. No v0.7.0 release may be published until the candidate is merged to `main`, validation passes there, and publication is explicitly authorized.

## Goal

Complete the Volume and Auction track with an evidence-based introduction to volume profile, value, acceptance, rejection, and auction context. Learners should use these tools as descriptive references within a risk-controlled process, never as guaranteed signals.

## Scope boundary

This increment completes Level 3. Footprint charts, bid/ask delta, cumulative volume delta, the depth of market, heatmaps, and other execution-level order-flow tools remain deferred to Level 4.

## Planned mission sequence

1. L03-M11 - Volume Profile Maps Activity by Price
2. L03-M12 - Building and Comparing Profile Windows
3. L03-M13 - Point of Control as a Descriptive Reference
4. L03-M14 - Value Area, VAH, and VAL
5. L03-M15 - High- and Low-Volume Nodes
6. L03-M16 - Balance, Imbalance, and Auction Rotation
7. L03-M17 - Acceptance and Rejection Without Certainty
8. L03-M18 - Combining Profile Context with Market Structure
9. L03-M19 - No-Trade Profile Conditions and Data Limitations
10. L03-M20 - Volume Profile and Auction Assessment

## Acceptance criteria

- Ten canonical English mission records and matching English lesson files are complete for L03-M11 through L03-M20.
- Every factual claim is supported by an approved source ID and distinguishes observed evidence from interpretation.
- Every mission has one numbered instructional illustration using the established visual system.
- Canonical data expands from 50 to 60 missions without duplicate IDs, broken prerequisites, or schema drift.
- Curriculum, knowledge graph, localization status, README, handbook source, validator, and build-status documentation agree on version and mission count.
- English remains the canonical source language; Arabic authoring remains deferred until the English master is reviewed and locked.
- Local validation reports 60 canonical English missions, 0 errors, and 0 warnings.
- Assessment items test contextual interpretation and no-trade judgment, not memorized indicator rules.
- A v0.7.0 ZIP is generated only after validation passes on the complete candidate.
- Publication remains a separate, explicitly authorized step from validated `main`.

## Educational and risk guardrails

- Volume profile describes traded activity by price for a selected dataset and window; it does not reveal intent or predict direction.
- POC, VAH, VAL, HVN, and LVN depend on instrument, venue, session, provider, profile window, and calculation settings.
- Acceptance and rejection are contextual interpretations that require subsequent price and participation evidence.
- Profile references are not guaranteed support, resistance, fair value, entries, stops, or targets.
- Examples must include invalidation, controlled risk, and a valid no-trade outcome.
- Lessons must state data limitations where centralized or complete volume is unavailable.

## Release discipline

Keep all v0.7.0 work on `build/v0.7.0` until the complete candidate passes acceptance. Do not merge to `main`, create a tag, publish a GitHub release, or describe v0.7.0 as released without separate authorization and verified workflow results.

## Exact next action

Await explicit authorization to merge `build/v0.7.0` to `main`. After authorization, merge the candidate, verify `Validate and package` succeeds on `main`, then request separate authorization before tagging v0.7.0 or dispatching `Publish release`. Do not publish from the build branch.
