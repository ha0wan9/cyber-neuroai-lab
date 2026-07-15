# Claims-Adversary Review — NeuroAI Field Map

## Verdict

**PASS-WITH-WARNINGS** — 2026-07-14.

An independent reviewer who did not author the synthesis checked the final
survey, coverage and bias audits, central paper index, claims contract, and
field files.

## Checks passed

- 40 / 40 unique diagram fields are present; the duplicated image box is
  intentionally merged once.
- Per-field selected counts match the actual lists: 189 field appearances and
  179 unique stable paper IDs.
- All 40 score rows map correctly from the four proxy scores to
  `S/M/L/XL → cap 3/5/8/12`.
- `P001–P179` are continuous and unique; cross-field tags agree with the three
  field files.
- `claims.jsonl` has 179 valid records and honestly limits each record to
  citation identity; Chinese lineage-role notes remain curator interpretation.
- No obvious classification or metadata issue was found that would make the
  delivered map untrustworthy.

## Documented warning

The independent final reviewer did not individually revisit all 179 landing
URLs. Link identities were assembled from DOI, publisher, official proceedings,
PMLR, OpenReview, arXiv, and explicitly identified stable archives, but link rot
remains possible, particularly for old technical reports.
