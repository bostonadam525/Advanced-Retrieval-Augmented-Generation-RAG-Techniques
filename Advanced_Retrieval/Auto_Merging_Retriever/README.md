# Auto Merging Retriever
* This technique aims to solve the problem of **discontinuous chunks**.
* Discontinuous chunks can create a non-coherent response from the LLM often with non-sense outputs or incomplete sentences and phrases. 

## How do discontinous chunks occur?
* Depending upon how you split and chunked your data, during a semantic search, the top_k chunks will be retrieved and synthesized by your retriever and the LLM.
* If you have chunks in your vector store that are lacking semantic context or metadata and they are retrieved, this will very often result in **discontinuous chunks**.

## What is Auto-Merging and how does it work?
* Vectors are stored in "levels".
  * Level 1 is the "parent chunk" node. 
  * Level 2 are the "child chunks" node.
* Usually a semantic search and retrieval is based on a threshold metric such as cosine similarity and/or a `top_k` value.
  * If a user query results in retrieving any non-consecutive chunks based on the thresholds of the system (e.g. chunk 1, chunk 2, chunk 4), then instead of returning these non-consecutive chunks the **parent chunk** is returned instead to prevent information loss.
 

## Advantages of Auto-Merging
1. Virtually no information loss.
  * Retrieved chunks and LLM outputs are generally more contextualy relevant and precise as a result of auto-merging.

2. Virtually NO FRAGMENTATION
   * Either consecutive child chunks are retrieved OR the parent chunk is retrieved (auto-merging) to prevent information loss and fragmentation.
  
3. Dynamic Content Integration
   * Merging ensures that smaller child chunks are merged to create more precise, coherent and information rich contextual outputs.
  

## Disadvantages of Auto-Merging
1. Complexity Increases
   * Hierarchical parent-child chunk structure is often complex and can be difficult to create and maintain.
   * Creating this "hierarchy" and the "auto-merging" workflow processes can take significant time and compute power.
  
2. Over generalization
   * Merging chunks can also lead to the wrong information being retrieved (it is not a perfect process). 
