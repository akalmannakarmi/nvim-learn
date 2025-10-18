# Write a Python program that reads a text file and prints out the top 5 most frequent words along with their counts.

from typing import Dict


def find_word_use_count(text: str) -> Dict[str, int]:
    words = text.split(" ")
    wordCounts = {}

    for word in words:
        if word not in wordCounts:
            wordCounts[word] = 0
        wordCounts[word] += 1

    return wordCounts


def run() -> None:
    with open("./challege/c1.txt") as f:
        text = f.read()

    wordCounts = find_word_use_count(text)

    topWordCounts = sorted(wordCounts.items(), key=lambda item: item[1], reverse=True)

    for word, count in topWordCounts[:5]:
        print(f"{word}\t{count}")


if __name__ == "__main__":
    run()
