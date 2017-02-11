import random

test = "test.txt"
achi = "GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS"

def convertLetters(text):
    conv = ""
    text = text.upper()
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            conv = conv + text[i]
        elif 192 <= ord(text[i]) <= 197:
            conv = conv + "A"
        elif 200 <= ord(text[i]) <= 203:
            conv = conv + "E"
        elif 204 <= ord(text[i]) <= 207:
            conv = conv + "I"
        elif 210 <= ord(text[i]) <= 214:
            conv = conv + "O"
        elif 217 <= ord(text[i]) <= 220:
            conv = conv + "U"

    text = conv
    return text


def mix():
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    melange = ""
    while len(alpha) != 0:
        x = random.randint(0,len(alpha)-1)
        melange = melange + alpha[x]
        alpha.remove(alpha[x])
    return melange


def createCylinder(file,n):
    save = open(file,"w")
    for i in range(n):
        cil = mix() + "\n"
        save.write(cil)
    save.close()


def loadCylinder(file):
    cylinder = {}
    load = open(file,"r")
    general = load.readlines()
    indice = 1
    for i in range(len(general)):
        value = general[i]
        value = value[0:26]
        cylinder[indice]=value
        indice += 1
    load.close()
    return cylinder


def keyOK(key,n):
    for i in range(1,n+1):
        occu = key.count(i)
        if occu != 1:
            return False
        else:
            continue
    return True


def createKey(n):
    listN = []
    key = []
    for i in range(1,n+1):
        listN.append(i)
    while len(listN) != 0:
        x = random.randint(0,len(listN)-1)
        key.append(listN[x])
        listN.remove(listN[x])
    return key


def find(letter,alphabet):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return i
        else:
            continue


def shift(i):
    if 0 <= i <= 25:
        a = (i+6)%26
        return a
    else:
        return -1


def unshift(i):
    if 0 <= i <= 25:
        a = (i-6)%26
        return a
    else:
        return -1


def cipherLetter(letter,alphabet):
    indice = shift(find(letter,alphabet))
    return alphabet[indice]


def uncipherLetter(letter,alphabet):
    indice = unshift(find(letter,alphabet))
    return alphabet[indice]


def cipherText(cylinder,key,text):
    n = len(cylinder)
    crypt = ""
    if not keyOK(key,n):
        return False
    else:
        text = convertLetters(text)
        for i in range(len(text)):
            crypt = crypt + cipherLetter(text[i],cylinder[key[i]])
        return crypt


def uncipherText(cylinder,key,text):
    n = len(cylinder)
    uncrypt = ""
    if not keyOK(key,n):
        return False
    else:
        for i in range(len(text)):
            uncrypt = uncrypt + uncipherLetter(text[i],cylinder[key[i]])
        return uncrypt




createCylinder(test,len(achi))
dico = loadCylinder("MP-1ARI.TXT")
print(dico)
key = [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]
text = uncipherText(dico,key,achi)
print(text)

