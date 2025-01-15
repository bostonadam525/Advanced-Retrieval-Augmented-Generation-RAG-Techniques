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


