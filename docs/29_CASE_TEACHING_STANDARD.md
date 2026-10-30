# Case Teaching Standard - Next Build

English is canonical. Arabic localization remains deferred. This standard changes
teaching design, not the evidence status of any trading method.

## Case Sequence

1. Preparation: identify instrument, venue/feed, contract, timezone, session and
   scheduled event context. Expand every abbreviation at first use.
2. Decision: freeze the chart before the decision. Do not expose future candles,
   outcome, profit labels or answer cues until the learner submits a plan.
3. Plan: state conditional trigger, contradictory evidence, invalidation, stop,
   target, size, cost assumptions and maximum planned loss. A watchlist zone is
   not an executed trade and is not enough to pass this stage.
4. Execution: distinguish planned prices from observed fills. Record slippage,
   charges and any departure from the original plan. Unknown fields stay unknown.
5. Review: reveal the continuation and compare decision quality with outcome.
   Include losers, skipped setups and ambiguous cases, not only selected winners.

## Assessment Rubric

Award 0-2 points each for context/data verification, conditional trigger,
invalidation, risk/cost calculation, contradictory evidence, and review quality.
0 means absent or unsafe; 1 means partial; 2 means explicit and reproducible.
An absent invalidation or maximum-loss calculation requires remediation even if
the total score is high. Profit never compensates for a safety failure.
These are educational thresholds, not proof of live trading readiness.

## Evidence Labels

- Synthetic: original teaching data; not a historical or performance claim.
- Historical observation: market data with provenance and reproducible settings.
- Reported outcome: author claim, not independently verified fills or returns.
- Verified execution record: supporting execution evidence has been reviewed;
  state exactly what was verified and what remains uncertain.

Never infer participant identity, manipulation, profitability or a repeatable edge
from a screenshot alone. Never reconstruct a missing stop to manufacture R.

## Private Source Boundary

Downloaded community charts, excerpts, member identities and source manifests
remain outside the public repository. Download permission is not publication
permission. Do not include private material in releases, commits, issues, pull
requests, tutor retrieval indexes or public examples. Use original synthetic
scenarios for published lessons until explicit reuse rights and privacy review
are documented. Removing an author's name alone does not establish reuse rights.

The release packager also excludes private-research, private-sources and
discord-downloads folders if accidentally placed within the repository. This is
a secondary safeguard, not permission to store private sources in Git.

## Delivery Resilience

Every live exercise needs an asynchronous fallback containing the same objective,
decision-time chart, learner prompts, answer rubric and reflection. A cancelled
session must not prevent a learner from completing the skill practice.

## Next Build Acceptance

- Ten trade-planning missions use the decision-before-outcome sequence.
- At least one failed, one skipped and one ambiguous synthetic case are included.
- A high-profit but rule-breaking answer fails the risk gate.
- Source material and personal identifiers are absent from the release archive.
- No community image is represented as licensed academy content.
