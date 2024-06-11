# Constructing Knowledge Graphs from Documents
* This repo goes over the process/steps for creating Knowledge graphs from documents.
* The first example we will see is from the Neo4j and deeplearning.ai course "Knowledge Graphs for RAG".
    * This is a great example because what they do is take an open source SEC 10k document which is 100s of pages long with multiple lines of text, headings and subheadings and turn it into a knowledge graph.
* The biggest takeaway (at least for me) is that the Knowledge Graph is created using a "classical" Data Science Process which is paramount in any machine learning workflow. To create the knowledge graph you have to understand what is in your data, if there any important codes that you can use to index documents and subdocuments to create nodes and edges and properties.
* Once the knowledge graph is created you then follow the typical NLP machine learning workflow of cleaning the text, chunking the text, vectorizing and embedding the text, and then plugging it into Neo4j for semantic similarity search. 
