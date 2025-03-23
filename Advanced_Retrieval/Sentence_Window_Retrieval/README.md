# Sentence Window Retrieval Optimization
* You would mostly use this technique when your **context relevancy score during the retrieval process is VERY LOW.**
  * Most RAG systems use the SAME chunk(s) for retrieval and generation pipelines.
  * This can sometimes be problematic if the chunk(s) being used do not contain ALL important contextual information. So how do you make sure that does not happen?
* To optimize a RAG pipeline, it’s essential to retrieve all **relevant information** related to a user query from the knowledge base or vector store. This can be achieved by tuning the chunk size:
  * Increasing chunk size: This can capture more context but may reduce retrieval accuracy.
  * Decreasing chunk size: Enhances retrieval accuracy but risks omitting some necessary content.


## Sentence Window Retrieval Technique
* The concept here is to segment large text documents into **individual sentences as retrieval chunks**, with each node representing a sentences.
* Another way to phrase this is: **"Decoupling Retrieval from the Generation Pipeline".**
  * The decoupling allows the split pipeline to do this:
    1. Retrieve the most relevant sentence(s).
    2. Enhance the Generative pipeline phase with the most relevant sentence(s) as metadata for the LLM to utilize. 
  * So instead of using classical chunking techniques such as `RecursiveCharacterTextSplitter` or a Semantic Splitter, you split your documents by sentence. 
* Sentence window retrieval refines the RAG pipeline by **grouping sentences into contextual windows.**
  * The premise is simple:
      * Single-sentence chunks often fail to provide enough context for generating high-quality responses, as the information within a single sentence might be incomplete or ambiguous.
      * Sentence window retrieval tackles this by **embedding adjacent sentences together,** enabling better coherence and understanding.
      * This works well because neighboring nodes contain sentences that are contextually related to each primary sentence.
* When a user query is sent to the RAG pipeline, this framework retrieves **similar vector sentence embeddings** from the vector database AND extracts **relevant neighbor sentences as metadata.**
* This method is powerful as it allows for the **inclusion of substantial content while maintaining a high level of accuracy.**
* [Image source](https://medium.com/@p.saha/optimizing-rag-pipelines-sentence-window-retrieval-or-auto-merging-retrieval-950b50a4eb76)

![image](https://github.com/user-attachments/assets/b5e415c9-92c1-45d6-ad16-a2e247459362)


### Advantages
1. **Increased Relevance and Context Enrichment**
   * Sentence window retrieval increases the relevance of retrieved documents/chunks by considering nearby information.
   * This results in enhances generative outputs from the LLM based on additional metadata context.

2. **Detailed Granularity and Specificity**
   * Adjusting window sizes allows for significant flexibility:
       * Smaller windows provide concise context and specificity related to a user query
       * Larger windows enrich understanding but at a higher cost.

3. **Greater Control: Balance between Large Context and Focused Context**
   * Sentence windowing allows the ablility to fine tune the balance between retrieval accuracy and cost.
   * The Retrieved sentence(s) can be balanced by the contextual sentence metadata for a more focused output response. 
     * Adding a sliding window approach can also enhance this significantly.

### Disadvantages
1. **Token Usage and Cost**
   * Large sentence windows increase the number of tokens processed and sent to the LLM, which may significantly raise computational costs.

2. **Limited Long-Range Context**
   * Sentence windows only focus on nearby sentences.
   * The problem with this is if relevant context appears much earlier or later in a document, or is randomly scattered throughout a document, then it may be missed unless the window size is dramatically increased (which can inflate token usage and costs).

3. **Complexity**
   * Chunking by sentences means more chunks to store in a vector database. This can create a more complex retrieval process by processing more semantic vectors during the search and retrieval phase.
   * In addition, by decoupling the "retrieval" and "generation" pipelines by not using the SAME chunk(s) for both pipelines, this can lead to downstream issues if not done correctly. 
