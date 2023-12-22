list = input().split(" ")

num1 = float(list[0])
num2 = int(list[1])

for i in range(num2 + 1):
    print("{0:.1f}**{1:d}={2:.2f}".format(num1, i, num1**i))
