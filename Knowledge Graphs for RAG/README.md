# Knowledge Graphs for RAG
* This repo will contain all things related to using Knowledge Graphs for Retrieval Augmented Generation.


## Comparison of RDBMS (Relational Databases) vs. Graph DBs

### RDBMS                          
1. Tables are created               
2. Insert Records —> Rows           
3. Data —> Columns, values          
4. Constraints                      
  * Primary key                     
  * Foreign key                    
  * Candidate key                  
5. Join Queries           


### Graph DBs
1. Graphs are created
2. Nodes are “records"
3. Data —> Properties and Values
4. Constrains are “Relationships”
   * e.g. Tesla —> owned —> Elon Musk
5. Traversal queries 

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
1. **Nodes**
   * Any object, place, person, thing, etc…
   * Usually a Noun

2. **Edges or Relationships**
   * Defines relationship between Nodes.
   * Relationships can be **Unidirectional** and/or **Bidirectional**

3. **Labels or Properties**
   * While edges represent the connections between nodes, labels describe the type of relationship that exists between them.
   * Properties usually have **key-value pairs**.

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
      * **Neo4j**
          * **Advantages of Neo4j**
              * Flexible schemas is a major advantage!
              1. Graph Data Model —> Nodes, Relationships, Properties and Values
              2. Real time insights immediately when graphs are created
              3. Easy Retrieval —> using Cypher queries 
              4. Cypher query language —> “Declarative” query language to represent the graph visually 
                  a. Cypher has human readable queries
              5. NO JOINS ARE NECESSSARY like in RDMBMS or SQL DBs 
              6. ACID — supported in Neo4j (as well as RDBMS)
                  * Atomicity 
                  * Consistency
                  * Isolation
                  * Durability 

      * AWS Neptune
   
  * Example of Property Graph (source: Neo4j - https://neo4j.com/blog/rdf-vs-property-graphs-knowledge-graphs/)

![image](https://github.com/user-attachments/assets/ad0ccc7c-e7d3-4004-b6e6-c78fbf79f23d)





2. **RDF (Resource Description Framework) graphs (aka "Triple stores”)**
  * “Subject-Predicate-Object” triple model
  * Most ideal for semantic data integration and knowledge graphs. 
  * Examples of RDF databases:
      * AWS Neptune
      * AllegroGraph
  * Uses SPARQL query language 
  * Triple stores store triples as independent elements, which allows them to scale horizontally but prevents them from rapidly traversing relationships.
      * In order to perform graph queries, triple stores must create connections from individual, independent facts — adding latency to every query.
   
  * Example of RDF graph model (source: Neo4j article above)

![image](https://github.com/user-attachments/assets/9a459f91-3cf6-4829-8980-522ec81749b4)


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
