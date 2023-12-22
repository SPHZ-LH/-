str = input()
list = list(str[::-1])
for i in list:
    if list[0] == "0":
        list.remove("0")
print("".join(list))
