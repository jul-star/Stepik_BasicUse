class Connection:

    def __init__(self):
        self.find = False
        self.inh = []
        self.req = {}
    @staticmethod
    def ReadInput():
        n = int(input())
        lst = []
        for i in range(n):
            lst.append(input().split())
        return lst
    @staticmethod
    def ReadInheritance():
        return Connection.ReadInput()
    @staticmethod
    def ReadRequest():
        return Connection.ReadInput()

    """
    :param Inheritance - list of list [[a, b, c], [a,d,e]]
    """
    @staticmethod
    def _BuildInheritance(Inheritance):
        inh = {}
        for lst in Inheritance:
            j = 0
            for c in lst:
                if j == 0:
                    child = c
                    inh[child] = []
                if j > 1:
                    inh[child].append(c)
                j += 1
        return inh
    @staticmethod
    def _BuildRequest(Request):
        req = {}
        for child, parent in Request:
            req[child]=parent

        return req

    def _find_inheritance(self):
        res = []
        for parent, child in self.req.items():
            self._check_parent(parent, child)
            if self.find:
                res.append(True)
                self.find = False
            else:
                res.append(False)
        return res

    def _check_parent(self, parent, child):
        if child in self.inh.keys():
            if parent in self.inh[child]:
                find = True
                return True;
            else:
                for cand in self.inh[child]:
                    if cand in self.inh.keys():
                        self._check_parent(parent, cand)
        else:
            return False
        return False

    def FindConnection(self, Inheritance, Request):
        self.inh = Connection._BuildInheritance(Inheritance)
        self.req = Connection._BuildRequest(Request)
        print("Inheritance: ", self.inh)
        print("Requests: ", self.req)

        return self._find_inheritance()

    def Find(self):
        Inheritance = Connection.ReadInheritance()
        Request = Connection.ReadRequest()
        res = self.FindConnection(Inheritance, Request)
        for i in res:
            if i:
                print("Yes")
            else:
                print("No")
        return


