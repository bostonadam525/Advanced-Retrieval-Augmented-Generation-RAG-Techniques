# Resource Description Framework (RDF) Graphs

---
## What is RDF?
* A way to make statements about things such as:
1. Documents
2. Physical Objects
3. People
4. Concepts
5. Data Objects

---
## What is an RDF Statement? 
* The RDF data model is built around "3 part statements" known as **Triples**.
* A set of RDF data is a set of triples.
* Each triple states that a certain resource, for a certain property, has a certain value.
* These three triple states are called:
  1. Subject (e.g. source being described)
  2. Predicate (e.g. relationship)
  3. Object (e.g. the thing related to the Subject)

* Multiple RDF statements are used to make up a **Knowledge Graph**.

---
## Advantages of RDF framework?
1. Consistent framework that encourages the sharing of metadata.
2. A standard syntax and query language capabilities to enable applications to exchange information more easily (e.g. interoperability)
3. Semantic search results are more precise as they are based on metadata.
4. Software agents have more semantic/meaningful data to work with and produce a more meaningful result. 


## Disadvantages of RDF Framework?
1. Standardized vocabulary for RDF resources/statements can often be difficult and time consuming.
2. Choosing the MOST appropriate syntax format takes practice, experience, and often many trials. 
3. Choosing the MOST appropriate query language really depends upon the needs of your application(s).

---
# RDF vs. (Labeled) Property Graphs (LPGS)
* LPGs are the most common alternative to RDF (and W3C standards for storing and using data in graphs).
* The LPG data model is as follows:
  1. Node properties are stored as **key-value pairs with each node**.
  2. Edge properties are stored similarly with each edge.
  3. Before the RDF-star and SPARQL-star extension to the RDF specification, this ability to store edge properties was an advantage of LPGs over the RDF model because earlier RDF syntaxes for representing edge properties were more cumbersome.)
  4. **Two LPG nodes may have multiple instances of the same edge between them.**

## LPG details
* Source: Ontotext

1. If a group of nodes in an LPG represent a set of employees, they can each be assigned a label of "Employee", much like assigning them a type or class membership. This is why these graphs are known as "labeled property graphs".
2. A given node can have multiple labels to indicate that it plays more than one role. (As we'll see, an RDF resource can be an instance of multiple classes.)

3. Instead of URIs, LPGs use internally stored identifiers for their nodes. These are unique within each graph. A given node in one graph may have the same identifier as an unrelated node in another graph, or it may have a different identifier from a node in another graph that represents the same entity.

4. LPG systems include Neo4j and TinkerPop.
   * An open source version of Neo4j's Cypher query language known as openCypher is one of the inputs of the Graph Query Language (GQL) project. (Don't confuse GQL with the JSON-based GraphQL API query language developed at Facebook that we will discuss later in this course.) GQL is now moving through the process of becoming an ISO standard. No corresponding LPG standards are available for representing instance data, data models, or data quality constraints on graph data.


## Advantages of LPGs
* An advantage of LPGs is that it's easier to implement classic computer science graph algorithms such as finding the shortest path between two nodes.
  * This is not part of the SPARQL query language standard, but GraphDB does offer **Graph Path Search extensions to SPARQL.**
  * A related advantage of LPGs for certain applications is **"index-free adjacency"**.
      * This is the ability for an application to **traverse from one node to another WITHOUT relying on an index.**

## Use Cases of LPGs
* Often for use cases requiring **graph traversal and related graph algorithms.**
* The graph model is often developed on a whiteboard as a team decides what should be the nodes, relationships, labels and properties needed in the graph to solve a specific problem.
* Industry and even company standards are less of an issue.
  * The graph data model is optimized for specific queries to address specific use cases. This means it can be deployed very quickly.

# Combining RDF & Property Graphs == Stronger Together!
* The relative strengths of both RDF and LPGs can be complementary.
* Often times when combining both approaches here is what you will do:
  1. Model and integrate data from multiple sources into a knowledge graph using RDF and the related standards
  2. Then export node and edge data to an LPG tool (e.g. Neo4j) to address the types of use cases where LPGs do well.

## Process
1. **RDF Steps**
   * The data cleaning, data wrangling, provenance, governance, entity linkage, entity resolution, entity recognition, and lineage done on the RDF side contribute to higher-quality data being loaded into the LPG tool.
  * In today's LLM world, you can use the `LLMGraphTransformer` from Neo4j/LangChain or the `Property Graph` package from LlamaIndex to build the RDF triples which are then inserted into the LPG or Property graph.

2. **LPG Steps**
* The LPG application can use relevant portions of the ontologies, taxonomies, and controlled vocabularies maintained by the enterprise or their industry in RDF, making the LPG application less of a graph data silo and more interoperable with other data in the enterprise and their industry.
* You can then use specific graph based algorithms to search/query the graph and perform Retrieval Augmented Generation using LLMs among other things. 
  


---
# RDF Graphs -- Open vs. Closed Source

## Open Source
1. GraphDB (Ontotext)
2. rdf4j
3. blazegraph
4. jena

## Closed Source (Paid Alternatives)
1. AllegroGraph
2. Amazon Neptune
3. Stardog
4. Virtuoso


---
# RDF Triples

## What are Triples?
* Give structure to the semantic relationships in an RDF graph.
* Triple statement holds the meaning. 
1. Subject
2. Predicate
3. Object

* Resources
  * These are references in data that link to the Subject, Predicate, Object. 

* Example of a triple in lifesciences, [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5843793/)

![image](https://github.com/user-attachments/assets/663df5ee-ba98-4a38-84ad-0a3a7d75387b)
