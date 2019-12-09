import itertools

"""
генератор простых чисел
"""
def primes():
    lst = []
    i = 1
    while True:
        i += 1
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                # print(i)
                yield i
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
            # print(i)
            yield i

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
