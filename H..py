#l, x1, v1, x2, v2 = map(int, input().split())
def difr(x, l):
    return x if x <= l/2 else l - x


def dogon(a, va, b, vb, r):#А догоняет Б до предела L
    t = 0
    r = abs(r)
    va = abs(va)
    vb = abs(vb)
    while r > 10**(-9):
        ta = r/va
        t += ta
        if ta*vb >= r:
            return 10**(10)
        r = ta*vb
    return t

def vstr(a, va, b, vb, r):#Двигаются навстречу
    r = r / (abs(va)+abs(vb))
    return abs(r)




def newFoo(l, x1, v1, x2, v2):
    if x1 < x2:
        a, va = x1, v1
        b, vb = x2, v2
    else:
        a, va = x2, v2
        b, vb = x1, v1

    if a == b or a == l - b:
        return 0
    if va < 0 and vb < 0:
        va, vb = abs(va), abs(vb)
        _a = l - a
        _b = l - b
        a, va, b, vb = _b, vb, _a, va

    if va == 0 and vb == 0:
        if a != b:
            return -1
        else:
            return 0

    if va == 0 or vb == 0:
        _a = l - a
        _b = l - b
        if va == 0:
            if vb > 0:
                if _a < a:
                    q = vstr(b, vb, _a, va, _a + _b)
                else:
                    q = vstr(b, vb, a, va, a + _b)
                return q
            else:
                if a <= _a <= b:
                    q = vstr(b, vb, _a, va, b - _a)
                else:
                    q = vstr(b, vb, a, va, b - a)
                return q

        if vb == 0:
            if va > 0:
                if a <= _b <= b:
                    return vstr(a, va, _b, vb, _b - a)
                else:
                    return vstr(a, va, b, vb, b - a)
            else:
                if a <= _b <= b:
                    return vstr(a, va, b, vb, a + _b)
                else:
                    if _b < a:
                        r = a - _b
                    else:
                        r = a + b
                    return vstr(a, va, _b, vb, r)


    if va >= 0 and vb >= 0:
        if 0 <= a <= l/2 and l/2 <= b <= l:
            _a = l - a
            _b = l - b
            if difr(a, l) <= difr(b, l):

                return vstr(b, vb, _a, va, _a - b)
            else:
                if vb > va:

                    return min(dogon(b, vb, a, va, a + _b), vstr(b, vb, _a, va, l-(b-_a)))
                else:
                    return min(dogon(a, va, b, vb, b - a), vstr(a, va, _b, vb, l - a + _b))

        elif 0 <= a <= b <= l/2:
            _b = l - b
            return min(vstr(a, va, _b, vb, _b - a), dogon(a, va, b, vb, b - a))
        elif l/2 <= a <= b <= l:
            _b = l - b
            return min(dogon(a,va,b,vb,b-a), vstr(a,va,_b,vb,l-a+_b))

    elif va < 0 and vb > 0:

        _b = l - b
        _a = l - a

        if 0<=a<=l/2 and l/2<=b<=l:

            if difr(a, l) < difr(b, l):
                q = dogon(b, vb, _a, va, _a - b)
            else:
                q = dogon(a, va, _b, vb, a - _b)

            return min(vstr(b,vb,a,va,a + l-b), q)


        elif 0<=a<=b<=l/2:
            return min(dogon(a, va, b, vb, b-a), vstr(a, va, _b, vb, _b - a))
        elif l/2 <= a <= b <= l:
            return min(vstr(a, va, b, vb, l - (b-a)), dogon(a, va, _b, vb, a - _b), dogon(b, vb, _a, va, _a + _b))


    elif va > 0 and vb < 0:
        _b = l - b
        _a = l - a

        if 0 <= a <= l / 2 and l / 2 <= b <= l:

            if difr(a, l) < difr(b, l):
                q = dogon(a, va, _b, vb, _b - a)
            else:
                q = dogon(b, vb, _a, va, b - _a)

            return min(vstr(a, va, b, vb, l - (a + _b)), q)
        elif 0 <= a <= b <= l/2:
            return vstr(a, va, b, vb, b-a)
        elif l/2 <= a <= b <= l:
            return vstr(a, va, b, vb, b-a)





def go():

    l, x1, v1, x2, v2 = map(int,input().split())
    result = newFoo(l, x1, v1, x2, v2)
    if result != -1:
        print('yes')
        print(result)
    else:
        print('no')

go()
#print(newFoo(12,8,10,5,20))
#print(foo(12, 8, 10, 5, 20))
#print(foo(6, 3, 1, 1, 1))
#print(newFoo(6, 3, 1, 1, 1))
#print(newFoo(5, 0, 0, 1, 2))
#print(newFoo(10, 7, -3, 1, 4))
#print(newFoo(10, 1, 1, 2, 1))




