class ExtendedStack(list):
    def sum(self):
        """
        операция сложения
        :return:top1+top2
        """
        top1 = super().pop()
        top2 = super().pop()
        _sum = top1 + top2
        super().append(_sum)
        return _sum

    def sub(self):
        """
        операция вычитания
        :return:
        """
        top1 = super().pop()
        top2 = super().pop()
        _sub = top1 - top2
        super().append(_sub)
        return _sub

    def mul(self):
        """
        операция умножения
        :return:
        """
        top1 = super().pop()
        top2 = super().pop()
        _mul = top1 * top2
        super().append(_mul)
        return _mul

    def div(self):
        """
        операция целочисленного деления
        """
        top1 = super().pop()
        top2 = super().pop()
        _div = top1 // top2
        super().append(_div)
        return _div
