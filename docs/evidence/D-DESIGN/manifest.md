# Evidence manifest &mdash; D-DESIGN

Bulk evidence for [dev/DECISIONS.md](../../DECISIONS.md) `D-DESIGN` (the blush-pink print identity). The files
themselves are the printed wedding materials the palette and typography were sampled from; they are bulk
(binary, not text-sized) and stay in the repo's untracked scratch area rather than under version control.
This manifest is the tracked record of what they are, so the citation stays checkable even where the bulk
is absent.

| File                    | Location     | Size (bytes) | SHA-256                                                            |
| ----------------------- | ------------ | -----------: | ------------------------------------------------------------------ |
| `svatebni-oznameni.pdf` | `tmp/style/` |      459,191 | `4c5a08f4a4d22b914b706faa96cb62c4967f96db51bd09725c43fe74eebb27ea` |
| `jmenovky-design.pdf`   | `tmp/style/` |      591,063 | `b1ca0ad4ec1cb6b5316e9075f36c2471973b7871a01c30f068ae4da82fcd4231` |

Checksums taken 2026-09-30. `tmp/` is gitignored, so these two files travel by hand between machines, not
by clone; if a copy goes missing, re-derive the checksums above to confirm a replacement is the same file.
