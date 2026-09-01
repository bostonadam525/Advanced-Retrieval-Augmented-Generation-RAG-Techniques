# Dev environment setup
- Need to get API keys from

1. OpenAI
2. platform.claude.com
3. Gemini
4. Groq

- The point is that you can call any foundation model API so pick your model of choice.

---
# RAG in Production with LangChain

---
## Basic Setup

### Setup UV
- If you need to install uv in your local or working environment then follow directions here: https://github.com/astral-sh/uv

- To setup `uv` in the project run: `uv init`

### Create venv
- Run in shell: `uv venv`

### Activate venv
- Creating virtual environment at: .venv
- Activate with: `source venv/Scripts/activate`


### Install Packages
- Run: uv add langchain langchain-core langgraph langchain-openai langchain-anthropic langchain-groq python-dotenv 
- You can also use the requirements.txt file: `uv add -r requirements.txt`

### Create API keys
- create `.env` file: touch .env
- add foundation model API keys

### Create `main.py` file
- run: `main.py`

### To run .py files
- You should be able to run: `uv run main.py`
- However, that may not work depending upon your operating system. So if it doesn't then simply use: `python3 main.py`
