# Release Handoff v0.8.0

## Release identity

- Repository: `ekhamis/institutional-trading-academy`
- Version: `0.8.0`
- Canonical English missions: 70
- Merged pull request: #5
- Merged main commit: `be51bd1a0a88dd44e444279ceffc868146b122b3`
- Publication state: release-ready but unpublished

## Completed gates

- Generated missions L04-M01 through L04-M10 and their English lesson files.
- Added instructional illustrations 57 through 66 at 1600 x 900.
- Regenerated the cumulative English handbook through mission 70.
- Validated canonical data, prerequisites, source references, schema alignment, localization records, illustrations, documentation, and version markers.
- Passed local validation with 70 canonical English missions, 0 errors, and 0 warnings.
- Passed candidate-branch workflow #10.
- Squash-merged pull request #5 into `main`.
- Passed automatic `main` workflow #11 and manual `main` workflow #12.

## Release-readiness correction

Before tagging, merge the small correction that:

- replaces obsolete build-branch and pending-workflow wording in README and v0.8.0 release documents;
- records the merged commit and successful `main` workflows;
- updates GitHub-maintained workflow actions to Node.js 24-compatible major versions; and
- leaves the curriculum, mission count, illustrations, handbook, and version unchanged.

The historical `PUSH_v0.8.0.cmd` and `scripts/push_v0.8_candidate.ps1` are no longer part of the active release procedure. They remain only as candidate-build history and should not be run again.

## Remaining release gates

1. Merge the release-readiness correction into `main`.
2. Confirm the resulting `Validate and package` workflow is green and has no Node.js 20 deprecation warning.
3. Record explicit authorization to publish v0.8.0.
4. Create tag `v0.8.0` from the exact validated release-readiness commit.
5. Confirm the `Publish release` workflow creates the GitHub release and attaches the versioned ZIP.
6. Verify the public release page, tag, release asset, and checksum-equivalent artifact identity.

## Safety rule

Packaging is not publication. Do not create or move the v0.8.0 tag until the final validated commit is known. Never retag a published version; create a patch version if a published release requires correction.
