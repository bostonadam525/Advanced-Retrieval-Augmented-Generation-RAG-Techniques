# Hybrid RAG with Vector DB and Graph DB Project in Neo4j
* By Adam Lang
* Date: 2/3/2025

# Overview
* This is a short project showing how to implement a "hybrid RAG" application using traditional RAG with semantic vector and keyword search in a vector database and concatenate that with a knowledge graph from a graph database such as Neo4j.


# RAG Pipeline Architecture
* This is the general RAG pipeline architecture that I am going to implement. This is one of the more common ways to do this. See my diagram below:

![image](https://github.com/user-attachments/assets/93aaa69c-b134-4de8-ac11-a996ee820227)



# Data ingestion for Knowledge Graphs
* There are various approaches to building KG's.
* In short, there is an "LLM few shot" method and there is a more structured method that involves using NER based relation extraction tools like REBEL or GliNER. 
* There are different ways of ingesting structured data such as CSVs, briefly here are 2 methods:

**1. Neo4j Runway**
* This is a package released by Neo4j that uses OpenAI and allows you to create your own knowlege graph on a CSV.
* It requires prompting and a human in the loop to iterate on the graph data model.
* Links:
  * [Neo4j runway](https://a-s-g93.github.io/neo4j-runway/)
  * [Neo4j runway data ingestion](https://medium.com/neo4j/easy-data-ingestion-with-neo4j-runway-and-arrows-app-1e5f121333a7)
  * [Neo4j runway github](https://github.com/a-s-g93/neo4j-runway/tree/main)

**2. WhyHow.AI**
* They have numerous resources, but here is a [great blog post to get you started](https://medium.com/enterprise-rag/tables-csvs-to-graphs-whyhow-ai-sdk-9ed6d95f2f8b)

**3. Rebel**
* Rebel is an open source model that you can utilize via Hugging Face.
* The idea is that the model has been trained to extract triplets for building knowledge graphs from unstructured data.
* The triplets extracted are helpful for inserting a graph into a Property Graph DB such as Neo4j.
    * So this is similar to what the Neo4j Runway does but it uses an open source BART-Large encoder-decoder transformer on which the original model was trained.
* The original training dataset was based on wikipedia abstracts.
* Rebel resources:
    *  [Building Knowledge Graphs with Rebel: Step By Step Guide for Extracting Entities & Enriching Info](https://medium.com/@kamaljp/building-knowledge-graphs-with-rebel-step-by-step-guide-for-extracting-entities-enriching-info-ec29f2566de)
    * [REBEL huggingface](https://huggingface.co/Babelscape/rebel-large)
    * [REBEL github](https://github.com/Babelscape/rebel?tab=readme-ov-file)
    * [REBEL blogpost](https://medium.com/@sauravjoshi23/building-knowledge-graphs-rebel-llamaindex-and-rebel-llamaindex-8769cf800115)
    * [NLP Planet blog - Building Knowledge Graphs from Texts](https://www.nlplanet.org/course-practical-nlp/02-practical-nlp-first-tasks/16-knowledge-graph-from-text)


**4. Metadata Extraction**
* Metadata is a very important component of building these graphs.
* There are multiple approaches to this, some include:
    1. Topic Modeling (e.g. LLM driven, BERTopic, TurfTopic, etc..)
    2. Keyword extraction (e.g. KeyBERT)
    3. Named Entity Recognition (NER)
       * A common approach today is to use zero-shot open source models such as GliNER from hugging face or
       * Another approach is to use a pre-trained model and fine tune it from hugging face..or
       * Another approach is to use an LLM with chain-of-thought prompting (in-context-learning) or zero/few shot prompting.
    4. LlamaIndex
       * APIs like this have resources for LLM driven metadata extraction including: LLM driven, entity driven, Data structure driven (e.g. Pydantic), agentic driven.
       * [LlamaIndex approaches](https://docs.llamaindex.ai/en/v0.10.19/module_guides/loading/documents_and_nodes/usage_metadata_extractor.html)
    5. LangChain
       * LangChain also has metadata extractors/taggers such as the [OpenAI metadata tagger](https://python.langchain.com/docs/integrations/document_transformers/openai_metadata_tagger/)
    6. unstructured.io
       * This library is a pioneer in this space and always a go to: [unstructured metadata extractor](https://docs.unstructured.io/api-reference/api-services/document-elements)
    7. Haystack
       * This is yet another pioneer in this space with ample resources: [Embedding Metadata for Improved Retrieval](https://haystack.deepset.ai/tutorials/39_embedding_metadata_for_improved_retrieval)
