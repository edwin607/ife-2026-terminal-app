# Train the Trainer: Three Keystone Blocks at the Terminal

A facilitator runbook for the AI Literacy Track, IFE 2026\. This is a sample of the depth we are aiming for across all 14 blocks. It covers three:

- **Block 3, The Sanity Report.** Observe. The terminal shows up for the first time.  
- **Block 8, Not the Writer, Not the Designer.** Operate. Pods build a real thing and get interrogated about who did the work.  
- **Block 13, The Automated Self.** Orchestrate. Agents, anti-sycophancy, and what we choose not to automate.

Observe, operate, orchestrate. Same arc as the curriculum: consumer to operator to position.

**One tool on purpose.** All three run on Claude Code. A trainer who knows one CLI well is calmer in front of 40 students than a trainer juggling four. Where the curriculum lists a different tool (Block 3 originally names Gemini CLI), this guide standardizes on Claude Code and notes the alternative for the take-home guide.

**How to read each block.** Before class (what you install and stage), The demo live (the exact session, in code blocks), When it does not go to plan (recovery), Hand to pods (the 40-student move), and the line you land on.

**One honest note up front.** The model responses printed below are illustrative. They will not match what you see word for word, because the model is doing pattern completion, not playback. That is not a bug in this guide. That is Week 1\.

---

## Shared prep, do this once at home

Never install in front of the room. Do this the night before, on the machine you will actually teach from.

```shell
# Claude Code needs Node 18 or newer. Check before anything else.
node --version          # expect v18.x.x or higher

# Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# Confirm it landed
claude --version
```

First launch handles sign in. Do it once, quietly.

```shell
# Start a session from any folder. First run walks you through
# browser sign in or an API key. Get this out of the way at home.
claude
```

Then a thirty second pulse check so you know it works before students arrive.

```shell
# -p is print mode: run one prompt, print the answer, exit. No session.
claude -p "Reply with the single word: ready"
# → ready
```

Two things to run once during prep so nothing surprises you live:

- `/context` inside a session shows what is filling the window. The exact layout shifts between versions. Run it once so you recognize your version's output.  
- `Shift+Tab` cycles permission modes (normal, auto accept edits, plan). Press it a few times at home so the live cycle is muscle memory.

A note on accounts for pod work. Claude Code authenticates against an Anthropic account or API key, separate from the OpenRouter keys the chat-model blocks use. For the one block where pods drive Claude Code themselves (Block 8), the cleanest setup is one shared API key per pod with a usage limit, provisioned before Week 3\. If that is not ready, run Block 8 as a one screen demo and have pods replicate in a browser tool. Decide which before the day, not during it.

---

## Block 3\. The Sanity Report

**W1 D4, 60 min. Instructor screen only for the demo.**

### What you are proving

Hallucination is not random. It is pattern completion against whatever fit in the context window. Students need to see the window fill and watch recall degrade, not hear it described on a slide.

### Before class

Stage a document you control, with numbered points you can quiz later. The whole trick is that you know what is on page 2 and the model is about to guess.

```shell
mkdir sanity-demo && cd sanity-demo
# Drop in a long document you own: a pitch transcript, a spec, an outline.
# Numbered lists are gold, because "the third bullet" is checkable.
ls
# → outline.md   transcript.md
```

If one file does not fill the window, that is fine. You have more ready, and adding them mid-demo is itself the lesson.

### The demo, live

```shell
cd sanity-demo
claude
```

Inside the session:

```
> Read transcript.md and outline.md, then wait for my questions.

● Read both. transcript.md is a 2,400-line pitch session.
  outline.md is a 12-section venture outline. Ready when you are.

> /context

  ⎿  Context  ████████░░░░░░░░  41% of window
     system + tools    8%
     files            30%
     messages          3%
```

Land the first beat here. The window is finite, and now it is visible. Everything the model can reason about right now is in that bar.

```
> Without scrolling back, what was the third bullet under "Risks"
  on page 2 of the outline?

● The third Risks bullet was "supply-chain dependency on a single vendor."
```

Stop. Check the file out loud. Often it is close but wrong, or it states something with full confidence that is not there at all. That gap is the entire block.

The line to say while they are watching: it did not look it up. It built the shape of a third risk bullet, because that is what fits. Confidence and correctness are not the same thing here.

If you want to push it further, fill the window and ask again.

```
> Also read research-dump.md and the two interview files. Then tell me,
  again, that third Risks bullet on page 2.

● [reads files]
  ⎿  Context  ███████████████░  92% of window

● I believe it referenced vendor concentration, though there were several
  risk factors discussed across the documents.
```

