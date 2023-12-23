def method(count, number):
    result = 0
    list = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            if i != 1:
                num = int(number / i)
                result = result + i + num
                list.append(i)
                list.append(num)
            else:
                result += i
                list.append(i)
    list.sort()
    if result == number:
        count += 1
        print(f"{number} = ", end="")
        for i in list:
            if i != list[len(list) - 1]:
                print(f"{i}", end=" + ")
            else:
                print(f"{i}")
    return count


list = input().split(" ")
num1 = int(list[0])
num2 = int(list[1])
count = 0
for i in range(num1, num2 + 1):
    count = method(count, i)
if count == 0:
    print("None")
