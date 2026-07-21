# MCP - Model Context Protocol
- Everything and anything related to MCPs.

---
# What is MCP?
- MCP is an open protocol that standardizes how your LLM applications connect to and work with your tools and data sources.
- The thing is that everything you can do with MCP can actually be done without MCP. However, MCP makes the process more efficient for LLMs and production systems. 

1. Rest APIs — standardize how web apps interact with backend
2. LSP — standardize how IDEs interact with language-specific tools. (Language server protocol - developed by MSFT)
3. MCP — standardizes how AI apps interact with external systems 

## What is development like without MCP?
- The simple answer: FRAGMENTED DEVELOPMENT PIPELINES!
- You end up with multiple parallel pipelines that do not work together/in tandem, do not communicate, are less efficient, and context is lost. Context is IMPORTANT for LLMs to retrieve not only the most similar, most relevant, and related information, but for it to synthesize this into logical outputs. 

<img width="1400" height="510" alt="image" src="https://github.com/user-attachments/assets/f2a544f7-1bc5-40bc-ab79-9d3fc927b493" />

- [Source](https://pub.towardsai.net/mcp-an-architectural-inflection-point-6db57d6957d3)

---
## What about the Difference Between MCP and Semantic Routing?

The difference between **Model Context Protocol (MCP)** and **semantic routing** is that MCP is a universal communication standard for connecting AI models to external tools and data sources, whereas semantic routing is a decision-making layer that uses vector similarity to direct a user query to the best tool or model.

---

### Model Context Protocol (MCP)
* **What it is:** An open standard created by Anthropic that standardizes how AI clients and agents discover and talk to external data sources, files, and tools.
* **Core function:** Acts like a "USB-C port for AI"—every MCP server exposes tools and resources in a uniform format so an AI can read schemas and execute commands without custom glue code per service.
* **Scope:** Focuses on transport, structure, and connection interoperability between a model and backend systems.

### Semantic Routing
* **What it is:** A fast classification technique using vector embeddings and cosine similarity to map user inputs to specific intents, destination models, or functions.
* **Core function:** Intercepts a prompt and matches its meaning against a pre-defined library of routes or tool descriptions to decide which tool or LLM should handle it *before* wasting tokens on a full LLM generation.
* **Scope:** Focuses strictly on optimization, intent classification, and fast routing logic.

---

### Key Comparisons

| Feature | Model Context Protocol (MCP) | Semantic Routing |
| :--- | :--- | :--- |
| **Primary Role** | Connection and data transport standard | Intent classification and query direction |
| **Mechanism** | Client-server JSON-RPC message passing | Vector embeddings and similarity matching |
| **Main Benefit** | Eliminates custom API integration chaos | Reduces latency and token costs by filtering tools/models early |

---
# MCP vs. RAG vs. GraphRAG: Architecture & Integration

The primary difference is that **MCP is a connection protocol (a highway)**, whereas **RAG and GraphRAG are memory retrieval systems (the destinations)**. 

MCP does not compete with or replace RAG. Instead, an AI agent uses **MCP as the infrastructure** to query and fetch data from a **RAG or GraphRAG database**.

---

## What about MCP vs. RAG vs. GraphRAG?

### Model Context Protocol (MCP)
* **What it is:** An open, standardized communication protocol created by Anthropic.
* **Role:** Acts like a "USB-C port" or universal API bridge for AI agents. 
* **Function:** Exposes development tools, local files, and enterprise databases to an LLM using a single, unified structure.

### Retrieval-Augmented Generation (RAG)
* **What it is:** A traditional data architecture for grounding LLMs in external text.
* **Role:** Searches raw documents (PDFs, wikis, logs) using semantic vector similarity.
* **Function:** Chunks text, finds relevant passages matching the user's prompt, and injects them into the model's context window.

### GraphRAG
* **What it is:** An advanced knowledge-graph-based retrieval system popularized by Microsoft.
* **Role:** Structures unstructured text into interconnected entities (people, places, concepts) and relationships.
* **Function:** Summarizes high-level themes, tracks complex hierarchies, and answers holistic, cross-document queries that standard RAG misses.

---

## How They Work Together with Agents

In a production-ready AI agent architecture, these technologies are stacked into a single, cohesive pipeline:

```
[ User Query ] 
      │
      ▼
[ AI Agent ] ──( MCP Request )──> [ MCP Server ] 
                                       │
                                 (Runs Search)
                                       │
                                       ▼
                       [ RAG / GraphRAG Database ]
                                       │
                                 (Returns Data)
                                       │
      ▼                                ▼
[ Final Answer ] <──( MCP Response )───┘
```
---
### The Step-by-Step Workflow

1. **The Request:** A user asks an AI agent a complex question (e.g., *"Summarize our entire project history with Client X"*).
2. **The Protocol Action:** The Agent determines it needs corporate data. Instead of using a custom API, it sends a standardized JSON-RPC request over an **MCP connection**.
3. **The Engine Execution:** The **MCP Server** receives the request and triggers a search. 
   * It uses **Standard RAG** to find specific text clauses.
   * It uses **GraphRAG** to map how Client X connects to various internal engineering teams and past projects.
4. **The Response:** The retrieved data is packaged by the MCP server, sent back across the standard protocol, and fed into the LLM to generate a factual, grounded answer.

---

## Key Feature Comparison

| Feature | Model Context Protocol (MCP) | Standard RAG | GraphRAG |
| :--- | :--- | :--- | :--- |
| **Primary Classification** | Communication & Tool Protocol | Document Retrieval Architecture | Relationship Retrieval Architecture |
| **Data Format** | JSON-RPC tool & resource schemas | Vectorized text chunks | Entity nodes, attributes, and edges |
| **What it Solves** | Integration chaos and custom API mess | Out-of-date model training data | Fragmented data, bias, and abstract queries |
| **Best Used For** | Connecting agents to tools securely | Finding isolated, specific text facts | Mapping broad themes and connections |

---
# MCP - Standardized AI Development
- This is from the DeepLearning.AI course by Anthropic:

<img width="1232" height="728" alt="image" src="https://github.com/user-attachments/assets/90a4b632-1708-4807-958b-711eaf0adb4b" />

- **What makes MCP logical and efficient is that it is modular and reusable across many developmental frameworks.**

---
# MCP Architectures - How Does it Work?
- MCP Client and MCP Server communicate
- The main components are:
  - Tools
  - Resources
  - Prompt Templates

- Example from Anthropic and deeplearning.ai:

<img width="1000" height="529" alt="image" src="https://github.com/user-attachments/assets/5bf518e0-6640-493f-8cc3-3c170d4b315d" />


---
# References
1. [deeplearning.ai - MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)

# Bibliography & Reference Resources

### 1. Model Context Protocol (MCP)

* **Anthropic. (2025).** *Model Context Protocol Specification*. Anthropic PBC. 
  Available at: [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2025-11-25).
* **Anthropic. (2026).** *Model Context Protocol: Standardizing the Integration Between LLMs and Tools*. GitHub Repository. 
  Available at: [GitHub - Model Context Protocol](https://github.com/modelcontextprotocol).
* **Model Context Protocol Steering Group. (2026).** *Reference Implementations and Open-Source MCP Servers*. GitHub Registry. 
  Available at: [GitHub - Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers).

### 2. Retrieval-Augmented Generation (RAG)

* **Lewis, P., Perez, E., Piktus, A., Petroni, F., Lewis, V., Riedel, S., ... & Kiela, D. (2020).** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems (NeurIPS), 33, 9459-9474. 
  Pre-print available at: [arXiv:2005.11401](https://arxiv.org/abs/2005.11401).
* **Meta AI Research. (2020).** *Retrieval-Augmented Generation (RAG) System Architecture & Publication Portal*. Meta AI. 
  Available at: [Meta AI Research Publications](https://ai.meta.com/research/publications/retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks/).

### 3. Knowledge Graph RAG (GraphRAG)

* **Edge, D., Trinh, H., Cheng, B., Bradley, J., Chao, A., Mody, N., ... & Larson, J. (2024).** *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. Microsoft Research.
  Project Documentation available at: [Microsoft Research - Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/).
* **Microsoft Open Source. (2026).** *GraphRAG: A Modular Graph-Based Retrieval-Augmented Generation Suite*. GitHub Software Repository. 
  Available at: [GitHub - Microsoft GraphRAG](https://github.com/microsoft/graphrag).
* **Microsoft. (2026).** *GraphRAG Indexing Pipeline and Search Query Architecture User Guide*. Microsoft GitHub Pages. 
  Available at: [Microsoft GraphRAG Documentation](https://microsoft.github.io/graphrag/).

### 4. System Integration (MCP + GraphRAG Ecosystem)

* **Neo4j Developer Network. (2025).** *Implementing Neo4j GraphRAG Retrievers as a Model Context Protocol Server*. Neo4j Technical Blog. 
  Available at: [Neo4j - GraphRAG Retrievers as MCP Server](https://neo4j.com/blog/developer/neo4j-graphrag-retrievers-as-mcp-server/).
