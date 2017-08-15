from itertools import groupby
from re import sub

def decode(input):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), input)


def encode(input):
    encoded = [(len(list(g)), k) for k, g in groupby(input)]
    encodedStr = ''
    for chunk in encoded:
        if(chunk[0] == 1):
            encodedStr = encodedStr + str(chunk[1])
        else:
            encodedStr  = encodedStr + str(chunk[0])+str(chunk[1])

    return encodedStr