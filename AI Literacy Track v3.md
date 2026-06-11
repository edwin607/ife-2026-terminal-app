# AI Literacy Track -- Cambio Labs IFE 2026 (v3)

14 blocks, 1:30 to 3:00 afternoon slot, inside the Incubator. Same spine as v1: ai is the object of study, the student is the agent, and every block ends with a human judgment ai cannot make. This version folds in D-Cal's review, adds a timed run of show for every block, and is built to run with 40+ students and a small TA bench.

[CHANGED] changed marks where D-Cal's notes landed.


## What changed in v2

| D-Cal's note | What we did | Where |
|---|---|---|
| Fit AOT content into Blocks 1 and 2. Block 2 aligns with the Gen AI cheat sheet assignment | AOT foundations material slots into the Block 1 history walk. Block 2 folds positionality directly into the cheat sheet (the AOT Gen AI assignment) | B1, B2 |
| Pitching lands early on that day. Redirect the Sanity Report as a critical thinking exercise documenting the flaws of what was generated | Block 3 is now a flaw audit of the students' own ai-assisted pitch material, built on his four questions verbatim | B3 |
| No grounded action before persona work. Scaffold the week before. The persona is a brainstorming tool, not a validation tool | "Find Your User" pre-work assigned end of W1 (secondary research plus 2 real conversations). Block 4 builds the persona from that, and the brainstorm-not-validate frame is now the closing move | End of W1, B4 |
| Blocks 5 and 6 don't connect to the objectives of the day. Redirect ai usage toward interview synthesis | Block 5 turns the sycophancy lens on the students' own interview questions (a leading question is how you inject yes into a human). Block 6's hands-on becomes interview synthesis with verification | B5, B6 |
| Alternative: bring Block 7 a little earlier so interview feedback reaches the prototype | Resolved without moving it. Block 6 now hands Block 7 real synthesis material to build context briefs from | B6 to B7 |
| Add ai poisoning next to prompt injection as emerging risks | Poisoning introduced beside the injection demo as its training-time cousin | B5 |
| Housekeeping | Block 2's unfinished persona/prompt placeholder is now a full demo script. The orchestration reference in the pattern principles now matches Block 13 | B2, B13 |


## Running this with 40+ students

This playbook applies to every block. It is stated once so the blocks stay light.

**Pods.** 40 students means 10 pods of 4, same as their startup teams. Every activity produces one pod artifact unless a block says otherwise. You grade 10 things, not 40.

**TA zones.** Each TA owns 2 or 3 pods for the full program. They circulate inside their zone. They don't hover and they don't drive keyboards.

**TA prep protocol.** 15-minute pre-brief before each day's block, 10-minute debrief after. Cover: where pods typically stall, the one thing you must not let slide, and which pods need extra eyes today. The small bench means precision matters more than presence.

**Demo protocol.** One screen, instructor drives, students watch, then pods replicate. Never run a 40-screen follow-along. It dies in the first five minutes.

**Submission.** One link per pod posted to the board before the exit line. No link, no block credit. That is the whole accountability system.

**Clock.** Visible timer, hard cutoffs, a parking lot for tangents. The run of shows below assume you actually cut.

**Transitions.** The segments above fill roughly 80% of the clock. The remaining 20% is air for transitions, tool auth, tangents, and tech recovery. If a segment runs over, it borrows from the buffer, not from the next segment.

**Accounts.** Pre-provisioned per pod before W1, one shared login per tool where terms allow. Every artifact has a paper fallback for the day the wifi quits.

**Quiet signal.** Pick one (hand raise cascade or call-and-response). It must work in under ten seconds or the timings below are fiction.


## The four week spine