The hedge is the point. As the window fills, precise recall blurs into plausible summary.

### When it does not go to plan

If the model nails the recall on the first try, do not panic. Use it.

```
> Good. Why did you get that right just now?
```

Then load three more documents and ask again. The slip will come as the window fills. Have the extra files staged so this is a ten second move, not a scramble. To reset cleanly between attempts:

```
> /clear
```

### Hand to pods

No pod terminals here. Pods take their own ai-assisted pitch material from yesterday and fill the four-column flaw audit on paper or in a shared doc: where was there no pushback, where does it look like ai slop, what did I not ask, what context did I not give. One report per pod to the board.

The CLI install itself goes home as an optional setup guide. Installing Claude Code or Gemini CLI on 40 machines in 60 minutes is a fire drill, not a lesson. For the take-home guide, Gemini CLI installs the same shape: `npm install -g @google/gemini-cli`, then run `gemini`. Verify the current package name before you publish the handout, since CLI tooling drifts.

### The line you land on

Hallucination is not random, it is structural. Your report is the receipt.

---

## Block 8\. Not the Writer, Not the Designer

**W3 D1, 90 min. Demo on one screen, then pods build.**

### What you are proving

ai does not have roles. You assign it scaffolding work, and the roles stay yours: director, editor, architect, taste-maker, ethical reviewer, debugger of meaning. Let the impressiveness land first, then name the seduction.

### Before class

Pre-stage one folder per pod so nobody loses three minutes to `mkdir`.

```shell
# Ten pod folders, zero-padded so they sort cleanly
for i in $(seq -w 1 10); do mkdir -p ife/pod-$i; done
ls ife/
# → pod-01  pod-02  pod-03  pod-04  pod-05  pod-06  pod-07  pod-08  pod-09  pod-10
```

Pick one small, real asset they can finish: a single landing page, a simple sign-up form, a one-screen tool. Small enough to build, real enough to judge.

### The demo, live

Let it be impressive on purpose. This is the seduction you will name in ten minutes.

```shell
cd ife/pod-01
claude
```

```
> Build a single-page landing site for a teen-run bike-repair co-op in the
  South Bronx. One HTML file, no build step, mobile first. Make reasonable
  choices, ask me nothing, then show me the file.

● I'll create index.html with a hero, a services list, hours, and a
  contact section. Bold type, high contrast, works on a phone.
  ⎿  Wrote index.html (138 lines)

● Done. Open index.html in a browser to view it.
```

```shell
# View it. Either open directly or serve the folder.
open index.html        # macOS
# or: python3 -m http.server 8000   then visit localhost:8000
```

Now the interrogation. This is the block.

Ask the room, in order: Did the ai write? No. It pattern-completed against millions of repos. Did it design? No. It applied defaults from its training distribution. So what did you just do? You directed it, you set the constraints, and now you are going to judge it. Those are the roles. They never left you.

Show the redirect, live, so they see direction as the actual work.

```
> The hero copy is generic. Rewrite it to name the neighborhood and the
  co-op model. Under 20 words. I will decide if it stays.

● Hero rewrite:
  "South Bronx riders fixing South Bronx bikes. Member-run, fair-price,
  walk-in repairs on Southern Boulevard."

> Better. Keep it.
```

That "keep it" is the lesson made visible. The taste was yours.

### When it does not go to plan

Claude Code sometimes over-builds: a framework, a package.json, six files you never asked for. Rein it in.

```
> Stop. Undo that. One HTML file, no dependencies, no build step.
```

If a pod's session is fully tangled, reset rather than fight it.

```
> /clear
```

On permissions: by default Claude Code asks before it writes a file or runs a command. For your one screen demo you can cycle to auto accept with `Shift+Tab` to keep the pace up. In pod hands, leave the default on. Approving each change is not friction, it is the operator move. Every "yes, write that" is a student deciding, not the machine.

### Hand to pods

Each pod in its own folder, one driver at a time, rotate the keyboard at the 20 minute mark so it is not the same kid coding the whole block. Pods finish two things: the small asset, and a Role Lattice that splits what ai scaffolded from what they own outright. One link per pod to the board.

### The line you land on

The seduction is real. Naming it is the literacy move.

---

## Block 13\. The Automated Self

**W4 D2, 90 min. Concept tour, then build. This is the agents block.**

### What you are proving

The question is never "can you automate it," it is "should you, and what is lost." Students build a pitch coach that refuses to flatter, which is the Week 2 Yes-Man lesson turned into infrastructure. Then they draw a line around what they will not automate.

### Before class

