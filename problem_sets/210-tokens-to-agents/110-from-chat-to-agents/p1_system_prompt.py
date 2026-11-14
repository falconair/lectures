"""
PROBLEM 1
Practises: describing a function as data, and putting the descriptions into a system prompt.

Task: fill in the functions describe_tool and tools_system_prompt.

To check your work, type:
    python p1_system_prompt.py

It should print the system prompt tools_system_prompt returned, then whether the library writes the same:
    # Tools

    You may call one or more functions to assist with the user query.

    You are provided with function signatures within <tools></tools> XML tags:
    <tools>
    {"type": "function", "function": {"name": "multiply", "description": "Multiply two numbers.", "parameters": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}}}
    {"type": "function", "function": {"name": "get_close", "description": "Get the closing price of a stock on a date.", "parameters": {"type": "object", "properties": {"ticker": {"type": "string"}, "date": {"type": "string"}}, "required": ["ticker", "date"]}}}
    </tools>

    For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
    <tool_call>
    {"name": <function-name>, "arguments": <args-json-object>}
    </tool_call>

    the library writes the same text: True
"""

import json


def describe_tool(name: str, description: str, arguments: dict[str, str]) -> dict:
    """Describe a function as data, in the form the model was trained on.

    Every argument is required, and each one is described only by its type.

    Args:
        name: the function's name.
        description: what the function does, in one sentence.
        arguments: each argument's name and its type ("number" or "string"), in order.

    Returns:
        The description, a dict like multiply_tool in the lecture.

    Example:
        describe_tool("multiply", "Multiply two numbers.", {"a": "number", "b": "number"})
    returns
        {'type': 'function', 'function': {'name': 'multiply', 'description': 'Multiply two numbers.',
         'parameters': {'type': 'object', 'properties': {'a': {'type': 'number'}, 'b': {'type': 'number'}},
         'required': ['a', 'b']}}}
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def tools_system_prompt(tools: list[dict]) -> str:
    """Write the system prompt that tells the model which tools it has and how to ask for one.

    The prompt is BEFORE_TOOLS, then each description written out with
    json.dumps on a line of its own, then AFTER_TOOLS. Both are below the
    "do not change" line; they are the lecture's wording.

    Args:
        tools: the descriptions, as describe_tool returns them.

    Returns:
        The text of the system prompt.

    Example:
        print(tools_system_prompt([describe_tool("add", "Add two numbers.", {"a": "number", "b": "number"})]))
    prints
        # Tools

        You may call one or more functions to assist with the user query.

        You are provided with function signatures within <tools></tools> XML tags:
        <tools>
        {"type": "function", "function": {"name": "add", "description": "Add two numbers.", "parameters": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}}}
        </tools>

        For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
        <tool_call>
        {"name": <function-name>, "arguments": <args-json-object>}
        </tool_call>
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
BEFORE_TOOLS = """# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
"""

AFTER_TOOLS = """</tools>

For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call>"""

QUESTION = "What is 7847 * 9283?"


if __name__ == "__main__":
    from transformers import AutoTokenizer

    tools = [
        describe_tool("multiply", "Multiply two numbers.", {"a": "number", "b": "number"}),
        describe_tool("get_close", "Get the closing price of a stock on a date.", {"ticker": "string", "date": "string"}),
    ]
    system_prompt = tools_system_prompt(tools)
    print(system_prompt)

    # what the lecture's library writes for the same tools and question ("The library we are using does what we did by hand")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
    by_library = tokenizer.apply_chat_template([{"role": "user", "content": QUESTION}], tools=tools, tokenize=False)
    by_hand = f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{QUESTION}<|im_end|>\n"
    print()
    print("the library writes the same text:", by_library == by_hand)


# NOTES
#   This program follows "The second fix: let the model ask for what it needs" in the lecture.
#   The check loads the lecture's tokenizer (no model), so it needs transformers.
