letters = "abcdefghijklmnopqrstuvwxyz"

# LETTERS = [letter for letter in letters]


def rotate(text, key):
    if key == 0 or key == 26:
        return text

    cipher_text = ""

    for element in text:
        is_upper = element.isupper()
        element = element.lower()
        pos = letters.find(element)
        if pos == -1:
            cipher_text += element
            continue
        final_pos = len(letters) - (pos + key) - 1
        if final_pos < 0:
            cipher_text += (
                letters[abs(final_pos) - 1].upper()
                if is_upper
                else letters[abs(final_pos) - 1]
            )
        else:
            cipher_text += (
                letters[pos + key].upper() if is_upper else letters[pos + key]
            )

    return cipher_text


text_test = "Gur dhvpx oebja sbk whzcf Bire gur ynml qbt"
key_test = 13

print(rotate(text_test, key_test))
