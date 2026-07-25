# Firoozbakht's Conjecture — SOURCE LEDGER

**Molecule:** `task-20260725-d320` (leg: `source-ledger`, crew role: sourcer)
**Run:** `germ-20260725-791a7c45`
**Date built:** 2026-07-25
**Target statement:** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently, the sequence
`(p_n)^{1/n}` is strictly decreasing. **Status: OPEN.** Neither assumed true nor assumed false.
**Seed anchors supplied:** none. This ledger was built from scratch.

**Ledger size: 20 rows** — 11 at tier **L0**, 3 at **L1**, 4 at **L2_strong**, 2 at **L2_weak**,
**0 at L3**. Every row has a BibTeX entry in §8 and a locator table or locator statement in §2.
Seven source PDFs were fetched and read in full; their MD5s are recorded per row.

---

## 0. Perimeter (v5.1 clause) — what may and may not enter this ledger

A **ledger row** is a *published source that was fetched in this run and located*. "Located"
means: I opened the actual text (PDF, journal page, or official documentation page), found the
statement, and recorded where it sits (theorem number / equation number / page). Every row below
carries a `Fetched` field naming the exact URL retrieved and, for PDFs, the MD5 of the bytes I
read.

**Explicitly excluded from the ledger:**

1. **Files in the working tree.** No file that merely happens to sit in
   `/Users/eserie/galaxies/firoozbakht-cleanroom/` is a ledger row, regardless of quality. The
   run's own prior legs (`decompose.md`, `frame-deliberation/`) are recorded in **§5 EXTERNAL
   PRIOR ART**, which is *outside* the citable ledger. Nothing downstream may cite §5 as
   literature.
2. **Recall.** Nothing is entered because I remember it. The upstream `decompose` leg's §7 was an
   explicitly-flagged recall list at tier L3; this ledger **resolves or refutes** those entries
   (§3) rather than inheriting them.
3. **Tertiary encyclopedias.** Wikipedia and MathWorld were seen in search results and are **not**
   entered as rows. Where they were the only lead, the row is absent and the gap is declared (§6).

---

## 1. Tier protocol

| Tier | Meaning |
|---|---|
| **L0** | Primary published source, fetched in this run, statement read at the recorded locator. |
| **L1** | Primary source fetched, but the recorded locator is an *edition/pagination I could not
independently confirm* (e.g. a preprint whose page numbers differ from the journal's). |
| **L2_strong** | Statement not read in the primary source, but attested at a specific locator by **two
or more independent fetched L0 sources**. |
| **L2_weak** | Statement attested at a specific locator by **one** fetched L0 source citing a work I did not open. |
| **L3** | Recall / unverified. **No L3 row appears in this ledger.** |

**Rule for downstream legs:** a claim in the final paper may rest on an L0 or L1 row directly. An
L2_strong or L2_weak row must be *attributed as second-hand in the text* ("as reported by X") or
be upgraded before the citation gate.

---

## 2. THE LEDGER

### 2.1 Origin and statement of the conjecture

---

**`firoozbakht1982unpublished`** — tier **L2_strong**

- **Attribution:** Farideh Firoozbakht (University of Isfahan), 1982. **Unpublished.**
- **Fetched:** <https://www.primepuzzles.net/conjectures/conj_030.htm> (Rivera, ed., *Conjecture 30.
  The Firoozbakht Conjecture*, The Prime Puzzles & Problems Connection, 2002).
- **Statement as posted there (verbatim):** "(pn)1/n decreases increasing n, in which pn is the nth
  prime number." The page further records Firoozbakht's own claim to have "verified (the conjecture)
  with the table of Maximal gaps between consecutive primes <= 4.444 * 10^12".