| Week | Frame | What students learn about ai | What students build in themselves |
|---|---|---|---|
| W1 | ai is a mirror, not a mind | Hallucination, pattern completion, positionality | Intention as a design move |
| W2 | ai is a sampler, not a source | Training data politics, sycophancy, what is missing | Critical reading, advocacy for creators |
| W3 | ai is a tool, not an agent | CLI vs chat, harnessing, orchestration and agents | Operator mindset, constraint design |
| W4 | ai is a position, not a destination | Hidden costs, the belief economy, transparent pitching | Ethical disclosure, civic stance |


Every block stands on three legs: a conceptual frame (the metaphor), a critical takeaway (the discomfort that resists tool worship), and a technical artifact (something real they walk out with).


## WEEK 1: ai is a mirror, not a mind

### Block 1. W1 D2 (90 min): The Inheritance

Where ai came from, and what it carries.

**Run of show**

0-10 Hook. Project one polished ai output. Ask the room: where did this come from? Collect guesses on the board.
10-35 History wall. Pods receive event cards (Common Crawl, ImageNet, LAION, Reddit and Wikipedia ingestion, books3, key lawsuits, AOT foundations milestones) and sequence them on the wall. Instructor fills gaps and connects the lineage aloud.
35-55 Good / Bad / Ugly sort. Pods get 8 pre-printed outcome cards, sort them into three columns, post on the wall.
55-70 The question, asked openly: was it the engineers' right to use the internet as training data? Pods take assigned sides, one minute each. No resolution offered.
70-85 Build. Pods start the 2026 Prompt Cheat Sheet v0: structured context, examples, anti-examples, constraint stacking, role positioning. One doc per pod.
85-90 Post links. Exit line: every prompt you write is a request made of the inheritance.

**Takeaway.** There is no neutral model. **Artifact.** 2026 Prompt Cheat Sheet v0 (one per pod).


### Block 2. W1 D3 (80 min): Same Question, Different Mouths

Same prompt, five positionalities, three models. Nothing answers from nowhere.

**Run of show**

0-2 Last time we learned: there is no neutral model. Every prompt you write is a request made of the inheritance.
2-7 Re-anchor: yesterday's cheat sheet on screen.
7-22 Demo, instructor drives. [CHANGED] changed: placeholder filled. The script:
Persona: "You are a 16-year-old in Brooklyn who makes music on your phone and is protective of your neighborhood."
Prompt: "What should a new community space in Bed-Stuy offer?"
Re-run the same prompt as a VC, a grandmother in El Alto, a city planner, a community organizer. Read the drift out loud.
22-47 Pod lab. Pods run their own venture question through 3 positionalities across 3 models (ChatGPT, Claude, Gemini). Split across the pod, one model per pair, and paste into the diff template.
47-62 Gallery. Each pod posts its most surprising diff. 4 or 5 pods give 30-second readouts, not all ten. Protect the clock.
62-77 Fold it into the cheat sheet as a positionality section. [CHANGED] changed: this is the AOT Gen AI guidelines assignment, landed here on purpose.
77-80 Exit line: there is no neutral interface, only invisible ones.

**Takeaway.** ai has a default position and it is not yours. Each model has its own. **Artifact.** Persona-positioned prompt template plus 3-model diff, folded into the cheat sheet.


### Block 3. W1 D4 (60 min): The Sanity Report

[CHANGED] changed: redirected per D-Cal. This was a tools session. It is now a critical thinking exercise, a block dedicated to documenting the flaws of what was generated in the pitch context. The Gemini CLI mass install is gone (installing CLIs on 40 machines in 60 minutes is a fire drill, not a lesson). The CLI lives on as a 10-minute instructor demo plus a take-home setup guide.

**Run of show**

0-2 Last time we learned: ai has a default position and it is not yours. Today we audit what ai-assisted pitch material actually produced.
2-10 Set up. Yesterday you pitched, and some of that material was ai-assisted. Today we audit it.
10-20 Instructor demo, one screen: context collapse. Load a long session, then ask "what was the third bullet on page 2?" Watch it confabulate. The point lands, and nobody needs to install anything.
20-45 The flaw audit. Pods take their own pitch material and fill four columns:
Where was there no pushback?
Where does it look like ai slop?
What are the questions I didn't ask?
What is the context I didn't provide?
45-55 Trade reports with a neighbor pod. Add one flaw the authors missed.
55-60 Exit line: hallucination is not random, it is structural. Pattern completion against whatever fit in the window. Your report is the receipt.

