
def F(x):
    d = list()
    for j in range(1, round(x**0.5) + 1):
        if x % j == 0:
            d.append(j)

    if len(d) == 4:
        d.pop(0)
        d.pop(-1)
        return d
    else:
        return 0

for i in range(174457, 174506):
    lst = F(i)
    if lst != 0:
        print(*lst)