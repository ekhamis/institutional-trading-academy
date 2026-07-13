# Build Plan v0.6.0

## Status

Completed and published. Version `0.6.0` was validated on `main` at commit `144ed6431bb6710af0f33f7bc4d09ef4b9b7d964` and published as the latest GitHub release.

## Goal

Begin the Volume and Auction track with a practical, evidence-based introduction to volume, participation, relative volume, VWAP, and contextual decision-making.

## Planned mission sequence

1. L03-M01 - Volume Measures Activity, Not Direction
2. L03-M02 - Reading Price and Volume Together
3. L03-M03 - Relative Volume and the Comparison Baseline
4. L03-M04 - Session Volume and Participation
5. L03-M05 - VWAP Foundations
6. L03-M06 - VWAP Context: Trend, Balance, and Distance
7. L03-M07 - Volume on Breakouts and Failed Breakouts
8. L03-M08 - Absorption, Effort, and Result Without Overclaiming
9. L03-M09 - No-Trade Volume Conditions and Data Limitations
10. L03-M10 - Volume and Auction Assessment

All ten structured missions are integrated into `data/missions_en-US_01_50.json`, with matching English lesson files and completed illustrations 37 through 46. They are included in the published v0.6.0 release.

## Acceptance criteria

- Ten English mission records and matching mission markdown files are complete.
- Every factual claim is supported by an approved source ID.
- Every mission has a numbered instructional illustration.
- Canonical data is expanded from 40 to 50 missions without duplicate IDs or broken prerequisites.
- Curriculum, localization status, README, handbook source, validator, and build-status documentation agree on version and mission count.
- Local validation reports 50 canonical English missions, 0 errors, and 0 warnings.
- A v0.6.0 ZIP is generated only after validation passes.
- Publication remains a separate, explicitly verified release step.

## Guardrails

- Volume is evidence of activity, not a standalone directional signal.
- Indicator calculations and available volume data vary by instrument, venue, session, and provider.
- VWAP is a computed reference, not guaranteed support, resistance, or fair value.
- No mission may imply guaranteed returns or encourage uncontrolled leverage.

## Exact next action

Preserve the verified v0.6.0 tag and release package. Define the next roadmap increment before beginning new curriculum or product work; do not append unreleased scope to v0.6.0.
