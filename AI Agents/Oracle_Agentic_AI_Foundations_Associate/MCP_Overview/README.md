# MCP (Model Context Protocol) - Overview
- What is MCP protocol?
- MCP core components
- How to use MCP with agentic workflows

---
# What is Model Context Protcol?
- MCP is an open standard that provides a universal interface for AI apps to connect with external tools, data sources, and systems -- securely and consistently. 
- MCP details:
    - Anthropic released in November 2024.
    - AI ecosystem supports: AWS, OpenAI, Oracle, Microsoft.
    - Foundation is built upon JSON-RPC 2.0 which is open source. [See this source](https://kovashikawa.github.io/ai/mcp-notes/)
    - RPC stands for "remote procedure call".
    - MCP is considered a "common language" that is governed by the Agentic AI foundation (Linux Foundation)
    - MCP is often compared to a "USB Port" meaning it can plug into any computer or API. 

## Problem MCP Solves
- Prior to MCP, every LLM or AI application needed a custom connector for every single tool it used which scales significantly and is not efficient. 
    - This is depicted as: `N x M problem`.
    - Quadratic complexity.

- With MCP we now have a `N + M solution`
    - Each side builds ONLY ONE MCP integration.
    - So if you have 3 separate LLM apps they all connect to the SAME MCP server which then calls multiple tools. 
    - Each tool exposes 1 MCP server that is standard and accessible. 
    - This improves efficiency significantly!

---
# MCP Architecture
1. MCP host
    - examples: Claude desktop, VS code, or any AI enable application.
    - LLM model within host (e.g. Claude, GPT, Gemini)
    - **KEY: 
2. MCP Client
    - LLM model reads 1 or more MCP clients.
    - **KEY: Any client can connect to ANY server.**
    - Each client maintains a dedicated connection with 1 MCP server. As an example:
        - MCP client 1 -> MCP server file system
        - MCP client 2 -> MCP server GitHub API
        - MCP client 3 -> MCP server Slack
3. MCP server
    - Expose tools, data, and prompts.
    - Communication via JSON-RPC 2.0.
    - Servers can run locally or remotely.

---
# MCP Core Components
- All MCP servers expose 3 types of primitives as we see below. 
- Important distinction: most of the time when people are talking about MCPs they are talking about tools, however, it is important to remember the 2 other aspect of an MCP. 

1. Tools - Do Something
    - Functions the AI model can call to perform actions.
    - **Do something:** POST endpoints -- execute code and produce side effects.
    - Examples:
    ```
    create_issue()
    send_message()
    query_database()
    run_test()

    ```
2. Resources - Read Something
    - Application-controlled.
    - Structured data the AI model can read for context.
    - **Read Something:** such as GET endpoins they will load info into the LLM's context window.
    - examples:
    ```
    file://project/readme.md
    db://users/schema
    api://config/settings

    ```
3. Prompts - Structure Something
    - User-controlled.
    - Templates that structure LLM interactions.
    - **Structure something:** such as slash commands -- users invoke them through UI elements.
    - examples:
    ```
    bug_report_template
    code_review_prompt
    summarize_doc_template

    ```

## MCP Connection Lifecycle
- There are generally 4 phases:

1. **Initialize**
    - client sends protocol version & capabilities to server.
    - "handshake" happens here between client + server to initialize action.

2. **Discover**
    - client requests list of tools, resources, prompts
    - Server responds with schemas.

3. **Operate**
    - LLM decides which tools to call --> client executes those calls against server.

4. **Shutdown**
    - Client closes transport and ends session.

## MCP uses JSON-RPC 2.0
- **Important distinction:** unlike REST which is primarily designed for client to server request, JSON-RPC 2.0 supports bi-directional communication.
- JSON-RPC 2.0 is a structured way to make requests and receive responses.
- JSON-RPC 2.0 includes:
    - **jsonrpc**(always "2.0").
    - **id**(used to match requests and responses, when applicable).
    - One of:
        - **method**(request)
        - **result**(success)
        - **error** (failure)
- However, in most cases frameworks like LangChain or FastMCP will handle this for you -- but understanding the structure helps with debugging.

## Key methods for MCP tools

1. MCP Method #1: tools/list
    - usually called when client connects to discover available tools.
    - server returns every tool it offers in a list -- this lets it understand what tools it has available!
    - agent discovers tools without you hardcoding them.
    - Example: **Request (client -> server)**
    ```
    {
    "jsonrpc": "2.0"
    "id": 1,
    "method": "tools/list"
    }
    ```
    - That is it. No parameters are needed. The request is simply: "Tell me what you have."

    - **Response (server -> client)
        - You don't have to hardcode tools! 
        - The tools are already there! 

2. MCP Method #2: tools/call
    - Called each time LLM decides it needs a tool.
    - Includes tool name and arguments.
    - LLM decides to call tool based on user's request and available tool descriptions.

## MCP Transport Mechanisms
- This is the reason why JSON-RPC was chosen so there are multiple transport mechanisms.

1. **STDIO Transport**
    - **This is the simplest process. Server must be installed locally though.**
    - Host spawns server as child process.
    - Messages flow through stdin / stdout
    - No network overhead -- fastest option
    - Server runs on same machine.
    - One client per server instance.
    - Best for local tools (files, git, shell, etc.)
    ```
    Client  stdin -> Server
            <- stdout
    ```

2. **Streamable HTTP Transport**
    - **Server runs non local as an HTTP service.**
    - **This is newer as of March 2025 for remote servers.**
    - Client -> Server via HTTP POST
    - Server -> Client via SSE streaming
    - Supports remote / cloud deployment
    - Multiple clients can connect
    - Standard HTTP auth (OAuth, tokens)
    ```
    Client POST-> Server
           <-SSE 

    ```