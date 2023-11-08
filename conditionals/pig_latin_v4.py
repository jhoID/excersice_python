VOWEL_SOUNDS = {"a", "e", "i", "o", "u"}
SPECIAL_SOUNDS = {"xr", "yt"}


def translate(text):
    translated_text = []
    for word in text.split():
        if word[0] in VOWEL_SOUNDS or word[0:2] in SPECIAL_SOUNDS:
            translated_text.append(word + "ay")
            continue

        for i in range(1, len(word)):
            if word[i] in VOWEL_SOUNDS or word[i] == "y":
                i += 1 if word[i - 1 : i + 1] == "qu" else 0
                translated_text.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(translated_text)
