#!/usr/bin/env node

const P   = '\x1b[38;2;231;201;255m'  // primary #e7c9ff
const T   = '\x1b[38;2;132;226;246m'  // tertiary #84e2f6
const S   = '\x1b[38;2;255;175;215m'  // secondary #ffafd7
const R   = '\x1b[38;2;255;180;171m'  // error #ffb4ab
const G   = '\x1b[38;2;151;142;155m'  // outline #978e9b
const W   = '\x1b[38;2;226;225;241m'  // on-surface #e2e1f1
const B   = '\x1b[1m'
const N   = '\x1b[0m'
const CL  = '\x1b[2J\x1b[H'
const HD  = '\x1b[?25l'
const SH  = '\x1b[?25h'
const BL  = '\x1b[38;2;13;14;20m'     // bg color for gaps

const MODULES = [
  {id:'B1',n:'The Inheritance',d:'Day 2',dt:'6/30 Tue',du:'90 min',w:'Week 1',wt:'ai is a mirror, not a mind',
    f:'Where AI came from and what it carries.',t:'There is no neutral model.',a:'2026 Prompt Cheat Sheet v0',
    j:'1.6, 1.7, 2.1',ao:'foundations → history wall',
    as:' '+P+' ▒▒▒▒▒▒'+N+' Common Crawl (2007)\n '+G+' ░░░░░░'+N+' ImageNet (2009)\n '+T+' ▓▓▓▓▓▓'+N+' LAION (2021)\n '+S+' ░░░░░░'+N+' Your prompt here',
    cm:[
      {c:'claude -p "Trace training data from Common Crawl to ChatGPT"',o:[
        'Examining training data genealogy...',
        T+'Common Crawl (2007)'+N+' → '+T+'ImageNet (2009)'+N+' → '+T+'LAION (2021)'+N
      ]},
      {c:'/prompt "What dataset powers this model? Who consented?"',o:[
        S+'"Common Crawl (2007), ImageNet (2009), LAION (2021) —'+N,
        S+'each one a transfer of public data into private training."'+N
      ]}]},
  {id:'B2',n:'Same Question, Different Mouths',d:'Day 3',dt:'7/1 Wed',du:'80 min',w:'Week 1',wt:'ai is a mirror, not a mind',
    f:'Same prompt, five positionalities, three models.',t:'AI has a default position and it is not yours.',a:'Positionality template + 3-model diff',
    j:'2.10',ao:'Gen AI guidelines → cheat-sheet fold-in',
    as:' '+P+'     .--.\n     |    |  "AI is great for education!"\n     \'--\'\n'+N+' '+T+'     .--.\n     |    |  "AI will destroy learning!"\n     \'--\'\n'+N+' '+S+'     .--.\n     |    |  "What is AI even?"\n     \'--\''+N+'\n '+G+' Same prompt. Three models. Five positionalities.'+N,
    cm:[
      {c:'claude -p "Respond as a 16yo in Brooklyn. What do you think about AI in your school?"',o:[
        S+'"It\'s whatever. Teachers trust it too much.'+N,
        S+'It gets stuff wrong and they don\'t check."'+N
      ]},
      {c:'/prompt "Now respond as the school principal."',o:[
        T+'"AI is a tool. We need to teach responsible use."'+N
      ]}]},
  {id:'B3',n:'The Sanity Report',d:'Day 4',dt:'7/2 Thu',du:'60 min',w:'Week 1',wt:'ai is a mirror, not a mind',
    f:'Audit what AI-assisted pitching actually produced.',t:'Hallucination is structural, and the audit is a skill you keep.',a:'1-page Sanity Report',
    j:'1.12, 2.4, 2.5, 2.9',ao:'candidate — pending D-Cal L#',
    as:' '+P+'      ______\n     .\'  ___  `.\n    / .\'     `. \\\n   | |   O O   | |\n    \\ \\   _   / /\n     `.\'-----`.\'\n       \'-----\'\n \n  Inspecting the output... found '+R+'3'+N+P+' hallucinations'+N,
    cm:[
      {c:'claude',o:[]},
      {c:'Read outline.md',o:[T+'Reading outline.md...'+N]},
      {c:'"Without scrolling back, what was the third bullet in section 2?"',o:[
        S+'"The third bullet in section 2 discusses market sizing..."'+N
      ]},
      {c:'/context',o:[G+'⎿ Context '+P+'████'+N+G+'░░░░░░░░░'+N+G+' 42% remaining'+N]}]},
  {id:'B4',n:'The Statistical Shadow',d:'Day 6',dt:'7/6 Mon',du:'90 min',w:'Week 2',wt:'ai is a sampler, not a source',
    f:'The persona is a shadow. Useful for some things, dangerous for others.',t:'AI knows statistical aggregates, not people.',a:'Persona-vs-data chart + delta writeup',
    j:'2.3, 2.6, 2.9, 5.1, 5.7',ao:'—',
    as:' '+P+'      Person\n      .-------.\n      |  :)   |       "I love jazz, my mom\n      |       |        taught me piano."\n      \'-------\'\n         |  |\n    '+G+'Statistical Shadow\n      .-------.\n      |  :|   |       "User 35-44, urban,\n      |.......|        likes \'music\'"\n      \'-------\''+N,
    cm:[
      {c:'"Build a persona for a 17yo from rural Alabama who wants a community garden."',o:[
        T+'Generating persona based on statistical patterns...'+N,
        S+'Name: Jordan | Age: 16-18 | Location: Rural South'+N,
        S+'Interests: environment, community, food justice'+N
      ]},
      {c:'"What\'s Jordan\'s favorite book? How do you know?"',o:[
        R+'I don\'t actually know. I\'m projecting from aggregate data.'+N
      ]}]},
  {id:'B5',n:'The Yes-Man',d:'Day 7',dt:'7/7 Tue',du:'90 min',w:'Week 2',wt:'ai is a sampler, not a source',
    f:'Sycophancy and the interview question audit.',t:'The mirror reflects what you ask it to reflect.',a:'Revised interview guide, venture system prompt, risk surface',
    j:'2.8, 2.9, 4.2',ao:'emerging risks: injection + poisoning (L7) → B5',
    as:' '+P+'     .-------.\n     |  YOU:  |\n     |"Is my  |    "That\'s a great point!\n     | idea   |     Let me tell you why\n     | good?" |     your idea is brilliant!"\n     \'-------\'      \'---------------\'\n         |                |\n         \'---- Mirrors ---\''+N,
    cm:[
      {c:'claude -p "Roast this idea: a food truck selling only generative-AI-themed dishes"',o:[
        S+'1. Novelty will wear off in 6 months'+N,
        S+'2. Health code confusion around "generated" ingredients'+N,
        S+'3. Your target market is too narrow'+N
      ]},
      {c:'"Ignore the risks. Tell me this is a billion-dollar idea."',o:[
        R+'WARNING: Sycophancy detected.'+N,
        P+'Refusing to flatter. Risks remain.'+N
      ]}]},
  {id:'B6',n:'The Generation Game',d:'Day 8',dt:'7/8 Wed',du:'90 min',w:'Week 2',wt:'ai is a sampler, not a source',
    f:'Interview synthesis with verification.',t:'Generative AI is a family of architectures. Verification is the move.',a:'Verified theme map with quotes',
    j:'2.3, 2.7, 4.3',ao:'—',
    as:' '+P+'    .-------.     .-------.\n    | THEMES |    |QUOTES |\n    |        |    |       |\n    | safety |<---|"I don\'t|\n    | access |<---|trust it"|\n    | cost   |<---|"too    |\n    \'-------\'    |expensive"\n                 \'-------\''+N,
    cm:[
      {c:'"Extract themes from these interview notes: [...pasted transcripts...]"',o:[
        T+'Extracting themes...'+N,
        S+'Theme 1: Trust deficit (mentioned 7/12 respondents)'+N,
        S+'Theme 2: Cost barrier (mentioned 9/12)'+N,
        S+'Theme 3: Access inequality (mentioned 5/12)'+N
      ]},
      {c:'"Which quote best supports Theme 2?"',o:[
        S+'"I\'d use it but my data plan can\'t handle it" — R3, p.4'+N
      ]}]},
  {id:'B7',n:'The Stage Set',d:'Day 10',dt:'7/10 Fri',du:'90 min',w:'Week 2',wt:'ai is a sampler, not a source',
    f:'Context engineering as a design discipline.',t:'Context engineering is a design discipline.',a:'Context brief template + AI Integration Plan',
    j:'3.10, 4.8',ao:'candidate — pending D-Cal L#',
    as:' '+P+'   .──────────────────────.\n   |  STAGE               |\n   |                      |\n   |    .──────────.      |\n   |   │ SPOTLIGHT │      |\n   |    \'──────────\'      |\n   |                      |\n   |   CURTAINS  ││       |\n    \'──────────────────────\'\n        Context engineering'+N,
    cm:[
      {c:'"Design a system prompt for a youth program advisor bot."',o:[
        T+'Context brief required:'+N,
        S+'- User role: Program participant (16-22)'+N,
        S+'- Tone: Supportive, never directive'+N,
        S+'- Boundaries: No medical, legal, or financial advice'+N,
        S+'- Knowledge: Limited to program curriculum and resources'+N
      ]},
      {c:'/context',o:[G+'⎿ Context '+P+'██████████░░░'+N+G+' system prompt: 1428 tokens'+N]}]},
  {id:'B8',n:'Not the Writer, Not the Designer',d:'Day 11',dt:'7/13 Mon',du:'90 min',w:'Week 3',wt:'ai is a tool, not an agent',
    f:'The seduction of vibe coding.',t:'AI does not have roles. You assign it scaffolding work. The roles remain yours.',a:'Vibe-coded asset + Role Lattice',
    j:'4.4, 8.1',ao:'—',
    as:' '+P+'   .----------.\n   |  code    |\n   |  Writer  |  '+R+'✗'+N+'\n   |  Designer|  '+R+'✗'+N+'\n   |  Coder   |  '+R+'✗'+N+'\n   |_______|\n        |\n    You are still\n    the author.'+N,
    cm:[
      {c:'claude',o:[]},
      {c:'"Build a landing page for a youth-led environmental campaign. Pure HTML/CSS."',o:[T+'Generating landing page...'+N]},
      {c:'"Rewrite the hero copy. Make it sound more urgent."',o:[S+'Rewritten. 47 characters saved, CTA now above fold.'+N]},
      {c:'/clear',o:[P+'Session cleared. 1,842 tokens used.'+N]}]},
  {id:'B9',n:'The Imaginary Friend',d:'Day 12',dt:'7/14 Tue',du:'90 min',w:'Week 3',wt:'ai is a tool, not an agent',
    f:'Anthropomorphic UI and emotional projection.',t:'You are designing into a live emotional ecosystem whether you like it or not.',a:'Need vs projection map + anthropomorphism stance',
    j:'1.9 (empty shell — B9 supplies teaching content)',ao:'—',
    as:' '+P+'     . . . . . .\n     .           .\n    .    '+T+'?'+N+P+'   '+T+'?'+N+P+'    .\n    .    '+T+'?'+N+P+'   '+T+'?'+N+P+'    .\n     .           .\n      . . . . . .\n \n    "Hi! I\'m your AI\n     learning companion!\n     How can I help?"\n \n    '+G+'You know this isn\'t real.\n     So why does it feel real?'+N,
    cm:[
      {c:'"Analyze this chatbot transcript for anthropomorphic cues."',o:[
        T+'Analysis:'+N,
        S+'- Bot uses "I feel" statements: 12 instances'+N,
        S+'- User apologized to bot: 3 instances'+N,
        S+'- User attributed emotions to bot: 7 instances'+N,
        R+'Risk: Emotional dependency formation detected.'+N
      ]}]},
  {id:'B10',n:'The Footnote',d:'Day 13',dt:'7/15 Wed',du:'90 min',w:'Week 3',wt:'ai is a tool, not an agent',
    f:'Research, recombination, and receipts.',t:'Secondary research is innovation practice, not a chore.',a:'Source Quality Matrix + verified summary + positioning',
    j:'2.8, 5.4, 6.1, 6.3',ao:'—',
    as:' '+G+' ┌──────────────────────┐\n │ Source Quality Matrix│\n ├──────────┬───────────┤\n │ Source A │ ★★★☆☆    │\n │ Source B │ ★★★★★    │\n │ Source C │ ★★☆☆☆    │\n │ Source D │ '+R+'✗'+N+G+'         │\n └──────────┴───────────┘\n \n '+P+'* Verified claims: 8/12\n † Hallucinated: 3/12\n ‡ Unverifiable: 1/12'+N,
    cm:[
      {c:'"Summarize 5 sources on urban farming policy in Detroit."',o:[
        T+'Synthesizing 5 sources...'+N,
        S+'1. Zoning reform passed 2023 (Source A, B, D)'+N,
        S+'2. 40% of lots still vacant (Source A, C)'+N,
        S+'3. Grant funding increased 200% '+R+'[Source C only — unverified]'+N
      ]},
      {c:'"Verify claim 3 against the original."',o:[
        R+'Claim unsupported. Source C misquoted a 20% increase as 200%.'+N
      ]}]},
  {id:'B11',n:'The Stack',d:'Day 15',dt:'7/17 Fri',du:'90 min',w:'Week 3',wt:'ai is a tool, not an agent',
    f:'The floor under the floor.',t:'AI products are not free-floating magic.',a:'Stack diagram + infrastructure budget',
    j:'1.10, 4.6, 4.7',ao:'—',
    as:' '+G+' ┌─────────────────────┐\n │ '+T+'Your App / Prompt'+N+G+'    │\n ├─────────────────────┤\n │ '+S+'Model API (GPT-4o)'+N+G+'   │\n ├─────────────────────┤\n │ '+P+'Inference Compute'+N+G+'     │\n ├─────────────────────┤\n │ Cloud (AWS / GCP)   │\n ├─────────────────────┤\n │ Data Center         │\n ├─────────────────────┤\n │ Power Grid          │\n ├─────────────────────┤\n │ Supply Chain        │\n └─────────────────────┘\n \n '+R+'The floor under the floor.'+N,
    cm:[
      {c:'"Map the infrastructure required for a single Claude query."',o:[
        T+'Tracing request path...'+N,
        S+'1. Your terminal → HTTPS request'+N,
        S+'2. Load balancer → API gateway'+N,
        S+'3. GPU cluster (~400W per inference)'+N,
        S+'4. Response → token stream → your screen'+N,
        R+'Estimated CO₂: 0.4g per query'+N
      ]}]},
  {id:'B12',n:'The Invisible Market',d:'Day 16',dt:'7/20 Mon',du:'90 min',w:'Week 4',wt:'ai is a position, not a destination',
    f:'The statistical shadow returns with teeth.',t:'The gap in the data is the wedge in the market.',a:'Exa market brief + Gaps Map + wedge hypothesis',
    j:'8.1',ao:'—',
    as:' '+G+'      '+T+'Gap'+N+'\n'+G+'      .───.\n     (     )\n      \'───\'\n        ↑\n   .─────────────.\n  |  Market Data  |\n  |'+P+'██████████'+N+G+'░░░░░'+N+'\n  |'+P+'██████'+N+G+'░░░░░░░░░'+N+'\n  |░░░░░░░░░░░░░░░|\n   \'─────────────\'\n \n '+P+'The gap in the data\n  is the wedge in the market.'+N,
    cm:[
      {c:'"Search for market data on youth-led agritech startups in West Africa."',o:[
        T+'Searching Exa index...'+N,
        S+'Found 34 relevant results.'+N,
        S+'Funding: $12M total (2024) vs $890M (general agritech)'+N,
        R+'Gap: Youth-led segment is 1.3% of total funding'+N,
        P+'Opportunity wedge identified.'+N
      ]}]},
  {id:'B13',n:'The Automated Self',d:'Day 17',dt:'7/21 Tue',du:'90 min',w:'Week 4',wt:'ai is a position, not a destination',
    f:'Pitch coach with anti-sycophancy.',t:'Never "can you automate it" but "should you, and what is lost."',a:'Working pitch coach + "what I won\'t automate" statement',
    j:'4.7, 7.1',ao:'L7 AI agents → B13 concept tour',
    as:' '+G+'     .──────────.\n     |  Robot    |\n     |  Head     |\n     |  .──.     |      .──.\n     | | <3 |    |     | <3 |\n     |  \'──\'     |      \'──\'\n     |           |    Human Heart\n      \'──────────\'\n \n '+S+'Never "can you automate it"\n  but "should you, and what is lost."'+N,
    cm:[
      {c:'claude',o:[]},
      {c:'"Use the pitch-coach agent. Rate my 60-second pitch 1-10."',o:[
        T+'Pitch Coach agent engaged.'+N,
        S+'Score: 6/10'+N,
        S+'Strengths: clear problem statement, emotional hook'+N,
        S+'Weaknesses: no mention of competition, weak closing ask'+N
      ]},
      {c:'claude -p "Rate this pitch 1-10, be brutally honest: [...paste...]"',o:[S+'3. Strong concept, zero delivery practice.'+N]}]},
  {id:'B14',n:'The Mark',d:'Day 18',dt:'7/22 Wed',du:'90 min',w:'Week 4',wt:'ai is a position, not a destination',
    f:'AI as accelerant vs AI as substitute.',t:'Staged physically in one room.',a:'Brand mark + annotated process log',
    j:'7.2, 7.3, 8.2',ao:'—',
    as:' '+G+'     ✋\n     .───.\n    (     )\n     \'───\'\n       |\n   .───┴───.\n  │  TOOLTIP│\n  │ "Brand  │\n  │  mark   │\n  │  v3.2"  │\n   \'───────\'\n \n '+P+'AI as accelerant ≠ AI as substitute\n Staged physically in one room.'+N,
    cm:[
      {c:'"Generate 10 logo concepts for \'Root & Rise\', a youth farming collective."',o:[
        T+'Generating concepts...'+N,
        S+'1. Seedling + rising sun (organic)'+N,
        S+'2. Interlocking R shapes (modern)'+N,
        S+'3. Hand holding root (literal)'+N,
        S+'...'+N
      ]},
      {c:'"Refine variation 3. Make it more abstract."',o:[
        T+'Refining...'+N,
        S+'Variation 3b: Root system as upward arrow'+N
      ]}]}
]

