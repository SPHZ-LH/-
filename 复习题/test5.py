strlist = eval(input())


def sum(strlist):
    result = 0
    for i in strlist:
        if isinstance(i, int):
            result += i
        if isinstance(i, list):
            result += sum(i)
        if isinstance(i, tuple):
            result += sum(i)
    return result


print(sum(strlist))
