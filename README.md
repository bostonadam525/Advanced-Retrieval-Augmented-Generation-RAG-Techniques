# Advanced-Retrieval-Augmented-Generation-RAG-Techniques
* A comprehensive review of Advanced RAG Techniques for LLMs
* Research by Adam Lang (February 7, 2024)
* I plan to add code samples to the repo demonstrating some of these techniques.

# Failure Points of RAG Systems

* From the paper by Barnett et al. “Seven Failure Points When Engineering a Retrieval Augmented Generation System.” arXiv:2401.05856v1. 11 Jan 2024

## FP1

**Missing Content**: The first fail case is when asking a question that cannot be answered from the available documents. In the happy case the RAG system will respond with something like “Sorry, I don’t know”. However, for questions that are related to the content but don’t have answers the system could be fooled into giving a response.

## FP2

**Missed the Top Ranked Documents**: The answer to the question is in the document but did not rank highly enough to be returned to the user. In theory, all documents are ranked and used in the next steps. However, in practice the top K documents are returned where K is a value selected based on performance.

## FP3

**Not in Context - Consolidation strategy Limitations**: Documents with the answer were retrieved from the database but did not make it into the context for generating an answer. This occurs when many documents are returned from the database and a consolidation process takes place to retrieve the answer.

## FP4

**Not Extracted**: Here the answer is present in the context, but the large language model failed to extract out the correct answer. Typically, this occurs when there is too much noise or contradicting information in the context.

## FP5

**Wrong Format**: The question involved extracting information in a certain format such as a table or list and the large language model ignored the instruction.

## FP6

**Incorrect Specificity**: The answer is returned in the response but is not specific enough or is too specific to address the user’s need. This occurs when the RAG system designers have a desired outcome for a given question such as teachers for students. In this case, specific educational content should be provided with answers not just the answer. Incorrect specificity also occurs when users are not sure how to ask a question and are too general.

## FP7

**Incomplete**: The answers are not incorrect but miss some of the information even though that information was in the context and available for extraction. An example question such as “What are the key points covered in documents A, B and C?” A better approach is to ask these questions separately.


# Overview of RAG

* RAG performs a semantic search across many text documents which could be a small subset of text or even up to billions of lines of text depending upon the use case. 
* Vector search is often used to ensure efficient and fast scaled semantic search.
    * Vector search is performed using vectorized text which means we place all words in a corpus into a vector space and compare their mathematical proximity to a query text vector using a metric such as cosine similarity.
    * Vectors are compressions of the "meaning" behind text into (usually) 768 or 1536-dimensional vectors.
    * Compression often results in some information loss because we're compressing this information into a single vector.
    * Often we will see the `top k` vector search documents may not contain all relevant information.



What can we do if semantically important information is located at a `lower k` query position in our retrieval chain? How can we make sure the LLM is able to see this information and use it to enhance our final output(s)?

* The most basic approach is to increase “top k” number of documents. Then we can pass this information to the LLM.
* Recall is the most common metric used which is a count of the number of relevant documents we retrieve.
* Recall does not consider the total number of retrieved documents — so we can “hack” the metric and get perfect recall by returning everything (Pinecone, 2023).
  
![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/41e57a5c-2c10-458d-b608-cf19c001cae2)



**However, due to “context windows” LLMs have limitations on how much text (or tokens) we can send to them, thus we are not able to return “everything” in every LLM query.**

* Some LLMs like Anthropic's Claude, have attempted to solve this problem with a larger context window of 100K tokens. 

    * So why isn’t everyone using the “Claude” LLM? With 100k tokens couldn’t we just “stuff” the context window and return all information in one shot? No, actually we can’t.

**Why is “Context stuffing” a bad idea?**

* Context stuffing significantly reduces the “LLM recall” which is NOT the same as the (retrieval) recall we mentioned above.

  ![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/ddf9a1d6-fc8e-4908-9d60-b0638cdc823a)



# Overview of the U-Shaped Curve above (source: Pinecone, 2023)

* This is called the “serial position effect” which states in free-association of elements in a list, humans tend to only remember the first and last elements. The serial-position effect plays a role in understanding how humans develop short- and long-term memory.
* A serial-position-like effect in language models is probably surprising, since the self-attention mechanisms underlying Transformer LLMs is technically equally capable of retrieving any token from their contexts (Liu et al, 2023).



# What is LLM Recall?