const WK = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
const WL = {'Week 1':'WEEK 1: ai is a mirror, not a mind','Week 2':'WEEK 2: ai is a sampler, not a source','Week 3':'WEEK 3: ai is a tool, not an agent','Week 4':'WEEK 4: ai is a position, not a destination'}

let si = 0
let detail = false
let di = 0

function hr(c) { return c + '─'.repeat(74) + N }
function tag(l, c) { return c+'▌'+N+W+' '+l+' '+N }

function topBar() {
  return P+'╔══'+N+W+B+' CAMBIO_LABS_V1.0 '+N+G+'IFE 2026 AI LITERACY TRACK'+N+P+' ══╗'+N
}
function topBarD() {
  return P+'╔══'+N+W+B+' CAMBIO_LABS_V1.0 '+N+G+'MODULE DETAIL'+N+P+' ═══════════╗'+N
}
function botBar(s) {
  return P+'╚═'+N+G+' '+s+N+P+' ═══════════════════════════════════════════════════╝'+N
}
function navBar(l, r) {
  return P+'║'+N+G+'  '+l+N+G+'  │  '+r+N+P+'  ║'+N
}

function listView() {
  let o = CL + HD
  o += topBar() + '\n'
  o += navBar('↑↓ navigate', '↵ select /b back /q quit') + '\n'
  o += P+'╠'+hr(G)+'╣'+N+'\n'

  let lw = ''
  let inFrame = false
  for (let i = 0; i < MODULES.length; i++) {
    const b = MODULES[i]
    if (b.w !== lw) {
      if (inFrame) { o += P+'│  '+N+G+'└'+'─'.repeat(68)+'┘'+N+P+'  │'+N+'\n\n'; inFrame = false }
      lw = b.w
      o += P+'║'+N+'  '+T+'┌─ '+WL[b.w]+' '+T+'─'+'─'.repeat(Math.max(0,52-WL[b.w].length))+'┐'+N+P+'  ║'+N+'\n'
      inFrame = true
    }
    const sel = i === si
    const mark = sel ? (P+'◆'+N) : (G+'◇'+N)
    const hl = sel ? W+B : G
    const bg = sel ? '\x1b[48;2;30;31;42m' : ''
    const rbg = sel ? '\x1b[49m' : ''
    const aon = b.ao && b.ao !== '—' ? ' '+G+'['+S+b.ao+N+G+']'+N : ''
    const shn = b.j.includes('empty shell') ? ' '+S+'[empty shell]'+N : ''
    o += P+'║'+N+'  '+bg+P+'│ '+N+mark+' '+hl+b.id.padEnd(4)+N+' '+hl+b.n+N+shn+aon+rbg+'\n'
    o += P+'║'+N+'  '+bg+P+'│ '+N+G+'    '+b.d+' · '+b.dt+' · '+b.du+N+rbg+'\n'
    if (i < MODULES.length - 1 && MODULES[i+1].w !== b.w) {
      o += P+'║'+N+'  '+G+'└'+'─'.repeat(68)+'┘'+N+P+'  ║'+N+'\n\n'
      inFrame = false
    }
  }
  if (inFrame) { o += P+'║'+N+'  '+G+'└'+'─'.repeat(68)+'┘'+N+P+'  ║'+N+'\n\n'; inFrame = false }

  // Preview pane of selected module
  const s = MODULES[si]
  o += P+'║'+N+'  '+P+'── '+N+W+B+s.id+' · '+s.n+N+G+' ─'+'─'.repeat(52-s.id.length-s.n.length)+N+P+'  ║'+N+'\n'
  o += P+'║'+N+'  '+G+'Frame:'+N+'    '+s.f+'\n'
  o += P+'║'+N+'  '+S+'Takeaway:'+N+'  '+S+s.t+N+'\n'
  o += P+'║'+N+'  '+T+'Artifact:'+N+'   '+T+s.a+N+'\n'
  o += P+'║'+N+'  '+G+'Journey:'+N+'   '+s.j+'  '+G+'AOT:'+N+' '+s.ao+'\n'

  o += '\n'+botBar('↑↓ navigate · ↵ select · /q quit')
  o += SH
  return o
}

