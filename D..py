import os

a = list()
d = {}
q = [[0 for i in range(8)] for j in range(8)]

for t in range(8):
    s = input()[:8]
    a.append(s)

for i in range(8):
    for j in range(8):
        if a[i][j] == 'R' or a[i][j] == 'B':
            if d.get(a[i][j]):
                d[a[i][j]].append((i, j))
            else:
                d[a[i][j]] = [(i, j)]
            q[i][j] = 1

if d.get('R'):
    for item in d['R']:

        for i in range(item[0]+1, 8):
            if a[i][item[1]] == '*':
                q[i][item[1]] = 1
            else:
                break
        for i in range(item[0]-1, -1, -1):
            if a[i][item[1]] == '*':
                q[i][item[1]] = 1
            else:
                break

        for j in range(item[1]+1, 8):
            if a[item[0]][j] == '*':
                q[item[0]][j] = 1
            else:
                break
        for j in range(item[1]-1, -1, -1):
            if a[item[0]][j] == '*':
                q[item[0]][j] = 1
            else:
                break

if d.get('B'):
    for x in d['B']:
        i, j = x[0]-1, x[1]-1
        while i >= 0 and j >= 0:
            if a[i][j] == '*':
                q[i][j] = 1
            else:
                break
            i -= 1
            j -= 1

        i, j = x[0]-1, x[1]+1
        while i >= 0 and j < 8:
            if a[i][j] == '*':
                q[i][j] = 1
            else:
                break
            i -= 1
            j += 1

        i, j = x[0]+1, x[1]-1
        while i < 8 and j >= 0:
            if a[i][j]=='*':
                q[i][j] = 1
            else:
                break
            i += 1
            j -= 1

        i, j = x[0]+1, x[1]+1
        while i < 8 and j < 8:
            if a[i][j] == '*':
                q[i][j] = 1
            else:
                break
            i += 1
            j += 1

count = 0
for i in q:
    #print(i)
    for j in i:
        count += j
print(64 - count)





