def method(a, b):
    sum = 0
    for i in range(b):
        sum += a * int((10**i))
    return sum


def fn(a, b):
    result = 0
    for i in range(1, b + 1):
        result += method(a, i)
    return result
