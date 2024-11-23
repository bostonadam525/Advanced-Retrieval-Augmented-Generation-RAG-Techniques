from dotenv import load_dotenv
import os 
from neo4j import GraphDatabase
load_dotenv()

## environment variables
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]
NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AUTH=(NEO4J_USERNAME, NEO4J_PASSWORD)

## need a driver for Graph DB
driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)


## Function to load driver and query graph database
def connect_and_query():
    # driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH, database=NEO4J_DATABASE)
    try: 
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run("MATCH (n) RETURN count(n)") #cypher query
            count = result.single().value() #get a single result
            print(f"Number of nodes: {count}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.close()


## run connect and query function
#connect_and_query()

## Create KG programatically
# 1. Create entities function
def create_entities(tx):
    # create Albert Einstein node using Cypher query
    tx.run("MERGE (a: Person {name: 'Albert Einstein'})")

    # create other nodes
    tx.run("MERGE (p:Subject {name: 'Physics'})")
    tx.run("MERGE (n:NobelPrize {name: 'Nobel Prize in Physics'})")
    tx.run("MERGE (g: Country {name: 'Germany'})")
    tx.run("MERGE (u: Country {name: 'USA'})")


# 2. Create Relationships in KG
def create_relationships(tx):
    # create studied relationship with NODE + EDGE
    tx.run(
        """
    MATCH (a: Person {name: 'Albert Einstein'}), (p:Subject {name: 'Physics'})
    MERGE (a)-[:STUDIED]->(p)

        """
    )
    # Create born in relationship with NODE + EDGE
    tx.run(
        """
    MATCH (a:Person {name: 'Albert Einstein'}), (g:Country {name:'Germany'})
    MERGE (a)-[:BORN_IN]->(g)
        """
    )

    # Create died in relationship NODE + ENTITY
    tx.run(
        """ 
    MATCH (a:Person {name: 'Albert Einstein'}), (u:Country {name: 'USA'})
    MERGE (a)-[:DIED_IN]->(u)

        """
    )


# 3. Function to connect and run simple Cypher query in NEO4J
def query_graph_simple(cypher_query):
    driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)
    try: 
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run(cypher_query)
            for record in result: 
                print(record["name"])
    except Exception as e: 
        print(f"Error: {e}")
    finally:
        driver.close()

# 4. Function to connect and run a Cyper query in NEO4J
def query_graph(cypher_query):
    driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)
    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run(cypher_query)
            for record in result: 
                print(record["path"]) #print path/relationship
    except Exception as e: 
        print(f"Error: {e}")
    finally:
        driver.close()

# 4. Function to Build knowledge graph in NEO4J
def build_knowledge_graph():

    try: 
        # open NEO4J session
        with driver.session(database=NEO4J_DATABASE) as session:
            # create entities in graph 
            session.execute_write(create_entities)
            # create relationships in graph 
            session.execute_write(create_relationships)

    except Exception as e: 
        print(f"Error: {e}")
    finally:
        driver.close()


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

## Simple Cypher query to find all node names
simple_query = """
MATCH (n)
RETURN n.name AS name
"""

# 5. MAIN function
if __name__ == "__main__":

    # 1. build knowledge graph
    #build_knowledge_graph()

    # 2. simple query function
    #query_graph_simple(
       # simple_query
    #) # this will return all paths related to Albert Einstein

    # 3. more advanced query graph
    query_graph(einstein_query)


