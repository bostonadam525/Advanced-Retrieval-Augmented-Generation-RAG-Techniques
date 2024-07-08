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



