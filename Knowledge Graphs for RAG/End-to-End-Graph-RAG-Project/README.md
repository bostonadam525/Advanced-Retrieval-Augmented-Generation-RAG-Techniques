# End to End Graph RAG Project
* This is an end to end demo project of how to perform RAG using a knowledge graph in NEO4J.
* This is the general concept of Graph RAG (source: Udemy)

![image](https://github.com/user-attachments/assets/55873fa5-b1e1-4d6d-ac5a-a60c2f3450db)


# Application Retriever Flow Concept
1. User enters query
2. LLM extracts entities 
3. Identify entities using knowledge graph
4. Relevant nodes with neighbors
5. Flatten information ("information compression")
6. Results that are passed to LLM for generative AI answer



# Building a RAG app with knowledge graph
* This is the process we will use:

1. Obtain Unstructured Data
2. Extract information/entities
3. Data integration
4. Generate a knowledge graph with entities-relationships in NEO4J
5. Ceate a Vector Storage retrieval system
6. Vector store
  * used for keyword search
  * used for vector search 

## Graph Retrieval Mechanism
* Integrate the ability for the LLM to access the knowledge graph and the vector store
LLM synthesizes information from knowledge graph & vector store.
* This project was inspired by a Udemy Course project
* Goal is to enhance the accuracy of RAG applications using knowledge graphs. 
* We will do this:
  * Get text/documents from Wikipedia about the Roman Empire.
  * Data Extraction
  * Data integration
  * Generate knowledge graph in NEO4J
  * Generate Vector store/embeddings
 


# Create virtual environment
* code to do this: `python -m venv <name of your venv>`
* activate venv: `source <name of venv>/bin/activate`


# Dependencies -- see `kg_requirements.txt` file
* neo4j
* python-dotenv
* langchain
* langchain-community
* langchain-core
* langchain-openai
* langchain-experimental
* tiktoken
* wikipedia

## Install dependencies
* run this code within the virtual environment: `pip install -r requirements.txt`



# To visualize Graph in NEO4J
* Once you use the LLMGraphTransformer to extract all entities and nodes from the text, you can visualize the entire knowledge graph in NEO4J using this cypher query: `MATCH (n)-[r]->(m) RETURN n, r, m;`
* Then if you zoom into the graph in the NEO4J GUI you will see something like this:

![image](https://github.com/user-attachments/assets/d0b458aa-3e37-4a64-93eb-f4e9c833db29)





