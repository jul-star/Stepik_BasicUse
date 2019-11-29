# x= [1,2,3]
# idX = id(x)
# idV = id([1,2,3])
# print(idX - idV)
# y = x
# print (x is y)
# x.append(5)
# print (x)
# s = "123"
# t=s
# t=t+"4"
# print(s)
# print(type(x))
#
# a= 1
# b=1
# c=1
# print(a is b)  # Переиспользование объектов
# print(a is c)

a = 1
b = 1
c= a
d = 2
f=4
objects = [None, 1,2,3, a, b, c, d,f , 1,2,3]
ans = 0
cur = None
types = {}
for obj in objects:
    if id(obj) not in types:
        ans += 1
    types[id(obj)] = 1
print(ans)