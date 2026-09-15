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
- Acts as a router for the entire body system -- the operating system!
- **The loop is the conductor of the symphony orchestration**
- These are the main components:

1. **Loop Management**
   - `Think-Act-Observe cycle` is run by this (entire "agent reasoning cycle")
   - It knows when to continue --> pause --> or stop.

2. **Reasoning Strategy**
   - Applies CoT, ReAct or other prompt techniques to break goals into granular steps.
  
3. **Memory Management**
   - Short-term scratchpad for current session
     - Query stored
     - History
     - Documents
     - Knowledge bases/sources
  - All is stored for long-term context

4. **Tool Routing**
   - Selects which tools to call
   - Formats the tool calls
   - Handles errors
   - Returns results back to LLM reasoning loop
  
5. **State Machine**
   - Tracking where in the planning the agent is.
   - Detects completion, loops, and failures.
  
6. **Safety & Guardrails**
   - This is usually hard-coded logic/policy rules that will override any LLM model reasoning when necessary to prevent hallucinations and fabrications.
---
# Reasoning Patterns
- These are very important for the reasoning component of agents.
- **There are 3 main reasoning frameworks:

## 1. **Chain-of-Thought (CoT)**
   - **What it does:** CoT breaks problems into sequential chains of intermediate reasoning steps before arriving at a conclusion. (e.g. "think step by step")
   - **When to use:**
     - Math
     - Logic
     - Step-by-step analysis

### CoT - Thinking Step by Step
- CoT is a well known prompting technique rather than an agentic pattern.
- **CoT alone does not make a model "smarter" but rather helps it use its reasoning capabilities in a more reliable manner.**
- **Core Concept:**
  - Instructs LLM to reason step-by-step BEFORE answering the user query or task.
  - Significantly improves accuracy on more complex tasks (e.g. math)
  - **Transparency!! (you can actually see the step by step reasoning)**
  - **Debugging!! (can actually see where reasoning/process went awry in the step by step process)**
  - **Variants of CoT:**
    - Zero-shot CoT: adding "lets think step by step" to any prompt.
    - Few-shot CoT: including specific examples of how to think step by step.

### CoT - limitations for Agents
- Only uses internal knowledge -- is NOT able to look up information.
- So, if the models internal knowledge is wrong or outdated, it can/will reason incorrectly with confidence (hallucinate/fabricate).
- **NOT able to self-correct vs. external reality or real-world data.**
- **NOT able to take actions in the real world.**
   
### Why CoT limitations are important for Agents?
- The limitations of CoT led to the ReAct framework!
- CoT gives agents the ability to "think" --> but we know CoT thinking using the model's own internal knowledge base as its foundation is not enough, it needs to be able to ACT on real-world data and tasks.
- **ReAct pattern == CoT + Tool use in loop**
  - Today's reasoning models (e.g. o1, DeepSeek, etc.) use CoT internally

---
## 2. **Reason + Acting (ReAct)**
   - **What it does:** Uses **reasoning/thought** with **actions** and **observations**. Intermediate reasoning is crucial for agents to determine how/when to act.
   - **When to use:**
     - Tool selection (which tool to use and why)
     - Multi-step tasks/workflows
     - External API calls
  - **In production, most Agents use ReAct frameworks - why?**
     - Balances transparency, capability, and cost.

### ReAct = CoT + Acting in loop
- Solves fundamental problem of CoT not having access to real-world data.
- ReAct bridges CoT reasoning to real world data and tasks.

### Why does ReAct work? 
- Model reasoning traces reveal and make **transparent** an agent's logic making it debuggable and more understandble.
- External tool use will ground the reasoning in real-world data --> can reduce hallucinations and fabrications
- Interleaved format prevents model from "making up" answers when it should look things up.
- **ReAct outperforms BOTH CoT-only and Action-only approaches on QA and decision-making benchmarks.**



