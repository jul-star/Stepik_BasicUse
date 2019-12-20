import xml.etree.ElementTree as ET


class Quebes:
    """
    <cube color="blue">
      <cube color="red">
        <cube color="green">
        </cube>
      </cube>
      <cube color="red">
      </cube>
    </cube>
    """
    @staticmethod
    def run():
        _str = Quebes.getInput()
        _tree = Quebes.str2tree(_str)


    @staticmethod
    def getInput()->str:
        _str = input()
        _str = _str.rstrip()
        return _str

    @staticmethod
    def str2tree(_str:str):
        _tree = ET.fromstring(_str)
        return _tree

    @staticmethod
    def calculate(_tree)->dict:
        _dict = {'red':0,
                 'green':0,
                 'blue':0}
        for el in _tree:
            if el.attrib is dict:
                print(el.attrib.keys(), el.attrib.items())
            else:
                print("Not a dict", el.attrib)
