# Project standing rules

Read this at the start of every session.

## Project
- Question: In preterm/VLBW infants fed human milk, what is the evidence for timing, dose, product choice, and safety of human milk fortification (HMF) vs no/delayed/alternative fortification, on short-term growth/tolerance and long-term neurodevelopmental outcomes? (Full PICO and 8 secondary-question domains in RESEARCH-BRIEF.md.)
- Track: narrative review, systematised (search documented/reproducible; synthesis narrative not meta-analytic)
- Target journal: not yet fixed — candidates ADC Education & Practice, Seminars in Fetal & Neonatal Medicine, J Perinatology (decide after phase 4)
- PROSPERO ID: N/A (narrative review)

## Non-negotiables
- Nothing enters any file without a verified PMID or DOI retrieved this session. Do not use a citation recalled from training.
- Unverifiable references are removed and listed in 02-extraction/could-not-verify.md, never hedged into the text.
- Numbers are transcribed as reported, never re-derived or rounded. Mark `[abstract only]` where full text was unavailable.
- Every interventional claim carries a GRADE label (High/Moderate/Low/Very low) with a one-line reason naming the downgrade domain.
- Every claim flags whether evidence is direct or extrapolated (Domains 2 and 3 are where most extrapolation sits — flag explicitly).
- Null and non-replication findings get equal prominence to positive ones — this field has several underpowered positive single-centre reports and several large trials/Cochrane reviews with null results.
- Write findings to disk incrementally. Never hold a domain's findings in context only.
- Append every search string, source, date and hit count to 01-search-log/searches.md as it runs — append-only, including zero-hit searches.
- Say plainly when the evidence is weak or absent. Do not hedge into vagueness.

## Terminology lock (see RESEARCH-BRIEF.md Section 4)
- **HMF** = human/breast milk fortifier generically (working abbreviation throughout).
- **BMF** reserved exclusively for *bovine milk-based fortifier* when quoting a paper that uses it that way (e.g. N-forte/Jensen trial). Check every paper using "BMF" and record in `bmf_terminology_check` column — never let this collapse "whether/when to fortify" with "bovine vs human-milk-derived fortifier".
- Record each trial's fortification threshold verbatim in `fortification_definition` (mL/kg/d and/or postnatal day) rather than forcing early/late binary.
- Keep SIP and NEC as distinct pathologies in extraction even when a paper reports them combined.

## Structure
00-protocol/ 01-search-log/ 02-extraction/ 03-synthesis/ 04-manuscript/ 05-references/
Domain files: 03-synthesis/domain-1-timing-dose.md … domain-8-concentrated-targeted.md, plus cross-cutting-synthesis.md and prisma-style-flow-counts.md.

## Handoffs
reference-builder (verification) | clinical-figures (figures) | medical-academic-researcher (polish) | peer-reviewer (pre-submission critique)
