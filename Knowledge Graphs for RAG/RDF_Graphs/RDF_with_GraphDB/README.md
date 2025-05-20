# RDF with GraphDB
* RDF Frameworks using GraphDB from Ontotext.



# RDF Triples Basic Workflow
1. Create new repository.
2. Three options to load RDF Files
   * Upload RDF files
   * Get RDF data from URL
   * Import RDF data from a text snippet --> this is how you define your Triple schema.
  
## Import RDF data from text snippet
* Creating RDF Triples

1. First we define a URI. This can be anything it does not have to exist as it is local.
   * Example: `<https://mymovies.com/data#
     * In this URI we have the domain/data/
     * Then with the `#` or `/` we add fragments for Triples --> Subject, Predicate, Object
     * Subject example: `<https://mymovies.com/data#KingdomOfHeaven>`
     * Predicate example: `<https://mymovies.com/concepts
       * domain is different here `concepts` -- Predicates are used more often so want it to be different.
     * Object example: `<https://mymovies.com/data#OrlandoBloom>` --- we only change the fragment
     * All triples need to end with this: `.`
  * Full example as Subject --- Predicate --- Object
       * `<https://mymovies.com/data#KingdomOfHeaven><https://mymovies.com/concepts#hasActor><https://mymovies.com/data#OrlandoBloom>.`


2. Import Triples into graph
   * Need to define which graph to import. A "default graph" is created when you build your triples. 
     a. From data
     b. The default graph -- This isn't an ideal name for a graph
     c. Named graph -- Define your own graph name, usually same as for Subjects and Objects above.
       * Here is example for name based on Subject & Object schema: `https://mymovies.com/data`
       * The resulting triple looks like this:

         ![image](https://github.com/user-attachments/assets/0453a675-b4d7-404f-b4fb-c3368337c4c9)

3. Visualize Triples
   * You can drill into each triple within the database as you see above.
   * You can also visualize the triples such as this:

   ![image](https://github.com/user-attachments/assets/c2b4f405-269b-4b7b-820b-23aca614a925)


## RDF Namespaces
* Here is how to think of namespaces
1. URIs (Uniform Resource Identifiers):
  * These are long, complex addresses that uniquely identify things in the web. They can be difficult to read and use. 

2. Namespaces:
  * A namespace provides a shortcut.
  * You can use a short, human-readable prefix (like foaf:) to represent the full URI (like http://xmlns.com/foaf/0.1/). 
  * Here's how namespaces work in RDF:
    1. Namespace Declaration:
      * You declare a namespace with a prefix (like xmlns:foaf) and its corresponding URI (like http://xmlns.com/foaf/0.1/).
    2. Using the Prefix:
      * You can then use the prefix in RDF statements to refer to elements within that namespace (e.g., foaf:name).
    3. Benefits:
      * Clarity: Makes it easier to understand the context of RDF statements.
      * Readability: Reduces the clutter of long URIs.
      * Consistency: Ensures that the same prefix always refers to the same URI.
      * Organization: Helps group related data together. 

## How to Create a namespace
* You can do this using turtle syntax.
* Here are the steps:
1. Go to VS Code and open a new folder.
2. Create a file such as: `data.ttl` --> `ttl` is turtle
3. Now, instead of using the long Subject-Object-Predicate such as this: 
`data:KingdomOfHeaven <https://mymovies.com/data#KingdomOfHeaven> <https://mymovies.com/concepts#hasActor> data:OrlandoBloom <https://mymovies.com/data#OrlandoBloom> .`
4. Instead, we can perform a semantic mapping using the `@predicate` prefix:

```
@prefix data: <https://mymovies.com/data#> .
@prefix concepts: <https://mymovies.com/concepts#> .

data:KingdomOfHeaven concepts:hasActor data:OrlandoBloom

data:OrlandoBloom concepts:isFrom data:UK .

data:OrlandoBloom concepts:hasOccupation concepts:Actor .

```

5. Now we can upload the Namespace turtle file mapping to the RDF triplestore GraphDB.
   * Simply upload RDF turtle file and make sure it is in the same Named Graph: `https://mymovies.com/data`

6. Now we can see the mapping that we did is in the graph as triples:

![image](https://github.com/user-attachments/assets/e65540a3-ae75-4349-ade4-d92667332214)


7. We can also visualize this:

![image](https://github.com/user-attachments/assets/55aae77d-96e0-4a95-b109-6b59a2d6de4c)