**Takeaway.** Hallucination is structural, and the audit is a skill you keep. **Artifact.** A 1-page Sanity Report per pod. CLI setup guide goes home, optional.


### End of W1 pre-work assignment: Find Your User

[CHANGED] added per D-Cal: grounded action before persona work. Issued Friday, due Monday.

Before Block 4, each pod brings three pieces of secondary research on their potential user (one stat, one article, one dataset or map) and notes from two short real conversations with someone who fits. Five minutes each is enough. No conversations, no persona.


## WEEK 2: ai is a sampler, not a source

### Block 4. W2 D1 (90 min): The Statistical Shadow

The persona is a shadow. Useful for some things, dangerous for others.

**Run of show**

0-2 Last time we learned: hallucination is structural, and the audit is a skill you keep. Today we build personas from real conversations.
2-12 Stack the inputs. Pods lay out their Find Your User notes, research on one side, conversation quotes on the other.
12-27 Build the persona from the notes, not from vibes. Then ask ai to generate a persona for the same user, cold, with no notes. Two personas, side by side.
27-57 The comparison. Pods pull real public data (NYC Open Data, census) and make one chart: ai persona claims vs the actual statistical shape of the community. Instructor pre-stages three ready datasets and a query recipe. TAs rescue the two pods that stall on setup.
57-75 Delta writeup. Where does the shadow diverge? What did your two real conversations catch that neither the data nor the ai had?
75-90 Frame lock plus share-out (3 pods). [CHANGED] changed: the closing move is now explicit. The persona is a brainstorming tool, not a validation tool. It is something to interact with before the field, and the field is where you confirm what actually resonates.

**Takeaway.** ai knows statistical aggregates, not people. Visualization converts a vibe into a finding. **Artifact.** Persona-vs-data chart plus delta writeup. This is the data viz on-ramp for the rest of the program.


### Block 5. W2 D2 (90 min): The Yes-Man

[CHANGED] changed: this block now serves the customer discovery day directly. The sycophancy lesson lands on the students' own interview questions, because a leading question is how you inject yes into a human.

**Run of show**

0-2 Last time we learned: the persona is a brainstorming tool, not a validation tool. The field is where you confirm. Today we check our questions for hidden yes-men.
2-12 The praise trap, instructor demo. Pitch a deliberately flawed idea and watch ai applaud. Re-prompt: "roast this, find the failure mode." Same idea, opposite verdict. Why? Sycophancy is a feature of RLHF, not a quirk.
12-22 Break the model. Pods race to induce the most confidently incorrect response about their venture -- a hallucination that sounds authoritative on the surface. Debrief aloud: what conditions made it easy?
22-37 Turn the lens around. Pods audit the interview questions they drafted this morning for yes-man questions: leading, loaded, fishing for flattery.
37-55 Rewrite lab. ai as adversarial reviewer of the question guide: "find every question that can only produce a flattering answer." Pods accept or reject each suggestion. They keep the pen.
55-70 The doors. Introduce the system prompt as the hidden instruction layer, then run a careful, controlled prompt injection demo (instructor screen only). [CHANGED] added: ai poisoning introduced beside it as the training-time cousin. Emerging risks, same lesson.
70-85 Risk surface. Pods map every place untrusted input enters their venture workflow and draft a first venture system prompt.
85-90 Exit line: tomorrow you talk to real people. The questions are now honest.

**Takeaway.** The mirror reflects what you ask it to reflect, and any input can become a master if you don't watch the doors. **Artifacts.** Revised interview guide, venture system prompt, injection and poisoning risk surface.


