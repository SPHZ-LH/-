number = float(input())
i = 1
sum = 0
k = 1
while k > number:
    k = float(1 / (i**2))
    i += 1
    sum += k

result = float((sum * 6) ** 0.5)
print("{:.6f}".format(result))
