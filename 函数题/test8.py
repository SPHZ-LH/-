def polyvalue(lst, x):
    result = 0
    for i in range(len(lst)):
        result += lst[i] * (x**i)
    return result