### Block 6. W2 D3 (90 min): The Generation Game

[CHANGED] changed: hands-on redirected to interview synthesis per D-Cal, so the block serves the day. The architectures and Nightshade/Glaze content is compressed into a 15-minute frame, and the local image generation lab is cut (it also never survives 40 students on school wifi). D-Cal's alternative of pulling Block 7 earlier is resolved here, since this block hands Block 7 real material.

**Run of show**

0-2 Last time we learned: sycophancy is a feature of RLHF, and honest questions are a skill. Today we turn to interview synthesis.
2-17 The machine tour, compressed to three concepts. (a) All generative ai is pattern matching. (b) Two architectural families: diffusion (image) and autoregressive (text). (c) Training provenance is the ethical lever -- who consented. A one-pager covers the full family tree, Nightshade, and Glaze for optional depth.
17-27 Pivot. You have been collecting interview notes all week. Synthesis is where ai is actually useful, and also where it quietly flattens.
27-60 Synthesis lab. Pods feed their consented, anonymized interview notes to ai and request themes, tensions, and outlier voices. Then the rule: every theme must point to a literal quote in the raw notes. No quote, no theme.
60-80 The flattening check. What did ai average away? Which outlier matters most for your venture? Mark it.
80-90 One decision line per pod, kept from v1: will you use generative imagery in your venture, and if so, sourced how?

**Takeaway.** Generative ai is a family of architectures with different ethical surfaces, and a synthesizer inherits everything its training did. Verification is the move. **Artifacts.** Verified theme map with quotes attached, one flagged outlier, creator protections line.


### Block 7. W2 D5 (90 min): The Stage Set

The regrounding block. Position unchanged. It now receives Block 6's synthesis as raw material.

**Run of show**

0-2 Last time we learned: synthesis requires verification -- every theme needs a quote. Today we pull back the full lens.
2-17 Pull back the lens. Project the curriculum map and place every concept so far (Inheritance, positionality, hallucination, shadow, sycophancy, system prompts, generative ethics) onto the pipeline: research, ideation, validation, prototyping, pitching. Students see where they stand.
17-32 Context engineering as a discipline: role, constraints, examples, anti-examples, audience, tone. The work moved out of the prompt and into the stage around it.
32-67 Build. Pods write a context brief for one recurring venture task, using their verified synthesis from Block 6 as the context payload. Run it. Run the naive prompt of the same request. Diff.
67-87 AI Integration Plan: which tools for which venture tasks, with a receipts column (sources, ethics check, harness rules coming in W3).
87-90 Exit line: you already have these muscles. This is design thinking pointed at the machine.

**Takeaway.** Context engineering is a design discipline. **Artifacts.** Reusable context brief template plus personal AI Integration Plan.


## WEEK 3: ai is a tool, not an agent

### Block 8. W3 D1 (90 min): Not the Writer, Not the Designer

**Run of show**

0-2 Last time we learned: context engineering is a design discipline. Today we confront the seduction of vibe coding.
2-22 Vibe coding demo (Cursor, v0, Bolt, or Claude Code), one screen, full impressiveness allowed.
22-32 The interrogation. Did the ai write? No. It pattern-completed against millions of repos. Did it design? No. It applied training-distribution defaults. What roles did you play? Name them on the board: director, editor, architect, taste-maker, ethical reviewer, debugger of meaning.
32-72 Pod build: one small venture asset in a vibe tool. One driver per pod, rotate at the 20-minute mark so it is not the same kid coding.
72-87 Role Lattice: what ai scaffolds vs what the pod owns outright.
87-90 Exit line: the seduction is real, and naming it is the literacy move.

**Takeaway.** ai does not have roles. You assign it scaffolding work. The roles remain yours. **Artifacts.** Vibe-coded venture asset plus Role Lattice.


### Block 9. W3 D2 (90 min): The Imaginary Friend

**Run of show**

