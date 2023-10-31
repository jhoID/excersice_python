def rotate(text, key):
    if key == 0 or key == 26:
        return text

    def caesar_cipher(char, shift):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            offset = ord("a") if is_upper else ord("a")
            shifted_char = chr(((ord(char) - offset + shift) % 26) + offset)
            return shifted_char.upper() if is_upper else shifted_char
        return char

    return "".join(caesar_cipher(char, key) for char in text)

text_test = "OMG"
key_test = 5

print(rotate(text_test, key_test))