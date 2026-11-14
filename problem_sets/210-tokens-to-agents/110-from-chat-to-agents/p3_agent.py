"""
PROBLEM 3
Practises: the agent loop: let the model write, run what it asks for, paste the result back, until it answers.

Task: fill in the function agent. It uses your find_tool_calls and run_tool_call from problem 2.

To check your work, type:
    python p3_agent.py "What was the closing price of AAPL on 2025-09-10?" "And of MSFT?"

It should print each question, what each tool the model asked for returned, and the model's answer
(the model runs on your computer: yours may differ a little):
    you>   What was the closing price of AAPL on 2025-09-10?
    tool>  226.79
    model> The closing price of AAPL on 2025-09-10 was $226.79.
    you>   And of MSFT?
    tool>  500.37
    model> The closing price of MSFT on 2025-09-10 was $500.37.
"""

from p2_tool_calls import find_tool_calls, run_tool_call  # your answers to problem 2


def agent(conversation: str) -> str:
    """Let the model work on the last question in the conversation until it answers without asking for a tool.

    Repeat at most MAX_STEPS times: add to the conversation an open assistant
    turn (ASSISTANT, below the "do not change" line), then model_reply(conversation)
    and a new line, and find the tool calls in that reply. If there are none, stop.
    Otherwise run each one and add a user turn holding the results, one per
    line, exactly as in the example.

    Args:
        conversation: the conversation so far, ending with the user's question.

    Returns:
        The conversation with everything the loop added.

    Example:
        A conversation ending with the question "What is 7847 * 9283?" has this added:
        <|im_start|>assistant
        <think>

        </think>

        <tool_call>
        {"name": "multiply", "arguments": {"a": 7847, "b": 9283}}
        </tool_call><|im_end|>
        <|im_start|>user
        <tool_response>
        72843701
        </tool_response><|im_end|>
        <|im_start|>assistant
        <think>

        </think>

        The product of 7847 and 9283 is 72843701.<|im_end|>
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
import re  # noqa: E402

from p2_tool_calls import model_reply, start_conversation  # noqa: E402  (the lecture's model, as in problem 2)

ASSISTANT = "<|im_start|>assistant\n<think>\n\n</think>\n\n"
MAX_STEPS = 5


def ask(conversation: str, question: str) -> str:
    """Add a question to the conversation (starting one if there is none yet), let agent answer, and show what it did."""
    if conversation == "":
        conversation = start_conversation(question)  # the system prompt with the tools, and the question
    else:
        conversation += f"<|im_start|>user\n{question}<|im_end|>\n"
    before = len(conversation)
    conversation = agent(conversation)
    added = conversation[before:]
    for result in re.findall("<tool_response>\n(.*?)\n</tool_response>", added):
        print("tool> ", result)
    print("model>", added.rsplit("</think>\n\n", 1)[-1].removesuffix("\n").removesuffix("<|im_end|>"))
    return conversation


if __name__ == "__main__":
    import sys

    conversation = ""
    if len(sys.argv) > 1:  # the questions on the command line, in turn
        for question in sys.argv[1:]:
            print("you>  ", question)
            conversation = ask(conversation, question)
    else:  # a chat
        question = input("you>   ")
        while question != "":
            conversation = ask(conversation, question)
            question = input("you>   ")


# NOTES
#   This program follows "Put it in a loop: that is an agent" in the lecture, and is the program its
#   "Problem set" box asks for: type   python p3_agent.py   with no question to chat with your agent
#   (an empty line stops it).
#   model_reply is the lecture's model, imported from problem 2. Call it like any other function.
