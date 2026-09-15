# Agentic AI Foundations
- Source: https://learn.oracle.com/ols/learning-path/become-an-oracle-agentic-ai-foundations-associate-2026/163512/163239


---
# Oracle University - AI Agents Certification 
- Notes related to this material. 



---
# AI Agents Overview


## Chatbot vs. Workflow vs. AI Agent
- Chatbot --> answers what you ask
- Workflow --> fixed sequence of predefined events or actions
- AI agent --> thinks + decides steps systematically


## AI Agent -- Mental Model
- Simple model:

```
AI Agent(LLM-based) = LLM + Tools + Loop

```
- LLM == brain
- Tools == hands
- Loop == system keeping processing going


### What can we say about AI agents?
1. Goal Directed
- working towards objective, not just responding to prompts

2. Autonomous
- decide what to do next without being told each step

3. Tool-using
- interact with APIs, databases, code execution, web search, and more. 

4. Iterative
- operates in a loop:

```
Observe --> Reason --> Act --> Observe again

```
- Key takeaway: AI agents are an architecture pattern that wrap an LLM

## Agent Execution Loop
1. Perceive -- receive input or observation
2. Reason -- selects next step in loop
3. Act -- call tool or respond to user
4. Observe -- receive tool result or feedback

**Note: loop continues until goal achieved or max iterations reached**

- Loop Termination Conditions
  - Agent decides it has the final answer
  - Maximum iteration count reached
  - Error or timeout triggers fallback


- What can go wrong in the loop?
  - Infinite loops (agent never decides it's done)
  - Hallucinated tool calls (tools get called that don't actually exist....)
  - Cost explosion (too many LLM API calls)
  - **This is why Guardrails are important**

### Example Execution Loop
- Key Takeaway: Reasoning is what drives the loop execution

- Steps:

1. User question --> book a flight from Boston to Denver
2. Agent Reasoning --> i need to book flights, i need a tool to search for these. 
3. Agent Action --> use flights tool --> search for destinations
4. Agent observation --> 3 options returned at 3 different price points
5. Agent Reasoning --> Results obtained --> agent should present options clearly to user
6. Agent Final answer --> here are the flights available

- **Reasoning determines when to call a tool and when to stop the loop.**

---
# AI Agent Core Components
- **Every single agent system no matter how complex will always have these 3 core components:**
1. **LLM**
   - 1 or multiple models (small or large!!)
   - Prompt strategies (e.g. CoT, ReAct, Tree of Thoughts, Expert based, etc...)
   - The same LLM can power various agents with different tool configs without having to fine-tune or train another model (which is why Agents are the go to stack for most now). 

2. **Tools**
   - This is what brings "power" to agents!
   - Tools create the BRIDGE between an agent and the outside world.
   - Real-time data access + real-world actions.
   - Function wrapping such as:
     - API calls
     - Database queries (SQL, NoSQL)
     - Code execution
     - File operations
     - Custom tools
     - Data validation and parsing
     - ....etc...
  - RAG and other technical skills can be leveraged (e.g. MCP, knowledge graphs, etc..)

3. **Loop (aka Orchestration)**
   - "Thinking loop" -- cyclical process that governs decisions.
   - Memory management (short-term + long-term)
   - State maintenance across multi-turn agent interactions and tool calls
   - Loops continue until the reasoning and goal(s) are achieved or stop/end is reached.
  

---
## 1 - LLM or "Agents Brain"

### What does an LLM actually do inside an agent?
  - User intent understanding from natural language queries
  - Multi-step sequence planning towards a desired goal
  - Tool decision making: which tool to call when and with what purpose or arguments?
  - Can stop or interrupt tool results and determine the next action
  - Final response generation to the user

### How do you select the LLM?
- **The most important considerations are: Latency, Cost, and Capabilities**
- **HOWEVER, the LLM is the CORE REASONING of the Agentic workflow and has many nuances MORE than just a standard benchmark score or cost or preference.**
- Model must be reliable to follow structured instructions (e.g. SYSTEM PROMPTS)
- Larger context windows are usually preferred but this can vary depending upon your task, data, domain, and more.
- Reasoning capabilities must be STRONG
- Loop iteration == 1+ API calls to LLM (foundation model vs. hosted model)
- Two-tier patterns: **cheap model for routing, capable model for reasoning capabilities**
- State of the art foundation models now have reasoning built-in to its training so chain-of-thought can automatically improve the agent's ability to reason.

---
## 2 - Tools or "Agents Hands"
- **Without tools, an LLM is just a text generator. With tools, an LLM becomes a functioning dynamic application to interact with real-world data and situations.**
- Here is the flow:

```
1. Agent defines Tools  ---> 2. Agent sends Tools to LLM ---> 3. LLM decides         --->              4. Agent Executes Tool call     --> 5. Agent returns results to LLM --> 6. Final answer or call another tool
- JSON schemas                  Tools + user query             text generation vs. tool call            code runs tool call


```
- **Important Security Boundary:**
  - LLM never executes the tool call request by itself. The LLM only submits a request to call the tool.
  - **The LLM is the "reasoning brain" for why the tool gets called.**
  - Code for the agent validates the LLM tool call then executes it.
  - MCPs provide a standardized way to connect LLMs with context they need to function such as resources, prompts, and tools.

---
## 3 - Loops Orchestration or "Agent Nervous System"
- Acts as a router for the entire body system.
- These are the main components

1. **Loop Management**
   - `Think-Act-Observe cycle` is run by this (entire "reasoning cycle")
   - It knows when to continue --> pause --> or stop.

2. **Reasoning Strategy**
   - 

