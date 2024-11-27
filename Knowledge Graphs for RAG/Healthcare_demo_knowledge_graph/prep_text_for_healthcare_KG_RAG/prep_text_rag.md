# Prep text for RAG 
* To prept text for RAG to use for a knowledge graph. 
* Same steps as previously done, we will still list them below. 
* The purpose is so that we can use the unstructured vectorized text to query the KG and the vectors at the same time which we will demonstrate in another project. 
* This is just one more important piece of the pipeline.


1. We need to create a virtual environment. 
    * run this code to create venv: `python -m venv <name venv>`
    * activate venv with this code: `source ragvenv/bin/activate` #based off what i named it
2. Setup requirements.txt file
    * install the file using: `pip install -r requirements.txt`
3. We need to init the env variables in `app.py` file.
4. The `app.py` file is where all the steps will take place:
    * 1. Setup vector index in neo4j
    * 2. Test to see if index was created
    * 3. Create embeddings and populate the index in NEO4J
    * 4. Run cypher query to check if embeddings and index were created properly.
    * 5. Now you can perform semantic queries via the stored vector index and embedding in NEO4J. This is an isolated step in the RAG pipeline.
        * To do this we come up with a natural language question.
        * Then we execute a cypher query using the question. 
    * 6. We can then print the semantic query result with similarity score.