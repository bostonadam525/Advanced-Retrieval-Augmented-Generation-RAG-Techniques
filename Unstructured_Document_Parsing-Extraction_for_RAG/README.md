# Unstructured Document Parsing and Information Extraction for RAG
* This repo is devoted to multiple techniques that can be used for information extraction from unstructured documents for building Retrieval Augmented Generation (RAG) applications.
* There are numerous techniques, methods, programming packages and various other approaches to parsing unstructured data. Below is not considered a complete list but a growing collection.



## Knowledge Graphs
* [Neo4j PDF to graph](https://neo4j.com/developer-blog/graphrag-llm-knowledge-graph-builder/)



## Python Based Packages/Libraries
1. [MegaParse](https://github.com/QuivrHQ/MegaParse)
2. [Docling](https://ds4sd.github.io/docling/)
3. [Pdf2image](https://github.com/Belval/pdf2image) with or without [Easy OCR](https://github.com/JaidedAI/EasyOCR)
4. cdqa (usually use it with BERT or another model)
   * [cdqa](https://github.com/cdqa-suite/cdQA?tab=readme-ov-file) is no longer maintained, so see link below for Haystack
   * [Haystack](https://github.com/deepset-ai/haystack)
6. [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
7. [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
8. [LlamaParse](https://github.com/run-llama/llama_parse)
9. [unstructured.io](https://docs.unstructured.io/welcome)


## Transformers
1. [ColPali](https://huggingface.co/vidore/colpali)
2. [Phi-3 Vision](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct)
3. [LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-base)
4. .....more to be added


## Document Classification
1. Huridocs
   * This repo has some methods to consider when building a document classifier. They also have other packages that are great for working with PDF data.
     * [entity-extractor](https://github.com/huridocs/trainable-entity-extractor)
     * [pdf-doc-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis)
    
2. ....more to be added
