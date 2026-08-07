# AI Agents in LangGraph

## Overview of Agents
* This is an excellent repo to refer to: [The Rise and Potential of Large Language Model Based Agents: A Survey](https://github.com/WooooDyy/LLM-Agent-Paper-List)
* This is an excellent review paper on agents: [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)


## What is LangGraph?
* LangGraph library for building stateful multi-actor apps using LLMs.
* Used to create agent and multi-agent workflows. 
* In the LLM ecosystem it is very beneficial because it offers:

1. Cycles
2. Controllability 
3. Persistence

* LangGraph also allows us to define flows that involve cyles that are essential for most agentic architectures which differentiates it from DAG-based solutions. 
  * DAG is a Directed Acyclic Graph, a type of graph whose nodes are directionally related to each other and don’t form a directional closed loop.
  * A knowledge graph or graph database is a DAG, while LangGraph is similar it is a bit different.

 ---
 ## 10 LangGraph Concepts every AI Engineer Should KNOW!
 - This image is courtesy of the AI Anytime YouTube Channel, all credit goes to him.
   - Source:https://github.com/AIAnytime/10-langchain-langgraph-concepts/blob/main/concepts.jpeg
   - Video: https://www.youtube.com/watch?v=jsT437atPvU
 - Image from above sources:

<img width="1535" height="1024" alt="image" src="https://github.com/user-attachments/assets/6321ada7-0c69-4b05-b25c-aef3f18a7770" />



 ---
## Why LangGraph?
1. **Simplifies development of mulit-agentic frameworks**
  * State Management
  * Agent Coordination

  * Example: 3 to 4 agents in a Gen AI application
      * Agent 1 —> Google search
      * Agent 2 —> Wiki search
      * Agent 3 —> Vector DB search

  * State management and coordination/communication is crucial between the agents
  * Agents may be state depenent upon each other.


2. **Things we need to define that LangGraph simplifies**
  * Workflows
  * Logic


3. **Flexibility**
  * Developers can define their OWN logic and communication protocols for agents. 
  * Agents allow more specific use cases for Generative AI. 
  * As an example:
      * Chatbots handling various types of user requests
      * Multi-agent system performing complex tasks
      * …etc....
   

4. **Scalability of Generative AI Applications**
  * Large scale multi-agent apps are possible with agentic workflows. 
      * Agents are able to handle **HIGH VOLUME** interactions between agents and complex workflows and data types.
      * Enterprise LangGraph is available for agentic workflows (scalable!)
  * However, there is a paper in 2024 that there are "scaling laws" when it comes to multi-agent frameworks.
      * [Scaling Large-Language-Model-based Multi-Agent Collaboration](https://arxiv.org/html/2406.07155v1)
      * The authors found that:
          1. *A small-world collaboration phenomenon exists, where topologies resembling small-world properties achieved superior performance.*
          2. *Additionally, a collaborative scaling law exists, indicating that normalized solution quality follows a logistic growth pattern as scaling agents, with collaborative emergence occurring much earlier than previously observed instances of neural emergence.*



5. **Fault Tolerance**
   * Handles errors with more ease.
   * Fault tolerance —> allows application to keep running
      * Reliability is the main key!!
   * Some of the main aspect of Fault Tolerance: [Mastering Agents: Why Most AI Agents Fail & How to Fix Them](https://www.galileo.ai/blog/why-most-ai-agents-fail-and-how-to-fix-them#:~:text=AI%20agents%20need%20to%20be,system%20crashes%20or%20degraded%20performance.)
    1. Redundancy
       * Deploy multiple instances of AI agents running in parallel.
       * If one instance fails, the other instances can continue processing requests without interruption.
       * This approach ensures high availability and minimizes downtime.

    2. Automated Recovery
       * Incorporate intelligent retry mechanisms that automatically attempt to recover from transient errors.
       * This includes exponential backoff strategies, where the retry interval increases progressively after each failed attempt, reducing the risk of overwhelming the system. Develop self-healing mechanisms that automatically restart or replace failed agent instances.

   3. Stateful Recovery
      * Ensure that AI agents can recover their state after a failure.
      * This involves using persistent storage to save the agent's state and context, allowing it to resume operations from the last known good state after a restart.



# "Agents are DEPENDENT variables"
* Agents depend on each other but also other factors in the "LLM pipeline".
* This is an excellent figure from the company Galileo that depicts these issues:

![image](https://github.com/user-attachments/assets/16ba4b07-ca77-4a7c-8a56-ebb4086480a6)


# Metrics for AI Agents
* See this [Galileo Blog Post](https://www.galileo.ai/blog/metrics-for-evaluating-llm-chatbots-part-1)

---
# AI Agents vs. Agentic AI — What is the Difference?


## AI Agents
- Refers to software programs designed to perform specific tasks without human intervention and/or with a degree of autonomy. 
- Advantages of AI Agents
    - 1) Reduces costs
    - 2) Reduces complex workflows
    - 3) Reduces need for complex expensive infrastructure 
    - 4) Improves system and task efficiency 



## Agentic AI Systems

- Frameworks where multiple AI agents can collaborate and make decisions independently to achieve a larger goal. 
- This can be conditional, this can be deterministic. 


## Examples

Input —> LLM  —-> output



Task: 
- please provide me with recent news for today, August 7, 2026. 
- What is the current temperature in Boston, MA today? 

LLMs are static trained models that can’t infer on unseen or current data. Which is why agents exist to augment and enhance the model with EXTERNAL sources. 
- If LLM can’t answer question —> can use agent-tool call to external resource to get the information to answer the question. 
- Some degree of autonomy for the LLM to know when and how to do this to call external resources: API, database, etc…


## How do Agentic AI systems Work? 
- Broader framework as this uses MULTIPLE AI AGENTS that can communicate to each other to solve problems and achieve goals via orchestration and reasoning. 

### Use Case - YOUTUBE Blog Generator
- Let’s say I have a collection of YOUTUBE videos and I want to convert them to blogs. 
- How would we make this into an agentic AI system? 

Architecture of what a person would do below. Now just imagine if we could automate this with multiple agents in an Agentic system that can do this in multiple sub tasks:

Start —> Videos —> script —> content —> title, description, code part, conclusion 

#### Workflow

1. Convert YOUTUBE videos (AI agent) —> Transcript [code] —> LangGraph via YOUTUBE APIs
2. Transcript —> subtasks (AI agent)
    1. Title
    2. Description
    3. Code part 

#### LangGraph Workflow (DAG - directed acyclic graph)

Input (video URL) —> YT —> transcript —> Blog generating agent —> End 
Agent 1 —-> Agent 2 —> Agent 3 —> etc…



#### Simple Workflow Example — Automate with LangGraph

Start —> Play —> Tennis or Basketball —> End 

Key points
1. Each action is a NODE (Python functions) —> Task
2. EDGEs connect NODEs (Conditional logic)
3. State schema
4. State graph —> entire structure of entire graph


<img width="2060" height="4166" alt="image" src="https://github.com/user-attachments/assets/bbd1a47f-330a-498f-a527-3e48db6c65a6" />
