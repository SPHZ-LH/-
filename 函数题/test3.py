def Fibonacci(number):
    list = [1, 1]
    for i in range(2, number + 1):
        list.append(list[i - 2] + list[i - 1])
    return list[number]


def fib(n):
    return Fibonacci(n)


def PrintFN(m, n):
    list = [1, 1]
    i, j = 0, 0
    while n > list[i]:
        list.append(list[len(list) - 2] + list[len(list) - 1])
        i += 1

    for x in range(len(list)):
        if m < list[x]:
            break
        else:
            j += 1

    resultlist = []
    for x in range(j, i):
        resultlist.append(list[x])
    return resultlist
