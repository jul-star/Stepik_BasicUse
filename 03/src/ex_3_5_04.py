import json


class Descendants:
    @staticmethod
    def getInput() -> dict:
        try:
            _inp_json = json.loads(input().strip())
            return Descendants.Clean(_inp_json)
        except json.JSONDecodeError as e:
            print("json error: ", e.msg, e.pos)

    @staticmethod
    def Clean(raw_inh: list) -> dict:
        _res: dict = {}
        for r in raw_inh:
            _res[r['name']] = r['parents']
        return _res

    @staticmethod
    def inh2graph(inh: dict) -> dict:
        _graph = {}
        _res = None
        for ch in inh.keys():
            if ch not in _graph.keys():
                _graph[ch] = [ch]
            for pr in inh[ch]:
                if pr not in _graph.keys():
                    _graph[pr] = [pr]
                _graph[pr].append(ch)

            _res = dict(sorted(_graph.items()))
            for k in _res.keys():
                _res[k].sort()
        return _res

    @staticmethod
    def getClasses(inh: dict) -> list:
        """
        {"B": ["A", "C"]}  ->  ['A','B','C']
        :param inh: list of dicts
        :return: list
        """
        _res = set()
        for k in inh.keys():
            _res.add(k)
            for p in inh[k]:
                _res.add(p)
        _out = []
        for r in _res:
            _out.append(r)
        _out.sort()
        return _out

    @staticmethod
    def Count(inh: dict, desc: list) -> dict:
        """
        :param inh: [{"B": ["A", "C"]}]
        :param desc: ['A','B','C']
        :return: {'A':1,'B':0,'C':1]
        """
        _res: dict = {}
        for pr in desc:
            _res[pr] = Descendants.CountDescendats(pr, inh)
        return _res

    @staticmethod
    def Diff(li1, li2):
        # return list(set(li1) - set(li2))
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif

    @staticmethod
    def CountDescendats(parent: str, graph: dict, visited=None) -> int:
        """
        :param parent: 'A'
        :param graph: {'A': ['A','B'], 'B': []}
        :param visited - set of visited vertexes
        :return: 2
        """
        _sum: int = 0
        if visited is None:
            visited = set()
        if parent not in visited:
            _sum += 1
            visited.add(parent)
        for child in graph[parent]:
            if child not in visited:
                _sum += Descendants.CountDescendats(child, graph, visited)

        # else:
        #     _sum += 0

        return _sum

    @staticmethod
    def Print(stat: dict) -> None:
        template = '{k} : {v}'
        for k, v in stat.items():
            print(template.format(k=k, v=v))

    @staticmethod
    def run():
        _inh = Descendants.getInput()
        _desc = Descendants.getClasses(_inh)
        _graph = Descendants.inh2graph(_inh)
        _stat = Descendants.Count(_graph, _desc)
        Descendants.Print(_stat)


if __name__ == "__main__":
    Descendants.run()
