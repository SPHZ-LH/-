number = int(input())
count = 0
for i in range(number):
    length = len(input().strip())
    if length > count:
        count = length
print(f"length={count}")
