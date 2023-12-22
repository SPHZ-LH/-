# 判断素数的方法
def PrimeMethod(num):
    Flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            Flag = False
            break
    return Flag


number = int(input())
for i in range(2, number):
    num1 = i
    if PrimeMethod(num1):
        num2 = number - num1
        if PrimeMethod(num2):
            print(f"{number} = {num1} + {num2}")
            break
