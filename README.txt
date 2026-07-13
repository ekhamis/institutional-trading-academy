ITA GitHub App Publisher v3
===========================

Purpose
-------
This package publishes a verified Institutional Trading Academy release ZIP to:

  https://github.com/ekhamis/institutional-trading-academy

It authenticates through your GitHub App:

  App ID: 4281903
  Private key path: C:\Users\ekham\Downloads\ita-academy-builder-ek.2026-07-12.private-key.pem

The private key is NOT included in this ZIP.

Recommended mode
----------------
Use pull-request mode first:

  PUBLISH_AS_PR.cmd

Direct push is also included:

  PUBLISH_TO_MAIN.cmd

Inputs requested by the script
------------------------------
1. Full path to the verified academy release ZIP.
2. Version string, for example: v0.4.0

What it does
------------
- Generates a short-lived GitHub App installation token locally.
- Clones or updates a local work copy.
- Applies the release ZIP safely into the repository work copy.
- Commits the update as the GitHub App bot identity.
- Pushes either:
  - a release branch and opens a pull request; or
  - main plus a version tag.

Important
---------
Do not put the private key into the repository.
Do not commit tokens, passwords, or .pem files.

v3 fix
------
Fixes PowerShell argument handling for Git flags such as:

  git add -A

The v2 publisher could treat -A as a PowerShell parameter instead of a Git
argument.
