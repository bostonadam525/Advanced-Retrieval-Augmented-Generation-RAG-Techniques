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

---
# LangChain Agents - Agentic Steps Under the Hood
- This is important to understand the fundamentals of what the code is doing. 

## 1. Run Python Code - Chain of Control
- Code calls LangChain. 
- LangChain prepares Prompt and Tool definitions.
- LangChain sends request to Model API. 
- **User never directly communicates with the LLM! (That part is important!)**

- This is the code:
```
run_agent("What is 15 multiplied by 8, then divided by 3?)

## run_agent does this:
result = agent.invoke({
         "messages": [("user", question)]
})

```

## 2. LangChain calls Model API
- This step is like giving the model a "toolbox" before actually asking a question.

- LangChain calls Model API with user messages and available tools:

```
Messages = conversations thus far.
Tools = list of functions model is allowed to call.
LangChain generated tool schemas from the @tool functions.

```

## 3. Model Returns a Tool Call #1
- Model sees question now and decides how to reason through the process:
   - First I need to multiply 15 by 8.
   - Then I need to divide result by 3. 
   - But model cannot execute Python code by itself. Instead, it **returns a structured Tool Call request/object.**
   - The first response may look like this:

   ```
   "role": "assistant",
   "content": "",
   "tool_calls": [
      {
         "id": "call_001",
         "type": "function",
         "function": {
            "name": "multiply",
            "arguments": "{\"a\":15, \"b\": 8}"
         }
      }
   ]

   ```

## 4. LangChain interprets the response
   - LangChain reads response and notices:
      - Did the LLM not give a final natural-language generated answer yet, instead it actually asked for a tool call.
      - This is the logic:
      ```
      Is there a text generated answer? 
      NO --> content is empty

      Are there tool_calls?
      YES --> tool call detected!
      ```

   - LangChain will extract 3 pieces of information from this as we see below. The tool `id` number is very important so that the model knows which tool call this is:

   ```
   1. tool_name = "multiply"
   2. tool_args = {"a": 15, "b": 8}
   3. id        = "call_001"

   ```
   - **Important distinction:** if you were building this without LangChain or a pre-defined framework, you would have to determine which Python function corresponds to the tool name used here "multiply" by writing your own parsing logic. 


### 4b. LangChain Maps Tool Name to real Python function reference
   - LangChain internally will maintain a registry of tools as we see below:

   ```
   tool_registry = {
      "add": add,
      "multiply": multiply,
      "divide": divide,
      "square_root": square_root,
   }

   ```
   - LangChain basically maintains a Python dictionary internally that maps string names to individual tool calls.
   - So all it has to do is perform a simple dictionary lookup:

   ```
   selected_tool = tool_registry["multiply"]

   ```
   - Now `selected_tool` points to the actual Python function:

   ```
   @tool
   def multiply(a: float, b: float) -> float:
      return a * b

   ```

- This can be simply interpreted as:

```
Model World: 
"multiply" --> just a string

Python World:
multiply(a,b) -> real function

```

## 5. LangChain executes Python Function
- Now the code can be run for the tool call:

```
@tool
def multiply(a: float, b: float) ->
   return a * b

# LangChain calls tool
result = multiply(a=15, b=8)
#result = 120

```

### In Real Agentic Systems Tools will do more:
- Query a database --> call external API
- Send email --> create support ticket
- Read/write files --> provision cloud resources

- Example function:
```
def lookup_order(order_id):
   return
database.query(...)

```


## 6. LangChain sends Tool#1 result back
- It sends the entire JSON payload back to the model.
- **The reason the model needs this FULL CONTEXT is because LLMs are STATELESS and do not remember previous system calls.**
- The payload would look like this, notice the metadata as well. We can see below it is broken up into 3 sections:
   - 1) messages
   - 2) metadata
   - 3) id of tool call

```
{
   "messages": [
      {
         "role": "user",
         "content": "What is 15 multipled by 8, then divided by 3?"
      },
      {
         "role": "assistant",
         "content": "",
         "tool_calls": [
            {
               "id": "call_001",
               "type": "function",
               "function": {
                  "name": "multiply",
                  "arguments": "{\"a\": 15, \"b\: 8}"
               }
            }
         ]
      },
      {
         "role": "tool",
         "tool_call_id": "call_001",
         "content": "120"
      }
   ],
   "tools": [...same tool definitions...]
}


```

## 7. Model reasons and requests Tools #2 -- call_002
- Model sees result = 120 and knows it still needs to divide by 3. 
- LLM reasoning process:

```
"15 x 8 = 120 -- ok now i need 120/3. Let me call the divide tool to get this."

```
- The important concept here is that the model will use input from 1 tool call into a new tool call. So it takes the output of the multiply tool and uses it as input to the divide tool call as we see below:

```
{
   "role": "assistant",
   "content": "",
   "tool_calls": [
      {
         "id": "call_002", ## new tool call id
         "type": "function",
         "function": {
            "name": "divide",
            "arguments": "{\"a\": 120, \"b\": 3}"
         }
      }
   ]
}

```
- **This is the real power of the AGENTIC LOOP. Each tool call is building upon the previous step.**
- **Same Pattern but NEW Data:**

```
New call ID: call_02
New tool: divide
New args: a=120, b=3

```

## 8. LangChain interprets and executes Python Function/tool #2
- Executes divide tool call function:

```
@tool
def divide(a: float, b: float) -> float:
   """Divide the first number by the second. Returns error if dividing by zero."""
   if b == 0:
      return "Error: Cannot divide by zero"
   return a / b

```

## 9. LangChain returns Tool #2 result
- entire conversation with metadata is sent back to model again. 
- This allows the entire chain of reasoning to be shared with the model. 


## 10. Model generates answer
- Model now understands it has all the information it needs to reason over the answer.
- Model can now generate final natural language answer. 
- "Exit signal" -- agentic loop is complete!
- This is the ReAct (reason and act loop completion)


## 11. Monitoring and Tracing
- We can monitor and trace the tool calls and reasoning.
- Its important to understand the internal abstractions that LangChain does for you esspecially if you do not use 