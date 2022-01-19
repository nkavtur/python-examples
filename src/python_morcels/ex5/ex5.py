import string
import sys
import unicodedata
from collections import Counter


# way1
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    letters2 = {*str2.lower()}
    return all(letter in letters2 for letter in str1.lower())


# way2
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    letters1 = {*str1.lower()}
    letters2 = {*str2.lower()}
    return letters1 == letters2


# way3
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


# way4
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(is_anagram("tea", "eat"))
print(is_anagram("tea", "treat"))
print(is_anagram("sinks", "skin"))
print(is_anagram("Listen", "silent"))


# bonus 1
# way1
def is_anagram(str1, str2):
    str1 = re.sub("\s+", "", str1)
    str2 = re.sub("\s+", "", str2)

    return Counter(str1) == Counter(str2)


# way2
def is_anagram(str1, str2):
    return letters_in(str1) == letters_in(str2)


def letters_in(string):
    return sorted(
        char
        for char in string.lower()
        if char.isalpha()
    )


print(is_anagram("coins kept", "in pockets"))


# bonus 2
# way1
def is_anagram(str1, str2):
    str1 = re.sub("[^\w]", "", str1.lower())
    str2 = re.sub("[^\w]", "", str2.lower())
    return Counter(str1) == Counter(str2)


# way2
def is_anagram(str1, str2):
    str1 = str1.lower().translate(str.maketrans("", "", string.punctuation))
    str2 = str2.lower().translate(str.maketrans("", "", string.punctuation))
    return Counter(str1) == Counter(str2)


is_anagram("a diet", "I'd eat")


# bonus 3
# way1
def is_anagram(str1, str2):
    str1 = re.sub("[^\w]", "", unicodedata.normalize("NFD", str1.lower()))
    str2 = re.sub("[^\w]", "", unicodedata.normalize("NFD", str2.lower()))
    return Counter(str1) == Counter(str2)


import re

# way2 (removing non-english punctuation)

tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                    if unicodedata.category(chr(i)).startswith('P'))


def is_anagram(str1, str2):
    str1 = remove_punctuation(unicodedata.normalize("NFD", str1.lower().replace(' ', '')))
    str2 = remove_punctuation(unicodedata.normalize("NFD", str2.lower().replace(' ', '')))
    return Counter(str1) == Counter(str2)


def remove_punctuation(text: str):
    return text.translate(tbl)


print(is_anagram("cardiografía", "radiográfica"))
