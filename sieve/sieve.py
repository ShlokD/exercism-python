import math

def sieve(limit):
    array_of_primes = []
    if limit >= 2:
        array_of_primes.append(2)
        non_primes = set()
        for i in range(3, limit + 1, 2):
            if i not in non_primes:
                array_of_primes.append(i)
                non_primes.update(range(int(math.pow(i, 2)), limit, i))

    return array_of_primes
