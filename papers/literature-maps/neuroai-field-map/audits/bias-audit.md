# Bias Audit — NeuroAI Field Map

## Quantitative checks

除明确标为 field appearances 的路线分布外，本审计按 179 个去重 P-ID 计数，
而不是按 189 个论文×领域出现次数计数。

| Bucket | Largest observed concentration | 60% trigger | Result |
|---|---:|---:|---|
| Decade | 2010s: 73/179 (40.8%) | 107/179 | pass |
| Single year | 2017: 15/179 (8.4%) | 107/179 | pass |
| First author | Friston: 4/179 (2.2%) | 107/179 | pass |
| Broad route | modern/cognitive cluster: 83/189 field appearances (43.9%) | 114/189 | pass |
| arXiv-linked records | 29/179 (16.2%) | 107/179 | pass; several are published works linked through arXiv |
| OpenReview-linked records | 6/179 (3.4%) | 107/179 | pass |

Decade distribution: 1940s 4; 1950s 5; 1960s 4; 1970s 3; 1980s 15;
1990s 25; 2000s 24; 2010s 73; 2020s 26.

## Metadata limitation

Institutions and countries were not normalized for every historical book,
technical report, and multi-author paper. Therefore the formal institution and
country buckets are **not load-bearing** in this version. Qualitatively, the map
is strongly Anglophone and weighted toward US/UK/Western European institutions,
reflecting both the chosen English-language scope and the canonical record used
by the source diagram. This limitation is visible rather than silently treated
as “no bias.”

## Selection-bias controls used

- Foundational age was not scored as obsolescence; old origin papers can remain
  representative without competing against modern empirical scale.
- Each mature field spans multiple lineage roles rather than taking the five
  highest-cited papers from one era.
- Critical/corrective works were deliberately included: P028, P037, P085,
  P110, P120, P129, P136, P140, P156 and P163.
- Unique-paper buckets were deduplicated before counting, preventing Yamins 2014,
  Fukushima 1980, Hopfield 1982 and other bridge papers from inflating those buckets;
  the broad-route row deliberately uses all 189 field appearances and says so explicitly.

## Accepted scope limitations

- English-language scholarly record only.
- No raw citation-count ranking; citation ecosystems are incomparable across
  1940s books, neuroscience journals and modern ML proceedings.
- “Representative” is optimized for learning the field's intellectual lineage,
  not for reproducing the current state of the art.
- Institution/country normalization is deferred to a future bibliometric
  version; conclusions about geographic diversity should not be drawn here.
