import math

str = input().split(" ")
num1 = int(str[0])
num2 = int(str[1])
print(math.gcd(num1, num2), math.lcm(num1, num2))
