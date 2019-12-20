import time

class Loggable:
    def __init__(self):
        self._val = 0
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        self._val = int(msg)
    def getVal(self):
        return self._val



class LoggableList(list, Loggable):
    def append(self, val):
        super().append(val)
        super().log(val)
