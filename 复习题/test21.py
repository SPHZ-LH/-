str = input()
list = list(str)
strlist = []
for i in list:
    if i in "0123456789ABCDEFabcdef":
        strlist.append(i)
number = int("".join(strlist), 16)
print("".join(strlist))
print(number)
