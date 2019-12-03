find = False

def get_inheritance():
    n = int(input())
    inh = {}
    for i in range(n):
        lst = input().split()
        j = 0
        for c in lst:
            if j == 0:
                child = c
                inh[child] = []
            if j > 1:
                inh[child].append(c)
            j += 1
    return inh

def get_request():
    req = {}
    k = int(input())
    for i in range(k):
        (child, parent) = input().split()
        if child not in req.keys():
            req[child] = []
        req[child].append(parent)
    return req

def find_inheritance(req):
    global find
    for parent, child in req.items():
        check_parent(parent, child)
        if find:
            print("Yes")
            find = False
        else:
            print("No")
    return

def check_parent(parent, child):
    global inh
    global find
    if child in inh.keys():
        if parent in inh[child]:
            find = True
            return True;
        else:
            for cand in inh[child]:
                if cand in inh.keys():
                    check_parent(parent, cand)
    else:
        return False
    return False

inh = get_inheritance()
req = get_request()
print("Inheritance: ", inh)
print("Requests: ", req)
find_inheritance(req)


