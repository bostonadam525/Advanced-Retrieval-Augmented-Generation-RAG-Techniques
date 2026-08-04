## TLDR
## This code is from the Weights & Biases short course on agentic engineering.
## This is a simple agent implementation consisting of a loop that
## 1) processes user input, 2) calls the model, and 3) handles the model's output.
## You can also use @weave for agentic traceability using weights and biases.
import json

import weave
from openai import OpenAI

import config
from utils import fn_to_schema, tag

weave.init(project_name=config.WEAVE_PROJECT)

## Agent class with tool definitions
class MiniAgent(weave.Model):

    client: OpenAI = None
    instructions: str = ""
    model: str = "o4-mini"
    tools: dict = {}
    tools_schema: list = []

    def __init__(self, instructions: str, tools: list, model: str = "o4-mini"):
        super().__init__()
        self.client = OpenAI() ## set open AI client
        self.instructions, self.model = instructions, model
        self.tools = {fn.__name__: fn for fn in tools}
        self.tools_schema = [fn_to_schema(fn) for fn in tools]

    # ---------- item handler -------------------------------------------
    # Each part of the model's output is handled here. This function processes reasoning, messages, and function calls.
    # see docs: https://developers.openai.com/api/docs/guides/function-calling
    def _handle_item(self, item):

        if item.type == "reasoning":
            print(tag("reasoning") + "".join(item.summary))
            return []

        if item.type == "message":
            txt = "".join(p.text for p in item.content if p.type == "output_text")
            print(tag("message") + txt + tag("endmessage"))
            return []

        if item.type == "function_call":
            args = json.loads(item.arguments or "{}")
            print(tag("function_call") + f"{item.name}({json.dumps(args)})")
            result = self.tools[item.name](**args) if args else self.tools[item.name]()
            print(tag("function_output") + json.dumps(result))
            return [
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(result),
                }
            ]

        return []
    ## @weave.op() decorator allows for traceability and logging of the function's execution in Weights & Biases.

    @weave.op()
    def _think(self, turn_input, prev_id):
        stream = self.client.responses.create(
                model=self.model,
                instructions=self.instructions,
                tools=self.tools_schema,
                input=turn_input,
                previous_response_id=prev_id,
                stream=True,
            )
        return stream

    # ---------- main loop ----------------------------------------------
    # Main agentic loop that handles user input, calls the model, and processes the output.
    @weave.op()
    def run(self, user_text: str):
        print("Input:", user_text)
        turn_input = [{"role": "user", "content": user_text}]
        prev_id, items = None, []

    # Main agent loop 
        while turn_input:
            stream = self._think(turn_input, prev_id)
            turn_input = []  # collect next‑turn inputs

            for event in stream:
                if event.type == "response.output_item.done":
                    turn_input += self._handle_item(event.item)
                    items.append(event.item)

                if event.type == "response.completed":
                    prev_id = event.response.id

        return {"response": items[-1], "thoughts": items}


@weave.op()
def add(a: int, b: int) -> int:
    """Add two numbers together and return the result."""
    return int(a) + int(b)


@weave.op()
def send_email(to: str, subject: str, body: str):
    """Send an email to the given address with the given subject and body."""
    print(f"Sending email to {to} with subject {subject} and body {body}")


@weave.op()
def run_handmade_agent(input: str):
    tools = [add, send_email]
    agent = MiniAgent(
        instructions="You are a helpful assistant that can handle adding numbers with tool `add`. You can also call the `send_email` tool to send an email.",
        tools=tools,
    )
    return agent.run(input)

if __name__ == "__main__":
    run_handmade_agent("What is 2 + 2?")
    run_handmade_agent("Send an email to John Doe with the subject 'Hello' and body 'How are you?'")
