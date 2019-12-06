import simplecrypt


def getEncripted():
    encrypted = ''
    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()
    return encrypted





def getPasswords():
    passwords = []
    with open("passwords.txt") as fp:
        line = fp.readline().strip()
        while line:
            passwords.append(line)
            line = fp.readline().strip()
    return passwords

def getDecrypted(encrypted, passwords):
    i = 1
    res = {}
    for pswd in passwords:
        # print(i)
        # print(pswd)
        try:
            res[i] = simplecrypt.decrypt(pswd, encrypted).decode('utf8')
        except:
            continue
            # print('Error')
        finally:
            i += 1
    return res

if __name__ == "__main__":
    encrypted = getEncripted()
    passwords = getPasswords()
    answers = getDecrypted(encrypted, passwords)
    for a in answers.keys():
        print(str(a) + ": " + answers[a])