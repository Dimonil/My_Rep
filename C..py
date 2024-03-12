count = 0
for _ in range(int(input())):
    x = int(input())
    count += x // 4
    if x % 4 == 1:
        count += 1
    elif x % 4 == 2 or x % 4 == 3:
        count += 2
print(count)
