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
