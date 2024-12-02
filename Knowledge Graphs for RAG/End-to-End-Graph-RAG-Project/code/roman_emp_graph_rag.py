from dotenv import load_dotenv
import os 
from langchain_community.graphs import Neo4jGraph

#langchain imports
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field #pydantic
from typing import Tuple, List
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
import os 
from langchain_community.graphs import Neo4jGraph #NEO4J import
from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import TokenTextSplitter #text splitter
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer

## vector store imports
from langchain_community.vectorstores import Neo4jVector #Graph embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
)

load_dotenv()

# Get env variables --> `.getenv` allows default values, `os.environ` provides a mapping to .env 
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]
NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AUTH=(NEO4J_USERNAME, NEO4J_PASSWORD)

## setup OPENAI environment vars
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_ENDPOINT = os.environ["OPENAI_ENDPOINT"]

## init ChatOpenAI instance --> this is the LLM we are using
chat = ChatOpenAI(api_key=OPENAI_API_KEY,
                  temperature=0, #deterministic
                  model="gpt-3.5-turbo", #llm
                  )

## init NEO4J 
kg = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    database=NEO4J_DATABASE,
)

# 1. Read in data --> wikipedia page for Roman Empire
# raw_documents = WikipediaLoader(query="The Roman empire").load()
# print(raw_documents)

# # 2. Chunk documents -- using text splitter
# text_splitter = TokenTextSplitter(chunk_size=512, #adjust this
#                                   chunk_overlap=24,
#                                   )
# # Define chunking strategy --> chunk & split docs
# documents = text_splitter.split_documents(raw_documents[:3])
# print(documents)

# # 3. Use LLMGraphTransformer -- extract graph data & generate KG
# ## from langchain_experimental --> may move langchain APIs in future

# ## first we init the llm_transformer
# llm_transformer = LLMGraphTransformer(llm=chat)

# ## then we extract the data --> convert into graph_documents
# graph_documents = llm_transformer.convert_to_graph_documents(documents)

# 4. store extracted graph_documents in NE04J graph DB
# res = kg.add_graph_documents(
#     graph_documents,
#     include_source=True, #links each node to original document
#     baseEntityLabel=True, #assigns entity labels to nodes
# )


# 5. Hybrid Retrieval for RAG
## Create vector index
vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(), #embeddings
    search_type="hybrid", 
    node_label="Document", 
    text_node_properties=["text"],
    embedding_node_property="embedding",
)

# 6. Create Graph Retriever
kg.query("CREATE FULLTEXT INDEX entity IF NOT EXISTS FOR (e:__Entity__) ON EACH [e.id]")

## Base class to Extract entities from text
## can make this more complex as needed
class Entities(BaseModel):
    """Identifying information about entities."""

    names: List[str] = Field(
        ...,
        description="All the person, organization, or business entities that"
        "appear in the text",
    )
## create prompt to extract entities from text
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your are extracting organization and person entities from the text.",
        ),
        (
            "human",
            "Use the given format to extract information from the following "
            "input: {question}",
        ),
    ]
)
## create chain with LCEL syntax
entity_chain = prompt | chat.with_structured_output(Entities)

## test it out
res = entity_chain.invoke({"question": "In the year of 123 there was an emperor who did not like to rule."}).names
# print(res)

# 7. Function to generate full text queries to map to knowledge graph
def generate_full_text_query(input: str) -> str:
    """
    Generate a full-text search query for a given input string.

    This function constructs a query string suitable for a full-text search.
    It processes the input string by splitting it into words and appending a
    similarity threshold (~2 changed characters) to each word, then combines
    them using the AND operator. Useful for mapping entities from user questions
    to database values, and allows for some misspellings.
    """
    full_text_query = ""
    words = [el for el in remove_lucene_chars(input).split() if el]
    for word in words[:-1]:
        full_text_query += f" {word}~2 AND"
    full_text_query += f" {words[-1]}~2"
    return full_text_query.strip()


## Fulltext index query
def structured_retriever(question: str) -> str:
    """
    Collects the neighborhood of entities mentioned
    in the question.
    """
    result = ""
    entities = entity_chain.invoke({"question": question})
    for entity in entities.names:
        #print(f" Getting Entity: {entity}")
        response = kg.query(
            """CALL db.index.fulltext.queryNodes('entity', $query, {limit:2})
            YIELD node,score
            CALL {
              WITH node
              MATCH (node)-[r:!MENTIONS]->(neighbor)
              RETURN node.id + ' - ' + type(r) + ' -> ' + neighbor.id AS output
              UNION ALL
              WITH node
              MATCH (node)<-[r:!MENTIONS]-(neighbor)
              RETURN neighbor.id + ' - ' + type(r) + ' -> ' +  node.id AS output
            }
            RETURN output LIMIT 50
            """,
            {"query": generate_full_text_query(entity)},
        )
        # print(response)
        result += "\n".join([el["output"] for el in response])
    return result


print(structured_retriever("Who is Commodus?"))

# 8. Final Retrieval Step
## Combine: Graph & Unstructured data --> RAG-LLM pipeline

def retriever(question: str):
    """Function that retrieves Stuctured Graph Data 
    and Unstructured Vector DB data and joins information
    into final retrieval relevan context for LLM to generate answer.
    """
    print(f"Search query: {question}")
    structured_data = structured_retriever(question)
    unstructured_data = [
        el.page_content for el in vector_index.similarity_search(question)
    ]
    final_data = f"""Structured data:
{structured_data}
Unstructured data:
{"#Document ". join(unstructured_data)}
    """
    print(f"\nFinal Data::: ==>{final_data}")
    return final_data


# 9. Define the RAG chain
# Condense a chat history and follow-up question into a standalone question
_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question,
in its original language.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""  # noqa: E501
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)


## Function to format chat history
def _format_chat_history(chat_history: List[Tuple[str, str]]) -> List:
    buffer = []
    for human, ai in chat_history:
        buffer.append(HumanMessage(content=human))
        buffer.append(AIMessage(content=ai))
    return buffer


_search_query = RunnableBranch(
    # If input includes chat_history, we condense it with the follow-up question
    (
        RunnableLambda(lambda x: bool(x.get("chat_history"))).with_config(
            run_name="HasChatHistoryCheck"
        ),  # Condense follow-up question and chat into a standalone_question
        RunnablePassthrough.assign(
            chat_history=lambda x: _format_chat_history(x["chat_history"])
        )
        | CONDENSE_QUESTION_PROMPT
        | ChatOpenAI(temperature=0)
        | StrOutputParser()
    ),
    # Else, we have no chat history, so just pass through the question
    RunnableLambda(lambda x: x["question"]),
)

# 10. Completes RAG chain
template = """Answer the question based only on the following context:
{context}

Question: {question}
Use natural language and be concise.
Answer:"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    RunnableParallel(
        {
            "context": _search_query | retriever,
            "question": RunnablePassthrough(),
        }
    )
    | prompt
    | chat # llm we are using
    | StrOutputParser()
)

# # TEST it all out!
# res_simple = chain.invoke(
#     {
#         "question": "How did the Roman empire fall?",
#     }
# )

# print(f"\n Results === {res_simple}\n\n")

## chat history test with follow up questions
res_hist = chain.invoke(
    {
        "question": "When did he become the first emperor?",
        "chat_history": [
            ("Who was the first emperor?", "Augustus was the first emperor.")
        ],
    }
)

print(f"\n === {res_hist}\n\n")