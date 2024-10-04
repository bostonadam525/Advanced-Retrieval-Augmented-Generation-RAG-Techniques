# ReAct Agents
* A repo devoted to ReAct Agents, experiments and use cases.

## What is ReAct? 
* Prompt patterns like `Chain-of-thought` enables LLMs to reason better.
* Tools and techniques such as `SayCan` and `WebGPT` enable LLMs to take better actions using tools.
* ReAct combines BOTH of these elements to empower LLMs to reason and take action!
  * Original paper: https://arxiv.org/abs/2210.03629
 
![image](https://github.com/user-attachments/assets/1fb631f7-7f7f-4e05-8557-b92ee2a2d5c8)

* ReAct stands for "Reasoning and Acting"
* ReAct is a pattern or agent.


## ReAct AI Agents Workflow
* Consists of LLM and Tools.
* The ReAct methodology is what is used to run the agent:
  * 1) If the agent says to take an action (e.g. use tool), relevant tools are run and results are returned to the agent.
  * 2) If the agent DID NOT ask to run tools, the response output is sent back to the user.
      
  

  ![image](https://github.com/user-attachments/assets/514a23ff-d852-4451-a543-8ede6ad6e45d)
   
Example: 
* Agent does NOT have enough information to answer user query.
  * Agent uses tool to search Wikipedia.
  * Wikipedia tool returns answer to agent.
  * Answer sent to LLM for "reasoning".
  * RESPONSE given to user. 


# Using LangGraph
* Most real-world complex agentic architectures use workflows involving several iterative steps and loops. 
* LangGraph allows you to easily model and use a directed graph with edges.

![image](https://github.com/user-attachments/assets/ea82e9a6-798d-4289-ba2b-dede32232036)


* Built on top of LangChain
* Allows creation of cyclical graphs essential for AI agents powered by LLMs
* Interface inspired by the NetworkX Library
* Enables coordination and checkpoints of multiple chains or actors through cyclical computational steps.

## Agentic Workflows with LangGraph
* LangGraph treats Agentic workflows as a cyclical Graph structure
* Main features:
    * Nodes —> functions or LangChain runnable objects such as tools.
    * Edges —> specify directional paths between nodes.
    * Stateful Graphs —> manage and update state objects while processing data through nodes.
* LangGraph leverages these features to create cyclical LLM call executions with state persistence which is often required for AI agents

## Multi-agent workflows with LangGraph
* Multi-agent workflows involve multiple independent agents powered by LLMs connected in a specific way. 
* Each agent can have:
    * Prompt
    * LLM
    * Tools 
    * Other custom code
* All of these components allow the agents to collaborate with other agents as needed. 
* LangGraph makes each agent a NODE in a graph.
    * Control flow is managed by edges
    * Edges communicate by adding to graph’s state

## How do you choose the BEST LLM to use with your Agents?
* Go to the [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)

