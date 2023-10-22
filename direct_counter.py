from string import punctuation
from collections import Counter
from pathlib import Path


def words_count(text: str) -> dict:
    text_low = text.lower()
    for ch in punctuation:
        text_word = text_low.replace(ch, "")

    dict_count = Counter(text_word)
    return dict_count.most_common(1)


path = Path("text_to_check.txt")
if path.exists():
    f = open("text_to_check.txt", "r")
    text = f.read()
    f.close()
else:
    print("Check your text file ")

result = words_count(text)
with open("results.txt", "w") as file:
    for letter, freq in result:
        print("The most common letter is:", file=file)
        print(letter, freq, file=file)