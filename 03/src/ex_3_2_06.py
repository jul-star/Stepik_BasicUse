def repl(s, a, b):
    _max = 1000
    i = 0
    if a in b and a in s:
        return 'Impossible'
    while a in s:
        i += 1
        if i > _max:
            return 'Impossible'
        else:
            s = s.replace(a, b)
            if s == -1:
                return i
    return i


st = input()
a1 = input()
b1 = input()
res = repl(st, a1, b1)
print(res)


# aabbcc
# aa
# aaa