## 3. **Tree-of-Thoughts (ToT)**
   - **What it does:** Explores multiple reasoning branches at the same time similar to a search tree. This is a popular prompt framework.
   - Each "thought" is then evaluated before the agent decides which branch of the tree to focus on.
   - **When to use:**
     - Creative tasks/workflows
     - Strategic planning
     - Exploration
     - Research


---
# Agent Frameworks
- Its important to know about these frameworks below. While LangGraph is the most popular and most heavily adapted, it is not the only framework you can use and this may depend on your infrastructure, domain, and data.

1. **LangChain/LangGraph**
   - largest agentic ecosystem
   - graph-based + stateful workflows
   - **When to use**: production systems needing flexibility in development with stateful systems
   - **Weakness:**
     - can be overengineered for simple tasks
     - multiple abstraction layers --> more complex
     - multiple package dependencies in langchain ecosystem
  
2. **Open AI Agents SDK**
   - you can define agents and orchestrate multi-agent workflows (based off the OpenAI Swarm)
   - **When to use:** OpenAI Agent Stack, Built-in Tracing, Guardrails, multi-agent systems
   - **Weakness**: less flexible than LangGraph for orchestration

3. **CrewAI**
   - Role-based multi-agent teams, very intuitive design and code
   - **When to use:** Workflows that simulate team and org structures

4. **Hugging Face SmolAgents**
   - minimal to use and great for learning/POC/testing
   - **When to use:** education, research, prototypes, POCs
  
5. **Google ADK**
   - Googles agent development kit
   - Native to Google vertex and GCP
  
---
# Basic Steps to Build an Agentic System

1. **Step 1 -- Pick the AI brain (LLM)**
-- This is the AI agent's "reasoning engine"
```
# example
from langchain.chat_models import init_chat_model

model = init_chat_model('openai-gpt-4o-mini')
```

2. **Step 2 -- Define tools**
```
# example
from langchain_core.tools import tool
import math

@tool
def add_tool(a: float, b: float) -> float:
  """Add two numbers together. Use for addition operations."""
  return a+b

```
3. **Step 3 -- Create Agent**
   - This is simply done in langchain with single line of code:
```
from langchain.agents import create_agent

agent = create_agent(
  model=model,
  tools=tools
 )
- Runs ReAct loop "in the backend": Reason -> Act --> Observe

```
4. **Step 4 -- Ask questions/query**
- invoking the agent:

```
def run_agent(question: str):
  """Run agent and print execution trace."""
  print(f" User: {question}")
  print("-" * 50)

  result = agent.invoke({
    "messages": [("user",question)]
  })
  print(" Agent:", result)


```

---
## Python essentials for building agents

1. **Decorators**
   - `@tool` will wrap functions so an agent can register it as a callable tool.
   - The `@` is the decorator label

2. **Docstrings**
   - `""" """`
   - Triple quoted strings describe what the tool does.
   - **Important** so the LLM reads the docstrings to determine WHEN and HOW to use each tool.
   - **Docstrings should be detailed. Vague docstrings will open the door for hallucinations and fabrications. These are instructions for the LLM to understand when and how to use the tool.**

3. **Type Hints**
   - example: `(a: float)`
   - This tells the LLM reasoning brain what data type each parameter is supposed to expect.
   - Agent reads these as type hints.
   - If the wrong data types are received this can lead to hallucinations and fabrications.
   - This is another reason why using Pydantic is often preferred.

4. **Return Types**
   - example: `(-> float)`
   - This after the function parameters will inform the agent what kind of data the tool sends back.
   - This helps the agent plan how to use a tool's output as another tool's input in a loop.
  
### Why this matters?
- The LLM never sees the entire function for your tools.
- The LLM gets a JSON send to it such as this below. These are explicit instructions for how the LLM can use the tool. 

```
{"name":"add","description":"Add two numbers...","parameters":{"a":{"type":"number"},"b":{"type":"number"}}}
```

