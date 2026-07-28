# Release Handoff v0.8.0

## Candidate identity

- Base repository: `ekhamis/institutional-trading-academy`
- Verified base commit: `9b06d41a018248a0b4664449bb958f793cceebbc`
- Candidate branch: `agent/ita-v0.8.0-master-build`
- Candidate version: `0.8.0`
- Canonical English missions: 70
- Publication state: unpublished

## Completed locally

- Generated missions L04-M01 through L04-M10 and their lesson files.
- Added instructional illustrations 57 through 66 at 1600 x 900.
- Regenerated the cumulative English handbook through mission 70.
- Validated the canonical dataset, prerequisites, source references, schema alignment, localization records, illustrations, documentation, and version markers.
- Local result: 70 canonical English missions, 0 errors, and 0 warnings.
- Generated `dist/institutional-trading-academy-v0.8.0.zip` after validation.

## GitHub handoff state

The connected repository integration allowed inspection but returned `403 Resource not accessible by integration` when asked to create the isolated build branch. No GitHub files, refs, tags, pull requests, or releases were changed by that failed operation.

From the extracted v0.8.0 package, double-click `PUSH_v0.8.0.cmd`, or run the candidate-specific PowerShell script:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\push_v0.8_candidate.ps1
```

The script applies only the files listed in `release/v0.8.0/update_manifest.txt`, verifies the exact base commit, rebuilds the handbook, reruns validation and packaging, creates the isolated branch, pushes it, and opens a draft pull request.

## Safety stops

The script stops rather than guessing when:

- the local candidate is incomplete;
- GitHub authentication is unavailable;
- the repository `main` SHA differs from the verified base;
- the remote candidate branch already exists;
- validation or packaging fails; or
- no intended files are staged.

## Remaining release gates

1. Push the candidate branch and open the draft pull request.
2. Verify the `Validate and package` workflow reports 70 missions, 0 errors, and 0 warnings.
3. Review the complete candidate and record the workflow run and artifact in `docs/24_BUILD_STATUS_v0.8.md`.
4. Merge to `main` only with explicit authorization.
5. Validate on `main`.
6. Tag and publish v0.8.0 only under a separate explicit authorization.
