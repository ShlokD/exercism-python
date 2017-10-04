import string, re

lower_letters = list(string.ascii_lowercase)
lower_letters_rev = list(reversed(lower_letters))

def get_letter_at_index(letter):
    try:
        index_of_letter = lower_letters.index(letter.lower())
        return lower_letters_rev[index_of_letter]
    except ValueError:
        return letter

def encode(string):
    letters = list(''.join([x for x in string if x.isalnum()]))
    encoded = ''.join(list(map(get_letter_at_index, letters)))
    return ' '.join(re.findall('.{1,5}', encoded))



def decode(string):
    encoded = encode(string).split()
    return ''.join(encoded)
