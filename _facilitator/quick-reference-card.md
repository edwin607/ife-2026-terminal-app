# IFE 2026 — AI Tools Quick Reference (Free / API-Only)

Everything here is either free open-source software or uses free API tiers. No paid subscriptions required.

## Free API Providers (No Credit Card)

| Provider | Models | Free Tier |
|----------|--------|-----------|
| Groq | Llama 3, Mixtral, Gemma | 30 req/min, no card needed |
| Google AI Studio | Gemini 2.0 Flash | 1,500 req/day, no card needed |
| OpenRouter | 200+ models (pay-per-use) | Some free models, $1 free credit |
| Local (cpu lp) | Llama 3.2 1B/3B | $0 — runs entirely offline |

---

## Entrepreneurship First Rule

> **"Today we learn _____. The AI helps us _____."**
>
> Never open with the tool. Open with the problem.

---

## Week-by-Week Tool Map

| Wk | Day | Activity | Tool | Setup | Activity | Key Prompt / Flow |
|----|-----|----------|------|-------|----------|-------------------|
| 1 | 2 | AI Whisperer | llm CLI | 5m | 25m | `llm -m groq "Describe X without using Y"` |
| 1 | 3 | Founder's Remix | ComfyUI | 10m | 30m | SDXL workflow, 10 prompt iterations |
| 1 | 4 | Domino Effect | llm CLI | 5m | 25m | `cat notes \| llm -s "List consequences"` |
| 2 | 1 | Grumpy User | llm CLI | 5m | 25m | `llm -s "Roleplay as skeptic" --no-stream` |
| 2 | 2 | Treasure Hunt | Langflow | 15m | 30m | Search agent (no-cost, local models) |
| 2 | 3 | The Translator | llm CLI | 5m | 20m | `llm \| llm \| llm` (chained pipes) |
| 2 | 5 | Sketch-to-Magic | ComfyUI | 15m | 35m | IP-Adapter + SDXL, no GPU cloud needed |
| 3 | 1 | Spy Agency | Langflow | 15m | 35m | 3-agent flow: Researcher > Analyst > Writer |
| 3 | 2 | Robot Court | ComfyUI+CLI | 10m | 40m | SD vs SDXL side-by-side, local comparison |
| 3 | 3 | Money Tree | llm CLI | 5m | 25m | `llm -m google-gemini "5 weird ways to $1"` |
| 3 | 5 | 5-Minute Bot | Langflow | 15m | 30m | Conditional emoji router node |
| 4 | 1 | Time Traveler | llm CLI | 5m | 25m | `llm -s "Write 2040 article about..."` |
| 4 | 2 | Dragon's Hoard | llm CLI | 5m | 30m | `llm "Burn rate: X spending Y vs Z"` |
| 4 | 3 | Elevator Race | Langflow | 15m | 35m | Coach > Critic > Summarizer agents |
| 5 | 1-2 | Hollywood Trailer | ComfyUI | 10m | 60m | Consistent asset generation + CapCut |

---

## Tool Setup (Zero Cost)

**llm CLI:** `pip install llm`
```
llm keys set groq          # free, no credit card
llm keys set google        # free, no credit card
llm -m groq "hello"        # first prompt
llm -m gemini-2.0-flash "hi"  # backup provider
```
No API key at all: `llm install llm-llama-cpp && llm -m llama-3.2-3b "hi"`

**ComfyUI:** Download portable from github.com/comfyanonymous/ComfyUI
- Runs on CPU (slow but free) or any GPU
- All models free: SDXL, SD3.5, FLUX (all open-weight)
- Key workflow: Image > IP-Adapter > Prompt > Output

**Langflow:** `pip install langflow && python -m langflow run`
- Opens at localhost:7860 — zero external dependencies
- Use local models via Ollama: `ollama pull llama3.2` then connect in Langflow
- Or use free API endpoints (Groq, Google) as provider nodes

---

## Offline / No-Cost Fallbacks

| Situation | Solution |
|-----------|----------|
| No internet | Print prompt cards. Students write prompts by hand. Facilitator runs them when connectivity returns. |
| No laptops | Whiteboard + sticky notes. Students roleplay the agents. "LLM" reads from pre-printed response deck. |
| API keys blocked | Local models via `llm install llm-llama-cpp` or ComfyUI (runs entirely offline after download). |
| School firewall | All tools run on localhost. No external requests needed once installed. |
| No GPU | ComfyUI runs on CPU. Slower (1-2 min per image) but usable for demonstrations. |
| Running short on time | Use CLI only. Covers 60% of activities, 30-second setup. |

---

## Session Script

1. **Hook** (2m): "Your customer won't tell you what's wrong. Let's build an AI persona that will."
2. **Entrepreneurship goal** (2m): State the business concept first.
3. **Tool intro** (1m): "We'll use llm CLI to do this — it's free, no account needed."
4. **Activity** (20-35m): Students work in teams.
5. **Debrief** (5m): What did the AI teach you about the business problem?
