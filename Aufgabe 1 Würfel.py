import random

versuche = 0
fertig = False
gewürfelt = 0

while fertig == False:
    versuche += 1
    gewürfelt = random.randint(1,6)
    print(gewürfelt)
    if gewürfelt == 6:
        fertig = True
        print("Du hast ", versuche, " Versuche gebraucht.")