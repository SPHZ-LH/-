n, m = map(int, input().split())
strlist, flag = [], True
for i in range(n):  # 输入的矩阵
    strlist.append(list(map(int, input().split())))

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (
            strlist[i][j] > strlist[i - 1][j]
            and strlist[i][j] > strlist[i + 1][j]
            and strlist[i][j] > strlist[i][j - 1]
            and strlist[i][j] > strlist[i][j + 1]
        ):
            flag = False
            print(strlist[i][j], i + 1, j + 1)

if flag:
    print("None", n, m)
