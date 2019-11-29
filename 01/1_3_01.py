# def f_name(arg1, arg2):
#     return  arg1 + arg2
#
# def f(a1, a2):
#     return a1*a2
#
#
# print("f=", type(f))

# a = []
#
# def foo(a1,a2):
#     a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
#
# print(a)

def f(x):
    y=x
    while 1 == 1:
        if y % 5 == 0:
            return y
        y += 1


# print(f(2))

def f1(a, *vs, b=10):
    res = a+b
    for v in vs:
        res += v
    return res
def f1Test():
    i = 1
    print(i, f1(21))
    i+=1
    print(i, f1(0,0,31))
    i+=1
    print(i, f1(11,10))
    i+=1
    print(i, f1(11, b=20))
    i+=1
    print(i, f1(11,10,10))
    i+=1
    print(i, f1(5,5,5,5,1))
    i+=1
    # print(f1(b=31))
    i+=1
    # print(f1(b=31,0))
    i+=1
    print(i,f1( 11,10,b=10))

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

# y=fib(5)
# print(y)

def c(n,k):
    if k > n:
        return 0
    else:
        if k == 0:
           return 1
        else:
            return c(n-1,k)+c(n-1,k-1)

# n,k = map(int, input().split())
# print(c(n,k))
def add(dc, nms, var):
    if nms in dc.keys():
       dc[nms][var] = 1
       return True
    else:
        for node in dc.keys():
            if isinstance(dc[node], dict):
                if add(dc[node], nms, var):
                    return


def create(dc, nms, parent):
    path = buildPass(parent)
    cur = dc
    for node in reversed(path):
        cur = cur[node]
    parents[nms] = parent
    cur[nms] = {}

def buildPass(nms):
    global parents
    lst = [nms]
    while nms is not None:
        if parents[nms] is not None:
           lst.append(parents[nms])
        nms = parents[nms]
    return lst

def get(nms, var):
    global dc
    global parents
    path = buildPass(nms)
    cur = dc
    for node in reversed(path):
        cur = cur[node]

    if var in cur.keys():
        print(nms)
    else:
        nms = parents[nms]
        if nms is None:
            print("None")
        else:
            get(nms,var)

n = int(input())
dc = {}
dc["global"]={}
parents={'global':None}
for i in range(n):
    cmd, nms, arg = input().split()
    if cmd == "add":
      add(dc, nms, arg)
    else:
        if cmd == "create":
            create(dc, nms, arg)
        else:
            if cmd == "get":
                get(nms,arg)
# print (dc)




