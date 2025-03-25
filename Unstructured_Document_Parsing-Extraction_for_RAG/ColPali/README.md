# ColPali

# Background
* Retrieval Augmented Generation (RAG) systems, combine information retrieval with LLMs for question answering, but they present several challenges:
* PDF Parsing
  * Extracting meaningful information from PDF files is often a complex task, often requiring multiple steps like Optical Character Recognition (OCR), layout detection, and chunking.
* Limited Explainability
  * Most embedding retrieval methods struggle to provide insights into why a particular document was retrieved, hindering user understanding and trust.
* Performance vs. Keyword-based Approaches
  * Keyword or “free-text” based retrieval methods like BM25 can perform as well as or even better than embedding methods for certain use cases which exactly highlights the limitations of current embedding approaches.


# Standard Retrieval/Indexing of PDF Documents
* Below is an image of what "Standard Retrieval" using OCR looks like. This image is taken from the original ColPali paper: [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)
* This is often a multi-step process as depicted in the image below:
  1. OCR extraction --> extract words from pages
  2. Document Layout Detection --> segment paragraphs, titles, and other page objects such as tables, figures, and headers
  3. Chunking experimentation and choosing an optimal embedding model (this process can be hit or miss)
     * A chunking strategy is then defined to group text passages with some semantical coherence, and modern retrieval setups may even integrate a captioning step to describe visually rich elements in a natural language form, more suitable for embedding models.


![image](https://github.com/user-attachments/assets/51316b92-f01d-4ab4-9505-b9ec9d7333ee)


# Solution to Problem: ColPali
* ColPali stands for: "Contextualized Late Interaction over PaliGemma"
  * ColPali makes processing PDF documents more efficient as it captures screenshots of each page and embeds entire document pages into a unified vector space using VLMs (vision language models).
  * This approach allows ColPali to bypass the complex extraction process seen above in the **standard retrieval** pipeline, improving retrieval accuracy and efficiency.


* ColPali can scale to billions of documents.
  * See this post: [Scaling ColPali to billions of PDFs with Vespa](https://blog.vespa.ai/scaling-colpali-to-billions/)

* ColPali presents a novel method that addresses these challenges mentioned above by leveraging the power of **vision language models**.
* Instead of relying ONLY on text, ColPali directly processes images of PDF pages, allowing it to **capture both textual and visual content.**


![image](https://github.com/user-attachments/assets/cf4dbb6b-a49f-46ab-97ec-575266f84095)

## Workflow of ColPali
1. **Document Processing**
  * Create images from PDFs.
  * Instead of running a pipeline to extract text --> creating chunks --> embed chunks, **ColPali directly embeds each screenshot of a PDF page into a vector representation**.
  * This step is analagous to snapping a picture of each page rather than attempting to extract its content.

2. **Images split into grids**
  * Each document page is divided into a **grid of uniform pieces called patches**.
  * Default grid size is 32x32, which creates 1024 patches per image.
  * Each patch is represented as a 128-dimensional vector.
  * You can think of each patch as one image with 1024 "words" describing those patches.

3. **Embeddings**
  * **Processing image patches**
    * ColPali transforms visual patches into embeddings using its Vision Transformer (ViT), which processes each patch to create a detailed vector representation.
  * **Aligning visual and text embeddings**
    * To match visual information with the search query, ColPali converts query text into embeddings in the **same vector space as the image patches.**
    * **This allows the ViT model to directly compare and match visual and textual content.**
  * **Query processing**
    * ViT model tokenizes the query, assigning each token a 128-dimensional vector.
    * It will use prompts such as “Describe this image ” to ensure the model focuses on the visual elements, allowing seamless text and visual data integration.
   
4. **Retrieval Process**
  * ColPali uses **late interaction similarity** to compare the query and document embeddings at query time.
  * This approach allows detailed interaction between all the image grid cell vectors and the query text token vectors, ensuring a comprehensive comparison.
  * Similarity is computed using a **"sum of maximum similarities"** approach:
      * Compute similarity scores between each query token and every patch token in the image.
      * Aggregate these scores to generate a relevance score for each document.
      * Sort the documents by the score in descending order, using the score as a relevance measure.

  * This method allows ColPali to match user queries effectively with relevant documents, focusing on the image patches that best align with the query text.
  * This will **highlight the most relevant portions of the document, combining textual and visual content for precise retrieval.**



## Advantages of ColPali:
1. **No need for complex preprocessing**
   * ColPali replaces the traditional pipeline of text extraction, OCR, layout detection, and chunking with a single VLM that takes a screenshot of the page as input.

2. **Multimodal visual and textual information extraction**
   * ColPali works directly on page images, thus it can incorporate **both textual content and visual layouts** in understanding complex documents.

3. **Efficient retrieval from visually rich documents**
   * ColPali leverages the "late interaction mechanism" from ColBERT that allows for fine-grained matching between queries and document content, enabling efficient retrieval of relevant information from complex, visually rich documents.

4. **Contextual Preservation**
   * ColPali works on entire page images, thus maintains the full context of the document, which often can is easily lost in traditional text-chunking approaches.
  
## Disadvantages/Challenges with ColPali
1. **Computational Complexity**
   * Compute requirements for ColPali grow quadratically with the number of query tokens and vision transformer patch vectors.
   * This means that as the complexity of queries or the resolution of document images **increases**, the computational demand grows rapidly.

2. **Memory Requirements**
   * The memory cost of ColBERT (later-interaction) approaches is **10x to 100x that of standard dense vector embeddings**.
   * This is because ColBERT approaches require **a vector for each token**.
   * The memory needs of a system scale linearly with 3 factors:
      1. Number of documents
      2. Number of image patches per document
      3. Dimensionality of vector representations

## Solutions to ColBERT issues
* Consider **precision reduction** which is often used for fine-tuning LLMs.
* By reducing higher-precision representations such as 32-bit floats to lower-precision formats 8-bit integers, you can dramatically reduce memory requirements with very little impact on the quality of retrieval. 


# ViDoRe Benchmark
* This was proposed by Fayesse et al. in the [original ColPali paper](https://arxiv.org/abs/2407.01449)
* The Visual Document Retrieval Benchmark, was introduced to assess retrievers on their capacity to retrieve visually rich information in docs, with tasks spanning various topics, modalities (figures, tables, text), and languages.
* The reason for this benchmark is that existing text embedding benchmarks are not adequate enough to benchmark Vision Language Models in these retrieval tasks.
* The [ViDoRe Leaderboard is here](https://huggingface.co/spaces/vidore/vidore-leaderboard)

# References
* [ColPali: Enhanced Document Retrieval with Vision Language Models and ColBERT Embedding Strategy](https://zilliz.com/blog/colpali-enhanced-doc-retrieval-with-vision-language-models-and-colbert-strategy)
