# Build Status v0.6.0

## Summary

The v0.6.0 build candidate expands the English-first academy from 40 to 50 authored missions. It is not published; v0.5.0 remains the latest release until all v0.6.0 acceptance criteria pass and publication is explicitly authorized.

## Added

- Missions L03-M01 through L03-M10
- Volume basics and price-volume context
- Relative volume and comparison baselines
- Session volume and participation
- VWAP foundations and contextual interpretation
- Breakout participation, failed breakouts, and cautious effort-versus-result analysis
- No-trade volume conditions and data-quality limitations
- Integrated Volume and Auction assessment
- Ten instructional diagrams, numbered 37 through 46
- Canonical mission dataset: `data/missions_en-US_01_50.json`
- Level-specific mission dataset: `data/volume_auction_missions_en-US.json`

## Educational safeguards

- Volume is evidence of activity, not a standalone directional signal.
- Volume data and indicator calculations can vary by instrument, venue, session, and provider.
- VWAP is a computed reference, not guaranteed support, resistance, or fair value.
- Every trade decision still requires defined invalidation and controlled risk.

## English-first policy

English remains the canonical source language. Arabic content remains deferred until the English master is reviewed and locked.

## Publication state

Release-ready but unpublished build candidate on `build/v0.6.0`. Local validation reports 50 canonical English missions, 0 errors, and 0 warnings. The local v0.6.0 ZIP passed archive integrity checks with all required canonical files present.

After explicit merge authorization, merge the candidate to `main`, verify the `Validate and package` workflow succeeds, then manually dispatch `Publish release` from `main` with tag `v0.6.0`. Do not publish from the build branch.
