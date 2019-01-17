from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    encrypted_text = []
    for i in text:
        encrypted_text.append(rotate_character(i, rot))
    new_text = "".join(encrypted_text)
    return new_text


def main():
    text = input("What phrase would you like to encrypt?")
    rot = int(input("How far would you like to rotate?"))
    print(encrypt(text, rot))


if __name__ == "__main__":
    main()
