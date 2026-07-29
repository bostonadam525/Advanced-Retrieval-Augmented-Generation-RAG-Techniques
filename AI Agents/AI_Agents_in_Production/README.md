# AI Agents in Production

---
# Where do Agents often break in production?
1. Processes crash mid-run
   - What: OOM kill, deployments, network drops
   - Problem: work is lost

2. Human-in-the-loop breaks
   - What: approvals are held in memory
   - Problem: timeout or restart the system? requests are lost

3. No visibility
   - What: In-process agents leave no trail or traces.
   - Problem: Can't replay, can't debug.
  
4. Scaling = reinventing
   - What: Across machines it is very difficult to scale a LangChain agent to 10,000 or more users. 
   - Problem: have to reinvent and rebuild the entire system!

---
# What 7 things do you need for an AI Agent to be Production Ready?
1. Durability --> survive system crashes
2. Retries --> per-step, automatic -- need automatic retries! 
3. Human-in-the-loop --> wait minutes or days
4. Observability --> replayable history -- need to see whats going on in real-time
5. Long-running tasks --> if an agent has to run for hours on end vs. seconds, either situation you need to handle
6. Scale --> across machines, etc.
7. Testing --> deterministic, no real LLM calls

---
## Agent Frameworks
- AgentSpan
- LangGraph
- Crew.ai
- n8n
- Foundation Model native (e.g. Anthropic ADK, OpenAI ADK, Google ADK, etc.)
- ....the list goes on...

---
## Architecture
- This example is using AgentSpan, see docs: https://agentspan.ai/docs/quickstart/
1. Worker (custom code/functions)
   - tool frameworks
   - business logic
   - can crash anytime!
2. Server
   - orchestrator
   - state + history database
   - retry + HITL queues
3. LLM
   - Claude - GPT - Gemini - etc...
   - Stateless
   - Swap in and out anytime
