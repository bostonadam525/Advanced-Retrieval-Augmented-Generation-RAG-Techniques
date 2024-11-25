import csv # to work with csv file
from dotenv import load_dotenv
import os 
from neo4j import GraphDatabase

# load environment variables from .env file
load_dotenv()


# Get env variables --> `.getenv` allows default values, `os.environ` provides a mapping to .env 
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]
NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AUTH=(NEO4J_USERNAME, NEO4J_PASSWORD)


## need a driver for Graph DB
driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)



# 1. Function to connect and run cypher query in NEO4J
def execute_query(driver, cypher_query, parameters=None):
    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            session.run(cypher_query, parameters)
    except Exception as e: 
        print(f"Error: {e}")


# 2. Function to create healthcare provider nodes -- these are based off the CSV column labels
def create_healthcare_provider_node(driver, provider, bio):
    print("Creating healthcare provider node")
    create_provider_query = """
    MERGE (hp:HealthcareProvider {name: $provider, bio: $bio})
    """
    parameters = {"provider": provider, "bio": bio}
    execute_query(driver, create_provider_query, parameters)


# 3. Function to create patient notes -- these are also based off the CSV column labels
def create_patient_node(
        driver, patient, patient_age, patient_gender, patient_condition
):
        # print when creating node
        print("Creating patient node")
        # NE04J cypher query
        create_patient_query = """
        MERGE (p:Patient {name: $patient, age: $patient_age, gender: $patient_gender, condition: $patient_condition})
        """
        parameters = {
             "patient": patient, 
             "patient_age": patient_age,
             "patient_gender": patient_gender,
             "patient_condition": patient_condition,

        }
        execute_query(driver, create_patient_query, parameters)

# 4. Function to create Specialization nodes -- this is a column in CSV file
def create_specialization_node(driver, specialization):
    print("Creating specialization node")
    create_specialization_query = """
    MERGE (s:Specialization {name: $specialization})
    """
    parameters = {"specialization": specialization}
    execute_query(driver, create_specialization_query, parameters)

# 5. Function to create location nodes -- Location is a CSV column
def create_location_node(driver, location):
    print("Creating location node")
    create_location_query = """
    MERGE (l:Location {name: $location})
    """
    parameters = {"location": location}
    execute_query(driver, create_location_query, parameters)


## Function to create relationships in NEO4J 
def create_relationships(driver, provider, patient, specialization, location):
    print("Creating relationships")
    # Create cypher syntax for NE04J queries
    create_relationships_query = """
    MATCH (hp:HealthcareProvider {name: $provider}), (p:Patient {name: $patient})
    MERGE (hp)-[:TREATS]->(p)
    WITH hp
    MATCH (hp), (s:Specialization {name: $specialization})
    MERGE (hp)-[:SPECIALIZES_IN]->(s)
    WITH hp
    MATCH (hp), (l:Location {name: $location})
    MERGE (hp)-[:LOCATED_AT]->(l)
    """
    parameters = {
         "provider": provider, 
         "patient": patient, 
         "specialization": specialization,
         "location": location,
    }
    execute_query(driver, create_relationships_query, parameters)



# Main function to read the CSV file and populate the graph 
def main():
     # init neo4j driver
     driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)
    
    # read and open the CSV file
     with open("healthcare.csv", mode="r") as file:
          reader = csv.DictReader(file) #read as dict 
          print("Reading CSV file...")

          ## loop through CSV file and extract each row[column] to variable
          for row in reader:
               provider = row["Provider"]
               patient = row["Patient"]
               specialization = row["Specialization"]
               location = row["Location"]
               bio = row["Bio"]
               patient_age = row["Patient_Age"]
               patient_gender = row["Patient_Gender"]
               patient_condition = row["Patient_Condition"]


               ## create nodes once data is extracted
               create_healthcare_provider_node(driver, provider, bio)
               create_patient_node(driver, patient, patient_age, patient_gender, patient_condition)
               create_specialization_node(driver, specialization)
               create_location_node(driver, location)
               create_relationships(driver, provider, patient, specialization, location)


# close NEO4J driver once completed
driver.close()
print("Graph populated successfully!")


# Run main function
if __name__ == "__main__":
     main()
