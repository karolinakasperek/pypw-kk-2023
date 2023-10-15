from string import punctuation
from collections import Counter
from pathlib import Path


def words_count(text:str) -> dict:
    text_low = text.lower()
    for ch in punctuation:
        text_low = text_low.replace(ch, "")
    text_word = text_low.split()

    dict_count = Counter(text_word)
    # dict_count = defaultdict(int)
    #
    # for word in text_word:
    #     dict_count[word] += 1
    return dict_count


path = Path("text_to_check.txt")
if path.exists():
    f = open("text_to_check.txt", "r")
    text = f.read()
    f.close()
    print(text)
else:
    print("Check your text file ")

result = words_count(text)
print(result)
