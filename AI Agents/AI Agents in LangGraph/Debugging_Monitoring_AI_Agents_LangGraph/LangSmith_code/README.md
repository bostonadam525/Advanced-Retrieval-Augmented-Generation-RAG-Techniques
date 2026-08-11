# LangSmith Code
- Using LangSmith to debug and trace agent tool calls and workflows.
- This demonstrates how to do this 2 ways as we see below.

## 1. Run agentic tool calls in notebook --> monitor tracing in LangSmith UI
- See .ipynb file above.
- Make sure you have uv installed to run `uv add -r requirements.txt`
- Example of tracing in LangSmith:

<img width="1294" height="726" alt="image" src="https://github.com/user-attachments/assets/7c2cbe8d-c31d-4dc8-bc63-71d5831132b3" />




## 2. Run agent.py file --> monitor tracing in LangGraph Studio
- Similar approach to above but uses agents.py file.
- To launch the LangGraph studio run in CLI/terminal: langgraph dev
- Example of tracing using the studio:

<img width="1293" height="691" alt="image" src="https://github.com/user-attachments/assets/5547e7bc-c4e8-43e6-88d8-dffb6327fce3" />
