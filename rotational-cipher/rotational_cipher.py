import string

def rotate(phrase, count):
    cipher = []

    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    lower_len = len(lower_letters)
    upper_len = len(upper_letters)

    for letter in list(phrase):
      if letter.isalpha():
        if letter.isupper():
            cipher_index = (upper_letters.index(letter) + count) % upper_len
            cipher.append(upper_letters[cipher_index])
        elif letter.islower():
            cipher_index = (lower_letters.index(letter) + count) % lower_len
            cipher.append(lower_letters[cipher_index])
      else:
        cipher.append(letter)

    return ''.join(cipher)

