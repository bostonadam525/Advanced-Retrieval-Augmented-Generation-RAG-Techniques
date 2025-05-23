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


## RDF Types
* Types are used to state a resource is an instance of a class.
* Instance --> `a / rdf:type` --> Class
* Here is an example:
  * Instead of this: `data:OrlandoBloom concepts:hasOccupation concepts:Actor .`
  * We write this: `data:OrlandoBloom a concepts:Actor .
  * However, the `a` syntax is not ideal. This is why `rdf:type` is more often used instead.
    * It will look like this: `data:OrlandoBloom rdf:type concepts:Actor .
  * Here is a full example with `rdf:type`. Notice we added the 3rd `@prefix` line with specific syntax. We also added `rdf:type` to take the place of any previous `concepts:` where Typing would be more semantically better. 

```
@prefix data: <https://mymovies.com/data#> .
@prefix concepts: <https://mymovies.com/concepts#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

data:KingdomOfHeaven concepts:hasActor data:OrlandoBloom .

data:OrlandoBloom concepts:isFrom data:UK .

data:OrlandoBloom rdf:type concepts:Actor .

data:OrlandoBloom concepts:actsAs data:Balian .

data:Balian rdf:type concepts:Blacksmith .

data:KingdomOfHeaven rdf:type concepts:Movie . 

data:KingdomOfHeaven concepts:hasRole data:Balian . 
```
* This is what results, we can see there are 2 predicates assigned though, so we will have to remove the `hasOccupation` predicate to use the more semantically friendly `type`.

![image](https://github.com/user-attachments/assets/8305634f-a467-4608-b908-b1c2ee1b0c48)

* To fix this we have to re-import to the turtle file as seen here, we can rename the graph if we want but I will keep the same:

![image](https://github.com/user-attachments/assets/266492a0-fb28-4d4d-86c3-0fe7e9dd7cf3)

* Now we can see we ONLY have `rdf:type` as the semantic relationship:

![image](https://github.com/user-attachments/assets/45c4ab1b-a5fb-4584-acb3-63929cd23e07)


## Turtle Syntax
* Best practice is to structure turtle code. These are a few important pieces of turtle syntax we will see:
1. Use semicolons to end multiline statements `;`
2. Nested related statements are better than multiple single line statements.
3. When using a comma at the end of the statement the next statement is focused on the current predicate.
4. Comments are made with a `#` just like in Python or other similar languages.
* Instead of 3 unique statements as we see below:

```
data:KingdomOfHeaven concepts:hasActor data:OrlandoBloom .
data:KingdomOfHeaven rdf:type concepts:Movie . 
data:KingdomOfHeaven concepts:hasRole data:Balian . 
```

* A Better syntax is this nested hierarchical structure:
  * What we can see is we added `rdf:type` and semicolons `;` after each statement.
  * We also nested the concepts within the original statement so concepts are inherited from `rdf:type`
  * We also end the statement on a new line with a period `.`

```
# This is a great movie 
data:KingdomOfHeaven rdf:type concepts:Movie ;
                     concepts:hasRole data:Balian ,
                                      data:Sybilla , 
                                      data:Baldwin , 
                                      data:Saladin ;
                     concepts:hasActor data:OrlandoBloom ;       
```
