# Setup for running code for Agents in LangGraph 


## Project setup
- Make sure that you have uv package manager installed: https://github.com/astral-sh/uv
- Create a directory for the project (e.g. mdkir)
- run in terminal: `uv init` --> sets up packages.
- create `requirements.txt` with dependencies
- create venv: `uv venv` --> automatically sets up the `venv`
- activate venv with: source .venv/bin/activate
- install requirements: `uv add -r requirements.txt`
- make sure to run: uv add ipykernel (if using jupyter notebooks for experiments, etc.)
- lastly, make sure to choose your kernel. 
