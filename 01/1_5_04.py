class Counter:
    def __init__(self, start = 0):
        self.count = start
    def incr(self):
        self.count += 1
    def reset(self):
        self.count = 0

x = Counter()
x.incr()
x.incr()
Counter.incr(x)
print ("counter =", x.count)