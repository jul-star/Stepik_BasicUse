import os.path

res = []
for cd, drs, fls in os.walk("sample_2_4_06"):
    # print(cd)
    # print(drs)
    # print(fls)
    # print('-----------------')

    for filename in fls:
        if filename.split(".")[-1] == 'py':
            dr = cd.replace('\\', '/')
            if dr not in res:
                res.append(dr)
                continue
res.sort()
print(res)