The coach's instructions are the heart of this block, so write them as a file you can hand out. Claude Code reads agent definitions from `.claude/agents`.

```shell
cd ife/pod-01
mkdir -p .claude/agents
```

```shell
cat > .claude/agents/pitch-coach.md << 'EOF'
---
name: pitch-coach
description: Critiques a startup pitch. Honest, specific, never flattering.
---

You are a pitch coach for teen founders. Your job is to make the pitch
stronger, not to make the founder feel good.

Rules:
- Never open with praise. Open with the weakest claim and why it is weak.
- Every critique names the exact sentence and gives a concrete fix.
- If a number has no source, ask for the source before anything else.
- Do not write the pitch for them. Ask the question that forces the rewrite.
- Scope is the pitch only. Refuse to wander into unrelated advice.
EOF
```

Say this out loud when you show the file: the default model flatters, because it was trained to please. This file overrides the default, in writing. That is what a system prompt is. It is the instruction set sitting above every answer.

### The demo, live

First the contrast that makes the whole block click. Run the coach, then run the same pitch with no coach.

```shell
claude
```

```
> Use the pitch-coach agent. My pitch: "We're the Uber of dog-walking for
  busy professionals. The market is huge, basically everyone with a dog."

● [pitch-coach] Weakest claim first. "The market is huge, basically everyone
  with a dog" is a red flag, not a market. Which owners, in which neighborhoods,
  paying what? Name one segment and one number with a source. Right now "huge"
  reads as "I have not looked."
```

```
> /clear
> My pitch: "We're the Uber of dog-walking for busy professionals. The market
  is huge, basically everyone with a dog." What do you think?

● Great concept with real potential! The dog-walking market is large and
  growing, and an on-demand model is a smart fit for busy owners...
```

There it is, on one screen. Same pitch, opposite response. The only difference is the instruction set you wrote.

Now name orchestration, plainly, because this is the part D-Cal asked us to finish. Orchestration is not magic. It is one step's output becoming the next step's input. Show it in two moves.

```shell
# Step 1 critiques. Step 2 scores the result. Chaining the two is orchestration.
claude -p "As a harsh pitch scorer, rate this pitch 1-10 on specificity and
name the single highest-leverage fix: 'We're the Uber of dog-walking...'"

# → 3/10 on specificity. Highest-leverage fix: replace "everyone with a dog"
#   with one named segment and a sourced number, e.g. dog owners in a specific
#   set of zip codes who already pay for walking.
```

Keep it at concept-tour depth. A swarm of agents is just more of this: defined roles, passing work down a line. The lesson is the shape, not a production pipeline.

Then the futures cone, the part that keeps the block honest. Probable, plausible, possible, preferable. The cone forces them to say what they are choosing not to build, which is harder than building.

### When it does not go to plan

If the coach still flatters, do not rewrite it from scratch. Tighten it in front of them, so editing the instruction set looks like the skill it is.

```
> You opened with praise. Remove every compliment and restate, weakest
  claim first.
```

Then add the missing rule to the file so it sticks next time.

```shell
# Append a sharper constraint to the agent definition
cat >> .claude/agents/pitch-coach.md << 'EOF'
- If you catch yourself praising, delete the praise and start over.
EOF
```

### Hand to pods

Each pod builds its own coach by editing the agent file, runs its real pitch through it, then runs pitch and coach as a pair in practice. Two artifacts: the working coach with its documented system prompt, and a "what I will not automate" statement. The first is technical. The second is the human judgment this block refuses to let the machine make.

### The line you land on

Never "can you automate it." Always "should you, and what is lost."

---

## Trainer's cheat strip

The commands you actually need, in one place. Tape it to the laptop.

```shell
node --version                          # confirm Node 18+
npm install -g @anthropic-ai/claude-code
claude --version                        # confirm install

claude                                  # start a session in the current folder
claude -p "prompt"                      # one-shot: run, print, exit

# inside a session:
/context                                # show what is filling the window
/clear                                  # wipe the session, start clean
/cost                                   # tokens and dollars this session
# Shift+Tab cycles modes: normal -> auto-accept edits -> plan
```

Verify on your own machine during prep: the exact `/context` layout and the `Shift+Tab` mode names can shift between versions. Run both once before you teach so nothing on screen is a surprise.

---

## What this sample is showing the rest of the track

Every block here ends on a human judgment the model cannot make: a flaw report, a kept line of copy, a refusal to automate. The terminal is never the point. It is the place where the student stops being impressed and starts making the calls. That is the whole curriculum in three blocks. The other eleven follow the same shape.  