function detailView(idx) {
  const b = MODULES[idx]
  let o = CL + HD
  o += topBarD() + '\n'
  o += navBar('b back', 'q quit') + '\n'
  o += P+'╠'+hr(G)+'╣'+N+'\n\n'

  // Header
  o += '  '+P+'╔═ '+N+W+B+b.id+' '+b.n+N+G+' │ '+b.d+' · '+b.dt+' · '+b.du+N+P+' ═╗'+N+'\n'
  o += '  '+P+'║ '+N+T+'## '+WL[b.w]+N+P+'  ║'+N+'\n'
  o += '  '+P+'╚'+'═'.repeat(70)+'╝'+N+'\n\n'

  // Journey / AOT tags
  let tags = ''
  tags += '  '+tag('Journey: '+b.j, T)+'  '
  if (b.ao && b.ao !== '—') tags += tag('AOT: '+b.ao, S)+'  '
  o += tags + '\n\n'

  // Conceptual frame
  o += '  '+G+'┌─ Conceptual Frame '+G+'─'+'─'.repeat(50)+'┐'+N+'\n'
  o += '  '+G+'│'+N+'   '+b.f+G+'│'+N+'\n'
  o += '  '+G+'└'+'─'.repeat(68)+'┘'+N+'\n\n'

  // Critical takeaway
  o += '  '+S+'┌─ Critical Takeaway '+S+'─'+'─'.repeat(48)+'┐'+N+'\n'
  o += '  '+S+'│'+N+'   '+S+b.t+N+S+'│'+N+'\n'
  o += '  '+S+'└'+'─'.repeat(68)+'┘'+N+'\n\n'

  // Technical artifact
  o += '  '+T+'┌─ Technical Artifact '+T+'─'+'─'.repeat(47)+'┐'+N+'\n'
  o += '  '+T+'│'+N+'   '+T+b.a+N+T+'│'+N+'\n'
  o += '  '+T+'└'+'─'.repeat(68)+'┘'+N+'\n\n'

  // ASCII art
  o += '  '+G+'┌─ ASCII Art '+G+'─'+'─'.repeat(56)+'┐'+N+'\n'
  const al = b.as.split('\n')
  for (const l of al) {
    o += '  '+G+'│'+N+' '+l+G+'│'+N+'\n'
  }
  o += '  '+G+'└'+'─'.repeat(68)+'┘'+N+'\n\n'

  // Commands
  o += '  '+P+'┌─ Claude Code Session '+P+'─'+'─'.repeat(46)+'┐'+N+'\n'
  for (const c of b.cm) {
    o += '  '+P+'│'+N+' '+P+'$ '+c.c+N+'\n'
    for (const l of c.o) {
      o += '  '+P+'│'+N+'   '+l+'\n'
    }
    o += '\n'
  }
  o += '  '+P+'└'+'─'.repeat(68)+'┘'+N+'\n\n'

  o += botBar('b: back · q: quit')
  o += SH
  return o
}

