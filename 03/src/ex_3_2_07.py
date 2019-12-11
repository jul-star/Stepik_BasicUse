def cnt(s, t):
    sum = 0
    LenT = len(t)
    left = len(s) - LenT + 1
    for i in range(left):
        if s.find(t, i, i + LenT) >= 0:
            sum += 1
    return sum


st = input()
ts = input()
res = cnt(st, ts)
print(res)
