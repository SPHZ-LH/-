list = input().split(" ")

rows = int(list[0])
columns = int(list[1])

colslist = [0] * columns
rowslist = [0] * rows

count = 0
for i in rowslist:
    rowslist[count] = colslist
    count += 1

for i in range(rows):
    list = input().split(" ")
    count = 0
    for j in list:
        rowslist[i][count] = j
        count += 1
    print(rowslist)

# list= [0]*5
# mylist=[0]*4
# mylist[0]=list
# mylist[1]=list
# mylist[2]=list
# mylist[3]=list
# for i in mylist:
#     print(i)
