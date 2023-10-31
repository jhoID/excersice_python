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
    # rule 1
    if text.startswith(VOWEL_SOUNDS):
        return text + "ay"

    # rule 3
    if (
        text.startswith(CONSONANT_SOUNDS)
        and text[1:3] == "qu"
        and not text.startswith(DOUBLE_CONSONANT_SOUNDS)
    ):
        return text[3:] + text[:3] + "ay"

    if text.startswith(DOUBLE_CONSONANT_SOUNDS) and text[2:4] == "qu":
        return text[4:] + text[:4] + "ay"

    # Rule 4
    if "y" in text[1:]:
        index = text.find("y")
        consonant_cluster = text[:index]
        return text[index:] + consonant_cluster + "ay"

    # Rule 2
    if text.startswith(CONSONANT_SOUNDS) and not text.startswith(
        DOUBLE_CONSONANT_SOUNDS
    ):
        return text[1:] + text[0] + "ay"

    if text.startswith(DOUBLE_CONSONANT_SOUNDS):
        return text[2:] + text[:2] + "ay"


print(translate("therapy"))
