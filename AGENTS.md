# AGENTS.md — IFE 2026 AI Literacy Track

## Chain of Authority

**Claude Code is the master orchestrator** and canonical decision-maker for the IFE 2026 AI Literacy Track project. It owns the instructor guide (`ife-2026-ai-instructor-guide.md`), scope decisions, and all canonical sources.

**OpenCode and any other agents are executors.** No agent may:
- Change scope or redefine deliverables without Claude Code sign-off
- Modify canonical source files (PROJECT-STATE.md, AI Literacy Track v3.md, terminal-blocks.md, journey-content/ files)
- Supersede decisions recorded in PROJECT-STATE.md
- Modify the original Google Sheet or any Google Drive source

## Canonical Sources

1. **Google Sheet "2026 IFE summer program AI modules"** — the single source of truth
   `https://docs.google.com/spreadsheets/d/1yRyQ0prUEzAzXGa9CrdZbpCZmKWjhAqbL2LAVGa-EUU/edit`
2. **PROJECT-STATE.md** — the authoritative map; treat as ground truth for module list, ordering, dates, Journey anchors, and AOT notes
3. **journey-content/journey-ai-anchor-lessons.md** — live capture of Journey lesson content; use for accurate "AI companion to" references. Lesson UUIDs are canonical (x.y numbering is unstable)
4. **AI Literacy Track v3.md** — content reference for block beats, timings, and artifacts
5. **ife-2026-train-the-trainer-terminal-blocks.md** — facilitation depth for Blocks 3, 8, 13
6. **_facilitator/cambio-colors.css** and **literacy-track.css** — brand colors and typography

## Scope Guardrails

- **Deliverables cover ONLY the AI delivery portion** (14 companion modules B1–B14)
- This is NOT the full youth social entrepreneurship curriculum — that is the Journey platform (CP1–CP8), delivered by others
- The AI modules COMPLEMENT Journey; reference Journey anchors but do NOT document Journey lessons themselves
- Hold the complementary posture throughout: the AI layer supports Journey, it does not dictate it

### Superseded / Legacy Files — DO NOT USE

| File | Reason |
|------|--------|
| `ife-2026-alignment-calendar.xlsx` | Stage-2 punch list, superseded by companion posture |
| `AI Literacy Track v3 (Cambio).pdf` | Stale render, superseded by v3.md |
| `cambio-labs-ai-literacy-track-ife-2026.pdf` | Earlier bundle, superseded |
| `_facilitator/quick-reference-card.md` | Pre-v3 tool stack, abandoned design |
| `microlearning_capsules/*.html` | Legacy activities, abandoned |
| `*(Cambio).pdf` / `cambio-labs-*.pdf` | All PDF renders are legacy |
| `ife-2026-projector.html` | Misinterpretation — was slideshow, replaced by ife-2026-ai-selector.js |
| Google Drive originals | Read-only; do not modify |

## File Inventory

| File | Status | Owner |
|------|--------|-------|
| `ife-2026-ai-modules-cards.html` | Created 2026-06-10 (1st pass: SVGs) | OpenCode (executor) |
| `ife-2026-block-cards.html` | Updated 2026-06-11 (Cambio V1.0 design system applied) | OpenCode (executor) |
| `ife-2026-projector.html` | SUPERSEDED — see ife-2026-ai-selector.js | OpenCode (executor) |
| `ife-2026-ai-selector.js` | Created 2026-06-11 (interactive terminal selector) — SUPERSEDED by ife-2026-terminal-app.html | OpenCode (executor) |
| `ife-2026-terminal-app.html` | Created 2026-06-11 (web-based terminal emulator, replaces node TUI) | OpenCode (executor) |
| `IFE 2026 AI Selector.app` | Created 2026-06-11 (macOS .app bundle with custom icon) | OpenCode (executor) |
| `ife-2026-ai-instructor-guide.md` | Created 2026-06-10 | Claude Code (owner) |
| `AGENTS.md` | Created 2026-06-10 | OpenCode (executor) |

## Work Log

### Entry 2026-06-10 — OpenCode executor build (update 1: Cambio Ethos)

**Created files:**

1. **ife-2026-ai-modules-cards.html** — Updated HTML block cards with custom inline SVGs. One card per AI module B1–B14 in canonical order with dates from PROJECT-STATE.md. Each card includes: block number + name, calendar day + date, conceptual frame, critical takeaway, technical artifact, Journey companion anchors (with shell notes where applicable), and AOT notes. Dark theme using Cambio brand colors (purple, teal, coral, amber). Responsive grid, print-friendly, no external deps except Google Fonts.

2. **ife-2026-ai-instructor-guide.md** — Formal instructional document for the AI Lead. Front matter with scope statement, ops playbook (10 pods, TA zones, demo protocol, submission system, clock discipline), tool stack, and TOC. All 14 modules follow the same template: module header, learning objectives (Capacities framing), Cambio Ethos assessment, materials & prep, minute-by-minute timed run of show, facilitation script, recovery notes, human-judgment close, deliverable & assessment. B3/B8/B13 mine the detailed terminal sessions from the train-the-trainer guide. Social Change Model references removed and replaced with unique Cambio Ethos blocks per module (2026-06-10 update).

3. **AGENTS.md** — this file: authority chain, canonical sources, scope guardrails, superseded file list, work log.

### Entry 2026-06-11 — OpenCode session 2 (terminal redesign + projector)

**Updated / created files:**

