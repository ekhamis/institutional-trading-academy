# v1.0.0 Review-Candidate Package Privacy Inspection

Checked: 2026-10-30

The repository remains version `0.13.0` until every English-lock gate is
clear, so the rebuilt review archive retains the v0.13.0 filename.

## Rebuilt archive

- Path: `dist/institutional-trading-academy-v0.13.0.zip`
- Size: 40,617,708 bytes
- Entries: 366
- SHA-256: `fe934e26fe46eb0a6873c9663eb20bb60621757eb79490878473150c15c3511e`

## Inspection

- Private, Discord-download, Git, cache, virtual-environment, and bytecode
  path matches: **0**.
- Filename matches for Discord names, handles, and common author/message/
  channel/user identifier fields: **0**.
- Six text files contained the word `Discord` or identifier-field terms. Each
  was manually checked and was a privacy rule, build-status statement,
  packaging exclusion, or privacy-test implementation; none contained source
  originals, channel names, handles, messages, or identifying metadata.
- `python scripts/test_package_privacy.py` also passed as part of the seven-test
  discovered suite.

## Gate status

Final package privacy review: **PASS for exact review head content rebuilt on
2026-10-30**. Rebuild and repeat after any later content change and before a
v1.0.0 release asset is published.

