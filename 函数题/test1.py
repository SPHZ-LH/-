# 判断是否为素数
def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 素数之和
def PrimeSum(m, n):
    Sum = 0
    for i in range(m, n + 1):
        if prime(i) and i != 1:
            Sum += i
    return Sum


m, n = input().split()
m = int(m)
n = int(n)
print(PrimeSum(m, n))
