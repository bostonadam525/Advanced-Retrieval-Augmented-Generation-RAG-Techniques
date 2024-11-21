# Knowledge Graphs for RAG
* This repo will contain all things related to using Knowledge Graphs for Retrieval Augmented Generation


## How do we represent knowledge graphs in code? 
1. RDF (Resource Description Framework)
2. SPARQL (SPARQL Protocol and RDF Query Language)
3. OWL (Web Ontology Language)
4. Neo4j


## Triples in KGs
* Knowledge graphs are built on Triples
1. Entities, which represent the data of the organization or domain area.
2. Relationships, which show how the data entities interact with or relate to each other. Relationships provide context for the data.
3. An organizing principle that captures meta-information about core concepts relevant to the business.

* In a knowledge graph, a "triple" refers to a basic unit of information that consists of three parts:
  * a subject
  * a predicate (relationship)
  * an object, essentially representing a statement or fact about two entities connected by a specific relationship; it's the fundamental building block of a knowledge graph, allowing complex information to be structured and easily queried.

### Key points about triples
1. Structure: A triple is written as "Subject - Predicate - Object".
  * Example: "Barack Obama" - "is President of" - "United States".
  * RDF connection: Triples are based on the Resource Description Framework (RDF) data model, where each element in a triple is uniquely identifiable using a Uniform Resource Identifier (URI). '

## Difference between Property Graph and RDF
* Property graphs and RDF are both used to model data, but they differ in several ways, including their structure, intended use, and how they handle relationships: 

1. Structure
  * RDF stores statements as subject–predicate–object triples, while property graphs can implement different types of graphs, such as hypergraphs, undirected graphs, and weighted graphs. 

2. Intended use
  * RDF is designed for data exchange and interoperability, while property graphs are designed for applications and analytics. 

3. Relationships
  * Property graphs can easily handle many-to-many relationships, while RDF entities and relationships are only recognized by their URIs and don't have internal structures. 

4. Data type
  * Property graphs are best for heterogeneous data with many attributes and complex graph operations, while RDF graphs are better for homogeneous data with few attributes. 

5. Standardization
  * RDF is based on a solid structure and follows rules set by the World Wide Web Consortium (W3C), while property graphs lack standardization. 

6. Scalability
  * RDF databases are designed to handle large knowledge graphs, while property graphs might face challenges managing and analyzing massive databases. 
  * RDF is a potential candidate to unify property graphs and RDF knowledge graphs. 
