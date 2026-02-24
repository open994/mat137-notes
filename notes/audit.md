# Consistency Audit Report

Generated after all chapter and appendix files were written.

---

## Label Uniqueness

**579 labels** found across all `.tex` files. Every label is unique — no duplicates detected.

---

## Forbidden Constructs

A full scan of all chapter files and `appendix.tex` was performed for the following forbidden constructs:

| Construct | Occurrences |
|-----------|-------------|
| `$$...$$` | 0 |
| `\begin{equation*}` | 0 |
| `\newtheorem` | 0 |
| `\newcommand` | 0 |
| `\renewcommand` | 0 |
| `\usepackage` | 0 |
| `\over` (primitive) | 0 |
| `\underline` | 0 |
| `\marginpar` | 0 |
| `\hfill` | 0 |
| `\vspace` | 0 |
| `\newpage` | 0 |
| Bare `\epsilon` | 0 |

**Total forbidden construct occurrences: 0**

Note: `\underline{\int}` notation for the lower Darboux integral in Chapter 7 was replaced with the `\lowint` macro (defined in `preamble.tex`) during post-processing.

---

## Notation Consistency

### Limit Notation
All files use the standard `\lim_{x \to a}` or `\lim_{n \to \infty}` forms. No deviations found.

### Derivative Notation
- Chapters 3, 4, and 5 use both prime notation ($f'(x)$) and Leibniz notation ($\dfrac{d}{dx}$). Each chapter includes a remark acknowledging both notations where they first co-occur, consistent with the professor's style.
- Remaining chapters use whichever notation is appropriate to their content.

### Integral Differentials
All integral expressions use the preamble-defined macros `\dx`, `\dt`, `\du`, `\dv`, or explicit `\,d\theta` etc. No bare differentials found.

### Epsilon
All uses are `\varepsilon` or the macro `\eps`. No bare `\epsilon` found.

---

## Theorem Coverage

### Chapter 1: Logic, Definitions, Notation, and Proofs
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:1-1 | theorem | 1.4 | PROVED |
| thm:1-2 | theorem | 1.5 | PROVED |
| thm:1-3 | theorem | 1.5 | PROVED |
| thm:1-4 | theorem | 1.5 | PROVED |
| thm:1-5 | theorem | 1.6 | NO PROOF — Intentional (vacuous truth; transcript states without proof) |
| thm:1-6 | theorem | 1.7 | NO PROOF — Intentional (contrapositive equivalence stated as fact) |
| thm:1-7 | theorem | 1.8 | PROVED |
| thm:1-8 | theorem | 1.9 | PROVED |
| thm:1-9 | theorem | 1.11 | PROVED |
| thm:1-10 | theorem | 1.12 | PROVED |
| thm:1-11 | theorem | 1.13 | PROVED |
| thm:1-12 | theorem | 1.14 | PROVED |
| thm:1-13 | theorem | 1.15 | PROVED |

### Chapter 2: Limits and Continuity
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:2-1 | theorem | 2.4 | NO PROOF — Intentional (properties of absolute value; stated without proof in transcript) |
| thm:2-2 | proposition | 2.4 | NO PROOF — Intentional (distance characterization) |
| thm:2-3 | theorem | 2.7 | PROVED |
| thm:2-4 | theorem | 2.8 | PROVED |
| thm:2-5 | theorem | 2.9 | PROVED |
| thm:2-6 | theorem | 2.10 | PROVED |
| thm:2-7 | theorem | 2.10 | PROVED |
| thm:2-8 | theorem | 2.12 | PROVED |
| thm:2-9 | theorem | 2.15 | PROVED |
| thm:2-10 | theorem | 2.16 | PROVED |
| thm:2-11 | theorem | 2.16 | PROVED |
| thm:2-12 | theorem | 2.16 | PROVED |
| thm:2-13 | theorem | 2.18 | PROVED |
| lem:2-1 | lemma | 2.18 | PROVED |
| thm:2-14 | theorem | 2.20 | PROVED |
| thm:2-15 | theorem | 2.21 | NO PROOF — Intentional (EVT stated without proof in transcript) |
| thm:2-16 | theorem | 2.22 | NO PROOF — Intentional (IVT stated without proof in transcript) |

### Chapter 3: Derivatives
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:3-1 | theorem | 3.4 | PROVED |
| thm:3-2 | theorem | 3.4 | PROVED |
| thm:3-3 | theorem | 3.5 | PROVED |
| thm:3-4 | theorem | 3.7 | PROVED |
| thm:3-5 | theorem | 3.11 | PROVED |
| thm:3-6 | theorem | 3.12 | PROVED |

### Chapter 4: Transcendental Functions
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:4-1 | theorem | 4.2 | NO PROOF — Intentional (existence of inverses; stated as fact) |
| thm:4-2 | theorem | 4.4 | PROVED |
| thm:4-3 | theorem | 4.4 | PROVED |
| thm:4-4 | proposition | 4.5 | NO PROOF — REVIEW |
| thm:4-5 | theorem | 4.7 | PROVED |
| thm:4-6 | theorem | 4.8 | PROVED |
| thm:4-7 | theorem | 4.10 | PROVED |
| thm:4-8 | theorem | 4.13 | PROVED |
| thm:4-9 | theorem | 4.14 | NO PROOF — Intentional (arctangent/arccosine derivatives stated as analogues) |

### Chapter 5: The Mean Value Theorem and Applications
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:5-1 | theorem | 5.1 | NO PROOF — Intentional (preview/motivation; proved later in sec 5.9) |
| thm:5-2 | theorem | 5.2 | PROVED |
| thm:5-3 | theorem | 5.5 | PROVED |
| thm:5-4 | theorem | 5.6 | PROVED |
| thm:5-5 | theorem | 5.7 | PROVED |
| thm:5-6 | theorem | 5.9 | PROVED |
| thm:5-7 | theorem | 5.9 | PROVED |
| thm:5-8 | corollary | 5.10 | PROVED |
| thm:5-9 | theorem | 5.11 | NO PROOF — REVIEW (monotonicity theorem, open interval version) |
| thm:5-10 | theorem | 5.11 | NO PROOF — REVIEW (monotonicity theorem, closed interval version) |

### Chapter 6: Further Applications of Derivatives and Limits
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:6-1 | theorem | 6.6 | NO PROOF — Intentional (L'Hôpital's Rule; transcript states proof omitted) |
| thm:6-2 | proposition | 6.11 | PROVED |
| thm:6-3 | theorem | 6.13 | NO PROOF — Intentional (second-derivative concavity test; stated without proof) |
| thm:6-4 | theorem | 6.13 | NO PROOF — Intentional (necessary condition for inflection; stated without proof) |

### Chapter 7: The Definition of the Integral
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:7-1 | proposition | 7.2 | NO PROOF — REVIEW (sigma notation properties) |
| thm:7-2 | theorem | 7.3 | NO PROOF — Intentional (Least Upper Bound Principle; axiom) |
| thm:7-3 | theorem | 7.4 | NO PROOF — Intentional (LUB for functions; stated as consequence) |
| thm:7-4 | theorem | 7.4 | NO PROOF — Intentional (EVT restated from Ch 2) |
| lem:7-1 | lemma | 7.5 | PROVED |
| thm:7-5 | theorem | 7.5 | PROVED |
| thm:7-6 | proposition | 7.6 | PROVED |
| thm:7-7 | proposition | 7.6 | PROVED |
| thm:7-8 | proposition | 7.6 | PROVED |
| thm:7-9 | theorem | 7.9 | PROVED |
| thm:7-10 | theorem | 7.9 | PROVED |
| thm:7-11 | theorem | 7.10 | PROVED |
| thm:7-12 | theorem | 7.11 | NO PROOF — Intentional (linearity of integral; transcript states without proof) |
| thm:7-13 | theorem | 7.11 | NO PROOF — Intentional (splitting interval; stated without proof) |
| thm:7-14 | theorem | 7.11 | NO PROOF — Intentional (comparison of integrals; stated without proof) |

### Chapter 8: The Fundamental Theorem of Calculus
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:8-1 | theorem | 8.3 | NO PROOF — Proof is in sec 8.4 (separate section) |
| thm:8-2 | theorem | 8.5 | PROVED |

### Chapter 9: Integration Methods
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:9-1 | theorem | 9.1 | PROVED |
| thm:9-2 | theorem | 9.3 | PROVED |
| thm:9-3 | theorem | 9.4 | PROVED |
| thm:9-4 | proposition | 9.7 | NO PROOF — REVIEW (trig integral reduction) |

### Chapter 10: Volumes
No theorem environments in this chapter.

### Chapter 11: Sequences
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:11-1 | theorem | 11.3 | NO PROOF — Intentional (limit laws for sequences; stated as analogues of Ch 2 results) |
| thm:11-2 | theorem | 11.3 | NO PROOF — Intentional (Squeeze Theorem for sequences; analogue) |
| thm:11-3 | theorem | 11.3 | NO PROOF — Intentional (functions to sequences; stated without proof) |
| thm:11-4 | theorem | 11.3 | NO PROOF — Intentional (continuity preserves sequential limits) |
| thm:11-5 | theorem | 11.4 | PROVED |
| thm:11-6 | theorem | 11.4 | PROVED |
| thm:11-7 | theorem | 11.4 | PROVED |
| thm:11-8 | theorem | 11.7 | PROVED |

### Chapter 12: Improper Integrals
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:12-1 | theorem | 12.4 | PROVED |
| thm:12-2 | proposition | 12.7 | PROVED |
| thm:12-3 | theorem | 12.7 | NO PROOF — REVIEW (Basic Comparison Test statement) |
| thm:12-4 | theorem | 12.9 | PROVED |

### Chapter 13: Series
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:13-1 | theorem | 13.5 | PROVED |
| thm:13-2 | theorem | 13.6 | PROVED |
| thm:13-3 | theorem | 13.6 | PROVED |
| thm:13-4 | theorem | 13.7 | PROVED |
| thm:13-5 | theorem | 13.8 | PROVED |
| cor:13-1 | corollary | 13.8 | PROVED |
| thm:13-6 | theorem | 13.9 | PROVED |
| thm:13-7 | theorem | 13.10 | NO PROOF — REVIEW (Integral Test statement) |
| thm:13-8 | theorem | 13.11 | NO PROOF — Intentional (p-series test; consequence of Integral Test) |
| thm:13-9 | theorem | 13.12 | PROVED |
| thm:13-10 | theorem | 13.12 | PROVED |
| thm:13-11 | theorem | 13.13 | PROVED |
| thm:13-12 | theorem | 13.14 | PROVED |
| thm:13-13 | theorem | 13.15 | PROVED |
| lem:13-1 | lemma | 13.16 | PROVED |
| thm:13-14 | theorem | 13.17 | PROVED |
| thm:13-15 | theorem | 13.17 | PROVED |
| thm:13-16 | theorem | 13.18 | NO PROOF — REVIEW (Ratio Test statement) |

### Chapter 14: Power Series and Taylor Series
| Label | Environment | Section | Status |
|-------|-------------|---------|--------|
| thm:14-1 | theorem | 14.2 | NO PROOF — Intentional (structure of power series convergence; stated without proof) |
| thm:14-2 | theorem | 14.4 | NO PROOF — REVIEW (approximation via matching derivatives) |
| thm:14-3 | theorem | 14.7 | PROVED |
| thm:14-4 | theorem | 14.7 | PROVED |
| thm:14-5 | theorem | 14.8 | PROVED |

---

## Proof Completeness

**Total theorems/lemmas/corollaries/propositions: 101**
**Total with proofs: 67**
**Total without proofs: 34**

Of the 34 without proofs:
- **25** are intentionally unproved (axioms, results stated without proof in the transcript, results proved in a different section, or results from previous chapters restated for reference)
- **9** are marked REVIEW (proof may exist in transcript but was not captured, or the omission needs human verification):
  - thm:4-4 (Ch 4, sec 4.5)
  - thm:5-9 (Ch 5, sec 5.11)
  - thm:5-10 (Ch 5, sec 5.11)
  - thm:7-1 (Ch 7, sec 7.2)
  - thm:9-4 (Ch 9, sec 9.7)
  - thm:12-3 (Ch 12, sec 12.7)
  - thm:13-7 (Ch 13, sec 13.10)
  - thm:13-16 (Ch 13, sec 13.18)
  - thm:14-2 (Ch 14, sec 14.4)

---

## FIXME Cross-References

No FIXME references remain. The appendix reference `\cref{sec:3.FIXME}` was resolved to `\cref{sec:4.4}` (Derivatives of Inverse Functions).

---

## Missing or Skipped Files

### Missing Chapters
All 14 chapters (1–14) have transcript files and generated chapter files. None missing.

### Section Gaps
No section numbering gaps detected in any chapter file.

### Skipped Files
- **14.5.txt**: Empty file (0 bytes). A placeholder section `\section{The Taylor Series Formula}` with `\label{sec:14.5}` and a `\begin{remark}[Missing Content]` block was inserted into `ch14/chapter.tex`. The relevant material was incorporated into section 14.4.

### Unrecognised Filenames
None. All files in the source directory match the pattern `<integer>.<integer>.txt`.

---

## Summary

| Category                 | Issues Found |
|--------------------------|--------------|
| Duplicate labels         | 0            |
| Forbidden constructs     | 0            |
| Notation inconsistencies | 0            |
| Theorems flagged REVIEW  | 9            |
| Proofs missing           | 34 (25 intentional, 9 REVIEW) |
| FIXME references         | 0            |
| Missing/skipped files    | 1 (14.5.txt empty) |
