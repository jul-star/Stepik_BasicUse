class MoneyBox:
    def __init__(self, capacity):
        self.sum = 0
        self.cap = capacity
# конструктор с аргументом – вместимость копилки


    def can_add(self, v):
        return self.sum + v <= self.cap
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v):
            self.sum += v
        # положить v монет в копилку

x = MoneyBox(10)
x.add(15)
print(x.sum)
x.add(5)
print(x.sum)
x.add(5)
print(x.sum)