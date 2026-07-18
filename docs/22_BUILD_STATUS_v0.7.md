# Build Status v0.7.0

## Summary

The release-ready v0.7.0 build candidate completes the English-first Volume and Auction track with 60 canonical English missions. Version v0.6.0 remains the latest published release. This candidate is not merged, tagged, or published. A workflow-generated candidate ZIP exists as a temporary Actions artifact; it is not a GitHub release asset.

## Added

- Missions L03-M11 through L03-M20
- Volume-profile datasets and comparison windows
- POC, value area, VAH, VAL, HVN, and LVN as descriptive references
- Balance, imbalance, auction rotation, acceptance, and rejection
- Profile context combined with observable market structure
- No-trade conditions and data-quality limitations
- Volume Profile and Auction assessment
- Ten instructional diagrams, numbered 47 through 56
- Canonical mission dataset: `data/missions_en-US_01_60.json`
- Cumulative handbook source: `handbooks/ITA_English_Handbook_Missions_01_60_v0.7.md`

## Educational safeguards

- Profile references depend on instrument, venue, provider, session, window, and calculation settings.
- POC, VAH, VAL, HVNs, and LVNs are not guaranteed support, resistance, fair value, entries, stops, or targets.
- Acceptance and rejection remain conditional interpretations of completed price and participation evidence.
- Every example requires invalidation, controlled risk, and a valid no-trade outcome.
- Incomplete, provider-specific, or incomparable data must be disclosed and can invalidate the analysis.

## English-first policy

English remains the canonical source language. Arabic authoring remains deferred until the English master is reviewed and locked.

## Validation state

The candidate contains 60 canonical English missions with matching lesson files and numbered illustrations. The cumulative English handbook is generated from canonical data. Local validation reports 60 canonical English missions, 0 errors, and 0 warnings. Workflow run `29635653642` passed validation and packaging at commit `35e347e`, and uploaded candidate artifact `institutional-trading-academy-35e347e2724419ce52706dc62acfa983ad0d2f98`.

## Release readiness

Release-ready but unpublished on `build/v0.7.0`. The next action requires explicit authorization: merge the candidate to `main`, verify `Validate and package` succeeds there, then request separate authorization before tagging v0.7.0 or dispatching `Publish release`.

## Publication state

Unpublished candidate on `build/v0.7.0`. Publication is a separate, explicitly authorized operation. Do not merge to `main`, create tag v0.7.0, or publish a GitHub release until authorization is recorded and the merged candidate passes validation on `main`.
