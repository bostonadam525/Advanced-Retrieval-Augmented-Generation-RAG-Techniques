# Vector Databases
* This folder contains all of my research, experiments and projects done with Vector Databases.


## Overview of Vector DBs
* Vector DBs store vectorized input in the form of embeddings.
* Why do Vector DBs index data?
   * One of the most important concepts to understand is that you should index to be stored in the Vector database prior to ingestion of the data.
   * An index provides the "map" or "guide" pointing to the vector embeddings stored in the database.
       * The "map" is formulated based on the specific search algorithm (e.g. ANN, HNSW, IVF) and the similarity metric being used to locate the vector(s).
   * Indexes allow efficient storage, search and retrieval.
   * 3 of the most common indexing algorithms are seen below (left to right):
       * 1. LSH (locality sensitive hashing)
       * 2. HNSW
       * 3. ANNOY
        
         ![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/2b00f1f9-4834-4f57-a8fa-af5a0068d852)


## Vector DB Vendors 
* Below are the most popular vector database vendors with their associated search algorithm.

  ![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/6f74cc48-137d-42d0-9f0a-dd4e524ca861)


![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/a631a925-8cb4-45fa-9db6-53b7995ce4e6)


![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/d0a75e19-bdb2-4ce3-a247-ad1e29af7759)


## Vector Search Algorithms - KNN vs. ANN - What are the differences?
* Typical Vector DBs use ANN instead of KNN due to scalability. ANN allows you to search more vectors in less time.

![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/cf2c1691-ce2f-469b-b2c8-86f27dc8a0bb)


## Most Common Search Mechanisms in Vector DBs
1. Keyword Search
  * BM25 algorithm (most common)
  * DOES NOT require a vector DB, however, can be included.
2. Semantic Search
  * Nearest Neighbors search
  * Vector search
  * Usually requires a vector DB
3. Hybrid Search
  * Uses both keyword and semantic.
  * Also can utilize cross-encoder for re-ranking search results.
  * Usually requires 2 databases: document database (keywords, bag-of-words) and vector database (embeddings)

![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/de0536c8-500a-4ba9-9bda-49bbe8fda2b1)


* 3 search algorithms

  ![image](https://github.com/bostonadam525/Advanced-Retrieval-Augmented-Generation-RAG-Techniques/assets/45008475/d2e78f95-cdf7-42c3-ad87-86fc3d31fc2f)




