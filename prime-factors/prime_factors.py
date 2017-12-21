def prime_factors(natural_number):
    pfs = []
    i = 2
    while natural_number > 1:
        while natural_number % i == 0:
            pfs.append(i)
            natural_number /= i
        i += 1
    return pfs
