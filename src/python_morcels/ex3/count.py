# ex1
def count_words1(str):
    word_count = {}
    for word in str.split():
        count = word_count.get(word.lower(), 0)
        word_count[word.lower()] = count + 1
    return word_count


# ex2 - sloweest performance o(n^2)
def count_words2(str):
    words = str.split()
    return dict((w, words.count(w) for w in words))


# ex3
def count_words3(str):
    counts = {}
    for word in str.split():
        counts.setdefault(word, 0)
        counts[word] += 1
    return counts


# ex4
def count_words4(str):
    words = str.split()
    counts = dict.fromkeys(words, 0)
    for word in words:
        counts[word] += 1
    return counts


# ex5
from collections import defaultdict


def count_words5(str):
    counts = defaultdict(int)
    for word in str.split():
        counts[word] += 1
    return dict(counts)


# ex6
from collections import Counter
import re


def count_words6(string):
    return Counter(re.findall(r"\b[\w'-]+\b+", string.lower()))


print(count_words3("Oh what a day what a lovely day"))
print(count_words2("Oh what a day what a lovely day"))
print(count_words6("Oh what a day, what a lovely day!"))
