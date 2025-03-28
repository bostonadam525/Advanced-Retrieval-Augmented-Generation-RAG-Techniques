# Fine Tuning Embeddings for RAG - Retrieval Augmented Generation


# Why would you do this?
* The most common use case for this is DOMAIN adaptation.
* As we know pre-trained embedding models are high dimensional and trained on various datasets.
* The high dimensionality often leads to the issue of "jack of all trades, master of none". What this means is that the embedding model can generalize over *most* queries in semantic search and similarity, but when it comes to specific domains with very specific language, acronymns, abbreviations, this is where embedding models often struggle.
* This is where fine-tuning embedding models can improve your search and retrieval results significantly, and especially in RAG applications.


# How does this work? 
* Generally speaking, the process goes like this:
1. Generate "question-retrieved context" positive pairs.
   * Usually this is done by the process of mining "hard negatives" which are pairs that are NOT alike. If your domain is highly specific this is often the process you need to use. 
   * However, there are numerous datasets available with contextual pairs depending upon your domain.

2. SentenceTransformers Loss function
   * This is used during the training process.
  
3. Pick an embedding model to fine-tune
   * This can vary based on your data dimensions, context, and domain (among other things). 


# What is the result of this?
* The usual result is an improvement in the hit rate (and other metrics) when it comes to similarity retrieval in RAG. 
