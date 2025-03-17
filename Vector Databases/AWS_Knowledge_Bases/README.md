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


## How to Create a Knowledge Base
* Navigate to AWS Bedrock.
* Go to side panel "knowledge bases".
* Click on "Create".
* Choose your knowledge base type: Vector Store, Structured Data, or Knowledge Base with Kendra GenAI Index.

![image](https://github.com/user-attachments/assets/f5939697-3700-4d5f-97cf-360c0bc00543)

* Next, name your knowledge base.
* Add any description as necessary.
* Either create an IAM role (AWS Bedrock does by default), or use existing one.
* Next, choose data source(s):
  * Amazon S3 bucket
  * Web Crawler
  * Custom
  * Confluence
  * Salesforce
  * Sharepoint
* You can also add logging abilities such as AWS Cloud Watch Logs.


## AWS Knowledge Base Parsing Strategies
1. Default Parser
2. Foundation Models as a Parser
   * This leverages Anthropics Claude models. The models will analyze your data and decide the right strategy to parse the data.
   * If you data is multimodal (e.g. PDF, tables, text, images) this is the more ideal parsing strategy.

## AWS Knowledge Base Chunking Strategies
1. Default Chunking
   * 300 token chunks is default setting. This is based on average sentence and paragraph lengths.

2. Other Chunking Strategies -- customize tokenization sizing
   * Fixed Size
   * Hierarchical
     * nested chunking (e.g. parent-child format, similar to LlamaIndex)
     * Semantic search occurs on the child chunks of each parent. However, retrieval will send the parent chunk only.
     * This approach can introduce noise into your data. 
   * Semantic
     * Based on semantic similarity embedding model(s) and specific similarity metric (e.g. cosine similarity, dot product).
     * Chunk size is based on semantic context. 
   * No chunking at all!! 1 document will == 1 chunk
  
## AWS Knowledge Base - Embeddings and Vector Databases
* This is the next step in building your knowledge base.
* You can select a foundation embedding model from AWS Bedrock such as Titan Text Embeddings or Cohere.
* The next step is to select a vector database to store your vectors. The usual options are:
  1. Quick Create -- Open Search Serverless instance, AWS Aurora PostgreSQL, AWS Neptune Graph DB (Graph RAG)
  2. Vector Database Vendor
     * Pinecone
     * Redis
     * Amazon Aurora
     * ...etc..

# Testing the Knowledge Base
* After your knowledge base is setup and configured, you should test it via the available APIs.
* As we mentioned above there are 2 APIs to test with: Retrieve, Retrieve and Generate.
* This is an example of how I tested a knowledge base I setup on AWS using the Retrieve and Generate API.
  * The first step is to select a foundation model LLM. I chose the Nova Pro model as it is multimodal and the data I was using was multimodal including PDFs with tables, images and text as well as word documents.
  * The main topic/subject of the documents is "insurance claims". Here is what the result looks like below. We can see that the specific chunks where the answer was synthesized from is cited in the response and you can drill down into each response via the metadata chunks. 

 ![image](https://github.com/user-attachments/assets/bea3d998-e148-4d89-803f-5a00a989d763)


# Updating the Knowledge Base
* You are able to update the knowledge base over time and in real-time as new information and data is available.
* The simple way to do this by "syncing" your knowledge base source, in this case the S3 bucket with your new data. 
