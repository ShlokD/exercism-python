from functools import reduce

def get_multiples(x, y):
    return [ i for i in range(1, y) if i % x == 0]

def sum_of_multiples(limit, numbers):
    multiples = set()
    for i in numbers:
        multiples.update(get_multiples(i, limit))

    if len(multiples) > 0:
      return reduce(lambda x,y : x + y, list(multiples))
    else:
        return 0
