def caesar(text, shift):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    shifted_text = alphabets[shift:] + alphabets[:shift]
    table = str.maketrans(alphabets, shifted_text)
    return text.translate(table)


encrypted_text_2 = caesar("freecodecamp", 5)
encrypted_text = caesar("freeCodeCamp", 5)
print(encrypted_text)
print(encrypted_text_2)
