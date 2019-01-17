def alphabet_position(letter):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in letter:
        if char in alphabet_upper:
            return alphabet_upper.index(char)
        elif char in alphabet_lower:
            return alphabet_lower.index(char)


def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
    if char.isalpha() is False:
        return char
    else:
        if char in alphabet_lower:
            letter_position = (alphabet_position(char) + rot) % 26
            return alphabet_lower[letter_position]
        elif char in alphabet_upper:
            letter_position = (alphabet_position(char) + rot) % 26
            return alphabet_upper[letter_position]
