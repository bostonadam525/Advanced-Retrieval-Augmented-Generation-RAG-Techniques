## imports
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
import os 
## setup env
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]="TestProject"

## init llm from groq models
from langchain.chat_models import init_chat_model
llm=init_chat_model("groq:llama-3.3-70b-versatile")

## Create State class
class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

## Function -- make tool graph
def make_tool_graph():
    ## Graph with tool call
    
    @tool
    def add(a:float,b:float):
        """Add two numbers"""
        return a+b
    tools=[add]
    tool_node=ToolNode([add])

    llm_with_tool=llm.bind_tools([add])

    def call_llm_model(state:State):
        return {"messages":[llm_with_tool.invoke(state['messages'])]}


    ## graph builder
    builder=StateGraph(State)
    builder.add_node("tool_calling_llm", call_llm_model)
    builder.add_node("tools",ToolNode(tools))

    ## Add Edges
    builder.add_edge(START, "tool_calling_llm")
    builder.add_conditional_edges(
        "tool_calling_llm",
        # if latest message (result) from assistant is tool call --> tools_condition route
        # if latest message (result) from assistant is not a tool call --> tools_condition
        tools_condition
    )
    builder.add_edge("tools", "tool_calling_llm")

    ## compile graph
    graph=builder.compile()
    return graph

## call function
tool_agent=make_tool_graph()