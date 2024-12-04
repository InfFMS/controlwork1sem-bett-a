def F(x):
    first = x // 1000
    second = x % 1000 // 100
    third = x % 100 // 10
    forth = x % 10

    fs = first + second
    st = second + third
    tf = third + forth

    lst = [fs, st, tf]
    lst.remove(min(lst))

    if lst[0] <= lst[1]:
        s = lst[0] * 100 + lst[1]
    else:
        lst[0], lst[1] = lst[1], lst[0]
        s = lst[0] * 100 + lst[1]

    return s

#print(F(9575))

for i in range(1000, 10000):
    if F(i) == 1418:
        print(i)
        break

# 1599