1. **ife-2026-block-cards.html** — Terminal-inspired redesign of the block cards (overwrote previous file). Claude Code startup banner as page header, ASCII art per block (not SVGs), real CLI commands and Claude Code /commands, terminal color scheme (#0d1117 bg, #3fb950 green, #58a6ff cyan, #d29922 amber, #f85149 red), JetBrains Mono font.

2. **ife-2026-projector.html** — Standalone full-screen slideshow projector for the block cards. Keyboard navigation (arrow keys, space, home), auto-advance (15s), timer, fullscreen toggle, click/touch navigation, responsive scaling for projection.

3. **AGENTS.md** — Updated file inventory and added this entry.

### Entry 2026-06-11 — OpenCode session 3 (terminal CLI selector)

**Created files:**

1. **ife-2026-ai-selector.js** — Interactive terminal CLI program. Claude Code-style ASCII banner, full module list grouped by week, arrow-key navigation, Enter to view module detail (ASCII art, CLI commands, conceptual frame, critical takeaway, technical artifact, Journey anchors, AOT notes). Uses Node.js raw-mode stdin, ANSI color codes matching block-cards theme (#3fb950 green, #58a6ff cyan, #d29922 amber, #8b949e gray). Run with `node ife-2026-ai-selector.js`.

2. **AGENTS.md** — Marked `ife-2026-projector.html` as superseded in file inventory and legacy list; added this entry.

### Entry 2026-06-11 — OpenCode session 4 (Cambio Labs V1.0 design system)

**Updated files:**

1. **ife-2026-block-cards.html** — Replaced color scheme with Cambio Labs V1.0 palette from Stitch: primary `#e7c9ff`, secondary `#ffafd7`, tertiary `#84e2f6`, surface `#12131d`/`#1e1f2a`, outline `#978e9b`. Added CRT scanline overlay, box-corner decorations (lavender 2px corners), terminal cursor blink, CRT text glow. Branding updated to `CAMBIO_LABS_V1.0` header bar. All JetBrains Mono (already was). Border-radius 0 throughout.

2. **ife-2026-ai-selector.js** — Updated ANSI escape color codes to match Cambio V1.0 palette. Banner redesigned to box-drawing style `CAMBIO_LABS_V1.0` header. Status bar uses tertiary (cyan) for navigation hints.

**Assumptions made:**

- The slideshow projector (`ife-2026-projector.html`) was a misinterpretation — user wants a real terminal executable, not a web page slideshow. Replaced by `ife-2026-ai-selector.js`.
- The Stitch project HTML is the canonical Cambio Labs V1.0 design system for all deliverables going forward.
- Node.js v22+ is available (confirmed).
- The canonical spine from PROJECT-STATE.md (dated 2026-06-10) is the latest and matches the Google Sheet
- Journey anchor lesson content from journey-ai-anchor-lessons.md (captured 2026-06-10) is accurate
- B3 and B7 AOT slots remain "candidate — pending D-Cal L#" per PROJECT-STATE.md
- Empty Journey shells (2.7, 2.8, 2.9, 4.8, 1.9, 2.5) are correctly identified in the capture; the AI modules supply the teaching substance

### Entry 2026-06-11 — OpenCode session 5 (web terminal emulator)

**Created files:**

1. **ife-2026-terminal-app.html** — Full web-based terminal emulator that replaces the Node.js CLI selector. Runs entirely in the browser. Presents the same Cambio V1.0 box-drawing TUI with all 14 modules in list and detail views. Features:
   - macOS-style terminal chrome (traffic-light dots, title bar, status bar)
   - CRT scanline overlay + vignette + text glow
   - Boot sequence animation (systemd-style startup messages)
   - ANSI escape code → HTML conversion for ASCII art/command output
   - Keyboard navigation: ↑↓, Enter, j/k, b/back, Esc/q
   - Click-to-select modules
   - All MODULES data ported with unicode box-drawing preserved
   - JetBrains Mono font, responsive down to 600px

**Legacy notes:**
- `ife-2026-ai-selector.js` (Node CLI) is superseded by the web app; the JS file is kept for reference
- The web app renders identically to the Node TUI but works in any browser without dependencies

**Updated files:**

1. **AGENTS.md** — Updated file inventory with `ife-2026-terminal-app.html`; marked `ife-2026-ai-selector.js` as superseded.

### Entry 2026-06-11 — OpenCode session 6 (Stitch Deep Space style applied)

**Updated files:**

1. **ife-2026-terminal-app.html** — Full visual reskin to match the Stitch "Deep Space Terminal" design system:
   - Deep Space palette: surface `#16111b`, primary `#faecff`, container `#231d28`, outline `#968e98`
   - Stitch CRT overlay (RGB channel separation + 4px scanline + animated scanline bar)
   - Flicker animation on keypress (matches Stitch's `flicker` effect)
   - Updated terminal chrome: `CAMBIO_SYSTEM_READY` title label, `surface-container-high` status bar, traffic-light dots with native macOS colors (`#ff5f56`/`#ffbd2e`/`#27c93f`)
   - Glow effects: `glow-text` (0 0 10px primary-container) and `glow-border` (0 0 15px primary)
   - All TUI functionality preserved (list/detail views, ANSI→HTML, keyboard/click nav, boot sequence)

**Open questions for Claude Code:**
1. D-Cal's AOT lesson list (L2–L6) is still needed to fill the "candidate" AOT slots (B3, B7) and blank AOT cells — has this been resolved?
2. Journey points values are still "TBD" on every day sheet — are these set now?
3. Verify the tool stack section in the instructor guide matches current provisioning decisions (shared API keys per pod vs individual accounts)
4. Should the humanizer skill be applied to the instructor guide text?
5. The cards file uses inline CSS (not linked to cambio-colors.css) for self-containment — confirm this is the right approach
