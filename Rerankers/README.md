# Rerankers for RAG
* This repo is devoted to all things related to rerankers used in RAG pipelines in Generative AI.


# What is a "Reranker"?
* Also known as a cross-encoder, a reranker model is a type of model that, given a query and document pair, will output a similarity score.
* We are able to then use this score to reorder the retrieved documents by relevance to a user query. 
* Example of a 2 stage retrieval system with a reranker model [source](https://www.pinecone.io/learn/series/rag/rerankers/)

![image](https://github.com/user-attachments/assets/c05cb0f0-6690-44c4-9bec-ccbba10d5f98)


# Classes of Rerankers
* These are the most common reranker models used in Generative AI today as outlined by [Galileo](https://www.galileo.ai/blog/mastering-rag-how-to-select-a-reranking-model)

![image](https://github.com/user-attachments/assets/45197cb8-6967-4ebd-b3e1-7764ca0c0578)



# Bi-encoders vs. Cross encoders
* While "retrievers" are FAST they are not precise nor the most accurate.
* The truth is that "rerankers" are MORE accurate than most embedding models even though they are slower.
* Embedding models used in most semantic search and NLP applications are **bi-encoders**.
  * Bi-encoders tend to have inferior accuracy to cross-encoders because bi-encoders must compress all of the possible semantic meanings of a document into a single vector space — which results in information loss.
  * Additionally, bi-encoders have no context on a given query because we don't know the query until we receive it (we create embeddings before user query time). Think of 2 people each on a different water slide and they meet at the bottom runout pool. [source]()![image](https://github.com/user-attachments/assets/7e19a2fc-2790-4b44-912c-71cf2a2aecef)

 
![image](https://github.com/user-attachments/assets/856c8305-1565-4f95-9faa-a885d7a870b1)

# Why do we care about Rerankers (cross encoders)?
* A reranker (cross encoder) can receive raw information directly into a large transformer computation, meaning there is **less information loss**.
* A reranker is often run at user query time, which gives the added benefit of analyzing a document's meaning specific to a user query — rather than trying to produce a generic, averaged meaning as a bi-encoder would. 
* Thus, rerankers avoid the information loss of bi-encoders — but they come with a different penalty — time -- they are really slow [source](https://www.pinecone.io/learn/series/rag/rerankers/)

![image](https://github.com/user-attachments/assets/7e1b0211-1891-457e-87fb-6dd3b39949dc)



# Reranking Techniques in Search and Machine Learning 
* Reranking is not a new concept. It has been used for a long time in search and machine learning applications.
* Below is a list of reranking methods that can be/are commmonly used in RAG pipelines but also in other search and ML applications:

1. **Learning to Rank (LTR)**
   * Learning to Rank is not a new concept in Machine Learning. This is more commonly applied in search and recommendation systems leveraging the 3 classes of LTR algorithms:
       * **Pointwise ranking**
         * Classification algorithms commonly used: Logistic Regression, Gradient Boosted Trees, SVM, Random Forest, Neural Networks, Regression models
         * Ranking problem is a "classification" task. Each query-document pair gets a target label, which would be 0 or 1 if binary classification and more than 1 if multi-class classification.
         * The ranking score is determined by training a model to predict the raw logits --> prediction probabilities --> prediction labels for each query-document pair.
         * So the final probablities are ranked on a scale suchas this below. Thus the final ranking would be d1 --> d3 --> d2.
           ```
           q1​,d1​→score: 0.6
           q1,d2→score: 0.1
           q1,d3→score: 0.4
           ```
       * **Pairwise ranking**
           * Pairwise algorithms commonly used: LambdaRank, RankNet, RankBoost, RankSVM, Factorization Machines
           * The goal of pairwise ranking is to bring in the contextual relevance of a ranking system.
           * Pointwise only gives us a "yes" or "no" answer based on a classification task.
           * Each query-document pair is passed to the model separately. The pairwise comparison helps a model learn the relative order of documents for a given query rather than predicting 1 similarity score.
           * However, the computational overload from the permutations of query-document pairs can be time consuming and complex. Also, individual pairs are focused on rather than global relationships. 
       * **Listwise ranking**
           * Listwise algorithms commonly used: ListNet, ListMLE, LambdaMART
           * Here the goal is to optimize the entire list of documents based on the documents relevance to a given query -- thus more global approach than focusing on each single document or the order they appear.
           * List-wise methods can extend beyond binary or multiclass classification into learning complex ranking functions, where models are trained to directly optimize ranking metrics across an entire list, improving the overall ranking quality in contrast to just focusing on individual pairwise comparisons.
        

2. **Relevance Feedback**
  * This usually involves using interactive feedback from users or other sources to iteratively refine the ranking of documents.
  * It can be done through explicit feedback (e.g., user ratings such as thumbs up or thumbs down) or implicit feedback (e.g., user behavior).
3. **Semantic Similarity**
  * Semantic similarity based on similarity metrics like cosine and dot product using embedding models. 
4. **Diversification**
  * Diverse set of relevant documents to a query using metrics such as MMR (Maximal Marginal Relevance).
5. **Query Expansion**
  * Expand original query with more terminology and context to retrieve more relevant documents.
6. **Contextual Reranking**
  *  user context or dialogue history can help improve the relevance of reranked documents in conversational search or recommendation systems.
7. **Hybrid Approaches**
  * Multiple approaches combined


# Reranker Evaluation Metrics
1. Relevancy
   * Common retrieval metrics such as NDCG.
2. Latency
3. Speed
4. [RAG Metrics](https://www.galileo.ai/blog/mastering-rag-how-to-select-a-reranking-model)
   * Chunk attribution
   * Chunk utilization
   * Context Adherence
   * Completeness

![image](https://github.com/user-attachments/assets/701cdcfa-9f66-4c24-bc6f-173e016221f6)