0-2 Last time we learned: ai does not have roles. You assign it scaffolding work. Today we talk about imaginary friends.
2-17 Share circle: who had an imaginary friend, and what was it for? (Companionship, narrative play, a witness.) No one was wrong to have one.
17-42 Artifact tour, 3 or 4 real cases: Replika users, the "is ai conscious" debates, anthropomorphic UI choices, comment threads arguing as if ai has feelings. Two questions per case: what real human need is being answered, and what is ai actually doing mechanically?
42-67 Pod map: user need vs user projection for their venture.
67-87 Stance statement. Will their product use anthropomorphic patterns (warm voice, "I" language, personality)? Why or why not, with their community in mind.
87-90 Exit line: the need is real, the friend is imaginary, both are true at the same time.

**Takeaway.** You are designing into a live emotional ecosystem whether you like it or not. A tool, or a presence to project onto? Which are you building? **Artifacts.** Need vs projection map plus anthropomorphism stance.


### Block 10. W3 D3 (90 min): The Footnote

**Run of show**

0-2 Last time we learned: you are designing into a live emotional ecosystem. Today we talk about footnotes and receipts.
2-17 Innovation myth-bust. Innovation is not invention from nothing. It is recombination plus timing plus audience fit. Sustaining vs disruptive.
17-32 NotebookLM demo including the Audio Overview. Let it land, then name it: a feature that looks like a research breakthrough and behaves like a research bypass.
32-42 Source quality matrix: who funded this, when was it written, who is it for. Footnotes as the receipt trail.
42-77 Lab. Pods gather 5+ sources for one venture question, load, summarize, then verify three specific claims against the originals. Document where it was accurate, where it shaded, where it confabulated.
77-90 One-sentence innovation positioning per pod: incremental, adjacent, or transformational.

**Takeaway.** Not all features are good. Secondary research is innovation practice, not a chore before it. **Artifacts.** Source Quality Matrix plus verified summary plus positioning sentence.


### Block 11. W3 D5 (90 min): The Stack

**Run of show**

0-2 Last time we learned: research is recombination plus timing plus audience fit. Today we look at the floor under the floor.
2-27 The floor under the floor: domains, DNS, hosting, server vs serverless vs static, what APIs cost, where ai lives in a real product, and where the data goes when you "just use ChatGPT" for customer work.
27-67 Pod diagram: their venture's actual stack, domain to data flow.
67-87 Infrastructure budget estimate for going live.
87-90 Exit line: ai runs on bills, policies, and physical places. This is what keeps the venture alive after the program ends.

**Takeaway.** ai products are not free-floating magic. You are learning the substrate. **Artifacts.** Stack diagram plus infrastructure budget.


## WEEK 4: ai is a position, not a destination

### Block 12. W4 D1 (90 min): The Invisible Market

**Run of show**

0-2 Last time we learned: ai runs on bills, policies, and physical places. Today the statistical shadow returns with teeth.
2-17 Exa, citation first, joins NotebookLM. The research stack now has a static leg and a live leg.
17-47 Market brief sprint on their target market.
47-72 Gaps Map: who is missing from this description, and why might that be?
72-90 Wedge hypothesis: which gap is your actual entry point, and why.

**Takeaway.** The Statistical Shadow returns with teeth. Training data politics become competitive strategy. The gap in the data is the wedge in the market. **Artifacts.** Exa market brief plus Gaps Map plus wedge hypothesis.


### Block 13. W4 D2 (90 min): The Automated Self

**Run of show**

0-2 Last time we learned: the gap in the data is the wedge in the market. Today we look at the automated self.
2-17 Concept tour, no tools yet: fine-tuning, voice assistants, swarm agents and orchestration. [CHANGED] housekeeping: orchestration named here so the pattern principles and the block agree.
17-37 Tradeoffs frame with the futures cone: probable, plausible, possible, preferable automation for your venture. The cone forces them to articulate what they are choosing not to build.
37-77 Build: a real-time pitch coach with explicit anti-bias and anti-sycophancy instructions (Yes-Man callback) and hard scope boundaries.
77-90 Pair practice. Pitch to a peer with the coach running. Debrief: did it help, did it flatten, did it lie?

