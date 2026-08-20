# Agentic Patterns
- This folder is devoted to agentic design patterns, architectures, implementations.
- I will use multiple resources for this, but the main core resource is this excellent course from neural-maze on agentic design patterns: https://github.com/neural-maze/agentic-patterns-course

---
# Agentic Patterns Commonly used
1. **Single Agent Patterns**

<img width="880" height="273" alt="Agentic patterns commonly used" src="https://github.com/user-attachments/assets/1094828a-f1c4-4b3f-990d-adee883fb3c4" />


2. **Sub Agent Patterns**
- The "main agent" handles most tasks but hands off specific tasks to other agents.

<img width="926" height="851" alt="sub agent patterns" src="https://github.com/user-attachments/assets/5216b65a-9786-44f7-b20e-88826deabd06" />



3. **Orchestrator Agent Pattern**

<img width="885" height="684" alt="orchestrator agent" src="https://github.com/user-attachments/assets/c1e1f50c-d6bb-4e18-aa69-0cd11b2918cb" />
















---
# Anthropic 2024 Paper
- In their [2024 paper, Anthropic defined Agents as 2 things](https://www.anthropic.com/engineering/building-effective-agents): 

1. Workflows -->  are systems where LLMs and tools are orchestrated through predefined code paths.
2. Agents --> are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

<img width="2856" height="2027" alt="image" src="https://github.com/user-attachments/assets/f5a89cd3-5cd1-4d4f-b4c5-8bb9ebf5bf4f" />

- source: https://huggingface.co/blog/VirtualOasis/agents-vs-workflows-en

## Workflow Design Patterns from Anthropic 
- These are meant to be approaches to problem solving rather than "set in stone" workflow design patterns. That means they are open to interpretation and may change based on the domain and use case(s).
- These include but are not limited to:

1. **Prompt Chaining**
   - Decompose larger task into smaller fixed sub-tasks
   - Goal: Break tasks into steps
      1. Decompose complex problems
      2. Modular, manageable subtasks
      3. Improves accuracy and clarity 
      4. Enables stepwise debugging
      5. Promotes use of prompt “modules”


2. **Routing**
   - Direct an input into a specialized sub-task, ensuring separation of concerns. 
   - Input —> LLM router —>route to another LLM with a specialized domain task —> output 

3. **Parallelization**
   - Breaking down tasks and running multiple subtasks concurrently. 
   - INPUT —> COORDINATOR —> multi-sub domain specialty LLMs —> AGGREGATOR —> OUT
  
4. **Orchestrator-Worker**
   - Very similar to Parallelization. 
   - HOWEVER, complex tasks are broken down dynamically and combined. 
   - INPUT —> ORCHESTRATOR —> multi-sub-specialty LLMs —> SYNTHESIZER —> OUTPUT


5. **Evaluator-Optimizer**
   - LLM output is validated by another LLM
   - INPUT —> LLM generator —> solution —> LLM evaluator —> OUTPUT
   - Note: the LLM evaluator can reject the LLM generator solution with feedback and this loop continues until the LLM evaluator accepts the output.
   - LLM as a judge is the common name for this.

## Agentic Design Patterns from Anthropic
- By nature these tend to be:

1. Open-ended
2. Feedback loops
3. No fixed path

- Most of these run in a continuous loop with tools to achieve a goal or desired outcome. 



---
# Reflection Pattern
- There are 2 main blocks in this pattern:
  - 1) Generate block
    2) Reflect block

### Workflow in Reflection patterns
- User prompt "Generate an essay on music of the 1990s"
- prompt sent to Generator (LLM)

<img width="716" height="546" alt="image" src="https://github.com/user-attachments/assets/aa6fd2b3-c794-4cc0-bbda-0ace31beb9d2" />