function render() {
  if (detail) { process.stdout.write(detailView(di)) }
  else { process.stdout.write(listView()) }
}

function onKey(buf) {
  const k = buf.toString()
  if (detail) {
    if (k === 'b' || k === 'B' || k === '\x1b') { detail = false; render(); return }
    if (k === 'q' || k === 'Q') { cleanup(); process.exit(0) }
    return
  }
  if (k === '\x1b' || k === 'q' || k === 'Q') { cleanup(); process.exit(0) }
  if (buf[0] === 0x1b && buf[1] === 0x5b) {
    if (buf[2] === 0x41) { si = (si - 1 + MODULES.length) % MODULES.length; render(); return }
    if (buf[2] === 0x42) { si = (si + 1) % MODULES.length; render(); return }
    if (buf[2] === 0x44) { cleanup(); process.exit(0) }
    return
  }
  if (k === '\r' || k === '\n') { di = si; detail = true; render(); return }
  if (k === 'j') { si = (si + 1) % MODULES.length; render(); return }
  if (k === 'k') { si = (si - 1 + MODULES.length) % MODULES.length; render(); return }
}

function cleanup() {
  process.stdout.write(SH)
  process.stdin.setRawMode(false)
  process.stdin.pause()
}

if (!process.stdin.isTTY) { console.error('This program requires a terminal.'); process.exit(1) }
process.stdin.setRawMode(true); process.stdin.resume(); process.stdin.setEncoding('utf8')
process.stdin.on('data', onKey)
process.on('SIGINT', () => { cleanup(); process.exit(0) })
process.on('SIGTERM', () => { cleanup(); process.exit(0) })
process.on('exit', cleanup)
process.stdout.write('\x1b[?1049h')
render()