* This is the ability of an LLM to retrieve information from any text placed within a context window.
* Liu et al. paper from 2023 revealed that “stuffing a context window” results in:

     * LLM recall degradation.
     * Overall decline in ability for LLM to follow prompt instructions.

* So, in summary: We can increase the number of documents returned by our vector database to increase retrieval recall, but we cannot send these to our LLM without degrading the overall LLM recall.



# What are the solutions to maximize LLM recall for Context Windows?

1. Retrieve a sufficient number of relevant documents, text or tokens.

2. Reduce the number of documents that are sent to the LLM.

3. Reorder documents retrieved so only those that are most semantically relevant are visible to our LLM.

4. “Reranking” is the most common technique used.


# Advanced RAG Solutions

* There are many new “Advanced RAG” techniques and approaches out there with new ones arising everyday.
* These are some of the “more relevant” or “feasible” techniques that we will take a closer look at.



# 1. Chunking + Vectorization

## Chunking

* `chunk size` is an important parameter to consider.
* Mostly dependent upon embedding model(s) used.
    * Encoder-only models such as BERT sentence-transformers handle a maximum of 512 tokens.
    * OpenAI ada-002 handles 8191 tokens.
* Question: Are the chunks retrieved by the LLM sufficient enough for semantic reasoning and comparison?
* Consider different chunking techniques discussed in this article by Pinecone (link: https://www.pinecone.io/learn/chunking-strategies/)
    * `Fixed-size chunking`
    * `Content-aware chunking`
        * Sentence splitting
            * Naive Splitting
                * split on sentences "."
                * doesn’t consider all possible edge cases, colloquial language or fragmented text.
             
            * NLTK
                * pre-configured sentence tokenizer
                * `from langchain.text_splitter import NLTKTextSplitter`
            * spaCy
                * pre-configured sentence tokenizer
                * `from langchain.text_splitter import SpacyTextSplitter`
             
    * Recursive Chunking
        * divides text into hierarchical and iterative structure, then recursively iterates on itself to retrieve “desired” chunk based on prompt criteria.
        * `from langchain.text_splitter import RecursiveCharacterTextSplitter`
     
    * Specialized chunking
        * Markdown and LaTeX - concept is to conserve the ‘original structured format' of your text data.
            * `from langchain.text_splitter import MarkdownTextSplitter`
            *  `from langchain.text_splitter import LatexTextSplitter`


* Medical Text Chunking
    * How do the chunking techniques perform on medical abbreviations and acronyms?
    * Consider paper: **“Token Classification for Disambiguating Medical Abbreviations”**
        * BERT models outperformed all others => bi-directional encoder transformer model
        * paper: https://arxiv.org/pdf/2210.02487.pdf



## Vector embeddings
* refer to MTEB Leaderboard: https://huggingface.co/spaces/mteb/leaderboard
* Currently using BGE embeddings: Might make sense to use https://huggingface.co/BAAI/bge-reranker-base because we've used a model from the same family for the base embeddings and first pass search, or if it would make more sense to use the MS MARCO models because they're NOT from that family.
    * Description from huggingface: Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. To balance the accuracy and time cost, cross-encoder is widely used to re-rank top-k documents retrieved by other simple models. For examples, use bge embedding model to retrieve top 100 relevant documents, and then use bge reranker to re-rank the top 100 document to get the final top-3 results.
    * MS MARCO models are more than 3 years old; the BGE cross-encoder came out just this past fall.
    * BAAI model is more recent
 
* What about Sentence Embeddings?
    * Cross encoders => might be difficult for us to use sentence-transformers directly as LangChain doesn’t wrap it.
    * SGPT: GPT Sentence Embeddings for Semantic Search: https://github.com/Muennighoff/sgpt?tab=readme-ov-file
 



# 2. Search Index

## Vector Store Index
* Flat Index” - most RAG implementations use “brute force” distance calculation between vector query and chunk vectors.
* 'Vector Index” - more ideal for efficient text retrieval. Examples include:
  1. FAISS: https://faiss.ai/
  2. nmslib: https://github.com/nmslib/nmslib
  3. Spotify's "annoy": https://github.com/spotify/annoy
  4. llamaIndex supports multiple vector DB indices: https://docs.llamaindex.ai/en/latest/community/integrations/vector_stores.html#
  5. Neo4J + LangChain Vector Index: https://blog.langchain.dev/neo4j-x-langchain-new-vector-index/
     ** Note about using Neo4J: would this be a good approach to take when using something like `RadGraph` which is a hierarchial mapping of named entities for radiology?

* Nearest Neighbors Implementations’
   * Clustering
   * Trees
   * HNSW: https://www.pinecone.io/learn/series/faiss/hnsw/
 

## Hierarchical Indices
* The concept is to create 2 indices:
1. Summaries
2. Document Chunks
* This is done by first retrieving ONLY relevant documents => then search within this top k relevant group for relevant chunks. See diagram below from Ilin, 2023:

  ![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/2006940c-99e8-493c-9121-4d5917419843)



## Context Enrichment
The concept of “context enrichment” is based on retrieving smaller chunks of text for “better quality” but add up or include the surrounding text or sentences for the LLM to reason with for semantic context. 

The 2 most common techniques are:
1. Sentence Window Retrieval
   a. each sentence is a separate embedding with a separate cosine similarity score.
   b. A “sliding window” is implemented to extend the semantic context of each targeted sentence embedding by “k” sentences before and after the target embedding sentence.
   c. This adds semantic context for the LLM to be able to better return a more relevant response. 

Diagram from Ilin, 2023 showing this:

![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/030b9959-7e58-43eb-afb2-26d3a79253f6)


2. Auto-merging retrieval
  a. Similar idea to “sentence window” above.
  b. Documents split into “Top K” relevant “child” chunks with hierarchical linkage to parent chunks.
  c. Depending upon the output, if “n” number of child chunks are the same as the parent chunks we merge them and feed the parent chunk to the LLM for final output.

Diagram from Ilin, 2023 showing this:

![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/c22e0cf5-a4eb-4279-b629-bb9b5e2f20a9)



## Fusion Retrieval (Hybrid Search)
* This is a “hybrid” or “fusion” approach that combines the powers of both search methods:
    * “keyword” (lexical) search: commonly done using NLP algorithm such as TF-IDF or BM25 (more common and standard)
    * “semantic” (vector) search

* Combine the 2 search methods using the “Reciprocal Rank Fusion” algorithm to obtain 1 result
    * Usually done with the “cosine similarity” score.
    * However, this can be a problem (I will explain this with re-ranking below)

* LangChain has the EnsembleRetriever to perform this: https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble




Diagram from Ilin, 2023 showing this method:



![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/de1631a8-fa74-4e1b-a00f-138ec79229a9)


# 3. Reranking
* This is an excellent introduction to understanding sentence embeddings: https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings/
* A standard RAG design uses embeddings precomputed by a **bi-encoder** which compresses an entire document chunk into a **single fixed-length vector** usually stored in a **vector database.**
* During language model inference, a user’s query is **encoded and compared** with the stored embeddings using **cosine similarity**. This means we are examining the specific similarity between two sentences by encoding the two sentences into two vectors and then compute the similarity between the two vectors. Bi-encoder models are trained to optimize the increase in the similarity between a user’s query and semantically relevant sentences and decrease the similarity between the query and the other sentences. This is why bi-encoders are better suited for search.
* **Bi-encoders** are fast and scale easily. If multiple sentences are fed to a RAG model, the bi-encoder will encode **each sentence independently**. Yes, this means the sentence embeddings are independent of one another. This is a good thing for search, as it allows us to encode millions of sentences in parallel.
* **However, we have a big problem now. The bi-encoder model doesn’t know anything about the relationship between the sentences.**

### When we use cross-encoders, we do something different. 

* A cross-encoder is an alternative model which takes **both the query and a retrieved document** as input to encode multiple sentences simultaneously and then output a **single unified classification score**. As the query and the document are passed simultaneously to the model, the **cross-encoder** suffers from **less information loss resulting in better performance.**
* If a cross-encoder gives better performance, why should we even waste time storing embeddings from a bi-encoder? Scoring thousands to millions of query/document pairs with a cross-encoder is computationally slow (significant memory usage) and results in suboptimal RAG performance.
* The most common solution is a **two-staged approach:**
  1. First retrieve `‘top k’` text chunks via the Bi-Encoder
  2. Then semantically re-rank `‘top k’` chunks using a Cross-Encoder

Two figures below demonstrating the bi-encoder vs. cross-encoder:

Figure 1. (source: Wehkamp, 2024)

![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/7cbc2a7e-8154-4eb7-aab8-dc4031648b1d)


Figure 2. (source: Pinecone, 2023)

![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/5532affc-effa-4367-b1c1-39d9c0683691)



# Let’s summarize what we’ve discussed so far.....

* LLMs struggle with “LLM recall” and get “lost in the middle” not being able to process every chunk of text placed in their context window. Less is more.
* Most embeddings use bi-encoder models which compresses chunks into single vector space. Each sentence is encoded with its own similarity score.
* Bi-encoders scale easy over large document chunks and are fast.
* Cross-encoders encode 1 similarity score for 2 or more sentences and suffer from less information loss.
* Cross-encoders alone are computationally expensive.
* A more optimal RAG model is a 2 stage approach:
  a. Bi-encoder retrieval
  b. Cross-encoder reranking



Reranking model (Pinecone, 2023):

![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/42e02144-0c39-4ffa-aa77-372b96d5fa4d)



# Are all “re-rankers” (cross-encoders) equal? RAG Metrics help us tell the story.
* No, it depends on the use case.
* “RAG metrics” are used to evaluate RAG models with and without re-rankers (Wehkamp, 2024).



## Hit Rate
* Calculates the fraction of queries where the correct answer shows up within the top-k retrieved documents.
* In plain English: **“how often our system gets it right within the top k tries.”**

## Mean Reciprocal Rank (MRR)
* With each query, MRR will evaluate RAG accuracy by looking at the rank of the **highest-placed relevant document.**
* This is the average of the reciprocals of these ranks across all queries.
* In plain English: If the 1st relevant document is the top k result, the MRR is 1, if it is 2nd MRR is 1/2, etc…..


## Mean Average Precision (MAP)
* Precision is the number of relevant results relative to all retrieved documents. If 10 documents are retrieved and only 5 are actually relevant, the calculated precision is 50%. A major problem with precision is that it does not take the **ranking order** into account which is especially relevant for LLM-RAG retrieval.
* Average precision is a metric which helps address this. Average precision at K is computed as an average of precision values for all possible values within K. The caveat here is that we only look at the precision values for ranks where the items are relevant.
* The concept behind this metric is that it favors getting the top ranks correct and penalizes errors in the early positions.
* Thus, the Mean Average Precision (MAP) is the mean of the Average Precision calculated for all queries.


## Normalized Discounted Cumulative Gain (NDCG)
* Normalized Discounted Cumulative Gain (NDCG) compares document rankings against with an ‘ideal ranking.’



# Re-ranker Study Results from LlamaIndex
* **LlamaIndex** published results of their study on their blog which I will list below, including the table and access to the code experiments (Theja, 2023).
    a. source: https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83
    b. notebook: https://colab.research.google.com/drive/1TxDVA__uimVPOJiMEQgP5fwHiqgKqm4-?usp=sharing

  ![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/6abd86fc-4c58-4d52-9c2e-0bd93dd24c3c)



## LlamaIndex Study Results - Performance by Embedding:

* **OpenAI**: Showcases top-tier performance, especially with the `CohereRerank`(0.926966 hit rate, 0.86573 MRR) and `bge-reranker-large`(0.910112 hit rate, 0.855805 MRR), indicating strong compatibility with reranking tools.
* **bge-large**: Experiences significant improvement with rerankers, with the best results from `CohereRerank`(0.876404 hit rate, 0.822753 MRR).
* **llm-embedder**: Benefits greatly from reranking, particularly with `CohereRerank`(0.882022 hit rate, 0.830243 MRR), which offers a substantial performance boost.
* **Cohere**: Cohere’s latest v3.0 embeddings outperform v2.0 and, with the integration of native `CohereRerank`, significantly improve its metrics, boasting a 0.88764 hit rate and a 0.836049 MRR.
* **Voyage**: Has strong initial performance that is further amplified by `CohereRerank`(0.91573 hit rate, 0.851217 MRR), suggesting high responsiveness to reranking.
* **JinaAI**: Very strong performance, sees notable gains with `bge-reranker-large`(0.938202 hit rate, 0.868539 MRR) and `CohereRerank`(0.932584 hit rate, 0.873689), indicating that reranking significantly boosts its performance.
* **Google-PaLM**: The model demonstrates strong performance, with measurable gains when using the `CohereRerank`(0.910112 hit rate, 0.855712 MRR). This indicates that reranking provides a clear boost to its overall results.


## Impact of Rerankers
* **WithoutReranker**: This provides the baseline performance for each embedding.
* **bge-reranker-base**: Generally improves both hit rate and MRR across embeddings.
* **bge-reranker-large**: This reranker frequently offers the highest or near-highest MRR for embeddings. For several embeddings, its performance rivals or surpasses that of the `CohereRerank`.
* **CohereRerank**: Consistently enhances performance across all embeddings, often providing the best or near-best results.


## Necessity of Rerankers:
* The data clearly indicates the significance of rerankers in refining search results. Nearly all embeddings benefit from reranking, showing improved hit rates and MRRs.
* Rerankers, especially `CohereRerank`, have demonstrated their capability to transform any embedding into a competitive one.


## Overall Superiority:
* When considering both hit rate and MRR, the combinations of `OpenAI + CohereRerank` and `JinaAI-Base + bge-reranker-large/ CohereRerank` emerge as top contenders.
* However, the consistent improvement brought by the `CohereRerank/ bge-reranker-large` rerankers across various embeddings make them the standout choice for enhancing search quality, regardless of the embedding in use.

In summary, to achieve the peak performance in both hit rate and MRR, the combination of `OpenAI` or `JinaAI-Base` embeddings with the `CohereRerank/bge-reranker-large` reranker stands out.



# ***Re-ranker coding options***
* Cohere re-rank endpoint: https://txt.cohere.com/rerank/
* LangChain examples:
  a. https://github.com/Coding-Crashkurse/Applied-Advanced-RAG/blob/main/code.ipynb
  b. https://www.youtube.com/watch?v=3w_D1L0F-uE
* LlamaIndex: https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83
* Ragas Metrics: https://docs.ragas.io/en/latest/concepts/metrics/index.html
  a. Ragas code walk through: https://medium.aiplanet.com/evaluate-rag-pipeline-using-ragas-fbdd8dd466c1
* FlashRank: https://www.youtube.com/watch?v=fUIeMuRtQr8&list=PLlfkLS1egxuOwtxigkIc584jX-dyTkDdH&index=7&t=1345s
  a. GitHub Repo: https://github.com/AIAnytime/ReRankin...
  b. Langchain Long Context Reorder: https://python.langchain.com/docs/mod...
  c. Flash Rank GitHub: https://github.com/PrithivirajDamodar...
* deeplearning.ai course: https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/



# 4. Reranking + Hybrid Search (Microsoft Azure AI)
source: Berntson, 2023
* Microsoft Azure AI published a white paper discussing the different search techniques they offer: Keyword, Vector, Hybrid, Semantic Ranking, and Hybrid retrieval with Semantic Ranking.
* The authors demonstrated that **Hybrid Retrieval + Semantic Ranking yields the best grounding results for Generative AI Applications.**
* Microsoft’s more specific findings detailed below:
    a. “Hybrid Retrieval brings out the best of Keyword and Vector Search.”
    b. “Keyword and vector retrieval tackle search from different perspectives, which yield complementary capabilities.”
    c. “Vector retrieval semantically matches queries to passages with similar meanings. This is powerful because embeddings are less sensitive to misspellings, synonyms, and phrasing differences and can even work in cross lingual scenarios.”
    d. “Keyword search is useful because it prioritizes matching specific, important words that might be diluted in an embedding.”

* Overall, the best performing search engine is **Hybrid search + Semantic Ranker**
    * **Chart 1 below is from the Microsoft white paper:** We can see the percentage of search queries where high-quality text chunks are found in the **top 1 to 5 results**, compared across all search techniques. All retrieval techniques used the same set of customer query/document benchmark. Document chunks were 512 tokens with 25% overlap.  Vector and hybrid retrieval used the OpenAI Ada-002 embeddings.
 
  ![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/9fa13812-12cc-4d2c-93a8-37d961e6cdc5)



  # 5. Contextual Compression
* When building a RAG model we often embed documents in equally-sized text chunks and store the embeddings in a vector store.
* When a user queries the RAG system, it embeds the query, performs a similarity search over the vector store, retrieves the most relevant documents (chunks of text), and appends them to the LLM prompt.
* Problems with this model:
  1. How do we know what information in our documents and vector store is irrelevant?
  2. Irrelevant information will distract the LLM from giving a semantically correct response.
  3. Irrelevant information takes up space in the vector store that could be occupied by relevant information.
  4. Embeddings are wonderful in that they facilitate the quantitative comparison of data with unwieldy dimensionality, but it is well known that embeddings inherently "non-invertible" due to the information lost when reducing the dimensionality of the original text input during weight extraction during the output phase of a neural network (Gilbert et al, 2023). Furthermore, embeddings are also known to be inherently "unstable", with their stability based primarily on the vector spaces and nearest-neighbors overlap even for the most common words in a corpus. However, domain specific embeddings tend to be more stable (Wendlandt et al. 2018).
 
So, to solve these issues of irrelevant documents and information retrieval as well as information loss, "contextual compression" was introduced as a RAG technique. 
* Contextual compression "minimizes the storage footprint of a piece of data while preserving as much of the original information as possible" (Gilbert et al. 2023).

Example of Contextual Compression as part of RAG pipeline in LangChain:

  ![image](https://github.com/talkasab/LLMCDECreator/assets/45008475/1748aab6-c2ae-4275-bccd-077fdd911bba)


* LangChain's suite of Contextual Compressors:
  a. "Out of the box" `DocumentCompressors'
  b. A `ContextualCompressionRetriever` which wraps another Retriever along with a `DocumentCompressor` and automatically compresses the retrieved documents of the base Retriever.
  link: https://blog.langchain.dev/improving-document-retrieval-with-contextual-compression/


  # 6. "RAPTOR"
  * New paper out of Stanford University.
  * Sarthi et al. “RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval”. arXiv:2401.18059v1 [cs.CL] 31 Jan 2024
      * paper link: https://arxiv.org/html/2401.18059v1
      * Summary: The authors introduced a novel technique to improve RAG by **“recursively embedding, clustering, and summarizing chunks of text, constructing a tree with differing levels of summarization from the bottom up.”**





# "Classical NLP" Statistical Sampling
* Different Sampling techniques resources
  a. https://vinija.ai/nlp/data-sampling/
  b. https://blog.allenai.org/a-guide-to-language-model-sampling-in-allennlp-3b1239274bc3
  c. https://medium.com/@raniahossam/sampling-methods-in-text-generation-unlocking-diversity-and-creativity-ab706b6250c9
* Parameter Efficient Fine Tuning (PEFT)
  a. https://medium.com/mlearning-ai/7-key-prompt-engineering-parameters-everyone-should-know-4b3a330865a8






  # References
  * Barnett et al. “Seven Failure Points When Engineering a Retrieval Augmented Generation System.” arXiv:2401.05856v1. 11 Jan 2024. link: https://arxiv.org/html/2401.05856v1
  * Berntson, 2023. “Azure AI Search: Outperforming vector search with hybrid retrieval and ranking capabilities.” Retrieved from: https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167
  * hackerllama, 2024. “Sentence Embeddings. Cross-encoders and Re-ranking.” Retrieved from: https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings2/
  * Gilbert et al. "Semantic Compression With Large Language Models." arXiv:2304.12512v1 [cs.AI] 25 Apr 2023. link: https://arxiv.org/pdf/2304.12512.pdf
  * He, 2023. https://medium.com/@hwspotato/introducing-hybrid-search-and-rerank-to-improve-the-retrieval-accuracy-of-the-rag-system-efbf968f9662
  * Kumar, 2023. “Strategies for Effective and Efficient Text Ranking Using Large Language Models.” Retrieved from: https://blog.reachsumit.com/posts/2023/12/towards-ranking-aware-llms/
  * Ilin, I, 2023. “Advanced RAG Techniques: an Illustrated Overview.” Retrieved from: https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6
  * Liu et al. “Lost in the Middle: How Language Models Use Long Contexts.” arXiv:2307.03172v3 [cs.CL] 20 Nov 2023. link: https://arxiv.org/pdf/2307.03172.pdf
  * Pinecone, 2023. “Rerankers and Two-Stage Retrieval.” Retrieved from: https://www.pinecone.io/learn/series/rag/rerankers/
  * Pinecone, 2023. “Chunking Strategies for LLM Applications.” Retrieved from: https://www.pinecone.io/learn/chunking-strategies/
  * Theja, 2023. “Boosting RAG: Picking the Best Embedding & Reranker models.” Retrieved from: https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83
  * Wendlandt et al. "Factors Influencing the Surprising Instability of Word Embeddings. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers), pages 2092–2102, New Orleans, Louisiana. Association for Computational Linguistics.
  * Wehkamp, 2024. “Elevating Your Retrieval Game: Insights from Real-world Deployments.” Retrieved from: https://blog.ml6.eu/elevating-your-retrieval-game-insights-from-real-world-deployments-84ccfcbe6422
