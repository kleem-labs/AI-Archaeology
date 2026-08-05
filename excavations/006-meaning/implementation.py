"""Build word-context counts from a tiny corpus."""

from collections import Counter, defaultdict


def tokenize(sentence):
    return sentence.lower().replace(".", "").split()


def context_counts(sentences, window=2):
    """Return nearby-word frequencies for every word."""
    counts = defaultdict(Counter)
    for sentence in sentences:
        words = tokenize(sentence)
        for index, word in enumerate(words):
            start = max(0, index - window)
            end = min(len(words), index + window + 1)
            counts[word].update(words[start:index] + words[index + 1:end])
    return counts


if __name__ == "__main__":
    corpus = [
        "the cat drinks milk",
        "the dog drinks water",
        "the cat is a quiet pet",
        "the dog is a loyal pet",
        "a kitten is a young cat",
    ]
    counts = context_counts(corpus)
    for word in ("cat", "dog", "milk"):
        print(f"{word:>4}:", counts[word].most_common())
