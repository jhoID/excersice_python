# This version is more optimal
def is_isogram(string):
    seen_letter = set()
    for letter in string.lower():
        if letter.isalpha():
            if letter in seen_letter:
                return False
            seen_letter.add(letter)
    return True
