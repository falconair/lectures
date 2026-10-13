# A language model is an autocomplete. Type the start of a text and it continues it.
#
# To run it, type:      python 1_autocomplete.py
# To stop, press Enter on an empty line.
#
# Things to try:
#   Stocks fell sharply on Monday as investors
#   Why do bond prices fall when interest rates rise?      (it will not answer!)
#   The same text twice. Do you get the same continuation?

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

torch.set_grad_enabled(False)
transformers.logging.set_verbosity_error()

print("Loading the base model...")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B-Base")
model     = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B-Base")
streamer  = TextStreamer(tokenizer, skip_prompt=True)

while True:
    text = input("\nstart of a text> ")
    if text == "":
        break

    ids = tokenizer.encode(text, return_tensors="pt")
    model.generate(ids, max_new_tokens=60, do_sample=True, streamer=streamer)
