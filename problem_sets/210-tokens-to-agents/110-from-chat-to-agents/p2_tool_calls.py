"""
PROBLEM 2
Practises: pulling the model's requests out of its reply, and running them.

Task: fill in the functions find_tool_calls and run_tool_call.

To check your work, type:
    python p2_tool_calls.py "Which closed higher on 2025-09-10, AAPL or MSFT?"

It should print the model's reply, then what run_tool_call returned for each request find_tool_calls found
(the model runs on your computer: yours may differ a little):
    the model wrote:
    <tool_call>
    {"name": "get_close", "arguments": {"ticker": "AAPL", "date": "2025-09-10"}}
    </tool_call>
    <tool_call>
    {"name": "get_close", "arguments": {"ticker": "MSFT", "date": "2025-09-10"}}
    </tool_call><|im_end|>
    run_tool_call returned:
    <tool_response>
    226.79
    </tool_response>
    <tool_response>
    500.37
    </tool_response>
"""

import json
import re
from pathlib import Path

import pandas as pd


def find_tool_calls(reply: str) -> list[dict]:
    r"""Find the model's requests in its reply.

    Each request is a line of JSON between a <tool_call> line and a </tool_call> line.

    Args:
        reply: the text the model wrote.

    Returns:
        The requests, in order, each read with json.loads. An empty list if there are none.

    Example:
        find_tool_calls('<tool_call>\n{"name": "add", "arguments": {"a": 1, "b": 2}}\n</tool_call><|im_end|>')
    returns
        [{'name': 'add', 'arguments': {'a': 1, 'b': 2}}]
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def run_tool_call(call: dict) -> str:
    r"""Run the function the model asked for, and write its result as the model expects to read it.

    The functions are in TOOLS, below the "do not change" line, by name.

    Args:
        call: one request, as find_tool_calls returns it.

    Returns:
        <tool_response>, the function's result and </tool_response>, each on a line of its own.

    Example:
        run_tool_call({"name": "multiply", "arguments": {"a": 7847, "b": 9283}})
    returns
        '<tool_response>\n72843701\n</tool_response>'
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def get_close(ticker, date):
    prices = pd.read_csv(PRICES)
    row = prices[(prices.ticker == ticker) & (prices.date == date)]
    if len(row) == 0:
        return f"no data for {ticker} on {date}"
    return round(float(row.close.iloc[0]), 2)


TOOLS = {"multiply": multiply, "add": add, "get_close": get_close}

# the lecture's descriptions of the three tools
TOOL_DESCRIPTIONS = [
    {"type": "function", "function": {"name": "multiply", "description": "Multiply two numbers.", "parameters": {
        "type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}}},
    {"type": "function", "function": {"name": "add", "description": "Add two numbers.", "parameters": {
        "type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}}},
    {"type": "function", "function": {"name": "get_close", "description": "Get the closing price of a stock on a date.",
        "parameters": {"type": "object", "properties": {
            "ticker": {"type": "string", "description": "Ticker symbol, for example AAPL"},
            "date": {"type": "string", "description": "Date as YYYY-MM-DD"}}, "required": ["ticker", "date"]}}},
]

MODEL = {}  # loaded the first time model_reply is called


def model_reply(conversation: str) -> str:
    """The lecture's chat model: what it writes to continue the conversation (greedy, at most 200 tokens)."""
    if not MODEL:
        import torch
        import transformers
        from transformers import AutoModelForCausalLM, AutoTokenizer

        torch.set_grad_enabled(False)
        transformers.logging.set_verbosity_error()
        transformers.logging.disable_progress_bar()
        MODEL["tokenizer"] = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
        MODEL["model"] = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
    ids = MODEL["tokenizer"].encode(conversation, return_tensors="pt")
    output = MODEL["model"].generate(ids, max_new_tokens=200, do_sample=False)
    return MODEL["tokenizer"].decode(output[0][len(ids[0]):])


def start_conversation(question: str) -> str:
    """The system prompt with the tools, and the question: as the library writes it."""
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
    return tokenizer.apply_chat_template([{"role": "user", "content": question}], tools=TOOL_DESCRIPTIONS, tokenize=False)


if __name__ == "__main__":
    import sys

    conversation = start_conversation(sys.argv[1]) + "<|im_start|>assistant\n<think>\n\n</think>\n\n"
    reply = model_reply(conversation)
    print("the model wrote:")
    print(reply)
    print("run_tool_call returned:")
    for call in find_tool_calls(reply):
        print(run_tool_call(call))


# NOTES
#   This program follows "Pull the request out of the model's reply" and "Run the function it asked for"
#   in the lecture. TOOLS is a dict of functions: TOOLS["add"] is the function add, so TOOLS["add"](1, 2) is 3.
#   f(**arguments) calls f with the dict's keys as the names of its arguments.
