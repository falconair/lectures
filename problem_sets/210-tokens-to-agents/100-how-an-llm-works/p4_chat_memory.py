"""
PROBLEM 4
Practises: the chat format, and chat memory: the whole conversation is sent on every turn.

Task: fill in the functions chat_prompt and chat_with_memory.

To check your work, type:
    python p4_chat_memory.py

It should print the length of each prompt chat_with_memory sent, then the last one:
    characters sent: 116, 278, 420
    the last prompt:
    <|im_start|>user
    My name is Marge and I own 100 shares of Apple.<|im_end|>
    <|im_start|>assistant
    Great to meet you! Marge, you own 100 shares of Apple.<|im_end|>
    <|im_start|>user
    How many shares do I own, and of which company?<|im_end|>
    <|im_start|>assistant
    You own **100 shares** of **Apple**.<|im_end|>
    <|im_start|>user
    I just bought 50 more. How many do I own now?<|im_end|>
    <|im_start|>assistant
    <think>

    </think>
"""


def chat_prompt(messages: list[dict[str, str]]) -> str:
    r"""Write a conversation out in the chat format, ending with an open assistant turn.

    Each message becomes one turn: <|im_start|>, the role, a new line, the
    content, <|im_end|> and a new line. After the last turn comes the start of
    an assistant turn for the model to continue, with an empty thinking block,
    exactly as in the example (\n is a new line).

    Args:
        messages: the conversation so far, in order. Each message is a dict
            with the keys "role" ("system", "user" or "assistant") and "content".

    Returns:
        The text to send to the model.

    Example:
        chat_prompt([{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": "What is a bond?"},
                     {"role": "assistant", "content": "A loan."},
                     {"role": "user", "content": "And a stock?"}])
    returns this text, written here one turn per line (Python joins strings
    written side by side into one):
        ('<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n'
         '<|im_start|>user\nWhat is a bond?<|im_end|>\n'
         '<|im_start|>assistant\nA loan.<|im_end|>\n'
         '<|im_start|>user\nAnd a stock?<|im_end|>\n'
         '<|im_start|>assistant\n<think>\n\n</think>\n\n')
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def chat_with_memory(questions: list[str]) -> list[str]:
    """Ask the model the questions one after the other, in a chat that remembers.

    For each question: add it to the conversation as a user message, send the
    whole conversation to the model as one prompt (made with chat_prompt), and
    add the model's answer, reply(prompt), to the conversation as an assistant
    message.

    Args:
        questions: what the user types, in order.

    Returns:
        The prompts sent to the model, one per question, in order.

    Example:
        prompts = chat_with_memory(QUESTIONS[:2])
        print(prompts[1])
    prints
        <|im_start|>user
        My name is Marge and I own 100 shares of Apple.<|im_end|>
        <|im_start|>assistant
        Great to meet you! Marge, you own 100 shares of Apple.<|im_end|>
        <|im_start|>user
        How many shares do I own, and of which company?<|im_end|>
        <|im_start|>assistant
        <think>

        </think>
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
QUESTIONS = [
    "My name is Marge and I own 100 shares of Apple.",
    "How many shares do I own, and of which company?",
    "I just bought 50 more. How many do I own now?",
]

# A stand-in for the chat model, so that nothing has to be downloaded: the replies
# Qwen3-0.6B wrote to these questions in the lecture (shortened), in order.
RECORDED_REPLIES = [
    "Great to meet you! Marge, you own 100 shares of Apple.",
    "You own **100 shares** of **Apple**.",
    "You now own **150 shares** of Apple.",
]


def reply(prompt: str) -> str:
    """The stand-in model: the recorded reply to the last question in the prompt."""
    return RECORDED_REPLIES[prompt.count("<|im_start|>user") - 1]


if __name__ == "__main__":
    prompts = chat_with_memory(QUESTIONS)
    print("characters sent:", ", ".join(str(len(prompt)) for prompt in prompts))
    print("the last prompt:")
    print(prompts[-1], end="")


# NOTES
#   This program follows "The chat format, piece by piece" and "Chat memory" in the lecture.
#   reply is below the "do not change" line: it stands in for the lecture's chat model.
#   Call it like any other function.
#   With the lecture's real model, chat_with_memory is what turns 2_chat_without_memory.py
#   into a chat that remembers.
