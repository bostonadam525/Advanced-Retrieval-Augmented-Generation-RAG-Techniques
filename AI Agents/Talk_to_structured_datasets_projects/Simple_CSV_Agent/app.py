import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_anthropic import ChatAnthropic
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv

##load dotenv for environment variables API access keys
load_dotenv()

## set page config
st.set_page_config(page_title="Talk to your CSV")

## set header
st.header("Talk to your CSV")

## CSV upload method
csv_file = st.file_uploader("Upload a CSV file", type="csv")

## initialize CSV pandas agent from langchain
if csv_file is not None:
    ## create csv_agent
    agent = create_csv_agent(
        ChatAnthropic(
            model_name='claude-3-haiku-20240307' ## pass LLM model name
        ),
        csv_file, ## pass it csv file
        verbose = True, 
        agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION, ## AgentType
    )

    ## text input method
    user_question = st.text_input("Ask a question about your CSV: ")

    ## setup spinner method
    if user_question is not None and user_question != "":
        with st.spinner(text = "In progress..."):
        ## run agent
            response = agent.invoke(user_question) ##invoke query to LLM
            st.write(response['output']) ##print output

