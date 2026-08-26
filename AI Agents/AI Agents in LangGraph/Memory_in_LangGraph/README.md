# Memory in LangGraph
- See LangGraph docs: https://docs.langchain.com/oss/python/concepts/memory

---
# Three Types of Working & Short-Term Memory for AI Agents
- This acts as a temporary scratchpad for active tasks and immediate conversation context.

## 1. Context Window Buffer
- The active memory space where the model processes current text; it vanishes completely once a chat session is closed.

## 2. Sliding Window Memory
- A technique that retains only the last few turns of a conversation to keep processing costs low and prevent the system from getting overwhelmed.

## 3. Summarized Memory
- A method where an AI agent actively condenses older parts of a conversation into short summaries to preserve context without wasting token space.


---
# Three Types of Long-Term Memory for AI Agents
- This permanently saves information outside the model's core workspace so it can be recalled days, weeks, or months later.

## 1. Semantic Memory
- **What it is:** storing FACTS
- **Example:** "things you learn in school"
- **Agentic example:** Facts about a USER

## 2. Episodic Memory
- **What it is:** Experiences
- **Example:** Things that I did in the past in certain situations. These are not facts but the memory of the situation itself.
- **Agentic example:** Past agent actions

## 3. Procedural Memory
- **What it is:** Instructions
- **Example:** instincts or motor skills
- **Agentic example:** Agent SYSTEM PROMPT

---
# How can Agents interact with Memories?
- Source: "Long-Term Agentic Memory with LangGraph" course from deeplearning.ai

<img width="763" height="429" alt="image" src="https://github.com/user-attachments/assets/3e9e1f60-6148-478e-80fe-7d99e31b8d41" />

- There are 2 general paradigms for MEMORY INTERACTION:

1. **"In the hot path"**
   - This is all at once interaction or "all in one go".
   - **Pros:** Single agent does everything (update memories + respond to users)
   - **Cons:** too much work for 1 agent to do by itself, adds latency to response

2. **"In the background"**
   - In a separate process
   - **Pros:** Two agents to do work: 1 to update memory, 1 to respond
   - **Cons:** Latency increases to respond

---
# Example: Email Agent
- Here we will work with the 3 types of memory
- They will be implemented in different parts of the DAG. 
1. Semantic Memory -- Memory Tool for agent to use
2. Episodic -- few shot examples added to the prompt
3. Procedural -- Calendar + Writing tool: SYSTEM PROMPTS

- The example below is from the deeplearning.ai course "Long-Term Agentic Memory with LangGraph"

<img width="763" height="429" alt="image" src="https://github.com/user-attachments/assets/b9bfdfa9-a5a9-4c26-8b64-c5d666cdcc70" />


