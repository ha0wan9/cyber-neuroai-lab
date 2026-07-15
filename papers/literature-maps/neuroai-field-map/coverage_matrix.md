# Coverage Matrix — NeuroAI Field Map

Status: `audit-passed-with-documented-metadata-limitations`

Each active cell lists representative stable IDs, not every eligible paper.
`closed-review` uses a canonical review/perspective; `closed-method` is the
survey's explicit curation method rather than a literature claim.

| SQ | theory | experiment | survey | critical-review | dataset | Status |
|---|---|---|---|---|---|---|
| SQ1 Boundary | P162, P171 | N/A | P020, P162 | P085, P163 | N/A | closed |
| SQ2 Scale | `survey.md` (closed-method) | N/A | `survey.md` (closed-method) | `audits/bias-audit.md` | N/A | closed |
| SQ3 Roots | P001, P002, P011, P026 | P006, P007, P012 | P004 | N/A | N/A | closed |
| SQ4 Classical connectionism | P022, P024, P032, P040 | P031, P034, P044 | P032 | P028, P037 | N/A | closed |
| SQ5 Biological mechanisms | P013, P048, P053, P071, P088 | P012, P015, P086, P089, P092 | P091 | P085, P163 | N/A | closed |
| SQ6 Cognitive systems | P016, P058, P107, P116, P173 | P019, P061, P106, P110, P174 | P020, P120 | P110, P120, P163 | P110 | closed |
| SQ7 Hardware and agents | P068, P071, P080, P095, P098 | P069, P070, P081, P082, P099, P100 | P098 | P098, `fields-biological.md` | N/A | closed |
| SQ8 Representation/alignment | P010, P141, P146, P161 | P127, P129, P138–P140, P144–P148 | P162 | P129, P163 | P110, P128 | closed |
| SQ9 Modern architectures | P101, P111, P164, P166 | P104, P105, P114, P168–P170 | P171 | P163 | N/A | closed |
| SQ10 Theory/credit assignment | P024, P149, P157, P158, P093, P094 | P150, P152, P153, P156 | P075, P091 | P052, P136, P156 | N/A | closed |
| SQ11 Historical lineage | P001–P179 | P006, P012, P031, P061, P086, P174 | P037, P067, P162, P171 | P028, P136, P163 | N/A | closed |
| SQ12 Limits | P028, P120, P163 | P110, P129, P140, P156, P179 | P037, P120 | P028, P085, P110, P120, P136, P163 | N/A | closed |

## Audit amendment

At frame time SQ2 and SQ7 activated `dataset`. The audit found that this was
mis-specified: SQ2 explicitly asks for an estimate rather than exact publication
counts, and no common dataset can validate a historical hardware/WBE/animat
lineage. Those two cells were changed to N/A, recorded in `index.md`; SQ6 and
SQ8 retain real benchmark/dataset coverage.

## Field inventory gate

- 40 / 40 unique labels have a size tuple and explicit cap.
- 40 / 40 have at least three representative works.
- 179 / 179 unique works have a stable P-ID and authoritative landing link.
- Narrow or contested fields carry an explicit boundary/limitation note in the
  field files or `survey.md`.

## Audit summary

| Measure | Result |
|---|---:|
| Active cells | 47 |
| Closed | 47 |
| Gap | 0 |
| Weak coverage cells | 0 |
| Documented metadata-level limitations | institution and country not normalized for all 179 records |
