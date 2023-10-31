def translate_to_pig_latin(word):
    # Regla 1: Palabra comienza con vocal o 'xr' o 'yt'
    if word[0] in "aeiou" or word[:2] in ["xr", "yt"]:
        return word + "ay"

    # Regla 3: Palabra comienza con consonante + 'qu'
    if word[:2] == "qu":
        return word[2:] + "quay"

    # Regla 4: Palabra contiene 'y' después de un grupo de consonantes
    if "y" in word[1:]:
        index = word.find("y")
        consonant_cluster = word[:index]
        return word[index:] + consonant_cluster + "ay"

    # Regla 2: Palabra comienza con consonante o consonante + 'qu'
    while word[0] not in "aeiou":
        word = word[1:] + word[0]

    return word + "ay"


# Función para traducir una frase a Pig Latin
def translate_phrase_to_pig_latin(phrase):
    words = phrase.split()
    translated_words = [translate_to_pig_latin(word) for word in words]
    translated_phrase = " ".join(translated_words)
    return translated_phrase


# Ejemplo de uso:
english_phrase = "yellow"
pig_latin_phrase = translate_phrase_to_pig_latin(english_phrase)
print(pig_latin_phrase)  # Resultado: "elloHay orldway"


# de mi otro intento
