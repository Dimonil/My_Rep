x, y = map(int, input().split(':'))
x2, y2 = map(int, input().split(':'))
t = int(input())
a = x + x2
b = y + y2
count = 0

if a <= b:
    count = b-a
    a += count
    x2 += count
    # a == b
    if t == 1:
        if x2 <= y:
            count += 1
    else:
        if x <= y2:
            count += 1
print(count)



