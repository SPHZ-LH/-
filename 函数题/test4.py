import math


def funcos(eps, x):
    sums = 0
    i = 0
    t = 1
    while True:
        if x**i / math.factorial(i) < eps:
            break
        else:
            sums += t * x**i / math.factorial(i)
            t = -t
        i += 2
    return sums
