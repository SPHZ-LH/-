StrList = eval(input())


def sum(count, StrList):
    result = 0
    for i in StrList:
        if isinstance(i, int):
            result += i * count
        if isinstance(i, list):
            result += sum(count + 1, i)
    return result


print(sum(1, StrList))
