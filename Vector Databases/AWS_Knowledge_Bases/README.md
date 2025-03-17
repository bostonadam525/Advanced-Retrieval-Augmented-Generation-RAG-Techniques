# AWS Knowledge Bases for RAG


# Normal RAG Pipeline
* The "normal" or typical RAG pipeline involves a data ingestion phase as seen at the bottom of this image.

![image](https://github.com/user-attachments/assets/2123c128-90f8-419f-bf95-e1667c2ecdd2)



# AWS Knowledge Bases
* This gives foundation models and agents contextual information from your own private data sources to utilize for RAG-LLM applications.

## What is a Knowledge Base?
* Full managed support for end-to-end RAG workflows
* Allows you to securely connect foundation models and agents to data sources.
* Ability to easily retrieve relevant data and augment prompts.
* Provides source attribution.

## Data Ingestion in Knowledge Bases
* The main advantage is that AWS Knowledge Bases "take over" the data ingestion pipeline as seen in the "Normal RAG Pipeline" above.

![image](https://github.com/user-attachments/assets/f6a799d8-ab8c-40a4-97e4-7e6eea09cdce)


## Retrieve API
* You don't have to create your own embeddings, the Retrieve API does the hard work for you to interact with the knowledge bases for RAG.

 ![image](https://github.com/user-attachments/assets/74b2621d-bcdf-4b26-ae76-35852a997399)


## Retrieve and Generate API
* This API does both retrieval of semantically similar chunks and sends them to the LLM for generation by the LLM.

![image](https://github.com/user-attachments/assets/6f26b1d9-8eb2-4023-b5ce-b7fc5d6e34bd)

