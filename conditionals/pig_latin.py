VOWEL_SOUNDS = (
    "a",
    "e",
    "i",
    "o",
    "u",
    "xr",
    "yt",
)

CONSONANT_SOUNDS = (
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
)

DOUBLE_CONSONANT_SOUNDS = (
    "ch",
    "sh",
    "st",
    "th",
    "ph",
    "gh",
    "kn",
    "wr",
    "wh",
    "ng",
    "qu",
    "ck",
)

TRIPLE_CONSONANT_SOUNDS = ("thr", "sch")


def translate(text):
    result = ''
    list_text = text.split(' ')
    def translate_word(word):
        # Rule 1
        if text.startswith(VOWEL_SOUNDS):
            return text + "ay"

        # Rule 2
        if text.startswith(TRIPLE_CONSONANT_SOUNDS):
            if text[4:6] == "qu":
                return text[6:] + text[:6] + "ay"
            return text[3:] + text[:3] + "ay"

        if text.startswith(DOUBLE_CONSONANT_SOUNDS):
            if text[2:4] == "qu":
                return text[4:] + text[:4] + "ay"
            return text[2:] + text[:2] + "ay"

        if text.startswith(CONSONANT_SOUNDS):
            if text[1:3] == "qu":
                return text[3:] + text[:3] + "ay"
            # Rule 3
            if "y" in text[1:]:
                index = text.find("y")
                consonant_cluster = text[:index]
                return text[index:] + consonant_cluster + "ay"
            return text[1:] + text[:1] + "ay"

    for word in list_text:
        result += translate_word(word) + ' '
    return result

print(translate("quick fast run"))
