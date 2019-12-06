from datetime import datetime
from datetime import timedelta

def add(date, delta):
    dt = datetime.strptime(date, '%Y %m %d')
    res = dt + timedelta(delta)
    return str(res.year) + ' ' + str(res.month) + ' ' + str(res.day)

if __name__ == "__main__":
    date = input()
    delta = int(input())
    print(add(date, delta))
