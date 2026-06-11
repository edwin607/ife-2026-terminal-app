<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4;
    margin: 2cm 2.2cm;
    @bottom-center {
      content: "IFE Facilitator Reference · page " counter(page) " of " counter(pages);
      font-size: 8pt;
      color: #94a3b8;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
  }
  body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1e293b;
  }

  /* Cover */
  .cover {
    text-align: center;
    padding-top: 5cm;
  }
  .cover .tag {
    font-size: 9pt;
    letter-spacing: 3pt;
    text-transform: uppercase;
    color: #3b82f6;
    font-weight: 700;
  }
  .cover h1 {
    font-size: 26pt;
    font-weight: 700;
    margin-top: 0.5cm;
    margin-bottom: 0.3cm;
    color: #0f172a;
  }
  .cover .subtitle {
    font-size: 12pt;
    color: #475569;
    max-width: 12cm;
    margin: 0 auto 1.5cm;
  }
  .cover .meta {
    font-size: 9pt;
    color: #94a3b8;
  }
  .cover .rule-box {
    background: #f0f5ff;
    border: 1px solid #bfdbfe;
    border-radius: 8pt;
    padding: 0.6cm 1cm;
    margin: 2cm auto 0;
    max-width: 10cm;
  }
  .cover .rule-box p {
    font-size: 11pt;
    font-weight: 600;
    color: #1e40af;
    margin: 0;
  }
  .cover .rule-box .small {
    font-size: 8pt;
    font-weight: 400;
    color: #3b82f6;
    margin-top: 4pt;
  }

  /* Sections */
  h2 {
    font-size: 14pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 4pt;
    margin-top: 1.2cm;
  }
  h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 0.6cm;
  }
  p { margin: 0.3cm 0; }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.4cm 0;
    font-size: 9pt;
  }
  th {
    background: #1e293b;
    color: white;
    padding: 6pt 8pt;
    text-align: left;
    font-weight: 600;
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
  }
  td {
    padding: 6pt 8pt;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }
  tr:nth-child(even) td { background: #f8fafc; }
  td:first-child { white-space: nowrap; font-weight: 600; }

  .tool-badge {
    display: inline-block;
    padding: 1pt 6pt;
    border-radius: 3pt;
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
  }
  .badge-cli { background: #dbeafe; color: #1d4ed8; }
  .badge-comfy { background: #fce7f3; color: #be185d; }
  .badge-langflow { background: #d1fae5; color: #047857; }

  .skill-tag {
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
    padding: 1pt 5pt;
    border-radius: 2pt;
    font-size: 7pt;
  }

  .principle-box {
    background: #fffbeb;
    border-left: 3pt solid #f59e0b;
    padding: 0.3cm 0.5cm;
    margin: 0.4cm 0;
    font-size: 9pt;
  }

  .page-break { page-break-before: always; }

  /* Setup guide entries */
  .setup-block {
    border: 1px solid #e2e8f0;
    border-radius: 6pt;
    padding: 0.4cm 0.5cm;
    margin: 0.4cm 0;
  }
  .setup-block h4 {
    font-size: 10pt;
    font-weight: 700;
    margin: 0 0 4pt;
  }
  .setup-block code {
    background: #f1f5f9;
    padding: 1pt 4pt;
    border-radius: 2pt;
    font-size: 8pt;
    font-family: 'SFMono-Regular', Consolas, monospace;
  }

  .quick-card {
    border: 2px solid #1e293b;
    border-radius: 8pt;
    padding: 0.5cm;
    margin: 0.4cm 0;
  }
  .quick-card table { font-size: 8pt; }
  .quick-card th { font-size: 7pt; padding: 4pt 6pt; }
  .quick-card td { padding: 4pt 6pt; }
</style>
</head>
<body>

<div class="cover">
  <p class="tag">IFE 2026 &middot; Facilitator Reference</p>
  <h1>AI Tools as Backbone</h1>
  <p class="subtitle">How <strong>llm CLI</strong>, <strong>ComfyUI</strong>, and <strong>Langflow</strong> support every entrepreneurship activity &mdash; without becoming the main event.</p>
  <div class="rule-box">
    <p>&ldquo;Today we learn <u>entrepreneurship</u>. The AI helps us <u>do it faster</u>.&rdquo;</p>
    <p class="small">Entrepreneurship First Rule &mdash; every session starts with the business goal, not the tool.</p>
  </div>
  <p class="meta">Generated from 2026 IFE Course Planning.xlsx &middot; AI Tracks Comparison</p>
</div>

<div class="page-break"></div>

<h2>How It Works</h2>

<p>Your curriculum gives you 90 minutes of AI instruction per day inside a larger entrepreneurship program. The AI is a multiplier, not the subject. These three open-source tools replace the paid tools listed in the curriculum while keeping the learning objectives intact.</p>

<h3>The Three Tools</h3>

<table>
  <tr>
    <th style="width:18%">Tool</th>
    <th style="width:30%">What It Does</th>
    <th>Best For</th>
    <th style="width:22%">Replaces</th>
  </tr>
  <tr>
    <td><span class="tool-badge badge-cli">CLI</span> llm</td>
    <td>Run prompts from the terminal. Pipe data in, get text out. Chain commands together.</td>
    <td>Text generation, data analysis, roleplay, prompt chaining, batch exercises</td>
    <td>ChatGPT Canvas, Perplexity Pro, Claude 4</td>
  </tr>
  <tr>
    <td><span class="tool-badge badge-comfy">UI</span> ComfyUI</td>
    <td>Node-based visual pipeline for AI image generation. Students see every step as a connected block.</td>
    <td>Image creation, prototyping, visual bias comparison, pitch assets</td>
    <td>Ideogram 2.0, Canva Magic Media, HeyGen</td>
  </tr>
  <tr>
    <td><span class="tool-badge badge-langflow">Flow</span> Langflow</td>
    <td>Drag-and-drop builder for multi-agent workflows. Agents, tools, and LLMs as visual nodes.</td>
    <td>Multi-agent research, chatbot building, pitch coaching, competitive analysis</td>
    <td>Browse.ai, Typeform AI, Elicit</td>
  </tr>
</table>

<div class="principle-box">
  <strong>Order of introduction:</strong> Start with the CLI (Week 1). It's text-only and teaches the core skill: talking to a model. Add ComfyUI in Week 2 when you need images. Bring in Langflow in Week 3 when students are ready to orchestrate multiple agents. Each tool builds on the one before.
</div>

<div class="page-break"></div>

<h2>Week-by-Week Tool Map</h2>

<p>Each row maps to the <strong>Fun &amp; Guided AI Track</strong> column in your spreadsheet. The tool listed is the recommended replacement for the paid tool originally specified.</p>

<h3>Week 1 &mdash; Foundations</h3>
<table>
  <tr><th style="width:10%">Day</th><th style="width:22%">Activity</th><th style="width:10%">Tool</th><th>What Students Do</th><th style="width:22%">Entrepreneurship Skill</th></tr>
  <tr>
    <td>1.2</td>
    <td>The AI Whisperer</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td>Students write prompts in the terminal to make the AI guess a secret word without using forbidden terms. They see how wording changes output.</td>
    <td>Structured Prompting (T) &middot; Probabilistic Logic (C)</td>
  </tr>
  <tr>
    <td>1.3</td>
    <td>Founder's Remix</td>
    <td><span class="tool-badge badge-comfy">UI</span></td>
    <td>Build a ComfyUI pipeline that turns 3 random objects into an image of a social enterprise for a superhero. 10 wild ideas in 10 minutes.</td>
    <td>Collaborative Design (C) &middot; Multimodal Engineering (T)</td>
  </tr>
  <tr>
    <td>1.4</td>
    <td>The Domino Effect</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td><code>cat problem_notes.txt | llm -s "List 5 ridiculous + 5 serious consequences"</code> Students pipe their research into the CLI to map second-order effects.</td>
    <td>Root Cause Analysis (C) &middot; Long-Context Management (T)</td>
  </tr>
</table>

<h3>Week 2 &mdash; Discovery &amp; Prototyping</h3>
<table>
  <tr><th style="width:10%">Day</th><th style="width:22%">Activity</th><th style="width:10%">Tool</th><th>What Students Do</th><th style="width:22%">Entrepreneurship Skill</th></tr>
  <tr>
    <td>2.1</td>
    <td>The Grumpy User</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td><code>llm -s "Roleplay as a skeptical 65-year-old..."</code> Interview the persona, then switch to a friendly version. Learn how tone changes what people reveal.</td>
    <td>Perspective Taking (C) &middot; Role-play Prompting (T)</td>
  </tr>
  <tr>
    <td>2.2</td>
    <td>Treasure Hunt</td>
    <td><span class="tool-badge badge-langflow">Flow</span></td>
    <td>Build a Langflow agent that searches the web for real complaints about a topic. Students dig for "hidden gold" in what they find.</td>
    <td>Qualitative Synthesis (C) &middot; Autonomous Web Agents (T)</td>
  </tr>
  <tr>
    <td>2.3</td>
    <td>The Translator</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td>Pipe messy team notes through chained <code>llm</code> calls: notes &rarr; haiku &rarr; rap &rarr; mission statement. One input, three outputs.</td>
    <td>Information Architecture (C) &middot; RAG-Based Retrieval (T)</td>
  </tr>
  <tr>
    <td>2.5</td>
    <td>Sketch-to-Magic</td>
    <td><span class="tool-badge badge-comfy">UI</span></td>
    <td>Photo of a napkin sketch &rarr; IP-Adapter in ComfyUI &rarr; realistic app mockup. Students see their paper idea become a screen.</td>
    <td>Modular Design (C) &middot; Component Prompting (T)</td>
  </tr>
</table>

<h3>Week 3 &mdash; Strategy &amp; Systems</h3>
<table>
  <tr><th style="width:10%">Day</th><th style="width:22%">Activity</th><th style="width:10%">Tool</th><th>What Students Do</th><th style="width:22%">Entrepreneurship Skill</th></tr>
  <tr>
    <td>3.1</td>
    <td>The Spy Agency</td>
    <td><span class="tool-badge badge-langflow">Flow</span></td>
    <td>Build a 3-agent Langflow graph: Researcher &rarr; Analyst &rarr; Writer. Each agent does one job. Students see the handoff between them.</td>
    <td>SWOT 2.0 (C) &middot; Multi-agent Research (T)</td>
  </tr>
  <tr>
    <td>3.2</td>
    <td>Robot Court</td>
    <td><span class="tool-badge badge-comfy">UI</span> + <span class="tool-badge badge-cli">CLI</span></td>
    <td>Run the same prompt through different models side by side. ComfyUI for image models, CLI for text. Compare outputs and spot bias.</td>
    <td>Meta-cognition (C) &middot; Model Comparison (T)</td>
  </tr>
  <tr>
    <td>3.3</td>
    <td>The Money Tree</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td><code>llm "List 5 weird ways people made \$1 from a similar idea"</code> Pipe results into a Google Sheet for unit economics modeling.</td>
    <td>Scalability Modeling (C) &middot; Logic-Chain Formulae (T)</td>
  </tr>
  <tr>
    <td>3.5</td>
    <td>The 5-Minute Bot</td>
    <td><span class="tool-badge badge-langflow">Flow</span></td>
    <td>Build an emoji-only chatbot in Langflow using conditional nodes. Test it on other teams for "vibe checks."</td>
    <td>Lean Methodology (C) &middot; Chatbot Orchestration (T)</td>
  </tr>
</table>

<h3>Week 4 &mdash; Markets, Money &amp; Pitching</h3>
<table>
  <tr><th style="width:10%">Day</th><th style="width:22%">Activity</th><th style="width:10%">Tool</th><th>What Students Do</th><th style="width:22%">Entrepreneurship Skill</th></tr>
  <tr>
    <td>4.1</td>
    <td>Time Traveler</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td><code>llm -s "Write a 2040 front-page article about how our startup changed the world"</code> Students craft the system prompt carefully to shape the narrative.</td>
    <td>Trend Extrapolation (C) &middot; Synthetic Data Simulation (T)</td>
  </tr>
  <tr>
    <td>4.2</td>
    <td>The Dragon's Hoard</td>
    <td><span class="tool-badge badge-cli">CLI</span></td>
    <td><code>llm "Calculate burn rate: \$X startup gold, spending \$Y/week like a King vs \$Z/week like an Inventor"</code> Students run scenarios and compare.</td>
    <td>Scenario Planning (C) &middot; Spreadsheet Automation (T)</td>
  </tr>
  <tr>
    <td>4.3</td>
    <td>The Elevator Race</td>
    <td><span class="tool-badge badge-langflow">Flow</span></td>
    <td>Debate flow: Coach Agent vs Critic Agent vs Summarizer Agent. Students pitch, get feedback, revise, repeat. Fastest iteration wins.</td>
    <td>Persuasive Communication (C) &middot; Real-time Speech Analysis (T)</td>
  </tr>
</table>

<h3>Week 5 &mdash; Finals</h3>
<table>
  <tr><th style="width:10%">Day</th><th style="width:22%">Activity</th><th style="width:10%">Tool</th><th>What Students Do</th><th style="width:22%">Entrepreneurship Skill</th></tr>
  <tr>
    <td>5.1&ndash;2</td>
    <td>Hollywood Trailer</td>
    <td><span class="tool-badge badge-comfy">UI</span></td>
    <td>Generate consistent pitch visuals through a ComfyUI pipeline. Export frames, add voiceover in CapCut (free).</td>
    <td>Storytelling Rhetoric (C) &middot; Video Synthesis (T)</td>
  </tr>
</table>

<div class="page-break"></div>

<h2>Tool Setup Guides</h2>

<p>Each guide is designed for school machines. No admin rights required for <code>pip install --user</code>. All three tools run on Mac, Windows, and Linux.</p>

<h3>1. llm CLI</h3>
<div class="setup-block">
  <h4>Installation</h4>
  <p><code>pip install llm</code> or <code>pip install --user llm</code><br>
  <code>llm keys set openai</code> (paste your API key)<br>
  <code>llm keys set anthropic</code> (paste your API key)</p>

  <h4>Quick Start for Students</h4>
  <p><code>llm "What is a stakeholder?"</code> &mdash; basic chat<br>
  <code>llm "Describe a park bench" --system "Use only 5 words"</code> &mdash; system prompt<br>
  <code>cat notes.txt | llm "Summarize this"</code> &mdash; pipe data in<br>
  <code>llm logs</code> &mdash; review your history</p>

  <h4>Day 1 Script (5 minutes)</h4>
  <p>1. Open terminal. 2. Type <code>llm "hello"</code>. 3. Type <code>llm "hello" --system "reply in pirate speak"</code>. 4. Discuss: same input, different system prompt, completely different output. That's structured prompting.</p>

  <h4>No-Internet Fallback</h4>
  <p>Print prompt templates on cards. Students write prompts on paper. Facilitator reads the best one into the CLI. The class sees the output together.</p>
</div>

<h3>2. ComfyUI</h3>
<div class="setup-block">
  <h4>Installation</h4>
  <p>Download the portable version from <code>github.com/comfyanonymous/ComfyUI/releases</code><br>
  Unzip and run. No Python setup needed for the portable build.</p>

  <h4>Quick Start for Students</h4>
  <p>Load the default workflow. It has one prompt node, one model node, one output node. Change the prompt, click "Queue Prompt," see the image appear. That's the whole mental model: prompt &rarr; model &rarr; output.</p>

  <h4>Key Workflows (Pre-built)</h4>
  <p><strong>Sketch-to-Mockup:</strong> Load a photo &rarr; IP-Adapter node &rarr; prompt node &rarr; output. Turns napkin drawings into app screens.<br>
  <strong>Bias Comparison:</strong> Two model nodes side by side, same prompt, same seed. Compare what each model generates. Different results = different training data = bias you can see.</p>

  <h4>No-Internet Fallback</h4>
  <p>Print node graph screenshots on poster paper. Students trace the pipeline with markers. They move paper "tokens" through each node to simulate what the AI does.</p>
</div>

<h3>3. Langflow</h3>
<div class="setup-block">
  <h4>Installation</h4>
  <p><code>pip install langflow</code><br>
  <code>python -m langflow run</code> &mdash; opens a browser at <code>localhost:7860</code></p>

  <h4>Quick Start for Students</h4>
  <p>Drag an "LLM" node onto the canvas. Connect it to a "Chat Input" node and a "Chat Output" node. Click play. You've built an AI. Now add a "Tool" node between input and output &mdash; that's an agent.</p>

  <h4>Key Flows (Export &amp; Import)</h4>
  <p><strong>Spy Agency (3 agents):</strong> Researcher Agent (searches the web) &rarr; Analyst Agent (finds weaknesses) &rarr; Writer Agent (writes a report). Each agent is one LLM node with a unique system prompt.<br>
  <strong>5-Minute Bot:</strong> Chat Input &rarr; Router Node (checks for emojis) &rarr; two paths: "valid emoji response" or "invalid, ask again."<br>
  <strong>Elevator Race:</strong> Student pitch &rarr; Coach Agent &rarr; Critic Agent &rarr; Summarizer &rarr; revised pitch.</p>

  <h4>No-Internet Fallback</h4>
  <p>Draw agent flowcharts on a whiteboard. Use sticky notes for each agent. Students physically move the sticky notes to show how a message travels through the system.</p>
</div>

<div class="page-break"></div>

<h2>Quick Reference Card</h2>

<div class="quick-card">
  <table>
    <tr><th style="width:8%">Wk</th><th style="width:8%">Day</th><th style="width:20%">Activity</th><th style="width:8%">Tool</th><th style="width:14%">Setup Time</th><th style="width:14%">Activity Time</th><th>Key Prompt / Flow</th></tr>
    <tr><td>1</td><td>2</td><td>AI Whisperer</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>25 min</td><td><code>llm -s "Guess the word. Forbidden: X,Y,Z"</code></td></tr>
    <tr><td>1</td><td>3</td><td>Founder's Remix</td><td><span class="tool-badge badge-comfy">UI</span></td><td>10 min</td><td>30 min</td><td>Text-to-image workflow, 10 prompts</td></tr>
    <tr><td>1</td><td>4</td><td>Domino Effect</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>25 min</td><td><code>cat notes | llm -s "List consequences"</code></td></tr>
    <tr><td>2</td><td>1</td><td>Grumpy User</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>25 min</td><td><code>llm -s "Roleplay as skeptical customer"</code></td></tr>
    <tr><td>2</td><td>2</td><td>Treasure Hunt</td><td><span class="tool-badge badge-langflow">Flow</span></td><td>15 min</td><td>30 min</td><td>Agent with web search tool</td></tr>
    <tr><td>2</td><td>3</td><td>The Translator</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>20 min</td><td><code>llm | llm | llm</code> (chained)</td></tr>
    <tr><td>2</td><td>5</td><td>Sketch-to-Magic</td><td><span class="tool-badge badge-comfy">UI</span></td><td>15 min</td><td>35 min</td><td>IP-Adapter + prompt workflow</td></tr>
    <tr><td>3</td><td>1</td><td>Spy Agency</td><td><span class="tool-badge badge-langflow">Flow</span></td><td>15 min</td><td>35 min</td><td>Researcher &rarr; Analyst &rarr; Writer</td></tr>
    <tr><td>3</td><td>2</td><td>Robot Court</td><td><span class="tool-badge badge-comfy">UI</span>+<span class="tool-badge badge-cli">CLI</span></td><td>10 min</td><td>40 min</td><td>Side-by-side model comparison</td></tr>
    <tr><td>3</td><td>3</td><td>Money Tree</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>25 min</td><td><code>llm "5 weird ways to make $1"</code></td></tr>
    <tr><td>3</td><td>5</td><td>5-Minute Bot</td><td><span class="tool-badge badge-langflow">Flow</span></td><td>15 min</td><td>30 min</td><td>Emoji router with conditional nodes</td></tr>
    <tr><td>4</td><td>1</td><td>Time Traveler</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>25 min</td><td><code>llm -s "Write 2040 article about..."</code></td></tr>
    <tr><td>4</td><td>2</td><td>Dragon's Hoard</td><td><span class="tool-badge badge-cli">CLI</span></td><td>5 min</td><td>30 min</td><td><code>llm "Burn rate: X at Y vs Z"</code></td></tr>
    <tr><td>4</td><td>3</td><td>Elevator Race</td><td><span class="tool-badge badge-langflow">Flow</span></td><td>15 min</td><td>35 min</td><td>Coach &rarr; Critic &rarr; Summarizer</td></tr>
    <tr><td>5</td><td>1&ndash;2</td><td>Hollywood Trailer</td><td><span class="tool-badge badge-comfy">UI</span></td><td>10 min</td><td>60 min</td><td>Consistent asset pipeline + CapCut</td></tr>
  </table>
</div>

<h2>Entrepreneurship First Rule</h2>

<div class="principle-box">
  <p><strong>Never open with the tool.</strong> Open with the problem.</p>
  <p style="margin-top:8pt;">Bad: "Today we're learning Langflow."<br>
  Good: "Today we're figuring out how big companies hide their weaknesses. Langflow will be our spy agency."</p>
  <p style="margin-top:8pt;">Bad: "Open the terminal and type this prompt."<br>
  Good: "Your customer won't tell you what's wrong. Let's build a persona that will."</p>
  <p style="margin-top:12pt;"><strong>The formula:</strong> "Today we learn <em>[entrepreneurship concept]</em>. The AI helps us <em>[action]</em>."</p>
</div>

<h2>Offline / Low-Tech Fallbacks</h2>
<table>
  <tr><th>Situation</th><th>What to Do</th></tr>
  <tr><td>No internet</td><td>Print prompt templates on cards. Students write prompts by hand. Facilitator queues them up and runs them when connectivity returns. The thinking work is the same.</td></tr>
  <tr><td>No laptops</td><td>Whiteboard + sticky notes. Draw agent flows manually. Students roleplay each agent. The person playing the "LLM" reads from a pre-printed response deck.</td></tr>
  <tr><td>API keys blocked</td><td>Use <code>llm</code> with local models via <code>llm install llm-llama-cpp</code>. Runs entirely on the machine. Slower but works.</td></tr>
  <tr><td>School firewall</td><td>ComfyUI and Langflow both run on <code>localhost</code>. No external requests needed once the models are downloaded.</td></tr>
  <tr><td>Time runs short</td><td>Skip the setup. Use the CLI for everything. It takes 30 seconds to start and covers 60% of the activities.</td></tr>
</table>

<div style="margin-top:1.5cm; padding-top:0.5cm; border-top:1px solid #e2e8f0; font-size:8pt; color:#94a3b8; text-align:center;">
  IFE 2026 &middot; AI Tools as Backbone &middot; Generated from 2026 IFE Course Planning.xlsx<br>
  Tools: llm (datasette.io/llm) &middot; ComfyUI (github.com/comfyanonymous/ComfyUI) &middot; Langflow (langflow.org)
</div>

</body>
</html>