[source:](https://levelup.gitconnected.com/agentic-ai-patterns-to-boost-your-llm-workflow-d424d25dfdae)

---
# Components of Agentic Design Patterns
1. System Prompt Design --> Define agent behavior, rules, examples, and output formats.
2. Tool Schema Design --> Name tools, set parameters, define input/output schemas
3. Context & Memory Mgmt --> Track history, summarize context, manage tokens and limits.

---
# Memory Types for AI Agents
- AI agents can use two main memory types:
  - 1) Session memory (limited to the context window) or Short-Term memory
    2) Long-term memory (persistent storage using key-value stores, structured graphs, vector stores, or hybrid approaches).
    3) Working Memory (the reasoning scratchpad -- solves multi-step task execution, complex reasoning chains). 
    4) Episodic Memory (specific past event recall -- long project continuity)
    5) Semantic Memory knowledge layer (solves problem of factual accuracy, domain specific expertise -- grounds agents in factual rasoning.)



## Why Prompt-only context fails
1. Limited context window size
2. High prompt cost and latency
3. No recall after session ends
4. Leads to repeated user queries
5. Cannot personalize or adapt

### 1. Session Memory
- Source: Weights & Biases course on Agentic Engineering
- Session memory is what you get by default when using any LLM within its natural context window:

- **Advantages:**
   - Very easy to implement
   - Agent remembers the entire conversation history (within limits)
   - Transparent - you can see exactly what the agent knows
   - Fast access to recent information

- **Limitations:**
   - Limited by context window size
   - Increasing costs as conversation lengthens
   - Growing latency with longer conversations
   - Memory is lost when the session ends
   - No continuity between different conversations

- This is why most foundation models and services (e.g. ChatGPT, Claude, Gemini) have implemented features to provide continuity between conversations - users expect their AI assistants to remember them between sessions.

### 2. Long-Term Memory
- There are a few different types (source: Weights & Biases, see below). When developing agentic systems, architectures and patterns, we need to carefully consider which memory approach or combination of approaches best serve a particualr use case, balancing factors like speed, cost, persistence, and personalization (among others).

1. Key-Value Stores
   - best for structured, lightweight memory
   - simple format for storing and retrieving information

2. Structured Graphs
   - Best for complex and relational representations in the data.
   - Can model relationships between different pieces of information for better reasoning efforts grounded in fact. 

3. Vector Stores
   - Perhaps the most popular approach
   - Leverages semantic similarity search (e.g. cosine similarity, euclidean distance) to load and save memory.
   - Retrieves info based on similarity to current context. Not necessarily relevance or related -- depends on system design.
   - Efficient for large amounts of information (RAG driven(

4. Hybrid Approaches
   - Combines multiple storage methods
   - Gets "the best of all worlds"
   - Can use different storage types for different kinds of information

---
# Memory Management for AI Agents -- Memory as Tools in Agentic Systems

## ONLINE (During Execution)
1. Retrieval Tools -- relevant information with filters and source tracking.
2. Update tools -- write back new facts with validation.
3. Grounded generation -- use retrieved knowledge to anchor outputs


## OFFLINE (Post-Execution)
1. Summarization -- chats and sessions compressed into short memory.
2. Extraction & Deduplication -- capture facts, remove dedundant information, entity resolution (e.g. same entities that mean the same thing in context)
3. Consolidation & Clean-up -- organize memories and discard stale data


---
# References
1. [The 5 Types of AI Agent Memory Every Developer Needs to Know - Part 1](https://dev.to/sreeni5018/the-5-types-of-ai-agent-memory-every-developer-needs-to-know-part-1-52fn)
2. [NVIDIA - Autonomous AI Agents](https://www.nvidia.com/en-us/glossary/ai-agents/)
3. [NVIDIA - AI Reasoning with Agents](https://www.nvidia.com/en-us/glossary/ai-reasoning/)
4. [NVIDIA - Nemotron Models](https://build.nvidia.com/models?q=nemotron)
5. [NVIDIA - Spotlight: xpander AI Equips NVIDIA NIM Applications with Agentic Tools](https://developer.nvidia.com/blog/spotlight-xpander-ai-equips-nvidia-nim-applications-with-agentic-tools/)
