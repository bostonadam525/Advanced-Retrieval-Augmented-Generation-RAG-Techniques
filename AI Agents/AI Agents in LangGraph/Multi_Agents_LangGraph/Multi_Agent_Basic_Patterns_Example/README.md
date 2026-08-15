# Multi Agents in LangGraph - Basic Patterns Examples
- This is example of 3 basic multi agent patterns in LangGraph

1. Simple multi-agent
2. Supervise multi-agent
3. Simple Hierarchical Multi-agent


---
# AI Agents in LangGraph

## How to get started
1. Make sure that uv is installed in your workspace. Go to the github and follow install: https://github.com/astral-sh/uv

2. setup uv: `uv init`

3. create venv: uv venv

4. activate venv: `.venv\Scripts\activate`

5. Set up requirements.txt file with libraries.

6. install the libraries with uv: `uv add -r requirements.txt`


---
# Important Notes
- From the project folder:
- If you want to add packages to the project metadata instead of just installing into the venv:
- Do not use:
    - for this project unless you intentionally want uv to interpret the file as a project dependency list. For a requirements file, uv pip install -r requirements.txt is the safer command.
    - Also, the warning about VIRTUAL_ENV not matching .venv is just because your shell was using a different active environment. Activating the project venv as shown above resolves that.

## Recommended final state
- Use this pattern:
    - Project dependency management: uv add ...
    - Environment install: `uv pip install -r requirements.txt`
    - Python version: 3.11 for LangGraph/LangSmith compatibility


## venv pattern
- use this pattern every time: 
```
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -U pip ipykernel
python -m ipykernel install --user --name "myproj-311" --display-name "Python 3.11 (MyProj)"
```
