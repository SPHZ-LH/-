for i in range(int(input())):
    flag = True
    num = int(input())
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("No")
            flag = False
            break

    if flag:
        print("Yes")
