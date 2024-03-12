import math
gold = (1+math.sqrt(5))/2


def foo(a, b):
    while True:
        b -= a
        if b <= 0:
            return True
        a -= b
        if a <= 0:
            return False


x = int(input())
y = int(input())
p = int(input())



t = x
k = 0
count = 1
y = y - x if y >= x else 0
if y != 0:
    k += p



def game(x, y, k):
    count = 1
    win = True
    gold = (1 + math.sqrt(5)) / 2

    t = x - y
    k -= t
    x -= k
    count += 1
    if x * gold <= k:
        win = False
    else:
        while k > 0:
            count += 1
            k -= x
            x -= k

    if win:
        return count
    else:
        return -1


def f_game(x, y, k):
    if y <= x:
        return (y, 1)

    t = x - k
    z = y - x
    count = z / t
    count = int(math.ceil(count))

    z -= t * count
    y -= count * t
    count += 1
    return (y, count)


def lst_step(x, y, k):
    t = x - y
    k -= t
    x -= k
    count = 1
    while k > 0:
        count += 1
        k -= x
        x -= k
        if x <= 0:
            return -1
    return count

def f2_game(x, y, k):
    y, count = f_game(x, y, k)
    #print(f'сделал до {x, y, k} за {count} ходов')
    l = []
    z = x - k
    b = y
    while b > 0:
        l.append([x, b, k])
        b -= z
    min_count = count + len(l) + lst_step(*l[-1])
    for i in range(len(l)):
        if lst_step(*l[i]) != -1:
            this_count = count + i + lst_step(*l[i])
            min_count = min(min_count, this_count)
    return(min_count)







def full_game(x, y, k):
    #print(x, y, k)
    if y == 0:
        print(1)
    elif y >= x and k >= x:
        #print('зашел в 1')
        print(-1)

    elif y < x and k >= x:
        #print('зашел в 2')
        print(game(x, y, k))

    elif k < x:
        #print('зашел во 3')
        print(f2_game(x, y, k))

#print(x, f_game(x, y, k), k)

full_game(x, y, k)














