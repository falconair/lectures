"""
PROBLEM 2
Practises: the generation loop: take the most likely word, add it to the text, ask again.

Task: fill in the function generate.

To check your work, type these two commands:
    python p2_generate.py "thou art more lovely and more temperate"
    python p2_generate.py "look in thy glass and tell the face thou viewest"

They should print the text, then | and the words generate returned (the first
stops after 15 words, the second because the next word was "."):
    thou art more lovely and more temperate | rough winds do i am not to the world will be the world will be
    look in thy glass and tell the face thou viewest | now is but that thou art
"""

import re
import sys
from pathlib import Path

import numpy as np

# sonnets.txt sits in the same folder as this file, wherever you run it from
SONNETS = Path(__file__).parent / "sonnets.txt"


def generate(words: list[str], max_new_words: int) -> list[str]:
    """Continue a text one word at a time, always taking the most likely next word.

    Real models seldom take the most likely word every time: problem 3 shows the
    more realistic way, rolling the dice for each word.

    Give the model the whole text so far with next_word_scores(words), take the
    word with the highest score (decode turns its number back into the word),
    add it to the end of the text, and ask the model again. Stop when the word
    is "." (do not add it), or when max_new_words words have been added.

    Args:
        words: the text to continue, as a list of words.
        max_new_words: the most words to add.

    Returns:
        The words that were added, in order (without the text you were given).

    Example:
        generate(["look", "in", "thy", "glass", "and", "tell", "the", "face", "thou", "viewest"], 15)
    returns
        ['now', 'is', 'but', 'that', 'thou', 'art']
    because the model's next word after "art" was ".".
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
# A stand-in for the language model, so that nothing has to be downloaded. Its
# tokens are words, and it looks only at the last word of the text: the score
# of each word is the log of how many times it came right after that word in
# sonnets.txt (the first 60 of Shakespeare's sonnets), and -inf if it never did.


def words_of(text: str) -> list[str]:
    """The words of a text in lower case; '.', '?' and '!' all become the word '.'."""
    text = text.lower().replace("?", ".").replace("!", ".")
    return re.findall(r"[a-z']+|\.", text)


def load_model() -> tuple[list[str], dict[str, dict[str, int]]]:
    """Return the vocabulary and, for each word, how often each other word followed it."""
    words = words_of(SONNETS.read_text())
    follows: dict[str, dict[str, int]] = {}
    for word, next_word in zip(words, words[1:]):
        counts = follows.setdefault(word, {})
        counts[next_word] = counts.get(next_word, 0) + 1
    return sorted(set(words)), follows


def next_word_scores(text_words: list[str]) -> np.ndarray:
    """The model: one score for every word it knows (score i is the score of word number i)."""
    vocabulary, follows = load_model()
    scores = np.full(len(vocabulary), -np.inf)
    for word, count in follows.get(text_words[-1], {}).items():
        scores[vocabulary.index(word)] = np.log(count)
    return scores


def decode(number: int) -> str:
    """The word with that number, like tokenizer.decode in the lecture."""
    vocabulary, _ = load_model()
    return vocabulary[number]


if __name__ == "__main__":
    _, follows = load_model()
    text_words = words_of(sys.argv[1])
    if text_words[-1] not in follows:
        sys.exit(f"the sonnets never use the word {text_words[-1]!r}: try another one")
    new_words = generate(text_words, 15)
    print(sys.argv[1], "|", " ".join(new_words))


# NOTES
#   This program follows "Pick a token, add it to the text, ask again" in the lecture.
#   next_word_scores and decode are below the "do not change" line: they stand in for
#   the lecture's model and tokenizer.decode. Call them like any other function.
