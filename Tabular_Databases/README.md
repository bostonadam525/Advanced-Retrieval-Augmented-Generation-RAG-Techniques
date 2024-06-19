# Tabular Databases with and without RAG
- In this repository we will go over best practices for how to understand, build and implement LLM solutions that work with tabular databases.

## General Overview

### Question: What is the difference between a Q & A pipeline vs. RAG pipeline?
source: https://www.youtube.com/watch?v=ZtltjSjFPDg&t=25s

### Answer: 
Q & A pipeline vs. RAG pipeline - fundamental difference between two?

1. **RAG pipeline**
* Goal of RAG pipeline --> Semantic vector search in vector database.
- First difference? There is an embedding model in the pipeline.
- User query is vectorized
- Vectorized query is sent to Vector DB 
- Retrieve vectors -->
- send to LLM -->
- answer sent back to user

![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/2585ab55-4823-4f70-b77d-52dba9ae0b2c)


=========================================================================
2. **Q & A pipeline**
* Goal of Q & A pipeline --> Exact query search in relational database.
    * Note: This is different than a keyword search such as BM25 or sparse vector search.
- First difference? You have an LLM agent in your pipeline.
- A user query is converted to a query language (SQL, cypher, etc..)
- SQL (or other) query is sent to tabular data (e.g. SQL database)
- Structured query extracts data from the tabular data/relational database
- passes result to LLM 
- returns answer to user

* **Advantages of Q & A agent pipeline:**
- Answers are usually more precise and exact.
- Queries/questions can be more precise as well.
- Answers are NOT abstractive as they may be with a RAG pipeline since we are not using vector search.

![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/a9fda25b-abae-4e47-8fad-8bd2549ea91a)





- Using LLM agents to interact with SQL databases

![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/bf16f570-2316-40f3-8a16-60c3181b0765)

