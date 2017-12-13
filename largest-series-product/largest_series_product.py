from functools import reduce

def product(s):
    list_s = map(int, list(s))
    return reduce((lambda x, y: x*y), list_s)

def largest_product(series, size):
    if size == 0:
        return 1

    if size < 0 or size > len(series) or not series.isdigit():
        raise ValueError


    length = len(series)
    substrings = [series[i:i+size] for i in range(0, length)]
    sub_products=[product(s) for s in substrings if len(s) == size]
    return max(sub_products)


largest_product("99099", 3)