num1 = int(input())
num2 = int(input())
str1 = bin(num1).replace("0b", "")
str2 = bin(num2).replace("0b", "")
str3 = bin(num1 + num2).replace("0b", "")
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)
if len1 < 8:
    count = 8 - len1
    print("0" * count + str1)
if len2 < 8:
    count = 8 - len2
    print("0" * count + str2)
print("--------")
if len3 < 8:
    count = 8 - len3
    print("0" * count + str3)