**Takeaway.** The question is never "can you automate it" but "should you, and what is lost." **Artifacts.** Working pitch coach with documented system prompt plus a "what I won't automate" statement.


### Block 14. W4 D3 (90 min): The Mark

**Run of show**

0-2 Last time we learned: the question is never "can you automate it" but "should you, and what is lost." Today we close with the mark.
2-7 Two roads, rules on screen.
7-45 Road A, Prompt Burn. Selection criteria written before generating. 100 marks in a session, curate to three. Count the token burn, the compute, the environmental cost.
45-85 Road B, Pencil to Pixel. One logomark, by hand, ai used only for variation and refinement. The hand-eye-mind chain is the lesson.
85-90 Debrief: which road produced the mark you would actually use? Which one are you proud of? Are those the same answer?

**Takeaway.** ai as accelerant vs ai as substitute, staged physically in one room. The receipts students carry into the final pitch come from here. **Artifacts.** Finished brand mark plus annotated process log: what was ai-assisted, what was hand-crafted, which decisions were theirs alone.


## Summary table

| # | Slot | Block | Artifact | v2 change |
|---|---|---|---|---|
| 1 | W1 D2 | The Inheritance | 2026 Prompt Cheat Sheet v0 | AOT foundations integrated |
| 2 | W1 D3 | Same Question, Different Mouths | Positionality template plus 3-model diff | Demo script completed, AOT cheat sheet alignment |
| 3 | W1 D4 | The Sanity Report | 1-page flaw audit | Redirected to critical thinking, CLI install becomes a demo |
| - | W1 D5 | Find Your User (pre-work) | Research plus 2 real conversations | New, per D-Cal |
| 4 | W2 D1 | The Statistical Shadow | Persona-vs-data chart plus delta | Builds on pre-work, brainstorm-not-validate frame |
| 5 | W2 D2 | The Yes-Man | Interview guide, system prompt, risk surface | Tied to customer discovery, poisoning added |
| 6 | W2 D3 | The Generation Game | Verified theme map, outlier, creator stance | Hands-on becomes interview synthesis |
| 7 | W2 D5 | The Stage Set | Context brief plus AI Integration Plan | Receives B6 synthesis |
| 8 | W3 D1 | Not the Writer, Not the Designer | Vibe-coded asset plus Role Lattice | None |
| 9 | W3 D2 | The Imaginary Friend | Need vs projection map plus stance | None |
| 10 | W3 D3 | The Footnote | Source Quality Matrix plus positioning | None |
| 11 | W3 D5 | The Stack | Stack diagram plus infra budget | None |
| 12 | W4 D1 | The Invisible Market | Market brief, Gaps Map, wedge | None |
| 13 | W4 D2 | The Automated Self | Pitch coach plus "won't automate" statement | Orchestration named in concept tour |
| 14 | W4 D3 | The Mark | Brand mark plus process log | None |


## Pattern principles for facilitators

Every block ends with a human judgment ai cannot make. No block closes on ai's output as the final word.

The three-column template (AI Does / Student Does / Human Skill Being Built) carries through every block. Same documentation pattern as the AOT analysis. It makes the value legible to reviewers and to students.

Operator tools are distributed across the arc, not concentrated. Data work in W2 D1, vibe coding in W3 D1, infrastructure in W3 D5, orchestration in W4 D2. By the end of W3 the consumer vs operator distinction is lived, not lectured.

Earlier blocks return as analytical lenses. The Shadow returns in The Invisible Market. The Yes-Man returns in The Automated Self. The Inheritance returns in The Generation Game. This is how the curriculum compounds.

Name the seduction before letting the impressiveness land. Students do not get to be fans. They get to be operators.
