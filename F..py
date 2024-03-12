n = int(input())
a = list(map(int, input().split()))
count = 0
x = 0
for i in range(n):
    if a[i] % 2 == 1:
        count += 1
        x = i

if count % 2 == 1:
    for _ in range(n-1):
        print(chr(43), end='')
else:
    for i in range(n-1):
        if i+1 != x:
            print(chr(43), end='')
        else:
            print(chr(120), end='')






