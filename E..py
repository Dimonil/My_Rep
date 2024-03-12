n, k, d = map(int, input().split())
n = n*10
b = False
for _ in range(10):
    #print(n)
    if n % k == 0:
        b = True
        break
    n += 1
if b:
    print(n, end='')
    for _ in range(d-1):
        print(0, end='')
else:
      print(-1)