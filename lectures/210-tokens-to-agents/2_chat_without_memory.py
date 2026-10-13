# A chat with no memory: every question is sent to the model on its own.
#
# To run it, type:      python 2_chat_without_memory.py
# To stop, press Enter on an empty line.
#
# Things to try, one after the other:
#   My name is Marge and I own 100 shares of Apple.
#   How many shares do I own, and of which company?

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

torch.set_grad_enabled(False)
transformers.logging.set_verbosity_error()

print("Loading the chat model...")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
model     = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
streamer  = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

while True:
    question = input("\nyou> ")
    if question == "":
        break

    # The text the model continues: this one question, and nothing else.
    prompt = f"<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"

    ids = tokenizer.encode(prompt, return_tensors="pt")
    model.generate(ids, max_new_tokens=300, do_sample=False, streamer=streamer)
