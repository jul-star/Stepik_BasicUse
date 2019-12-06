from random import random

class RandIter:
    def __iter__(self):
        return self

    def __init__(self, edge):
        self.edge = edge
        self.i  = 0

    def __next__(self):
        self.i += 1
        if self.i < self.edge:
            return random()
        else:
            raise StopIteration

x = RandIter(10)
for i in x:
    print(i)