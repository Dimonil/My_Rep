p, v = map(int, input().split())
q, m = map(int, input().split())


if p > q:
    p, q = q, p
    v, m = m, v


l = (p-v, p+v)
r = (q-m, q+m)
count = v*2 + 1 + m*2 + 1

if l[1] >= r[0]:
    count = max(l[1], r[1]) - min(l[0], r[0]) + 1


print(count)