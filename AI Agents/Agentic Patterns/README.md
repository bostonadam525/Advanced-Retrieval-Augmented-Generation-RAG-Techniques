# Agentic Patterns
- This folder is devoted to agentic design patterns, architectures, implementations.
- I will use multiple resources for this, but the main core resource is this excellent course from neural-maze on agentic design patterns: https://github.com/neural-maze/agentic-patterns-course

---
# Anthropic 2024 Paper
- In their [2024 paper, Anthropic defined Agents as 2 things](https://www.anthropic.com/engineering/building-effective-agents): 

1. Workflows -->  are systems where LLMs and tools are orchestrated through predefined code paths.
2. Agents --> are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

<img width="2856" height="2027" alt="image" src="https://github.com/user-attachments/assets/f5a89cd3-5cd1-4d4f-b4c5-8bb9ebf5bf4f" />

- source: https://huggingface.co/blog/VirtualOasis/agents-vs-workflows-en

## Agentic Design Patterns from Anthropic 


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

