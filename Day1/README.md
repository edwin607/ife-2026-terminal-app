# Day 1 — Orientation + Journey Login + Core Terminal Fun

**Folder:** `/Users/eolivera/Documents/Clients/Cambio Labs/IFE/Day1`

## Purpose

Day 1 gets every student:

1. Logged into **Journey**
2. Comfortable opening a terminal
3. Running a simple “Hello, World” command
4. Running a personalized greeting: `Hello, world! My name is ...`
5. Submitting a short reflection in Journey

This day is intentionally simple, social, and low-risk. The goal is not mastery — it is **first contact with the terminal**.

---

## Files in this folder

| File | Purpose |
|---|---|
| `hello.sh` | Tiny Bash script students can run for the final personalized greeting |
| `terminal_cheatsheet.md` | Quick commands for terminal, WSL, and fun commands |
| `journey_reflection_prompt.md` | Exact reflection prompt to post in Journey |
| `day1_run_of_show.md` | 90-minute facilitator plan with TA notes |
| `day1_spreadsheet_row.md` | Ready-to-paste row for the planning spreadsheet |
| `README.md` | This overview |

---

## Core student flow

1. Log into Journey.
2. Open a terminal.
3. Run:
   ```bash
   echo "Hello, world!"
   ```
4. Try one fun command:
   ```bash
   figlet -f slant "Hello"
   cowsay "Hello, world!"
   toilet --gay "Hello"
   echo "Hello" | lolcat
   ```
5. Run the personalized greeting:
   ```bash
   echo "Hello, world! My name is [YOUR NAME]."
   ```
6. Submit the Journey reflection.

---

## Journey reflection prompt

Post this in Journey:

> **Quick Reflection**
> 1. How did it feel to use the terminal command today?
> 2. Had you used a terminal before?
> 3. How do you think using AI through the terminal will change the way you look at AI?

---

## Notes for the facilitator

- Keep the activity **individual**.
- Allow peer help, but each student should run their own command.
- If WSL or local setup stalls for more than 3–4 minutes, switch to the cloud-terminal fallback.
- The final output should be the personalized greeting line.
