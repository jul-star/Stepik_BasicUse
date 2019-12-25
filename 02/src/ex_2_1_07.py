from typing import List, Any


class Exceptions:
    @staticmethod
    def Find() -> dict:
        _tmp_inh = Exceptions.ReadInput()
        _inh = Exceptions.getInheritance(_tmp_inh)
        _tmp_catch = Exceptions.ReadInput()
        _catches = Exceptions.getCatches(_tmp_catch)
        _extra = Exceptions.getExtra(_inh, _catches)
        return _extra

    @staticmethod
    def RefineExtra(extra: dict) -> list:
        _res: List[Any] = []
        for k in extra.keys():
            if extra[k]:
                _res.append(k)
        return _res

    @staticmethod
    def ReadInput() -> list:
        """
        :return: list of strings
        """
        n = int(input())
        lst = []
        for i in range(n):
            line = input().rstrip()
            _lst = line.split()
            lst.append(_lst)
        return lst

    @staticmethod
    def getInheritance(raw: list) -> dict:
        """
        :param raw: [['ArithmeticError'],['ZeroDivisionError', ':', 'ArithmeticError']]
        :return: {'ArithmeticError':[],'ZeroDivisionError' :['ArithmeticError']}
        """
        _inh = {}
        for _lst in raw:
            _i = []
            j: int = 0
            _child: str = str()
            for i in _lst:
                if j == 0:
                    _child = i
                    _inh[_child] = []
                else:
                    if i == ':':
                        continue
                    else:
                        _inh[_child].append(i)
                j += 1
        return _inh

    @staticmethod
    def getCatches(raw: list) -> list:
        """
        :param raw:[['ArithmeticError'],['ZeroDivisionError']]
        :return:['ArithmeticError','ZeroDivisionError']
        """
        _catches = []
        for _lst in raw:
            for i in _lst:
                _catches.append(i)
        return _catches

    @staticmethod
    def getExtra(inh: dict, catches: list) -> dict:
        _res = {}
        if catches is None:
            return _res
        j: int = 0
        _len = len(catches)
        if _len > 0:
            _res[catches[0]] = False
        for forward in range(_len):
            for backward in range(forward):
                if catches[forward] == catches[backward]:
                    _res[catches[forward]] = True
                    break
                if Exceptions.InConnection(catches[forward], catches[backward], inh):
                    _res[catches[forward]] = True
                    break
                else:
                    _res[catches[forward]] = False
        return _res

    @staticmethod
    def InConnection(catch: str, above: str, inh: dict) -> bool:
        _res: bool = False
        if catch == above:
            return True
        if catch in inh.keys():
            if above in inh[catch]:
                return True
            else:
                for catch_candidate in inh[catch]:
                    if Exceptions.InConnection(catch_candidate, above, inh):
                        return True

        return _res

    @staticmethod
    def printResult(extra: list) -> None:
        for val in extra:
            print(val)


if __name__ == "__main__":
    _extra = Exceptions.Find()
    _res = Exceptions.RefineExtra(_extra)
    Exceptions.printResult(_res)
