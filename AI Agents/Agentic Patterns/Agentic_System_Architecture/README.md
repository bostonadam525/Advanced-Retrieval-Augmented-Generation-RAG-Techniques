# Agentic System Architectures

---
# What are AI Agents?
- Systems with a specific goal that can do the following:
1. **Perceive**: Recognize user's speech, image or text input.
2. **Decide**: Evaluate options to solve the users input based on user preferences.
3. **Act:** Generate a response or take a specific action on a disease, diagnosis, or financial plan.
4. **Automation:** automate repetitive tasks in decision making and problem solving.
5. **Multi-agent systems**: multiple agents working together in orchestration. 

---
## Autonomous Agents
- What makes them unique: **Can be deployed on a SERVER or EMBEDDED in a device.**
- Agents DO NOT need to be deployed on their own. They can work together.

## Predictive vs. Generative vs. Agentic AI
- Predictive AI system --> analyze, forecast, estimate --> not based on REAL-TIME reasoning
- Generative AI system --> ingest, synthesize, generate new data
- Agentic AI system
  - Very different capabilities and underlying architecture.
  - This is a "SYSTEM OF SYSTEMS".
  - An agents relationship to its environment is important.
 
## Types of Autonomous AI Agents
1. Reflex agent
   - sense something and look up action
   - decision making is immediate without memory
   - simple tasks and are part of a larger solution

2. Model based reflex agent
   - makes decisions based on current perception, internal model(s), and predefined rules.
   - often have multiple models

3. Goal based agent
   - Makes decisions based on planned sequence of actions necessary to achieve its goal.
  
4. Utility based agent
   - Take actions to maximize the most desirable outcome.
   - Example: measure of utility can be a measure of customer satsifaction

---
# Key Components of AI Agents
- As we know from above AI Agents at a high level can/should:
  - Perceive
  - Decide
  - Act
- Professor Andrew Ng says the key components of agents are:

1. **Reflection**
   - AI agent can look back at its own thoughts, actions, or outputs --> evaluate them --> decide how to improve, revise, or proceed differently.
     
2. **Tool Use**
   - Search web
   - Scape web
   - API calls
   - Image/Video analysis
   - Email, Calendars
   - Monitoring/Logging
   - Code execution
   - Embeddings
   - Retrieval/Memory
   - Vector DB integration
   - IoT integrations
   - File manager
   - Text to speech/ASR
   - GIS/Geospatial
   - Authentication & Authorization
3. **Planning**
   - **Example: Financial planning**
     - Planning chain might look like this:
       - Real-time updates that ensure analysis reflects current financial trends
       - Interpreting competitive positioning and qualitative risks
       - User-Friendly Reports: Structures data to be intuitive and immediately actionable
4. **Multi-agent collaboration**
   - Role based approach (multiple roles)
   - Coordination strategy
     - Centralized (planner/manager tells each agent what to do)
     - Decentralized (agents made decisions independently and negotiate
     - Hybrid: combines BOTH


---
# AI Agents Frameworks
- These are the most popular frameworks:
1. LangGraph
2. crewai
3. Swarm (OpenAI Agents SDK)
4. PydanticAI

---
## Simple Example
- Lets say you are building a hospital AI agent
- The directed acyclic graph would look like this in LangGraph:

```
start --> front_desk_agent --> physician_agent --> radiologist_agent


```
# Multi-Agent Agentic RAG Example
- input query -->
- Agent 1 (Database search X, Database search Y)
- Agent 2 (Vector DB search A, Vector DB search B)
- Agent 3 (Web Search tool)
- Agent 4 (Tools: Email, social media, user profile, etc.)
- LLM synthesis
- Generated output

---
# Temporal Knowledge Graphs with AI Agents
- Zep is a company that makes this software [Graphiti](https://github.com/getzep/graphiti)
- This allows incorporation of time-series with agents
- This is how it works:

1. Raw data ingestion
2. Entity/Relation extraction and resolution
   - build nodes and edges of graphs
3. Community detection algorithm
   - Use community detection algorithms to cluster the nodes and edges
4. Search Layer
   - Hybrid (semantic + keyword)

5. Reranker
   - sort results

6. Context construction
   - formats information for LLM
  
7. Data for Evaluation
---
# Postman - API Agents 
- How do you know the APIs you want to integrate into your application agent-tool calls will work? Postman lets you test this.
- https://www.postman.com/ai/ai-ready-apis/

---
# Resources
- [7 Practical Design Patterns for Agentic Systems](https://www.mongodb.com/resources/basics/artificial-intelligence/agentic-systems)
- [GCP - Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- [The Roadmap to Mastering Agentic AI Design Patterns](https://machinelearningmastery.com/the-roadmap-to-mastering-agentic-ai-design-patterns/)
