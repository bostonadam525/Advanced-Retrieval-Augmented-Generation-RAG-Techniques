# Tools and ReAct in LangGraph
- This repo contains examples of using the following:


1. Tool calling
2. ReAct patterns
3. Memory in LangGraph
4. Streaming
5. ...tbd

--- 
# Tools


---
# ReAct Patterns


---
# Memory

---
# Streaming Techniques
- Methods: `.stream()` and `astream()`
    - These methods are sync and async methods for streaming back results.

- Additional parameters in streaming modes for graph state:
    - **values:** streams full state of graph after each node is called.
    - **updates:** streams updates to the state of the graph after each node is called.

- See docs: https://docs.langchain.com/oss/python/langgraph/streaming
