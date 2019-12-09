class multifilter:
    """
    допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
    """
    def judge_half(pos, neg):
        return pos >= neg

    """
    допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
    """
    def judge_any(pos, neg):
        return pos >= 1
    """
    допускает элемент, если его допускают все функции (neg == 0)
    """
    def judge_all(pos, neg):
        return neg == 0

    """
    iterable - исходная последовательность
    funcs - допускающие функции
    judge - решающая функция
    """
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

        # ed 1.0
        self.res = []
        # for i in self.iterable:
        #     pos = 0
        #     neg = 0
        #     for f in funcs:
        #         if f(i):
        #             pos += 1
        #         else:
        #             neg += 1
        #     if judge(pos,neg):
        #         self.res.append(i)

    """
    возвращает итератор по результирующей последовательности
    """
    def __iter__(self):
        # ed. 2.0
        for i in self.iterable:
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos,neg):
                yield i