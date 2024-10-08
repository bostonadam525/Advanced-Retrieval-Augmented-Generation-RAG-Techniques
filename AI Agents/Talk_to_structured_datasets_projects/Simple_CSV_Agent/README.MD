# Talk to CSV Demo App with LangChain, Claude 3 and Streamlit
* Project by Adam Lang
* Date: 10/8/2024

# Steps to duplicate this:
1. Create virtual environment via conda: `conda create -n genai`
2. Activate the virtual env: `conda activate genai`
    * Clear terminal: `cls` for windows, `clear` for macos
3. Create `requirements.txt` file with the following:
    * langchain
    * langchain-experimental
    * langchain-anthropic
    * streamlit

4. Using terminal install the requirements:
    * macOs: `pip3 install -r requirements.txt`
    * windows --> start command with `pip`

5. Create python file for application: `app.py` or any name you wish. 
6. `clear` terminal if needed.
7. Initialize the app in the `app.py file`
    * import streamlit
    * `set_page_config(page_title=")`
    * `header("<name of app>")`
8. Open app in browser to test --> `python3 -m streamlit run app.py`
9. Create upload method for CSV file --> `st.file_uploader()`
10. Create CSV agent to query Pandas dataframe
    * import `create_csv_agent` from langchain_experimental
    * instantiate the agent: `agent = create_csv_agent()`
    * import ChatAnthropic from langchain
    * Insert Anthropic or LLM model name
    * pass CSV file to agent
    * Import `AgentType` from langchain.agents
11. Setup the user input question field
12. Setup streamlit spinner
13. Invoke response from LLM
14. Setup Anthropic API key for LLM access --> .env file
    * Note this step will vary for AWS Bedrock API!
15. Import `dotenv()`