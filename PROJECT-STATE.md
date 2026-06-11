# IFE 2026 — AI Literacy Track · Project State Map

> Read-only orientation file. It records which artifact is canonical and what every
> other file in this folder is, so anyone opening the directory can find the true
> latest state. It changes no source content. Last reconciled: 2026-06-10.

## TL;DR

The **canonical, latest-greatest source is the Google Sheet "2026 IFE summer program
AI modules"** (in Drive, owned by edwin@cambiolabs.org). It carries all 14 AI blocks as
**companion modules inside the 23-day social-entrepreneurship calendar**, anchored to
Journey lessons. Everything in this folder is a predecessor of that sheet.

- Sheet: https://docs.google.com/spreadsheets/d/1yRyQ0prUEzAzXGa9CrdZbpCZmKWjhAqbL2LAVGa-EUU/edit
- File ID: `1yRyQ0prUEzAzXGa9CrdZbpCZmKWjhAqbL2LAVGa-EUU`

## Build status (2026-06-10)

The AI-delivery deliverables are built (OpenCode executor; see `AGENTS.md` work log):
- **`ife-2026-ai-instructor-guide.md`** — the **MASTER document** for the AI portion. Open
  this in the Claude desktop app (Fable 5) to generate the final shareable document.
- **`ife-2026-ai-modules-cards.html`** — block cards with inline SVGs.
- **`AGENTS.md`** — agent authority/coordination file (Claude Code = master orchestrator).

Framing decisions now locked into the master:
- ✅ **Cambio Ethos** add-on — greenlit; one per block, kept.
- ✅ **Social Change Model framing removed** — it was added by mistake by an earlier Opus
  run. The 9 C's were dropped by OpenCode; the residual "Capacities (Conceptual/Technical/
  Social)" objective labels were re-mapped to the v3 curriculum's own three legs
  (**conceptual frame / critical takeaway / technical artifact**). No SCM language remains.

## How the project evolved (why files disagree)

The thinking moved through three postures on 2026-06-10. Files on disk are scattered
across these stages — that is the source of all the version skew.

| Stage | Posture | Core idea |
|---|---|---|
| 1. Standalone track | AI track *dictates* | 14 AI "blocks" with their own names/numbering, run as a parallel curriculum |
| 2. Alignment + punch list | AI track *demands Journey rearrange* | 25-item punch list: "move 2.10," "pull 8.1 ahead," "unlock 5.7" |
| **3. Companion modules** ⭐ | AI track *complements* Journey | Each block re-presented as the "AI companion to" an existing Journey lesson; punch list collapses; coding spine becomes the operator-arc complement |

**Stage 3 is current.** It lives in the Google Sheet above. The on-disk files are Stage 1
and Stage 2.

## What each file in this folder is

| File | Role now |
|---|---|
| **(Google Sheet) 2026 IFE summer program AI modules** | ⭐ CANONICAL — live source of truth |
| `ife-2026-ai-instructor-guide.md` | **MASTER document** for the AI portion — feed to Claude desktop (Fable 5) to make the final doc. Cambio Ethos in; SCM framing out. |
| `ife-2026-ai-modules-cards.html` | Block cards (B1–B14) with inline SVGs. |
| `AGENTS.md` | Agent authority/coordination file. Claude Code = master orchestrator. |
| `AI Literacy Track v3.md` (+ `AI Literacy Track v3.pdf`) | Content reference — block detail (beats, timings, artifacts) is current and matches the sheet; the standalone framing is superseded |
| `ife-2026-train-the-trainer-terminal-blocks.md` | Still useful — only place with deep "run it at the terminal" facilitation depth (exact CLI sessions, recovery moves). Needs a companion-posture re-head. Standardizes Blocks 3/8/13 on Claude Code; Gemini CLI is the take-home alternative. |
| `ife-2026-alignment-calendar.xlsx` | SUPERSEDED — Stage-2 punch list. Its "move 2.10 / pull 8.1 / unlock 5.7" asks were all replaced by "banks when reached, no unlock needed." Do not action its punch list. |
| `AI Literacy Track v3 (Cambio).pdf` | Stale render of v3 (older footer, raw `[CHANGED]` tags). Redundant. |
| `cambio-labs-ai-literacy-track-ife-2026.pdf` | Earlier 28-page bundle (curriculum + train-the-trainer). Superseded by the sheet + the two `.md` files. |
| `_facilitator/quick-reference-card.md` | LEGACY — pre-v3 tool stack (llm CLI / ComfyUI / Langflow / Groq). Different, abandoned design. |
| `microlearning_capsules/*.html` | LEGACY — map to the abandoned quick-reference-card activities (e.g. grumpy_user). |
| `journey-content/journey-ai-anchor-lessons.md` | Live capture (2026-06-10) of every Journey lesson the 14 AI blocks companion to, by checkpoint, tagged to its block. Reference for the companion mapping. |
| `journey-content/CP1-initiation.md` | Full CP1 lesson capture (incl. onboarding/survey) — the capture-format sample. |
| `2026 IFE Course Planning.xlsx` | Planning sheet (high-level breakdown, hourly breakdown, curriculum, AI tracks comparison). Upstream input. |
| `hallucination_trap_activity.pdf`, `_facilitator/` generators & CSS | Supporting assets / PDF generation tooling. |
| `OpenHuman_*.dmg` | Unrelated installer; not part of the curriculum. |

