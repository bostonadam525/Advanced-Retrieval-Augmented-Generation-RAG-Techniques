# Loop Engineering



---
## The Current Problem
- Most people follow this workflow

1. Input request
2. Wait
3. Read answer and fix/iterate on it
4. Input prompt again

- The problem? Every step runs through you. You have to decide what to ask, judge the outputs and decide the next iteration.
- The AI is not running autonomously and using its full capacity efficiently.

---
## Prompt Engineering vs. Loop Engineering
- A loop is an automated system that runs for you. You set it up --> it finds the "work" --> gives AI models what they need --> let it run --> check result --> decides what happens next (on its own accord).
- A loop is NOT a for-loop in your code.
- The diagram below is from Analytics Vidhya:



<img width="1026" height="408" alt="image" src="https://github.com/user-attachments/assets/6f078f0f-2d11-4d7a-862f-9dd0e46323cd" />

---
## Where did Loops come from?
- This has been an evolution it did not just show up overnight.
- Here is the timeline:

1. 2022 -- ReAct
   - The concept of "reason and act".
   - The model reasons --> acts --> observes --> repeats.
   - One model, one loop, a human watching every step.
   - This is still used by many applications today.
  
2. 2023 -- AutoGPT
   - Pushed the concept one step further.
   - Let an agent run with less human supervision.
  
3. 2025 -- Ralph
   - Same prompt --> same spec --> fresh context at every pass.
   - One task at a time until its done.
  
4. 2026 -- `/goal`
   - Claude Code and Codex use this.
   - Agent runs until a validator confirms it is done.

5. July 2026 -- Orchestration
   - Loops that supervise other loops.
  
---
## Anatomy of Loops

### The 3 main concepts are:

1. **Verify**
   - This is a real built-in check on the work being done and NOT the AI model(s) grading its own work.
   - This answers: "Did the test pass?", "Is the number above the target?"
   - Without a real checks and balances, you don't actually have a loop --> what you have is the AI agreeing with itself on repeat. 
2. **State**
   - This is the record of work.
   - This tells us what the loop agents have already tried, what has not worked or failed, and what is next.
   - Without the loop it will repeat the same mistake over and over again.
   - **With the loop --> the next set of iterations will pick up where it left off using the memory of what worked vs. what didn't vs. what else should be tried next.**
3. **Stop**
   - Finish line and hard cap -- "safety". 
   - If a loop does not have an exit point it will run until it succeeds, breaks, or uses up your $$$$$$.
   - Without this step, your loop will run out of control. 

### What Every Loop Needs to Run Safely
1. Trigger -- schedule or event that starts the loop. No trigger, no loop, just a one-off run that happens once.
2. Worktrees -- isolated copies of the project --> so parallel agents don't trip over each other.
3. Skills -- resuable, recipes that store knowledge the AI would otherwise hallucinate or fabricate.
4. Connectors -- how the loop plugs into tools that are already being used --> e.g. github, slack, etc...
5. Subagents -- helpers with fresh memory that handle one focused job and report back --> so the main agent never gets overwhelmed.

### The Four types of loops
1. Heartbeat (continuous)
2. Cron (scheduled)
3. Hook (event-based)
4. Goal (verified finish)

- The chart below is from Analytics Vidhya:


<img width="1089" height="608" alt="image" src="https://github.com/user-attachments/assets/b5a05507-d652-4b59-8ab2-aa6cfd49a930" />
