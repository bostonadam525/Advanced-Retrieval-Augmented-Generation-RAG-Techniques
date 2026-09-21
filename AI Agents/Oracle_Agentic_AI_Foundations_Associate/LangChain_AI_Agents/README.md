# LangChain for AI Agents


---
## Why use LangChain for AI Agents
- **Key takeaway: LangChain is not just for "calling foundation model APIs", its for building modular systems around the model(s).**

1. Connect
   - link LLMs to external tools, APIs, & databases

2. Orchestrate
   - Chaining of multiple steps into smart workflows.

3. Build
   - Build AGENTS, chatbots, RAG, and more.

---
## LangChain Ecosystem for AI Agents
1. LangChain -- chains, prompts, tools, memory
2. LangGraph -- graph-based Agent orchestration engine
3. LangSmith -- observability, tracing, testing, debugging
4. Integrations -- 500+ connectors for foundation models, tools, databases, APIs, and more.

----
# What Makes an AI Agent?

1. Basic LLM Call

```
Input -> Moddel -> Output

No tool usage
No dynamic reasoning
No memory of past steps
Single-shot response

```

- vs. 

2. **LangChain Agent**
- Agents are fundamentally different.
- **What makes agents so powerful is the LLM decides what tool to call, when to use the tool, and reasons over the information from the ReAct loop.**

```
Reason -> Act -> Observe -> Repeat

- Decides which tools to use
- Multi-step reasoning
- Remembers past context
- Iterates until goal is met


```

---
# Tools - Giving LLMs Superpowers
- Tools are functions that an LLM can call during its reasoning process. 
- Tools extend the model beyond text generation to allow real-world dynamic data interactions and decisions. 
- **The LLM does not use the tool. The LLM generates the request to put the tool into action in the loop. This is what makes Agentic systems powerful and allow safety/controls as we can use guardrails if an LLM hallucinates a tool call request.**
- Review examples of tools:

```
1. Web Search
- look up real-time, up-to-date info online.

2. Database Queries
- Read/write data in SQL or NoSQL

3. Code Execution
- Run Python or other code for custom functions.

4. API calls
- Can call any external API or endpoint and retrieve real-time information. 

```

---
## Anatomy of Agentic Tools
- `@tool` **Decorator** -- registers the function below as a tool the agent can discover and call.
- `a:float` **Type hints** -- tells LLM what data types to pass (auto-generates JSON schema).
- `->float` **Return type** -- tells agent what data type tool sends back.
- `"""..."""` **Docstring** -- LLM reads this to decide **WHEN** to use this tool.
   - **Clear descriptions = accurate tool selection**
- Function example:

```
@tool
def add(a: float, b: float) -> float:
   """
   Add two numbers together. Use for addition
   operations. 
   """
   return a + b


```

## ReAct (Agent) Pattern
1. **Reason** -- think about what to do next.

2. **Act** -- call a tool or respond to user.

3. **Observe** -- examine tool's results.

4. **Loop continues 1 to 3 until the goal is achieved or maximum iterations reached.**

---
# Build LangGraph Agent -- Steps

1. Create virtual environment

```
python -m venv langchain-env
source langchain-env/bin/activate

```

2. Install packages

```
pip install langchain langchain-openai langgraph
pip install python-dotenv

```

3. Set API key in .env file

```
OPENAI_API_KEY=<your-key-here>

```

## Steps to implement agent
1. Initialize model
2. Define tools (`@tool`)
3. Create Agent
4. Run agent