## Canonical spine (from the live sheet's Index)

Single source of truth for block ↔ Journey ↔ AOT alignment. Days 1, 5, 9, 14, 19–23
carry Journey/pitch work with no AI module.

| Day | Date | AI Module | Journey anchors | AOT utilized |
|---|---|---|---|---|
| 2 | 6/30 Tue | B1 The Inheritance | 1.6 1.7 2.1 | foundations milestones → B1 history wall |
| 3 | 7/1 Wed | B2 Same Question, Different Mouths | 2.10 | Gen AI guidelines assignment = B2 cheat-sheet fold-in |
| 4 | 7/2 Thu | B3 The Sanity Report | 1.12 2.4 2.5 2.9 | candidate slot (confirm L# with D-Cal) |
| 6 | 7/6 Mon | B4 The Statistical Shadow | 2.3 2.6 2.9 5.1 5.7 | — |
| 7 | 7/7 Tue | B5 The Yes-Man | 2.8 2.9 4.2 | emerging risks: injection + poisoning (L7) → B5 |
| 8 | 7/8 Wed | B6 The Generation Game | 2.3 2.7 4.3 | — |
| 10 | 7/10 Fri | B7 The Stage Set | 3.10 4.8 | candidate slot — B7 is the live refresh of stale 4.8 |
| 11 | 7/13 Mon | B8 Not the Writer, Not the Designer | 4.4 8.1 | — |
| 12 | 7/14 Tue | B9 The Imaginary Friend | 1.9 | — |
| 13 | 7/15 Wed | B10 The Footnote | 2.8 5.4 6.1 6.3 | — |
| 15 | 7/17 Fri | B11 The Stack | 1.10 4.6 4.7 | — |
| 16 | 7/20 Mon | B12 The Invisible Market | 8.1 | — |
| 17 | 7/21 Tue | B13 The Automated Self | 4.7 7.1 | L7 AI agents → B13 concept tour |
| 18 | 7/22 Wed | B14 The Mark | 7.2 7.3 8.2 | — |

### How AI artifacts ride Journey lessons (no new lessons required)
- B3 flaw audit → submits as the **1.12** assignment
- Find Your User pre-work → rides as the **2.9** assignment (issued 7/2, due 7/6)
- B4 persona-vs-data chart → banks as **5.7** when students reach CP5
- B6 verified theme map → banks as **4.3** evidence
- B7 AI Integration Plan → banks as **4.8** (live refresh of the stale "How to Use AI in Your App")
- B8 vibe-coded asset → reads against **4.4 / 4.5** (HTML/CSS you didn't write)
- B13 coach.py → the **3.3–3.8** Python ladder is the path to modifying your own coach

## Journey platform structure (verified from screens)

CP1 Initiation (1.1–1.12) · CP2 Teams & Tracks (2.1–2.10) · CP3 Discovery (3.1–3.12) ·
CP4 (4.1–4.8) · CP5 (5.1–5.7) · CP6 Startup Experimentation (6.1–6.4) ·
CP7 Startup Financials (7.1–7.3) · CP8 Final Launchpad (8.1–8.4).

Known duplicates (residue of merging two course templates): 2.5 ≡ 3.11 (Stakeholder
Mapping), 2.6 ≡ 3.12 (Who's Your Customer), prototyping in 5.3 & 6.1, Lean Startup in
2.2 & 6.2. The Python spine (3.1–3.8) and web-dev (4.4–4.6) appear nowhere on the
planning sheet — under Stage 3 they are reframed as the operator-arc complement, not retired.

### Live capture findings (see `journey-content/journey-ai-anchor-lessons.md`)
On 2026-06-10 every AI-anchor lesson was captured from the platform. Key takeaways that
reinforce the companion posture:
- **Several anchors are empty submission shells** — 2.7, 2.8, **2.9 (all of customer
  discovery)**, **4.8 "How to Use AI in Your App"**, 1.9, 2.5. The AI blocks supply the
  teaching substance these Journey numbers lack — they're companions, not duplicates.
- **Live interview teaching lives in CP4** (4.2 Fieldwork Prep, 4.3 Empathy Research
  Challenge), not in the thin CP2 customer-discovery lessons.
- **Platform numbering is unstable** — the same lesson renders under different `x.y`
  numbers depending on the selected checkpoint. **Lesson UUIDs (recorded in the capture
  file) are the only reliable identifiers.** CP3 actually runs 3.1–3.14.

## Open items to fully close the loop

1. **D-Cal's AOT lesson list (L2–L6)** — needed to fill the "candidate" AOT slots (B3, B7)
   and the blank AOT cells. Confirmed already: L7 (B5, B13), foundations (B1), Gen AI
   guidelines (B2), and replacing stale 4.8.
2. **"Journey points: TBD"** on every day sheet — pending the gem values.
3. **`ife-2026-alignment-calendar.xlsx` contradicts the canonical sheet** — it still shows
   the abandoned punch list. Treat as superseded; do not action it.
