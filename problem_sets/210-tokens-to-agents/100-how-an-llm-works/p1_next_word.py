"""
PROBLEM 1
Practises: turning a model's scores into probabilities, and listing the likely next words.

Task: fill in the functions softmax and top_words.

To check your work, type:
    python p1_next_word.py "and this gives life to"

It should print how many probabilities softmax returned and their sum, then
what top_words returned. The stand-in model looks only at the last word, "to":
    1790 probabilities, one per word of the vocabulary, adding up to 1.000
    the 5 most likely next words after "to":
        the      0.064
        thee     0.058
        be       0.045
        my       0.038
        his      0.026
"""

import re
import sys
from pathlib import Path

import numpy as np

# sonnets.txt sits in the same folder as this file, wherever you run it from
SONNETS = Path(__file__).parent / "sonnets.txt"


def softmax(scores: np.ndarray) -> np.ndarray:
    """Turn a score for every word of the vocabulary into a probability for every word.

    The probability of word i is exp(scores[i]) divided by the sum of the exp of
    every score. A higher score gives a higher probability, and the
    probabilities add up to 1.

    Args:
        scores: one score per word of the vocabulary (the model's output).

    Returns:
        An array of the same length: the probability of each word.

    Example:
        softmax(np.array([1.0, 3.0, 2.0]))  # the scores of "cat", "dog" and "fish"
    returns
        array([0.09003057, 0.66524096, 0.24472847])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def top_words(
    probabilities: np.ndarray, vocabulary: list[str], n: int
) -> list[tuple[str, float]]:
    """Return the n most likely next words, the most likely first.

    Args:
        probabilities: the probability of each word; probabilities[i] is the
            probability of vocabulary[i].
        vocabulary: every word the model knows.
        n: how many words to return.

    Returns:
        A list of n (word, probability) pairs, the highest probability first.

    Example:
        top_words(np.array([0.09003057, 0.66524096, 0.24472847]), ["cat", "dog", "fish"], 2)
    returns
        [('dog', 0.66524096), ('fish', 0.24472847)]
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
    """The model: one score for every word of the vocabulary."""
    vocabulary, follows = load_model()
    scores = np.full(len(vocabulary), -np.inf)
    for word, count in follows.get(text_words[-1], {}).items():
        scores[vocabulary.index(word)] = np.log(count)
    return scores


if __name__ == "__main__":
    vocabulary, follows = load_model()
    text_words = words_of(sys.argv[1])
    if text_words[-1] not in follows:
        sys.exit(f"the sonnets never use the word {text_words[-1]!r}: try another one")
    probabilities = softmax(next_word_scores(text_words))
    print(
        f"{len(probabilities)} probabilities, one per word of the vocabulary, adding up to {probabilities.sum():.3f}"
    )
    print(f'the 5 most likely next words after "{text_words[-1]}":')
    for word, probability in top_words(probabilities, vocabulary, 5):
        print(f"    {word:8} {probability:.3f}")


# NOTES
#   This program follows "Tokens in, a score for every possible next token out" in the lecture.
#   np.exp(a) is exp of every value of the array a; a.sum() adds them up.
#   Not in the lecture (it used torch.topk): np.argsort(a) gives the positions of a's
#   values from the smallest to the largest, so np.argsort(-a) from the largest.
