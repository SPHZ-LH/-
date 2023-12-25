def Avg(lst):
    for i in range(len(lst)):
        sum = 0
        for j in lst[i]:
            sum += j
        lst[i] = sum / len(lst[i])
    return lst
