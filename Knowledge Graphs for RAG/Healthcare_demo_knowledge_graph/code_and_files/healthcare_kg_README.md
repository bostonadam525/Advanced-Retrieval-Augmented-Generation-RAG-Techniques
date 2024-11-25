# Neo4j project directions
1. Setup `.env` file with neo4j credentials.
2. Create virtual environment using: `python -m venv <name of venv>`
    * In this case we named the venv: `healthvenv`
3. Activate venv: `source healthvenv/bin/activate`
4. Install dependencies:
    * `pip install neo4j`
    * `pip install python-dotenv`
    * `pip install csv`
    * Can also just put this in a `requirements.txt` file
        * To run this: `pip install -r requirements.txt`
5. Create .py file: `kg_simple.py`
    * See this file for details.


To deactivate the virtual environment run this: `deactivate`

--------
* To run the app run this in virtual env: `python3 healthcare_kg.py`

------------------------
# Information about the `healthcare.csv` file
* This is a simple `.csv` file that represents a healthcare provider with their metadata such as:
    * location
    * specialty
    * location
    * Patient name
    * Patient age
    * Condition
    * ...etc...

# How we are creating the entities and nodes in the knowledge graph
* Note: These are the COLUMNS in the CSV file. 
* Step 1: Define Entities and Relationships for healthcare provider
    * Entities: 
        * Provider 
        * Patient 
        * Specialization 
        * Location 


    * Relationships:

        * TREATS
        * SPECIALIZES_IN
        * LOCATED_AT

* Step 2: Define entities and relationships between Patient columns in the CSV file
    * Patient
    * Patient_Age
    * Patient_Gender
    * Patient_Condition

* Step 3: Define entities and relationsips between Specialization nodes in CSV column
    * Specialization

* Step 4: Same as above, but for Location node CSV column
    * Location


# Now create relationships between each CSV column
* To do this use cypher language.

# Then create a MAIN function to read the CSV file 

----------------
To view the entire graph we created in NEO4J run this code: `MATCH (n)-[r]->(m) RETURN n, r, m`
