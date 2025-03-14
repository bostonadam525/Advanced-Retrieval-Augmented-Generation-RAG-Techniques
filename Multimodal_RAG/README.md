# Multimodal Retrieval Augmented Generation (Multimodal RAG)
* This repo contains all things related to building multimodal RAG applications. 




# Concept and Scenario of Multimodal RAG
* The image below is from the Analytics Vidhya course taught by Suman Debnath from AWS. He is a guru in the field of NLP and Multimodal RAG.
* These are some of my notes from his lectures.

![image](https://github.com/user-attachments/assets/83932220-176e-47d0-b433-94f95144fa2b)


* Scenario based on image above
  * Imagine you have a multimodal dataset that contains: images, text, and tables.
  * Thus we have unstructured (images, text) and structured data (tables) that is also multimodal.
  * So how would you extract the information and build a system to perform RAG on this?

* Architectural Approaches
     * First you would as with any project, extract the multimodal data (images, text, tables) from documents. There are a myriad of approaches to doing this but a popular library is PyMuPDF and the LLM version which is PyMuPDF4LLM.

1. **Option 1 -- "Classical RAG"**
     * Create Multimodal embeddings for **images**, **tables**, **text** and store in a vector database/store. The concept is that all modalities that are similar will be indexed in the same vector space for retrieval.
     * Perform semantic search and retrieval over the raw images, tables and text and feed most relevant vector chunks to a multimodal LLM to generate answer.
         * Multimodal LLM is important here because it needs to be able to retrieve multimodal data.
      
2. **Option 2 -- "Retrieve Summarizations & Embeddings**
     * Utilize small language models (e.g. open-source transformers) to generate summaries of the images, tables, and text.
     * Create **Text Embeddings** from the 3 classes of summaries and store in a vector database. The difference here is that we are storing the **summary of data** and the **metadata of those summaries**. This is usually done via a hashmap or dictionary.
     * User then asks a question and we perform a semantic or hybrid search that retrieves chunks of summaries and feeds these relevant chunks to the LLM to synthesize an answer. The LLM DOES NOT need to be multimodal as we are only working with text.
  
3. **Option 3 -- "Retrieve image summary & Pass raw image to LLM"**
     * Same steps as Option 2 where you create summaries using small language models of the images, tables, and text and store those in separate indicies with their metadata in a vector database.
     * The difference in this approach though is when a user performs a query, the semantic search will:
         * **The "summaries" are being used ONLY as search vectors for the original dictionary or hashmap to retrieve the actual raw relevant chunks for the final response.**
         * Extract the relevant chunks from the vector database.
         * A recursive retrieval is performed as the next step is to go back to the original dictionary or hash map that stored the summaries and determine the modality that these relevant chunks came from: image, text and/or tables.
         * The final result is to then retrieve those modalities, so for example this could be an image and text and pass this to a Multimodal LLM to give the answer.
         * This is a case where a multimodal LLM is necessary as the result may be multimodal. 
