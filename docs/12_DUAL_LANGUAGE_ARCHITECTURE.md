# Dual-Language Architecture - English First

## Decision
English is the master authoring language for the first release. Arabic is structurally supported from day one but content translation/localization starts only after the English curriculum and terminology are approved.

## Why this sequence
- Prevents parallel rewriting of unstable material.
- Creates one authoritative source for facts, learning outcomes, visuals, and assessments.
- Allows Arabic to be localized naturally rather than translated sentence by sentence.
- Keeps mission IDs, evidence tags, assets, and assessments aligned across languages.

## Content structure
```
content/
  en-US/
    foundation/
  ar/
    foundation/
locales/
  en-US/ui.json
  ar/ui.json
```

## Canonical fields
Language-neutral fields live in the mission manifest: ID, prerequisites, competency mappings, assessment type, evidence classification, illustration IDs, and source IDs.

Localized fields live in language files: title, objective, explanation, examples, exercise instructions, quiz wording, feedback, and glossary entries.

## Arabic rules for the later phase
- Native RTL layout rather than mirroring text only.
- Natural Modern Standard Arabic.
- Preserve widely recognized abbreviations such as POC, VWAP, ETF, BOS, and CVD with an Arabic explanation on first use.
- Do not release Arabic content until the English mission is marked `content_locked`.
- Arabic review requires both a finance reviewer and a language reviewer.
