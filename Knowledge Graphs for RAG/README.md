# Knowledge Graphs for RAG
* This repo will contain all things related to using Knowledge Graphs for Retrieval Augmented Generation.


## What is a Knowledge Graph?
* A **Semantic Network** of real world entities 
* As an example, you can have:
   * Events, Situations, Concepts —> a relationship exists between each of them. 
* NLP has many use cases of KGs in both classical NLP and modern NLP (e.g. Transformers, Generative AI)
   * As an example sentence: “Tom Brady is the captain of the New England Patriots.”
   * We could parse this with NER. model which may be shown as:
      * **Person: Tom Brady**
      * **Role: Captain**
      * **Place: New England**
      * **Team: Patriots**
* However, we know there are specific **semantic relationships** for each of these entities and this is where KG’s come into play.


## 3 Main Components of a Knowledge Graph
1. Nodes
   * Any object, place, person, thing, etc…
   * Usually a Noun

2. Edges
   * Defines relationship between Nodes

3. Labels 
   * While edges represent the connections between nodes, labels describe the type of relationship that exists between them

### Real World Examples of KGs
* Google Search is based on semantic structural relationships as described by KGs.




## How do we represent knowledge graphs in code? 
1. RDF (Resource Description Framework)
2. SPARQL (SPARQL Protocol and RDF Query Language)
3. OWL (Web Ontology Language)
4. Neo4j


# Graph DB Architectures
1. **Property Graphs**
  * nodes and edge relationships 
  * Examples:
      * Neo4j
      * AWS Neptune

2. **RDF (Resource Description Framework) graphs (aka "Triple stores”)**
  * “Subject-Predicate-Object” triple model
  * Most ideal for semantic data integration and knowledge graphs. 
  * Examples of RDF databases:
      * AWS Neptune
      * AllegroGraph
  * Uses SPARQL query language 
  * Triple stores store triples as independent elements, which allows them to scale horizontally but prevents them from rapidly traversing relationships.
      * In order to perform graph queries, triple stores must create connections from individual, independent facts — adding latency to every query.

3. **Hypergraph**
  * Relationships called “hyperedges” can connect any number of given nodes. 
  * Allows for ANY number of nodes at either end of a relationship.



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
