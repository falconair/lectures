"""
PROBLEM 3
Practises: temperature, and rolling the dice for each next word, as real models do.

Task: fill in the functions temperature_probabilities and generate_with_temperature.

To check your work, type these two commands:
    python p3_temperature.py "thou art more lovely and more temperate" 0.2
    python p3_temperature.py "thou art more lovely and more temperate" 1.8

They should print the text, then what generate_with_temperature returned when it
was called three times. At 0.2 the model keeps to its most common words; at 1.8 it
picks rare ones:
    temperature 0.2: thou art more lovely and more temperate | ...
        rough winds do but that thou art
        rough winds do but thou art
        rough winds do i am debarred the world will be the world
    temperature 1.8: thou art more lovely and more temperate | ...
        rough winds do allow for whether revolution be outstripped by thy abundance
        rough winds do contend
        rough winds do allow for thee one shade shines so wary as
"""

import re
import sys
from pathlib import Path

import numpy as np

# sonnets.txt sits in the same folder as this file, wherever you run it from
SONNETS = Path(__file__).parent / "sonnets.txt"


def temperature_probabilities(scores: np.ndarray, temperature: float) -> np.ndarray:
    """Turn the model's scores into probabilities at a temperature.

    Divide every score by the temperature, then apply softmax: the probability
    of word i is exp(scores[i] / temperature) divided by the sum of that over
    all the scores. Below 1 the likely words get more likely; above 1 the
    unlikely words get a bigger share.

    Args:
        scores: one score per word of the vocabulary.
        temperature: a number above 0. At 1 the probabilities are the plain softmax.

    Returns:
        The probability of each word; they add up to 1.

    Example:
        temperature_probabilities(np.array([1.0, 3.0, 2.0]), 0.5)  # the scores of "cat", "dog" and "fish"
    returns
        array([0.01587624, 0.86681333, 0.11731043])
    Plain softmax (temperature 1) gives "dog" 0.665; at temperature 0.5 it gets 0.867.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def generate_with_temperature(
    words: list[str], max_new_words: int, temperature: float
) -> list[str]:
    """Continue a text one word at a time, rolling the dice for each word.

    The same loop as generate in problem 2, except how the next word is picked:
    turn the model's scores, next_word_scores(words), into probabilities with
    temperature_probabilities, then roll DICE (below the "do not change" line)
    to pick the number of the next word, each number as often as its
    probability says; decode turns it into the word. Stop when the word is "."
    (do not add it), or when max_new_words words have been added.

    Args:
        words: the text to continue, as a list of words.
        max_new_words: the most words to add.
        temperature: a number above 0, passed to temperature_probabilities.

    Returns:
        The words that were added, in order (without the text you were given).

    Example:
        generate_with_temperature(["thou", "art", "more", "lovely", "and", "more", "temperate"], 12, 0.2)
    returns, the first time the program calls it,
        ['rough', 'winds', 'do', 'but', 'that', 'thou', 'art']
    and other words the next time, because the dice have rolled on.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
# A stand-in for the language model, so that nothing has to be downloaded. Its
# tokens are words, and it looks only at the last word of the text: the score
# of each word is the log of how many times it came right after that word in
# sonnets.txt (the first 60 of Shakespeare's sonnets), and -inf if it never did.

# the dice: a random number generator that rolls the same numbers each time the program runs
DICE = np.random.default_rng(0)


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
    """The model: one score for every word of the vocabulary."""
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
    temperature = float(sys.argv[2])
    print(f"temperature {temperature}: {sys.argv[1]} | ...")
    for attempt in range(3):
        print("   ", " ".join(generate_with_temperature(text_words, 12, temperature)))


# NOTES
#   This program follows "Why does the same question get different answers?" in the lecture.
#   DICE.choice(n, p=probabilities) picks a number from 0 to n - 1: number i with
#   probability probabilities[i], as torch.multinomial(probs, 1) did in the lecture.
#   next_word_scores and decode are below the "do not change" line, as in problem 2.
