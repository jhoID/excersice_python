ENGLISH_LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]


def is_pangram(sentence):
    result = False
    if len(sentence) < 26:
        return False
    for letter in ENGLISH_LETTERS:
        if letter in sentence or letter.upper() in sentence:
            result = True
        else:
            return False
    return result