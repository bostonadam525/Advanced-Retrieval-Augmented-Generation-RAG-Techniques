# Neo4j project directions
1. Setup `.env` file with neo4j credentials.
2. Create virtual environment using: `python -m venv <name of venv>`
3. Activate venv: `source venv/bin/activate`
4. Install dependencies:
    * `pip install neo4j`
    * `pip install python-dotenv`
    * Can also just put this in a `requirements.txt` file
        * To run this: `pip install -r requirements.txt`
5. Create .py file: `kg_simple.py`
    * See this file for details.


To deactivate the virtual environment run this: `deactivate`


-------
# To view entire graph in NEO4J once built
* Run this cypher query:
    * `MATCH (n)-[r]->(m)`
    * `RETURN n, r, m;`

# Simple Cypher query to find all node names
simple_query = """
MATCH (n)
RETURN n.name AS name
"""

# More Complex Cypher Query
## More advanced/complex query to find paths related to Albert Einstein
einstein_query = """
MATCH path=(a:Person {name: 'Albert Einstein'})-[:STUDIED]->(s:Subject)
RETURN path
UNION 
MATCH path=(a:Person {name: 'Albert Einstein'})-[:WON]->(n:NobelPrize)
RETURN path
UNION
MATCH path=(a:Person {name: 'Albert Einstein'})-[:BORN_IN]->(g:Country)
RETURN path
UNION
MATCH path=(a:Person {name: 'Albert Einstein'})-[:DIED_IN]->(u:Country)
RETURN path
"""
