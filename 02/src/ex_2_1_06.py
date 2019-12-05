class ExceptionOrder:
    @staticmethod
    def ReadInput():
        n = int(input())
        dr = []
        for i in range(n):
            dr.extend(input().split(':'))
        return dr

    @staticmethod
    def getUnique( dr):
        seen = set()
        unique = []
        for i in dr:
            if i not in seen:
                seen.add(i)
                unique.append(i)
        return unique
    @staticmethod
    def getAnswer():
        dr = ExceptionOrder.ReadInput()
        unique = ExceptionOrder.getUnique(dr)
        for i in unique:
            print(i)


ExceptionOrder.getAnswer()