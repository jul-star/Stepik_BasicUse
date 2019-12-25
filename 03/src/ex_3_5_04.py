import json


class Descendants:
    @staticmethod
    def getInput() -> list:
        s = input().rstrip()
        _res = []
        try:
            _res = json.loads(s)
        except json.JSONDecodeError as e:
            print("json error: ", e.msg)
        _out = Descendants.Clean(_res)
        return _out

    @staticmethod
    def Clean(raw_inh: list) -> list:
        _res = []
        for r in raw_inh:
            _dict: dict = {}
            _key: str = str()
            for k in r.keys():
                if k == "name":
                    _key = r[k]
                if k == "parents":
                    _dict[_key] = r[k]
            _res.append(_dict)
        return _res

    @staticmethod
    def getClasses(inh_raw: list) -> list:
        """
        [{"B": ["A", "C"]}]  ->  ['A','B','C']
        :param inh_raw: list of dicts
        :return: list
        """
        _res = set()
        for ln in inh_raw:
            for k in ln.keys():
                _res.add(k)
                for p in ln[k]:
                    _res.add(p)
        _out = []
        for r in _res:
            _out.append(r)
        _out.sort()
        return _out

    @staticmethod
    def Calculate(inh: list, desc: list) -> dict:
        """
        :param inh: [{"B": ["A", "C"]}]
        :param desc: ['A','B','C']
        :return: {'A':1,'B':0,'C':1]
        """
        _res: dict = {}
        for pr in desc:
            _res[pr] = Descendants.CalculateDescendats(pr, inh)
        return _res

    @staticmethod
    def CalculateDescendats(parent: str, inh: list) -> int:
        """
        :param parent: 'A'
        :param inh: [{"B": ["A", "C"]}]
        :return: 1
        """
        _sum: int = 0
        for d in inh:  # getting dict
            for child in d.keys():  # one key in a dict of child:[prnt1,...prntN]
                if parent == child:
                    _sum += 1
                if parent in d[child]:  # check if parent in parent's list
                    _sum += 1
                    _sum += Descendants.CalculateDescendats(child, inh)
                # else:
                #     _sum += 0
        return _sum


if __name__ == "__main__":
    Descendants.getInput()
