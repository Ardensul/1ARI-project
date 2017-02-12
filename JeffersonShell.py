import random

test = "test.txt"
achi = "GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS"

def convertLetters(text):
    conv = ""  #création d'une variable permetant la convertion
    text = text.upper() #mise en majuscule du texte a convertir
    for i in range(len(text)):  #boucle traitant tout les carractère de text
        if 65 <= ord(text[i]) <= 90: #si la lettre est déjà une lettre majuscule non accentuée, la rajoute à conv
            conv = conv + text[i]
        elif 192 <= ord(text[i]) <= 197: #si la lettre est un A accentué rajoute un A à conv
            conv = conv + "A"
        elif 200 <= ord(text[i]) <= 203: #si la lettre est un E accentué rajoute un E à conv
            conv = conv + "E"
        elif 204 <= ord(text[i]) <= 207: #si la lettre est un I accentué rajoute un I à conv
            conv = conv + "I"
        elif 210 <= ord(text[i]) <= 214: #si la lettre est un O accentué rajoute un O à conv
            conv = conv + "O"
        elif 217 <= ord(text[i]) <= 220: #si la lettre est un U accentué rajoute un U à conv
            conv = conv + "U"

    text = conv #remplace la variable text par une chaine de caractère en majuscule non accentué et sans espace ni ponctuation
    return text


def mix():
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #liste contenant toutes les settres de l'alphabet
    melange = "" #création d'une variable qui serra une permutation d' l'alphabet
    while len(alpha) != 0: #une boucle qui tant que il y a une lettre dans alpha continu
        x = random.randint(0,len(alpha)-1) #créé un nombre alléatoire entre 0 et la longeur de l'alphabet encore présent
        melange = melange + alpha[x] #ajout de la lettre a l'indice x (tirré aléatoirement a ligne 31) a la variable melange
        alpha.remove(alpha[x]) #supression de la lettre choisie de la listte alpha
    return melange #renvoie une permutation sans repetition de l'alphabet


def createCylinder(file,n):
    save = open(file,"w") #ouvre le fichier qui contiendra les cylindres
    for i in range(n): #boucle qui permet la création de n cylindre
        cil = mix() + "\n" #créé une chaine de caractère contenant une permutation sans répétition de l'alphabet fini du carractère d'échapement \n
        save.write(cil) #écrit dans le fichier la permutation de l'alphabet genérée
    save.close() #fermeture du fichier


def loadCylinder(file):
    cylinder = {} #création d'un dictionnaire vide
    load = open(file,"r") #ouverture en lecture seule du fichier contenant les cylindres
    general = load.readlines() # création d'une liste où chaque ellement correspond a une permutation de l'alphabet finisant pas \n
    indice = 1 #innicialisation du générateur de clef du dictionaire
    for i in range(len(general)): #boucle créant l'ensemble du dictionnaire
        value = general[i] #récupération de la chaine de caractère à l'indice i
        value = value[0:26] #supression du caractère \n des permutation sans répétition de l'alphabet
        cylinder[indice]=value #création de la valeur associer a la clef "indice" dans le dictionaire
        indice += 1 #ajoute 1 a l'indice
    load.close() #ferme le fichier
    return cylinder #retourne le dictionaire ayant en clef le numéro du cylindre et la permutation associé


def keyOK(key,n):
    for i in range(1,n+1): #boucle allant de 1 jusqu'a l'entier n compris
        occu = key.count(i) #conte le nombre de fois que l'entier i est présent dans la liste key
        if occu != 1: # si l'entier i est présent  plus de 1 fois ou n'est pas présent retourne False
            return False
        else: #Sinon continu la boucle
            continue
    return True #si les entier compris entre 1 et n sont présent une seul et unique fois alors retourne True


def createKey(n):
    listN = [] #création d'un liste qui contiendra tout les entien entre 1 et n
    key = [] #création d'une liste qui sera la clef de cryptage et decodage
    for i in range(1,n+1): #boucle allant de 1 à n
        listN.append(i) # ajout de l'entier i a la liste
    while len(listN) != 0: #boucle créant la clef
        x = random.randint(0,len(listN)-1) #créé un nombre alléatoire correspondant a l'indice d'un entier compris entre 1 et n
        key.append(listN[x]) #ajout de l'entier a l'indice x de listeN à la clef
        listN.remove(listN[x]) # supprétion de l'entier a l'indice x de la liste listN
    return key #retourne la clef composé d'une permutation sans répétition des entien de 1 à n


def find(letter,alphabet):
    for i in range(len(alphabet)): #boucle parcourant la permutation sans repetition de l'alphabet
        if letter == alphabet[i]: #si la lettre cherché correspond dans la permutation sans répétition de l'alphabet
            return i #retourne i qui est l'indice de la lettre
        else: #sinon
            continue #continu la boucle


def shift(i):
    if 0 <= i <= 25: #si i est pompris entre 0 et 25 compris
        a = (i+6)%26 # a est congru a i+6 modulo 26
        return a #retourne la valeur de a
    else: #sinon
        return -1 #retourne -1


def unshift(i):
    if 0 <= i <= 25: #si i est pompris entre 0 et 25 compris
        a = (i-6)%26 # a est congru a i-6 modulo 26
        return a ##retourne la valeur de a
    else: #sinon
        return -1 ##retourne -1


def cipherLetter(letter,alphabet):
    indice = shift(find(letter,alphabet)) #calcul l'indice de la lettre 6 ligne en dessou de la lettre à crypté
    return alphabet[indice] #retourne la lettre à crypté


def uncipherLetter(letter,alphabet):
    indice = unshift(find(letter,alphabet)) #calcul l'indice de la lettre 6 ligne au dessu de la lettre à décoder
    return alphabet[indice] #retourne la lettre à décoder


def cipherText(cylinder,key,text):
    n = len(cylinder) #récupère le nombre de cylindre
    crypt = "" #création d'une variable qui contiendra le message crypté
    if not keyOK(key,n): #si la clef n'est pas bonne arrete la fonction
        return False
    else: #sinon lance le cryptage
        text = convertLetters(text) #converti le text en suite de lettre majuscule
        for i in range(len(text)): #boucle traitant chaque carractère à crypter
            crypt = crypt + cipherLetter(text[i],cylinder[key[i]]) #ajoute la lettre crypté a crypt
        return crypt #retourne le message entièrement crypté


def uncipherText(cylinder,key,text):
    n = len(cylinder) #récupération du nombre de cylinde
    uncrypt = ""  #création d'une variable qui contiendra le message décodé
    if not keyOK(key,n): #si la clef n'est pas valide arrete la fonction
        return False
    else: #sinon lance le décodage
        for i in range(len(text)): #boucle traitant tout les carractère a décodé
            uncrypt = uncrypt + uncipherLetter(text[i],cylinder[key[i]]) #ajout de la lettre décodé à uncrypt
        return uncrypt #retour du message en claire




createCylinder(test,len(achi))
dico = loadCylinder("MP-1ARI.TXT")
print(dico)
key = [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]
text = uncipherText(dico,key,achi)
print(text)