- **Why L2_strong, not L0:** there is no 1982 publication to fetch. The 1982 date and the
  unpublished status are attested independently by **three** fetched L0 sources: Kourbatov
  (`kourbatov2015bounds`, §1: *"In 1982 Firoozbakht proposed the following conjecture [6, p. 185]"*),
  Ferreira–Mariano (`ferreira2017consequences`, §1: *"In 1982 (see [5]), the Iranian mathematician
  Farideh Firoozbakht, from the University of Isfahan, conjectured the following"*), and Visser
  (`visser2019verifying`, ref. [24]: *"Faride Firoozbakht, (1982), unpublished."*).
- **Downstream use:** attribution and date only. **Do not cite this row for any mathematical
  content.**

---

**`ribenboim2004little`** — tier **L2_strong** (locator attested twice, book not opened)

- **Citation:** P. Ribenboim, *The Little Book of Bigger Primes*, 2nd ed., Springer, New York, 2004.
  DOI `10.1007/b97621`.
- **Locator:** **p. 185.**
- **What it supplies:** the first *printed* appearance of the conjecture; the standard reference for
  its statement.
- **Evidence for the locator:** two mutually independent fetched L0 sources cite exactly `p. 185`:
  Kourbatov (`kourbatov2015bounds`, §1, ref [6]) and Sun (`sun2013sequence`, §1, ref [R]:
  *"The unsolved Firoozbakht conjecture (cf. [R, p. 185]) asserts that ⁿ√p_n > ⁿ⁺¹√p_{n+1} for all
  n ∈ Z⁺"*).
- **Not fetched.** No copy of the book was retrieved in this run. **Flagged for the citation gate:**
  if the final paper cites Ribenboim p. 185 as its statement source, a physical/PDF check is
  required to reach L0. Otherwise cite Kourbatov or Sun directly, both of which are L0 here.

---

**`kourbatov2015bounds`** — tier **L0** ★ *most load-bearing row in this ledger*

- **Citation:** Alexei Kourbatov, "Upper bounds for prime gaps related to Firoozbakht's conjecture",
  *Journal of Integer Sequences* **18** (2015), Article 15.11.2. arXiv:1506.03042.
- **Fetched:** <https://arxiv.org/pdf/1506.03042> — v4, 12 Mar 2019, 8 pp., MD5
  `5b4b61ea6ad4d5bcca2dbf3bd604e151`. (The journal's own HTML/PDF at
  `cs.uwaterloo.ca/journals/JIS/VOL18/Kourbatov/` returned HTTP 404 in this run; the arXiv v4 is
  used, and it carries a §7 Corrigendum, see below.)
- **Statements supplied — all read at the locator:**

  | Locator | Exact statement |
  |---|---|
  | §1, eq. (1) | Firoozbakht's conjecture ⟺ `p_{k+1} < (p_k)^{1+1/k}` for all `k ≥ 1`. |
  | §2, **Theorem 1** | "If conjecture (1) is true, then `p_{k+1} − p_k < log² p_k − log p_k − 1` for all `k > 9`." |
  | §4, **Theorem 3** | "If `p_{k+1} − p_k < log²p_k − log p_k − 1.17` for all `k > 9` (`p_k ≥ 29`), then Firoozbakht's conjecture (1) is true." — i.e. (B) with `b = 1.17` implies (A). **The `k > 9` threshold is part of the hypothesis; do not drop it.** |
  | §4, **Theorem 4** | Three further sufficient conditions with `b → 1`, e.g. `g_k < log²p_k − log p_k − 1 − 3.83/log p_k`, each assumed for all `p_k > 4·10¹⁸`. |
  | §5 Appendix, **Theorem 5** | `f_k := p_k^{1+1/k} − p_k = log² p_k − log p_k − 1 + o(1)` as `k → ∞`. |
  | §3, discussion + Table 1 | The gap bound (2)/(3) is a *corollary* of (1), so (2) may hold while (1) fails. Worked counter-illustration at `p_k = 2010733` (line 7 of Table 1), where a prime `q = 2010929` lies in `[p_k+f_k, p_k+ℓ_k]`. |
  | §7 **Corrigendum** | In (11), "x ≥ 5.43" must read "x ≥ 2634800823"; the range restriction propagates through Theorem 3. Incorporated in arXiv v4. **Cite v4, never v1–v3.** |

- **Supports:** decompose §1.2 (F4), §1.3, §4.2 (T2), §2 P6 — and it *pre-empts* the decomposition's
  "Claim A" (see §4 below).
- **Downstream hazard:** Theorem 1 is one-directional. Do not use it as an equivalence.

---

**`kourbatov2015verification`** — tier **L0**

- **Citation:** Alexei Kourbatov, "Verification of the Firoozbakht conjecture for primes up to four
  quintillion", *International Mathematical Forum* **10** (2015), no. 6, 283–288. arXiv:1503.01744.
- **Fetched:** <https://arxiv.org/pdf/1503.01744>, MD5 `1c4b19bf468e2bdfbb4f603c1d9bc7aa`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | Abstract | "We use the table of first-occurrence prime gaps in combination with known bounds for the prime-counting function to verify the Firoozbakht conjecture for primes up to four quintillion (4×10¹⁸)." |
  | §3, eq. (5) | Firoozbakht ⟺ `π(p_k) < log p_k / (log p_{k+1} − log p_k)`. |
  | §3, eq. (3) | `π(x) < x/(log x − 1.1)` for `x ≥ 60184`, credited to **[2, p. 9, Theorem 6.9]** = Dusart 2010. |
  | §4, **Theorem** (p. 288) | "Inequality (1) is true for all primes `p_k < 4 × 10¹⁸`." |
  | §4, method | A gap of size `g` "can never violate" the conjecture once the first occurrence of `g` exceeds a computable safe bound; checked for all even `g ∈ [2, 1476]`. |
  | **Endnotes, added 5 Jan 2023** | "Firoozbakht's conjecture (1) is true for all primes `p_k < 2⁶⁴`; prime gaps of size `g < 1920` cannot violate (1)." |

- **Supports:** decompose §2 P5 (verified range) — **with a correction**, see §4.
- **Downstream hazard:** the title says `4×10¹⁸`; the paper's own 2023 endnote says `2⁶⁴ ≈
  1.8447×10¹⁹`. Quote the endnote, not the title, and say which.

---

### 2.2 The Cramér side — the heuristic that contradicts Firoozbakht

---

**`cramer1936order`** — tier **L0** (scanned original read page-by-page)

- **Citation:** H. Cramér, "On the order of magnitude of the difference between consecutive prime
  numbers", *Acta Arithmetica* **2** (1936), 23–46.
- **Fetched:** <http://matwbn.icm.edu.pl/ksiazki/aa/aa2/aa212.pdf> (ICM Warsaw digitisation), MD5
  `32a0d8b46aa366cabbb90b8ead921dcb`. The scan has **no text layer**; the four pages cited below
  were read as images.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | **p. 24, eq. (4)** | "It is suggested that the true maximum order of `p_{n+1} − p_n` should be equal to `(log p_n)²`, so that we should be able to replace (1) and (3) by … `p_{n+1} − p_n = O((log p_n)²)`." |
  | **p. 27, final display** | "Combining these two results, we obtain the following theorem: **With a probability = 1, the relation** `limsup_{n→∞} (P_{n+1} − P_n)/(log P_n)² = 1`" |
  | pp. 26–27 | The urn model: urns `U_n` with white-ball probability `1/log n`; `P_n` = index of the urn giving the `n`-th white ball. The `limsup = 1` theorem is a theorem **about `P_n`, the model**, not about `p_n`. |

- **Critical nuance for every downstream leg:** Cramér **proves** `limsup = 1` for the *random*
  sequence and only *suggests* the analogue for the primes. Writing "Cramér conjectured
  `limsup g_n/log²p_n = 1`" is a compression that the source does not literally support; the
  defensible form is "Cramér's model yields `limsup = 1` with probability 1, which he offered as a
  suggestion for the primes." Granville (`granville1995cramer`, p. 10) frames it the same way:
  *"So what Cramér seems to be suggesting…"*.

---

**`granville1995cramer`** — tier **L1** ★ *the load-bearing citation of the refutation-side argument*

- **Citation:** Andrew Granville, "Harald Cramér and the distribution of prime numbers",
  *Scandinavian Actuarial Journal* **1995**, no. 1, 12–28. DOI `10.1080/03461238.1995.10413946`.
- **Fetched:** <https://chance.dartmouth.edu/chance_news/for_chance_news/Riemann/cramer.pdf>
  (author's preprint, 16 pp.), MD5 `55e81c7af1aa9960b4dbf47b6fa02205`. The same file is the one
  OEIS A111943 links to at `dms.umontreal.ca/~andrew/PDF/cramer.pdf`.
- **Why L1, not L0:** the fetched file is the **preprint, paginated 1–16**. The journal is paginated
  **12–28**. Every locator below is a *preprint* page. I did not obtain the journal PDF and
  therefore **cannot map preprint page → journal page**. Any citation must either say "preprint
  pagination" or be re-located against the journal copy before the citation gate.
- **Statements supplied — read verbatim:**

  | Locator (preprint) | Exact statement |
  |---|---|
  | **p. 2**, after eq. (2) | "…implies that we expect there to be `∼ 2e^{−γ} x/log x` primes ≤ x, where `2e^{−γ} ≈ 1.12292…`" (with footnote 1: "A constant which does not seem to have a simpler definition, and seems likely to be transcendental."). |
  | **p. 10, eq. (14)** | "`max_{p_n ≤ x}(p_{n+1} − p_n) ∼ log² x`. This statement (or the weaker `O(log²x)`) is known as 'Cramér's Conjecture.'" |
  | **p. 10**, table | Record gaps to `10¹⁴` with `(p_{n+1}−p_n)/log²p_n`: `31397→.6715`, `370261→.6812`, `2010733→.7025`, `20831323→.7394`, `25056082087→.7953`, `2614941710599→.7975`, `19581334192423→.8177`. |
  | **p. 12**, after eq. (20) | "Moreover, with our new model above, Cramér's arguments suggest that `max_{p_n≤x}(p_{n+1} − p_n) ⪆ 2e^{−γ} log² x`, **which contradicts Cramér's conjecture (14)!**" |
  | **pp. 12–13** | "The computational evidence alone (see above) would not lead one to predict that (14) errs on the small side… there are now a number of independent computors trying to find examples with `(p_{n+1}−p_n)/log²p_n > 1`." |
  | **p. 12** | The mechanism: Maier's theorem exploits the inconsistency between the sieve heuristic (2) and Cramér's model, "a severe blow to Cramér's model." |

- **Verdict on the decompose leg's highest-risk recall (A9): CONFIRMED.** Both the constant
  (`2e^{−γ} ≈ 1.12292`) and the **direction** (Cramér–Granville predicts gaps *larger* than `log²x`,
  hence contradicts Firoozbakht) are as the decomposition recalled them.
- **Downstream hazard:** the sign `⪆` in the source is "suggests", not "proves". Granville's own
  framing is that Cramér's *arguments under a corrected model* suggest this. It is a heuristic. It
  is **not** a falsification test (decompose §4.5 T5 is correct to say so).

---

### 2.3 The empirical frontier

---

**`oeis_A111943`** — tier **L0**

- **Citation:** N. J. A. Sloane (ed.), *The On-Line Encyclopedia of Integer Sequences*, sequence
  **A111943**, "Prime p with prime gap q − p of n-th record Cramer-Shanks-Granville ratio, where q
  is smallest prime larger than p and C-S-G ratio is `(q−p)/(log p)²`."
- **Fetched:** <https://oeis.org/search?q=id:A111943&fmt=text> — version `#75 Nov 14 2025`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | `%e` table | The 12 record CSG ratios: `0.6103@23`, `0.6264@113`, `0.6575@1327`, `0.6715@31397`, `0.6812@370261`, `0.7025@2010733`, `0.7394@20831323`, `0.7953@25056082087`, `0.7975@2614941710599`, `0.8177@19581334192423`, `0.8311@218209405436543`, **`0.9206@1693182318746371`**. |
  | `%C` | "a(12) was discovered by Bertil Nyman in 1999." |
  | `%C` | "Shanks conjectures that the ratio will never reach 1. Granville conjectures the opposite: that the ratio will exceed or come arbitrarily close to `2/e^γ = 1.1229…`." |
  | `%C` (Kourbatov, Jan 28 2016) | "Firoozbakht's conjecture implies that the ratio is below `1 − 1/log(p)` for all primes `p ≥ 11`; see Th.1 of arXiv:1506.03042." |
  | `%C` | "Primes less than 23 are anomalous and are excluded." |

- **Corroborating fetch (L0, secondary):** T. R. Nicely, "New maximal prime gaps and first
  occurrences", <https://faculty.lynchburg.edu/~nicely/gaps/gaps.html> — records the gap **1132**
  following **1693182318746371**, found by Nyman 24 Jan 1999, with CSG ratio
  **0.92063858855742**, "the greatest known value".
- **Verdict on decompose recall A10: CONFIRMED** (ratio `≈ 0.9206`, gap `1132`, `p ≈ 1.693·10¹⁵`).
- **Downstream use:** this is the strongest single empirical statement about how close the
  conjecture comes to failing. Note the Kourbatov comment gives a *sharper* Firoozbakht-implied
  ceiling (`1 − 1/log p`) than the crude `1`.

---

**`oliveira2014goldbach`** — tier **L2_weak**

- **Citation:** T. Oliveira e Silva, S. Herzog, S. Pardi, "Empirical verification of the even
  Goldbach conjecture and computation of prime gaps up to `4·10¹⁸`", *Mathematics of Computation*
  **83** (2014), no. 288, 2033–2060. DOI `10.1090/S0025-5718-2013-02787-1`.
- **Fetch attempted:** the AMS page returned HTTP 403. Metadata (title/authors/volume/issue/pages/
  year/DOI) confirmed from search-result records; **the article text was not read.**
- **What it supplies:** the first-occurrence prime-gap table to `4·10¹⁸` that Kourbatov's
  verification rests on.
- **Evidence:** `kourbatov2015verification` ref. [6] cites it with exactly these coordinates and its
  Acknowledgements thank "Tomás Oliveira e Silva, Siegfried Herzog, and Silvio Pardi whose
  computation extended the table of first-occurrence prime gaps".
- **Downstream rule:** cite it only as *the computational basis reported by Kourbatov*, never for a
  statement read in it. **Flagged to the citation gate** as the one row whose text was never opened.

---

**`oeis_A182514`** — tier **L0**

- **Citation:** OEIS **A182514**, "Primes prime(n) such that `(prime(n+1)/prime(n))^n > n`".
- **Fetched:** <https://oeis.org/search?q=id:A182514&fmt=text> — version `#146 Jun 28 2026`.
- **Statements supplied:**
  - Terms: `2, 3, 7, 113, 1327, 1693182318746371` — the *near-misses*: primes where the naive
    `n`-bound (not `p_n`) is breached. Prime indices `1, 2, 4, 30, 217, 49749629143526`.
  - `%C` (J. W. Nicholson, Dec 02 2013 / Oct 19 2016): "[Stronger than Firoozbakht] conjecture: All
    `(prime(n+1)/prime(n))^n` values, with `n ≥ 5`, are less than `n·log(n)`." — **this is the
    primary published trace of Nicholson's conjecture**, which is otherwise unpublished.
  - `%C` (D. Forgues, Apr 26 2014): the weaker "Forgues conjecture"
    `(log p_{n+1}/log p_n)^n < e`.
  - `%C` (T. Ordowski, Mar 16 2015): the defining inequality "is equivalent to
    `prime(n+1) − prime(n) > log(n)·log(prime(n))` for sufficiently large n".
- **Downstream use:** the `1693182318746371` term recurring here *and* as the CSG record in A111943
  is the same event seen from two angles — worth one sentence in the paper.

---

### 2.4 The strengthenings — Nicholson and Farhadian

---

**`visser2019verifying`** — tier **L0**

- **Citation:** Matt Visser, "Verifying the Firoozbakht, Nicholson, and Farhadian conjectures up to
  the 81st maximal prime gap", arXiv:1904.00499v2 [math.NT], 8 Apr 2019, 10 pp.
- **Fetched:** <https://arxiv.org/pdf/1904.00499>, MD5 `d0281c2af1ef65cffdab81b5977e6bc2`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | **Conjecture 3**, eqs. (2.4)–(2.6) | `g_n ≤ p_n(p_n^{1/n} − 1)` (n ≥ 1; Firoozbakht); `g_n ≤ p_n((n ln n)^{1/n} − 1)` (n > 4; Nicholson); `g_n ≤ p_n((p_n ln n/ln p_n)^{1/n} − 1)` (n > 4; Farhadian). |
  | **Conjecture 1**, eq. (1.1) | Firoozbakht, two most common versions: `(p_{n+1})^{1/(n+1)} ≤ (p_n)^{1/n}`; equivalently `ln p_{n+1}/(n+1) ≤ ln p_n/n`. |
  | **Conjecture 2**, eqs. (2.1)–(2.3) + following sentence | "the standard inequalities `n ln n < p_n < n ln p_n` show that **Farhadian ⟹ Nicholson ⟹ Firoozbakht**." |
  | §1, eq. (1.3) | Kourbatov's sufficient condition restated: `g_n ≤ ln²p_n − ln p_n − 1.17` (n ≥ 10; p_n ≥ 29). |
  | §1, eq. (1.4) + surrounding | "certainly the Firoozbakht conjecture holds for all primes `p < 2⁶⁴ = 18,446,744,073,709,551,616 ≈ 1.844×10¹⁹`. Note that this automatically verifies a strong form of Cramér's conjecture `g_n ≤ ln²p_n` (n ≥ 5; p_n ≥ 11)". |
  | Abstract | All three conjectures "unconditionally and explicitly verified for all primes below the location of the 81st maximal prime gap, certainly for all primes `p < 2⁶⁴`." |
  | §3, **Sufficient condition 2** | `g_n < (ln(n ln n) − 1)·ln(n ln n)` for `n > 4`, `n ≥ 2` — a *monotone* sufficient condition, obtained from Dusart's `p_n > n(ln(n ln n) − 1)`. |
  | Refs [24], [33], [34], [35] | Firoozbakht 1982 unpublished; Nicholson 2013 unpublished (traced to OEIS A182514); Farhadian's primepuzzles preprint; Farhadian–Jakimczuk, *Int. Math. Forum* **12** (2017), no. 12, 559–564. |

- **Verdict on decompose A11: RESOLVED.** The decomposition deliberately omitted the Nicholson and
  Farhadian statements as "recalled too vaguely to state safely". They are now available verbatim
  at an L0 locator and may be stated.
- **Downstream hazard:** Visser's §1 narrative reports *three different* frontier figures in
  sequence (`4×10¹⁸`, `1×10¹⁹`, `2⁶⁴`) as the history advanced. Quote `2⁶⁴` and the 81st-maximal-gap
  framing, not the intermediate values.

---

**`farhadian2017new`** — tier **L2_strong**

- **Citation:** R. Farhadian, R. Jakimczuk, "On a new conjecture of prime numbers", *International
  Mathematical Forum* **12** (2017), no. 12, 559–564. DOI `10.12988/imf.2017.7335`.
- **Not fetched** (article text not retrieved in this run).
- **Statement it is cited for:** Farhadian's conjecture, `(p_{n+1}/p_n)^n ≤ p_n^{ln n/ln p_n}` for
  `n > 4`.
- **Evidence:** identical coordinates given by two independent fetched L0 sources —
  `visser2019verifying` ref. [35] and `oeis_A182514` `%H`. The *statement* itself is available at
  L0 from Visser (Conjecture 2, eq. 2.3) and from Ferreira–Mariano (Conjecture 4.3).
- **Downstream rule:** cite Visser or Ferreira–Mariano for the statement; cite this row only for
  the attribution.

---

### 2.5 Consequences of Firoozbakht, and one unconditional partial result

---

**`ferreira2017consequences`** — tier **L0**

- **Citation:** Luan Alberto Ferreira, Hugo Luiz Mariano, "Some consequences of the Firoozbakht's
  conjecture", arXiv:1604.03496v2 [math.NT], 17 Mar 2017. Published as "Prime gaps and the
  Firoozbakht Conjecture", *São Paulo J. Math. Sci.* (2018), DOI `10.1007/s40863-018-0113-0`
  (the published version was **not** fetched; locators below are to the arXiv v2).
- **Fetched:** <https://arxiv.org/pdf/1604.03496>, MD5 `c389c4244d6a4e4a6f5451e47981e877`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | §1 | "In 1982 the Iranian mathematician Farideh Firoozbakht, from the University of Isfahan, conjectured the following: Let `{p_n}` be the sequence of prime numbers. Then the sequence `{ⁿ√p_n}` is strictly decreasing." |
  | **Theorem 2.2** | "If the Firoozbakht's conjecture is true, then `g_n < ln²(p_n) − ln(p_n) − 1, ∀ n ≥ 10`. In particular, `g_n < ln²(p_n) − ln(p_n), ∀ n ≥ 5`, and `limsup_{n→∞} g_n/ln²(p_n) ≤ 1`." — **the last clause is exactly decompose's Corollary A1, and it is published.** Proof is marked "(Following [15])" = Kourbatov; the underlying `π(x)` input is Axler Corollary 3.6. |
  | **Theorem 2.3** | "If `g_n < ln²(p_n) − ln(p_n) − 1,17, ∀ n ≥ 10`, then the Firoozbakht's conjecture is true." — **stated without proof**, "we refer the reader to [15]" = Kourbatov Thm 3. Not an independent derivation. |
  | **Theorem 3.1** (attributed) | Baker–Harman–Pintz: `g_n ≤ p_n^{0.525}` for `n ≫ 0`. "It is easy to see that Firoozbakht's conjecture improves the Baker-Harman-Pintz's bound significantly." |
  | **Lemma 3.2** | If Firoozbakht is true, then `g_n < √n` for all `n ≥ 3645`. |
  | **Consequence 3.3** (Sierpiński) | Firoozbakht ⟹ every row of the `n × n` array of `1…n²` contains at least one prime (and, for each `k`, at least `k` primes for `n ≥ n₀(k)`). |
  | **Theorem 4.4** | `p_n > n ln n` for all `n` (Rosser); and `ln n + ln ln n − 1 < p_n/n < ln n + ln ln n` for `n ≥ 6`. |
  | **Theorem 4.5** | "**Farhadian ⟹ Nicholson ⟹ Firoozbakht ⟹ Forgues.**" With proof. |
  | **Theorem 5.1** (attributed) | Zhang: `liminf g_n < ∞`. Ref. [20] = Y. Zhang, "Bounded gaps between primes", *Ann. of Math.* **179** (2014), no. 3, 1121–1174. |
  | **Theorem 5.2** | "**There are infinitely many `n ∈ N` such that `ⁿ√p_n > ⁿ⁺¹√p_{n+1}`.**" — i.e. Firoozbakht's inequality holds infinitely often, **unconditionally**, as a consequence of bounded gaps. Proof given in full, "(Following [12])" = Ferreira's own 2016 USP PhD thesis. |

- **Why this row matters most after Kourbatov and Granville:** **Theorem 5.2 is the only
  unconditional theorem in this ledger that says something positive about the conjecture itself.**
  The `decompose` leg did not have it. It should be stated in the final paper.
- **Downstream hazard:** Theorem 5.2 is "infinitely often", not "eventually". It is compatible with
  infinitely many failures. Do not let it drift into "F holds for large n".

---

**`sun2013sequence`** — tier **L0**

- **Citation:** Zhi-Wei Sun, "On a sequence involving sums of primes", *Bulletin of the Australian
  Mathematical Society* **88** (2013), 197–205. arXiv:1207.7059.
- **Fetched:** <https://arxiv.org/pdf/1207.7059>, MD5 `5a087b883aa2b17d49f6d424f7dc32ff`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | §1, opening | "The unsolved Firoozbakht conjecture (cf. [R, p. 185]) asserts that `ⁿ√p_n > ⁿ⁺¹√p_{n+1}` for all `n ∈ Z⁺`, i.e., the sequence `(ⁿ√p_n)_{n≥1}` is strictly decreasing." |
  | §1, next sentence | "This implies the inequality `p_{n+1} − p_n < log²p_n − log p_n + 1` for large n, which is even stronger than Cramér's conjecture `p_{n+1} − p_n = O(log²p_n)`." |
  | §1 | `P_n` = product of first `n` primes ⟹ `(ⁿ√P_n)_{n≥1}` is strictly **increasing** (elementary, proved in one line). |
  | **Theorem 2.1** | The sequences `(ⁿ√S_n)_{n≥2}` and `(ⁿ√(S_n/n))_{n≥1}` are strictly decreasing, where `S_n = p_1 + … + p_n`. |
  | Remark 2.2 | Theorem 2.1 is offered explicitly as the *provable analogue* of Firoozbakht. |

- **Verdict on decompose A3: Sun's variant CONFIRMED, and it is the `+1` form** — i.e. **weaker**
  than Kourbatov's `−1`. The decomposition guessed this correctly. Kourbatov's `−1` (Theorem 1) is
  the sharp one and is the one to use.
- **Downstream use:** Theorem 2.1 is the natural "what *can* be proved in this shape" contrast for
  the paper's framing.

---

### 2.6 The analytic toolbox — effective bounds

---

**`dusart2010estimates`** — tier **L0**

- **Citation:** Pierre Dusart, "Estimates of some functions over primes without R.H.",
  arXiv:1002.0442v1 [math.NT], 2 Feb 2010.
- **Fetched:** <https://arxiv.org/pdf/1002.0442>, MD5 `b6540b68b8083df37266f57fab34db68`.
- **Statements supplied:**

  | Locator | Exact statement |
  |---|---|
  | **Theorem 6.9**, eq. (6.5) | `(x/ln x)(1 + 1/ln x) ≤ π(x)` for `x ≥ 599`; `π(x) ≤ (x/ln x)(1 + 1.2762/ln x)` for `x > 1`. |
  | **Theorem 6.9**, eq. (6.6) | `x/(ln x − 1) ≤ π(x)` for `x ≥ 5393`; `π(x) ≤ x/(ln x − 1.1)` for `x ≥ 60184`. |
  | **Proposition 6.6** | `p_k ≤ k(ln k + ln₂k − 1 + (ln₂k − 2)/ln k)` for `k ≥ 688383`. |
  | **Proposition 6.7** | `p_k ≥ k(ln k + ln₂k − 1 + (ln₂k − 2.1)/ln k)` for `k ≥ 3`. |
  | **Proposition 6.8** | For all `x ≥ 396738` there is a prime `p` with `x < p ≤ x(1 + 1/(25 ln²x))`. |
  | Ref [6] | Dusart, "The k-th prime is greater than `k(ln k + ln ln k − 1)` for `k ≥ 2`", *Math. Comp.* **68** (1999), 411–415. |

- **Supports:** decompose §2 P4 (effectivity), §3.6/S6 (the smooth model `x ↦ (log x + log log x)/x`)
  — Propositions 6.6/6.7 are *exactly* the two-sided form the smooth model needs, and they are
  effective. Also the `π(x) < x/(ln x − 1.1)` bound that Kourbatov's verification runs on.
- **Note:** the later Dusart, "Explicit estimates of some functions over primes", *Ramanujan J.*
  **45** (2018), 227–251, DOI `10.1007/s11139-016-9839-4`, sharpens these. Its text was **not**
  fetched (the one open copy found served an expired TLS certificate). Recorded here as a pointer,
  **not** as a ledger row.

---

**`axler2014newbounds`** — tier **L2_strong**

- **Citation:** Christian Axler, "New bounds for the prime counting function `π(x)`",
  arXiv:1409.1780 (2014); with Corrigendum, *Integers* **16** (2016), A22, 15 pp.
- **Not fetched.**
- **Statements it is cited for, at the locators Kourbatov records:**
  - **Corollary 3.6:** `x/(log x − 1 − 1/log x − 1/log²x) < π(x)` for `x ≥ 1772201`.
  - **Corollary 3.5:** `log x − 1 − 1.17/log x < x/π(x)` for `x ≥ 2634800823` (this range is the
    subject of the Corrigendum); plus a family of upper bounds
    `π(x) < x/(log x − 1 − 1/log x − 3.83/log²x)` for `x ≥ 9.25`, etc.
- **Evidence:** `kourbatov2015bounds` quotes these at exactly these corollary numbers in the proofs
  of its Theorems 1, 3, 4 and 5, and its §7 Corrigendum cites Axler's own *Integers* corrigendum.
- **Downstream rule:** these are the effective `π(x)` bounds that make Kourbatov's Theorems 1/3/5
  *rigorous*. If the final paper reproves anything in that chain, Axler must be fetched to L0
  first. **Flagged to the citation gate.**

---

**`baker2001difference`** — tier **L1**

- **Citation:** R. C. Baker, G. Harman, J. Pintz, "The difference between consecutive primes, II",
  *Proceedings of the London Mathematical Society* **83** (2001), no. 3, 532–562. DOI
  `10.1112/plms/83.3.532`.
- **Fetched:** <https://academic.oup.com/plms/article-abstract/83/3/532/1479119> — **abstract page
  only**; the full text is paywalled.
- **Abstract, verbatim:** "The authors sharpen a result of Baker and Harman (1995), showing that
  `[x, x + x^{0.525}]` contains prime numbers for large x. An important step in the proof is the
  application of a theorem of Watt (1995) on a mean value containing the fourth power of the zeta
  function."
- **Why L1:** publication data and the theorem statement are read at the publisher's own page, but
  no numbered theorem locator inside the paper was obtained.
- **Corroboration:** `ferreira2017consequences` Theorem 3.1 states it as `g_n ≤ p_n^{0.525}` for
  `n ≫ 0` and attributes it to this paper.
- **Supports:** decompose §2 P3a. The decomposition's own note — that the qualitative point (a power
  of `p`, not a power of `log`) is what matters — holds.

---

**`ford2016large`** — tier **L1**

- **Citation:** Kevin Ford, Ben Green, Sergei Konyagin, Terence Tao, "Large gaps between consecutive
  prime numbers", *Annals of Mathematics* **183** (2016), no. 3, 935–974. DOI
  `10.4007/annals.2016.183.3.4`. arXiv:1408.4505.
- **Fetched:** <https://arxiv.org/abs/1408.4505> and
  <https://annals.math.princeton.edu/2016/183-3/p04> — **abstract pages**; the full PDF was not
  retrieved.
- **Abstract, verbatim:** "Let `G(X)` denote the size of the largest gap between consecutive primes
  below `X`. Answering a question of Erdős, we show that
  `G(X) ≥ f(X) · log X log log X log log log log X / (log log log X)²`, where `f(X)` is a function
  tending to infinity with `X`. Our proof combines existing arguments with a random construction
  covering a set of primes by arithmetic progressions."
- **Supports:** decompose §3 S3 and the "not viable" verdict on constructing a counterexample gap —
  and it **confirms the decomposition's arithmetic**: this best-known lower bound exceeds `log X` by
  an iterated-log factor and remains a full power of `log` below the `log²X` a counterexample needs.
- **Downstream hazard:** the decomposition's §3 quotes the exponent on `log log log X` as `1`
  ("`/log log log n`"); the published abstract has **`(log log log X)²`**. Use the abstract's form.

---

**`shanks1964maximal`** — tier **L2_weak**

- **Citation:** Daniel Shanks, "On maximal gaps between successive primes", *Mathematics of
  Computation* **18** (1964), no. 88, 646–651. DOI `10.2307/2002951`.
- **Not fetched.**
- **What it is cited for:** the "Shanks side" of the Shanks-vs-Granville disagreement — that the CSG
  ratio never reaches 1; and the reformulation `p_n ≈ e^{(1+o(1))√g}` for the first occurrence of a
  gap of size `g`.
- **Evidence:** the reformulation is stated at L0 in `granville1995cramer` p. 10 ("Shanks
  reformulated this statement to suggest that the first occurrence of a gap … of size > g would
  occur with `p_n = e^{(1+o(1))√g}`"); the "never reaches 1" conjecture is stated at L0 in
  `oeis_A111943` `%C`, which links this DOI.
- **Downstream rule:** cite Granville or A111943 for the content; this row is the attribution only.

---

### 2.7 Formalization substrate (Lean 4 / Mathlib)

---

**`mathlib_nat_nth`** — tier **L0**

- **Citation:** `Mathlib.Data.Nat.Nth`, mathlib4 documentation,
  <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Nth.html> (fetched
  2026-07-25).
- **Statements supplied:**
  - Module docstring, verbatim: "This file defines a function for 'what is the nth number that
    satisfies a given predicate p', and provides lemmas that deal with this function and its
    connection to `Nat.count`."
  - **`noncomputable def Nat.nth (p : ℕ → Prop) (n : ℕ) : ℕ`**
  - `theorem Nat.nth_lt_nth {p : ℕ → Prop} (hf : (Set.ofPred p).Infinite) {k n : ℕ} : nth p k < nth p n ↔ k < n`
  - `theorem Nat.count_nth {p : ℕ → Prop} [DecidablePred p] {n : ℕ} (hn : ∀ (hf : (Set.ofPred p).Finite), n < hf.toFinset.card) : count p (nth p n) = n`
  - `@[simp] theorem Nat.nth_count {p : ℕ → Prop} [DecidablePred p] {n : ℕ} (hpn : p n) : nth p (count p n) = n`
- **Load-bearing consequence — this row settles a decompose §5.2 claim:** `Nat.nth` is declared
  **`noncomputable`**. The decomposition asserted that `Nat.nth Nat.Prime n` "is not efficiently
  kernel-reducible" so `decide` stalls on *producing* `p_n`. The documentation shows the situation
  is stronger than "inefficient": the definition is noncomputable, so there is no kernel reduction
  at all. The recommended workaround (prime literals + `Nat.Prime` certificates + a "no prime
  strictly between" lemma + `norm_num`) is **correct and is in fact mandatory**, not merely faster.
- **`Nat.nth_lt_nth`** is the strict-monotonicity lemma the `p_{n+1} > p_n` steps will need, and it
  requires an `Infinite` hypothesis — i.e. `Nat.infinite_setOf_prime` must be threaded in.

---

**`mathlib_nat_prime_nth`** — tier **L0**

- **Citation:** `Mathlib.Data.Nat.Prime.Nth`, mathlib4 documentation,
  <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Nth.html>
  (fetched 2026-07-25).
- **Contents, as listed:** exactly five `@[simp]` lemmas —
  `Nat.nth_prime_zero_eq_two` (`nth Prime 0 = 2`), `Nat.nth_prime_one_eq_three`,
  `Nat.nth_prime_two_eq_five`, `Nat.nth_prime_three_eq_seven`,
  `Nat.nth_prime_four_eq_eleven`.
- **Load-bearing consequence:** Mathlib's *prime-specific* `nth` API is **five base cases and
  nothing else** — no `p_n` growth bound, no `π`/`nth` bridge specialised to primes, no gap lemmas.
  Any Lean leg must budget for building that scaffolding itself. The decomposition's §6 "honest
  expectation" is, if anything, generous.
- **Note on indexing:** Mathlib's `nth` is **0-indexed** (`nth Prime 0 = 2`) while the conjecture as
  posed in this run is **1-indexed** (`p_1 = 2`). The off-by-one must be fixed *in the statement
  file* (L1) or every downstream index threshold — `n ≥ 10`, `k > 9`, `n ≥ 3645` — will be wrong by
  one. **This is the single most likely source of a silent error in the Lean legs.**

---

## 3. Coverage of the `decompose` leg's recall list (§7 A1–A12)

Every A-tag from the upstream decomposition, and what this ledger did to it.

| A-tag | Recalled as | Ledger verdict | Row(s) |
|---|---|---|---|
| A1 | Firoozbakht 1982, via Ribenboim 2004 | **Confirmed.** 1982, unpublished; Ribenboim p. 185 attested twice. | `firoozbakht1982unpublished`, `ribenboim2004little` |
| A2 | Kourbatov, verified to `4·10¹⁸` | **Confirmed but SUPERSEDED** — frontier is `2⁶⁴ ≈ 1.844·10¹⁹`. | `kourbatov2015verification`, `visser2019verifying` |
| A3 | Sun/Kourbatov: `F ⟹ g_n < log²p_n − log p_n − 1`, `n ≥ 10` | **Confirmed at L0**, and the `n ≥ 10` threshold is real (Kourbatov Thm 1: `k > 9`). Sun's is the weaker `+1` variant. | `kourbatov2015bounds` Thm 1; `sun2013sequence` §1 |
| A4 | "converse-direction criteria" — *unsourced, do not build on* | **RESOLVED.** Kourbatov Theorem 3: `b = 1.17` is sufficient. Theorem 4 gives a `b → 1` family. | `kourbatov2015bounds` Thms 3–4 |
| A5 | Baker–Harman–Pintz 2001, `g_n ≪ p_n^{0.525}` | **Confirmed** (abstract read at publisher). | `baker2001difference` |
| A6 | Dusart, explicit `π(x)` | **Confirmed at L0**, with exact theorem numbers, plus two-sided `p_k` bounds. | `dusart2010estimates` |
| A7 | Ford–Green–Konyagin–Maynard–Tao | **Confirmed**, published in *Annals* 183 (2016). Exponent correction below. | `ford2016large` |
| A8 | Cramér 1936, `limsup = 1` | **Confirmed at L0** — with the model-vs-primes nuance made explicit. | `cramer1936order` pp. 24, 27 |
| A9 | Granville 1995, `2e^{−γ} ≈ 1.1229`, contradicts Cramér | **CONFIRMED VERBATIM — constant and direction both correct.** The refutation-side argument stands. | `granville1995cramer` pp. 2, 10, 12 |
| A10 | Record CSG ratio `≈ 0.9206`, gap 1132 at `p ≈ 1.693·10¹⁵` | **Confirmed to 4 d.p.** (`0.92063858855742`), Nyman 1999. | `oeis_A111943` + Nicely |
| A11 | Nicholson, Farhadian — *statements deliberately omitted* | **RESOLVED.** Both statements now available verbatim, with the implication chain. | `visser2019verifying` Conj. 2–3; `ferreira2017consequences` Thm 4.5 |
| A12 | Oliveira e Silva–Herzog–Pardi 2014 | **Metadata confirmed; text not read** (AMS 403). Lowest-confidence row. | `oliveira2014goldbach` |

**Score: 12/12 addressed. 9 at L0/L1, 3 at L2. Zero rows remain at L3.**

---

## 4. Corrections the ledger forces on the `decompose` leg

Stated plainly, because a ledger that quietly agrees with the document it audits has not been used.

1. **The verified frontier is `2⁶⁴ ≈ 1.8447·10¹⁹`, not `4·10¹⁸`.** Kourbatov's own 2023 endnote to
   arXiv:1503.01744 and Visser's abstract both say so. The decomposition's §8.6 ("twelve orders of
   magnitude short of the recalled published frontier `4·10¹⁸`") should read **≈12.8 orders** short
   of `2⁶⁴`. *(The in-run sieve reached `3·10⁶`; `2⁶⁴/3·10⁶ ≈ 6.1·10¹²`, i.e. `log₁₀ = 12.79`. The
   original figure of 12 was computed against `4·10¹⁸`, where `log₁₀ = 12.12` — so the
   decomposition's arithmetic was right for the frontier it believed in.)*

2. **The FGKMT exponent is squared.** The decomposition writes the large-gap bound with
   `/ log log log n`; the published abstract has **`/(log log log X)²`**. The strategic conclusion
   ("still a full power of `log` below `log²`") is unaffected — the correction makes the gap
   *larger*, so the "not viable" verdict on S3 is if anything safer.

3. **"Claim A" is not new — it is Kourbatov's Theorem 5 (2015).** The decomposition presents
   `T_n = log²p_n − log p_n − 1 + O(1/L)` as an in-run derivation with `[needs-anchor]` on the
   effectivity. It is published, with an explicit error term
   (`log²p_k − log p_k − 1 − 3.83/log p_k < f_k < log²p_k − log p_k − 1`), resting on Axler's
   `π(x)` bounds. **The decomposition's declared gap §8.3 ("Claim A's `O(1/L)` is not made
   effective") is already closed in the literature.** Do not re-derive; cite.

4. **A4 is no longer an open hole.** The decomposition marked converse-direction criteria "do not
   build on until sourced". They are sourced: **Kourbatov Theorem 3** — `g_k < log²p_k − log p_k −
   1.17` for all `k > 9` **implies** Firoozbakht — plus the `b → 1` family of Theorem 4. A
   sufficient condition exists and is explicit.
   **Caveat, and it matters for the citation gate:** Ferreira–Mariano Theorem 2.3 restates this but
   is *not* an independent confirmation — it carries no proof, only "we refer the reader to [15]"
   (= Kourbatov). Likewise their Theorem 2.2 is proved "(Following [15])". **The entire
   sufficient-condition result rests on a single author and, beneath him, on Axler's Corollary 3.5 —
   the corollary whose range of validity Axler himself had to correct.** Treat this chain as
   single-threaded, not corroborated.

5. **There is an unconditional theorem the decomposition did not have.** Ferreira–Mariano
   **Theorem 5.2**: Firoozbakht's inequality holds for **infinitely many `n`**, unconditionally, via
   Zhang's bounded gaps. This belongs in the paper. It is "infinitely often", not "eventually".

6. **Cramér did not conjecture `limsup = 1` about the primes — he proved it about his model.**
   Read at p. 27 of the original. The decomposition's §3.3/§4.4 phrasing should be tightened; so
   should any sentence in the final paper of the form "Cramér conjectured that…".

7. **`Nat.nth` is `noncomputable`, not merely slow.** The decomposition's §5.2 correction was right
   in its conclusion and understated in its reason. The literal-plus-certificate route is mandatory.

8. **Mathlib is 0-indexed on `nth`; this run's statement is 1-indexed.** Not mentioned anywhere
   upstream. Every index threshold in the literature (`k > 9`, `n ≥ 10`, `n ≥ 3645`, `n ≥ 5`) is
   stated in the 1-indexed convention. Fix once, in the L1 statement file.

9. **A sharper empirical bar than the decomposition's exists.** Kourbatov's OEIS comment: Firoozbakht
   implies the CSG ratio is below `1 − 1/log p` for all `p ≥ 11`. At the record (`p ≈ 1.69·10¹⁵`,
   `log p ≈ 35.1`) that bar is `≈ 0.9715` against an observed `0.9206` — a margin of about **5.2%**,
   which corroborates the decomposition's §4.3 estimate of "roughly 5%" and is now sourced rather
   than recalled.

---

## 5. EXTERNAL PRIOR ART — *outside the citable ledger*

**Nothing in this section is a source. Nothing downstream may cite it as literature.** It is listed
so that the record of what informed this run is complete, and so that no reader mistakes a run
artefact for a reference.

| Item | Provenance | Status |
|---|---|---|
| `attack/decompose.md` (636 lines) | Produced by molecule `task-20260725-c062`, leg `decompose`, **this run** (`germ-20260725-791a7c45`), 2026-07-25. Self-declared: all of its §7 is unverified recall at tier L3. | **Run artefact.** It is the *object* this ledger audits, never a citation. Its §5.1 computations were performed in-run and are unpublished. |
| `attack/frame-deliberation/{frame,synthesis,outcomes}.md` + `responses/{wheeler,godel,knuth,feynman,popper}.md` | Produced by the `frame-deliberation` leg, **this run**, 2026-07-25. Multi-persona deliberation output. | **Run artefact.** Opinion, not literature. |
| `attack/probe.py`, `attack/probe2.py` | Sieve/verification scripts written in-run. | **Run artefact.** |
| `trace/` (`build_trace.py`, `events.jsonl`, `hashes.tsv`, `briefs.md`) | Orchestrator provenance for this run. | **Run artefact.** |

**Survey of the working tree performed 2026-07-25.** The repository
`/Users/eserie/galaxies/firoozbakht-cleanroom` contains **no** mathematical document of external
origin — no downloaded paper, no third-party note, no vendored proof. Every `.md` and `.py` in the
tree was generated by this run. **There is no external prior art in the working tree.** The
cleanroom is clean.

*Note on the fetched PDFs:* the seven PDFs I retrieved and read live in the session scratchpad at
`/private/tmp/claude-501/…/scratchpad/`, **not** in the repository. They are not committed. Their
MD5s are recorded per-row above so that a later leg can re-fetch and confirm it read the same bytes.

---

## 6. Declared gaps — what this ledger does NOT establish

Stated so no downstream leg mistakes silence for coverage.

1. **Ribenboim's book was not opened.** `p. 185` rests on two independent citers. If the paper wants
   the origin at L0, fetch the book.
2. **Oliveira e Silva–Herzog–Pardi was not opened** (AMS returned 403). It is the only row whose text
   I never saw. Everything it supports is mediated through Kourbatov.
3. **Axler was not opened.** Corollaries 3.5 and 3.6 are quoted through Kourbatov's proofs. Since
   Kourbatov's Theorems 1, 3 and 5 *depend* on them, and since Axler's own corrigendum materially
   changed the range of validity of Corollary 3.5 (from `x ≥ 5.43` to `x ≥ 2634800823`), this is the
   most consequential unopened source in the ledger. **Priority 1 for the citation gate.**
4. **Granville's pagination is the preprint's, not the journal's.** Preprint pp. 1–16 vs journal
   pp. 12–28. All Granville locators must be re-expressed against the journal copy, or explicitly
   marked "preprint pagination", before publication. **Priority 2 for the citation gate.**
5. **Baker–Harman–Pintz and Ford–Green–Konyagin–Maynard–Tao: abstracts only.** No internal theorem
   numbers. Adequate for the qualitative use both are put to; inadequate if any constant is quoted.
6. **Dusart (2018, *Ramanujan J.*) and Farhadian–Jakimczuk (2017) were not fetched.** The one open
   copy of the former served an expired TLS certificate; I did not bypass it.
7. **Shanks (1964) was not opened.** Both things it is cited for are available at L0 elsewhere.
8. **No source in this ledger proves or refutes the conjecture.** After a full sweep of the primary
   literature: the conjecture is open. The strongest unconditional statements available are
   (a) it holds for all `p < 2⁶⁴`, and (b) it holds for infinitely many `n`. Neither is close to a
   proof, and nothing found here refutes it.
9. **Nicholson's conjecture has no publication.** Its only citable trace is an OEIS comment
   (A182514, J. W. Nicholson, 2013/2016) and Visser's restatement. Attribute accordingly.
10. **The Lean rows are documentation snapshots, not a pinned toolchain check.** They were read from
    the *current* mathlib4 docs on 2026-07-25. Names drift. The `lean-probe` leg must re-confirm
    against whatever toolchain is actually pinned. This ledger does not substitute for that.

---

## 7. Priority order for the citation gate

1. `axler2014newbounds` — load-bearing under Kourbatov Thms 1/3/5; a corrigendum already moved one
   of its ranges by nine orders of magnitude.
2. `granville1995cramer` — the refutation-side argument. Content confirmed; **pagination is not**.
3. `ribenboim2004little` — the origin locator, second-hand.
4. `oliveira2014goldbach` — the empirical foundation, never opened.
5. Everything else — L0, statement read at the recorded locator.

---

## 8. BibTeX

```bibtex
@article{kourbatov2015bounds,
  author  = {Kourbatov, Alexei},
  title   = {Upper bounds for prime gaps related to {Firoozbakht's} conjecture},
  journal = {Journal of Integer Sequences},
  volume  = {18},
  year    = {2015},
  note    = {Article 15.11.2; arXiv:1506.03042v4 (with Corrigendum)},
  eprint  = {1506.03042},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@article{kourbatov2015verification,
  author  = {Kourbatov, Alexei},
  title   = {Verification of the {Firoozbakht} conjecture for primes up to four quintillion},
  journal = {International Mathematical Forum},
  volume  = {10},
  number  = {6},
  pages   = {283--288},
  year    = {2015},
  note    = {arXiv:1503.01744; endnotes added 5 Jan 2023 extend the range to $2^{64}$},
  eprint  = {1503.01744},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@article{cramer1936order,
  author  = {Cram{\'e}r, Harald},
  title   = {On the order of magnitude of the difference between consecutive prime numbers},
  journal = {Acta Arithmetica},
  volume  = {2},
  pages   = {23--46},
  year    = {1936}
}

@article{granville1995cramer,
  author  = {Granville, Andrew},
  title   = {Harald {Cram{\'e}r} and the distribution of prime numbers},
  journal = {Scandinavian Actuarial Journal},
  volume  = {1995},
  number  = {1},
  pages   = {12--28},
  year    = {1995},
  doi     = {10.1080/03461238.1995.10413946}
}

@article{ferreira2017consequences,
  author  = {Ferreira, Luan Alberto and Mariano, Hugo Luiz},
  title   = {Prime gaps and the {Firoozbakht} Conjecture},
  journal = {S{\~a}o Paulo Journal of Mathematical Sciences},
  year    = {2018},
  doi     = {10.1007/s40863-018-0113-0},
  note    = {Preprint: arXiv:1604.03496v2, ``Some consequences of the Firoozbakht's conjecture''},
  eprint  = {1604.03496},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{visser2019verifying,
  author  = {Visser, Matt},
  title   = {Verifying the {Firoozbakht}, {Nicholson}, and {Farhadian} conjectures up to the 81st maximal prime gap},
  year    = {2019},
  eprint  = {1904.00499},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@article{sun2013sequence,
  author  = {Sun, Zhi-Wei},
  title   = {On a sequence involving sums of primes},
  journal = {Bulletin of the Australian Mathematical Society},
  volume  = {88},
  pages   = {197--205},
  year    = {2013},
  eprint  = {1207.7059},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{dusart2010estimates,
  author  = {Dusart, Pierre},
  title   = {Estimates of some functions over primes without {R.H.}},
  year    = {2010},
  eprint  = {1002.0442},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@misc{axler2014newbounds,
  author  = {Axler, Christian},
  title   = {New bounds for the prime counting function $\pi(x)$},
  year    = {2014},
  eprint  = {1409.1780},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT},
  note    = {Corrigendum: {\em Integers} {\bf 16} (2016), A22, 15 pp.}
}

@article{baker2001difference,
  author  = {Baker, R. C. and Harman, G. and Pintz, J.},
  title   = {The difference between consecutive primes, {II}},
  journal = {Proceedings of the London Mathematical Society},
  volume  = {83},
  number  = {3},
  pages   = {532--562},
  year    = {2001},
  doi     = {10.1112/plms/83.3.532}
}

@article{ford2016large,
  author  = {Ford, Kevin and Green, Ben and Konyagin, Sergei and Tao, Terence},
  title   = {Large gaps between consecutive prime numbers},
  journal = {Annals of Mathematics},
  volume  = {183},
  number  = {3},
  pages   = {935--974},
  year    = {2016},
  doi     = {10.4007/annals.2016.183.3.4},
  eprint  = {1408.4505},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}

@book{ribenboim2004little,
  author    = {Ribenboim, Paulo},
  title     = {The Little Book of Bigger Primes},
  edition   = {2},
  publisher = {Springer},
  address   = {New York},
  year      = {2004},
  doi       = {10.1007/b97621}
}

@article{oliveira2014goldbach,
  author  = {Oliveira e Silva, Tom{\'a}s and Herzog, Siegfried and Pardi, Silvio},
  title   = {Empirical verification of the even {Goldbach} conjecture and computation of prime gaps up to $4\cdot10^{18}$},
  journal = {Mathematics of Computation},
  volume  = {83},
  number  = {288},
  pages   = {2033--2060},
  year    = {2014},
  doi     = {10.1090/S0025-5718-2013-02787-1}
}

@article{shanks1964maximal,
  author  = {Shanks, Daniel},
  title   = {On maximal gaps between successive primes},
  journal = {Mathematics of Computation},
  volume  = {18},
  number  = {88},
  pages   = {646--651},
  year    = {1964},
  doi     = {10.2307/2002951}
}

@article{farhadian2017new,
  author  = {Farhadian, Reza and Jakimczuk, Rafael},
  title   = {On a new conjecture of prime numbers},
  journal = {International Mathematical Forum},
  volume  = {12},
  number  = {12},
  pages   = {559--564},
  year    = {2017},
  doi     = {10.12988/imf.2017.7335}
}

@misc{oeis_A111943,
  author = {Sloane, N. J. A.},
  title  = {Sequence {A111943}: Prime $p$ with prime gap of $n$-th record {Cramer-Shanks-Granville} ratio},
  howpublished = {The On-Line Encyclopedia of Integer Sequences},
  note   = {\url{https://oeis.org/A111943}, version \#75, Nov 14 2025}
}

@misc{oeis_A182514,
  author = {Sloane, N. J. A.},
  title  = {Sequence {A182514}: Primes $\mathrm{prime}(n)$ such that $(\mathrm{prime}(n+1)/\mathrm{prime}(n))^n > n$},
  howpublished = {The On-Line Encyclopedia of Integer Sequences},
  note   = {\url{https://oeis.org/A182514}, version \#146, Jun 28 2026}
}

@misc{firoozbakht1982unpublished,
  author = {Firoozbakht, Farideh},
  title  = {Conjecture on the monotonicity of $p_n^{1/n}$},
  year   = {1982},
  note   = {Unpublished. First recorded in print in \cite{ribenboim2004little}, p.~185, and posted as
            Conjecture 30 at \url{https://www.primepuzzles.net/conjectures/conj_030.htm} (C. Rivera, ed., 2002)}
}

@misc{mathlib_nat_nth,
  author = {{The mathlib Community}},
  title  = {\texttt{Mathlib.Data.Nat.Nth} --- mathlib4 documentation},
  note   = {\url{https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Nth.html}, retrieved 2026-07-25}
}

@misc{mathlib_nat_prime_nth,
  author = {{The mathlib Community}},
  title  = {\texttt{Mathlib.Data.Nat.Prime.Nth} --- mathlib4 documentation},
  note   = {\url{https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Nth.html}, retrieved 2026-07-25}
}
```

---

## 9. Standing instruction to downstream legs

The conjecture is **open**. The literature sweep changes nothing about that verdict; it sharpens
both sides of it.

- The strongest *pro* statements now sourced: verified for all `p < 2⁶⁴` (`kourbatov2015verification`
  endnote, `visser2019verifying`), and true for infinitely many `n` unconditionally
  (`ferreira2017consequences` Thm 5.2).
- The strongest *contra* statement now sourced: the corrected Cramér model predicts
  `max gap ⪆ 2e^{−γ} log²x` with `2e^{−γ} ≈ 1.12292`, which contradicts Firoozbakht
  (`granville1995cramer`, preprint p. 12) — as a heuristic, not a proof.
- The observed record CSG ratio is `0.9206`; the Firoozbakht-implied ceiling at that size is
  `≈ 0.9715` (`oeis_A111943`). About 5% of headroom, and the record has stood since 1999.

Every claim in the final paper must name a citekey from §2 and a locator from that row's table.
A claim that cannot is a gap, and must be written as one.
