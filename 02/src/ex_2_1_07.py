class BadName(Exception):
    pass
def Hello(msg):
    if msg[0].isupper():
        print ("Hello, "+msg)
    else:
        raise BadName("Wrong name:"+msg)



while True:
    try:
        Hello(input())
    except BadName:
        print("Catched:  ValueError")
        print("Try again")
    else:
        break

