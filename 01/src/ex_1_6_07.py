class Connection:
    find = False

    @staticmethod
    def ReadInput():
        n = int(input())
        lst = []
        for i in range(n):
            line = input().rstrip()
            _lst = line.split()
            lst.append(_lst)
        return lst

    @staticmethod
    def getInheritance(_raw: list) -> list:
        _inh = []
        for l in _raw:
            _i = []
            for i in l:
                if i == ':':
                    continue
                else:
                    _i.append(i)
            _inh.append(_i)
        return _inh

    @staticmethod
    def getRequest(_raw: list) -> list:
        return _raw

    @staticmethod
    def BuildInheritance(inheritance: list) -> dict:
        inh = {}
        for lst in inheritance:
            j = 0
            for c in lst:
                if j == 0:
                    child = c
                    inh[child] = []
                else:
                    inh[child].append(c)
                j += 1
        return inh

    @staticmethod
    def BuildRequest(request: list) -> list:
        req = []
        for ln in request:
            for parent, child in ln:
                req.append([parent, child])
        return req

    @staticmethod
    def FindInheritance(_inheritance: dict, requests: list) -> list:
        res = []
        for r in requests:
            parent, child = r
            Connection._check_parent(_inheritance, parent, child)
            if Connection.find:
                res.append(True)
                Connection.find = False
            else:
                res.append(False)
        return res


    @staticmethod
    def _check_parent(_inheritance: dict, parent, child):
        if child == parent and child in _inheritance.keys():
            Connection.find = True
            return True
        if child in _inheritance.keys():
            if parent in _inheritance[child]:
                Connection.find = True
                return True
            else:
                for candidate in _inheritance[child]:
                    if candidate in _inheritance.keys():
                        Connection._check_parent(_inheritance, parent, candidate)
        else:
            return False
        return False


    @staticmethod
    def FindConnection():
        _tmp = Connection.ReadInput()
        _raw_inh = Connection.getInheritance(_tmp)
        _tmp = Connection.ReadInput()
        _raw_req = Connection.getRequest(_tmp)
        _inheritance = Connection.BuildInheritance(_raw_inh)
        _requests = Connection.BuildRequest(_raw_req)
        _res = Connection.FindInheritance(_inheritance, _requests)
        Connection.printResult(_res)


    def printResult(self, res):
        for i in res:
            if i:
                print("Yes")
            else:
                print("No")



if __name__ == "__main__":
    Connection.FindConnection()