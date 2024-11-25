from dotenv import load_dotenv
import os 
from langchain_community.graphs import Neo4jGraph

# load env variables
load_dotenv()


# Get env variables --> `.getenv` allows default values, `os.environ` provides a mapping to .env 
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]
NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AUTH=(NEO4J_USERNAME, NEO4J_PASSWORD)

## instantiate NE04J graph instance
kg = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    database=NEO4J_DATABASE,
)

# simple cypher query
cypher = """
MATCH (n)
RETURN count(n) as numberOfNodes
"""

## get result of query
result = kg.query(cypher)
print(f"There are {result[0]['numberOfNodes']} nodes")


## Match only Provider nodes specify count
cypher = """
MATCH (n:HealthcareProvider)
RETURN count(n) AS numberOfProviders
"""
## get result
res = kg.query(cypher)
print(f"There are {res[0]['numberOfProviders']} Healthcare Providers in this graph.")


## Return names of healthcare providers
cypher = """
MATCH (n:HealthcareProvider)
RETURN n.name AS ProviderName
"""
## get result
res = kg.query(cypher)
print("Healthcare Providers:")
for r in res: 
    print(r["ProviderName"])

## list all patients in graph
cypher = """
MATCH (n:Patient)
RETURN n.name AS PatientName
LIMIT 10
"""
## get result
res = kg.query(cypher)
print("Patients:")
for r in res: 
    print(r["PatientName"])

## list all medical specializations in the graph
cypher = """
MATCH (n:Specialization)
RETURN n.name as SpecializationName
"""
## get result
res = kg.query(cypher)
print("Medical Specializations:")
for r in res: 
    print(r["SpecializationName"])


## get locations
cypher = """
MATCH (n:Location)
RETURN n.name AS LocationName
"""
## get result
res = kg.query(cypher)
print("Provider Location: ")
for r in res:
    print(r["LocationName"])

## list all patients treated by speficic provider
cypher = """
MATCH (hp:HealthcareProvider {name: 'Dr. Smith'})-[:TREATS]->(p:Patient)
RETURN p.name AS PatientName
"""
## get results
res = kg.query(cypher)
print("Patients treated by Dr. Smith: ")
for r in res:
    print(r["PatientName"])