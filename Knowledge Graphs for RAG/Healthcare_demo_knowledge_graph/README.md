# healthcare demo knowledge graph RAG
* This is a demo example of how to create a knowledge graph with some fake healthcare data.
* In this example we create a Knowledge graph using NEO4J cypher from a raw CSV file.
* We can then visualize the graph nodes-entities-relationships in NEO4J as well as query the graph using LangChain.
* This example will demonstrate 2 components of a Graph RAG pipeline:
  * 1. Knowledge Graph
       * The general architecture is this:
       * `unstructured data —> Extraction —> Data Integration—> Generate knowledge graph —> query graph (using cypher or cypher with langchain wrapper)`
       * This is just 1 component of “Graph-RAG” which ulitmately allows a RAG-LLM system to utilize a KG and Vector DB. However, it is important to understand this piece of the pipeling by itself. 
  * 2. Vector DB
      * This is the 2nd most important component of Graph RAG.
      * The Graph creates the relationships between the columns.
      * The Vector DB will allow an LLM to utilize vector embeddings and a knowledge graph to perform precision queries and information retrieval to augment an LLMs knowledge and ultimately generate a more precise response to a user query. 


# Visualization of healthcare demo knowledge graph
* Below is the entire constructed graph. 

![image](https://github.com/user-attachments/assets/c7b86a26-6886-4d4f-8eb8-57f6cbb8c5f2)




* Below is example of drilling into specific entities and nodes. Here we can see the relationships between each provider and their practice location.

![image](https://github.com/user-attachments/assets/335eacc3-c875-4011-af6a-0e972f44caaa)


* Another example below we can see the patients that 1 provider treats and drill into each fake patient's profile.
![image](https://github.com/user-attachments/assets/0934f1bb-2d95-4d68-ab41-eb390d994baf)

