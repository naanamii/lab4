from collections import Counter
import re

text = input("Введите текст: ")

words = re.findall(r'\w+', text.lower())

word_counts = Counter(words)

sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word)