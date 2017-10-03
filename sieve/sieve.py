import math

def sieve(limit):
    array_of_primes = []
    if limit >= 2:
        array_of_primes.append(2)
        multiples = set()
        for i in range(3, limit + 1, 2):
            if i not in multiples:
                array_of_primes.append(i)
                multiples.update(range(int(math.pow(i, 2)), limit, i))

    return array_of_primes
