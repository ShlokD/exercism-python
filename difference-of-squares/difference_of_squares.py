def square_of_sum(n):
    sum = (n * ( n + 1)) / 2
    return sum * sum


def sum_of_squares(n):
    return (n * ( n + 1 ) * (( 2 * n ) + 1)) / 6


def difference(n):
    return abs(sum_of_squares(n) - square_of_sum(n))
