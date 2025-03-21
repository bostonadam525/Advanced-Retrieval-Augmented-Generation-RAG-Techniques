# Unstructured Document Parsing and Information Extraction for RAG
* This repo is devoted to multiple techniques that can be used for information extraction from unstructured documents for building Retrieval Augmented Generation (RAG) applications.
* There are numerous techniques, methods, programming packages and various other approaches to parsing unstructured data. Below is not considered a complete list but a growing collection.


# Unstructured.io PDF Processing
* Unstructured.io is just one of many tools that we as Data Scientists have at our disposal for processing complex PDF files.
* Here is a great [blogpost](https://unstructured.io/blog/how-to-process-pdf-in-python) from unstructured.io where they run through some of their best practices and approaches. There is an excellent diagram that shows a PDF processing pipeline from the blogpost:

![image](https://github.com/user-attachments/assets/bf03fa59-a742-45e6-b5a6-0393b062b460)


# Various Techniques for Unstructured Document Parsing

## 1. Knowledge Graphs
* [Neo4j PDF to graph](https://neo4j.com/developer-blog/graphrag-llm-knowledge-graph-builder/)



## 2. Python Based Packages/Libraries
1. [MegaParse](https://github.com/QuivrHQ/MegaParse)
2. [Docling](https://ds4sd.github.io/docling/)
3. [Pdf2image](https://github.com/Belval/pdf2image) with or without [Easy OCR](https://github.com/JaidedAI/EasyOCR)
4. cdqa (usually use it with BERT or another model)
   * [cdqa](https://github.com/cdqa-suite/cdQA?tab=readme-ov-file) is no longer maintained, so see link below for Haystack
   * [Haystack](https://github.com/deepset-ai/haystack)
5. [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
6. [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
   * [Unlocking the Secrets of PDF Parsing: A Comparative Analysis of Python Libraries](https://medium.com/@elias.tarnaras/unlocking-the-secrets-of-pdf-parsing-a-comparative-analysis-of-python-libraries-79064bf12174)
7. [LlamaParse](https://github.com/run-llama/llama_parse)
   * [Awesome LlamaParse tutorial](https://www.youtube.com/watch?v=wRMnHbiz5ck&list=PLz-qytj7eIWUWChyIYOWY1DtToKk56ZTE&index=4)
8. [unstructured.io](https://docs.unstructured.io/welcome)


## 3. Transformers
1. [ColPali](https://huggingface.co/vidore/colpali)
   * [Weaviate recipe](https://github.com/weaviate/recipes/blob/main/weaviate-features/named-vectors/NamedVectors-ColPali-POC.ipynb)
2. [Phi-3 Vision](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct)
3. [LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-base)
4. .....more to be added


## 4. Document Classification
1. Huridocs
   * This repo has some methods to consider when building a document classifier. They also have other packages that are great for working with PDF data.
     * [entity-extractor](https://github.com/huridocs/trainable-entity-extractor)
     * [pdf-doc-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis)
    
2. ExtractThinker
   * ExtractThinker is a flexible document intelligence tool that leverages Large Language Models (LLMs) to extract and classify structured data from documents, functioning like an ORM for seamless document processing workflows.
   * [Link to ExtractThinker repo](https://github.com/enoch3712/ExtractThinker)
