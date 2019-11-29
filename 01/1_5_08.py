class Buffer:
    def __init__(self):        # конструктор без аргументов
        self.sum = 0
        self.border = 5
        self.lst = []

    def add(self, *a):  # добавить следующую часть последовательности
        for i in list(a):
            self.lst.append(i)
            if len(self.lst) >= self.border:
                self.sum = 0

                for i in range(self.border):
                    p = self.border - i - 1
                    self.sum += self.lst[p]
                    del self.lst[p]
                print(self.sum)

    def get_current_part(self):        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        print(self.lst)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]