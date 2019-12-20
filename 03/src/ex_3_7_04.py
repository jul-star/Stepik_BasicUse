import xml.etree.ElementTree as ET


class Quebes:
    @staticmethod
    def run():
        _str = Quebes.getInput()
        _root = Quebes.str2tree(_str)
        _dict = {'red': 0,
                 'green': 0,
                 'blue': 0}
        worth: int = 1
        Quebes.addWorth(_dict, _root.attrib, worth)
        Quebes.calculate(_root, worth, _dict)
        Quebes.printResult(_dict)

    @staticmethod
    def getInput() -> str:
        _str = input()
        _str = _str.rstrip()
        return _str

    @staticmethod
    def str2tree(_str: str) -> ET:
        """

        :param _str:
        :return: root of XML obj
        """
        _root = ET.fromstring(_str)
        return _root

    @staticmethod
    def calculate(_root, worth: int, _dict: dict):
        # print(_root.attrib)
        for el in _root:
            Quebes.addWorth(_dict, el.attrib, worth + 1)
            Quebes.calculate(el, worth + 1, _dict)

    @staticmethod
    def addWorth(_dict: dict, attr: ET, worth: int):
        _colors = ['red', 'green', 'blue']
        for k in attr.keys():
            if k == "color":
                if attr[k] in _colors:
                    _dict[attr[k]] += worth

    @staticmethod
    def printResult(_dict):
        template = "{red} {green} {blue}"
        print(template.format(red=_dict['red'], green=_dict['green'], blue=_dict['blue']))


if __name__ == "__main__":
    Quebes.run()
