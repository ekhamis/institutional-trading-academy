# English Master Review Plan for v1.0.0

## Objective

Lock the 120-mission English master only after automated integrity checks and independent editorial, instructional, risk-language, source-freshness and privacy review. Arabic authoring remains deferred until every lock gate is clear.

## Automated gate

- Canonical mission count, unique IDs and prerequisite ordering.
- Mission Markdown parity with the canonical dataset.
- Registered HTTPS source references and source usage inventory.
- English remains the source locale and Arabic mission count remains zero.
- Existing project, arithmetic, playbook-guardrail and package-privacy tests remain green.

Run `python scripts/audit_english_master.py --write` to refresh the machine-readable report in `release/v1.0.0-review/english_master_audit.json`.

## Manual gates

1. Review all 120 missions for clarity, duplication, terminology and answer quality.
2. Independently review instructional sequencing, uncertainty language and risk claims.
3. Spot-check time-sensitive specifications against the official sources in `data/sources.json` immediately before lock.
4. Rebuild the package and inspect it for private source originals, Discord channel names, handles and identifying metadata.

## Release rule

Do not change `VERSION` to `1.0.0`, start Arabic authoring, tag or publish until the automated gate passes and every manual gate has recorded evidence. Review corrections use the `build/v1.0.0-review` branch and preserve the 120-mission scope unless a documented defect requires a content change.
