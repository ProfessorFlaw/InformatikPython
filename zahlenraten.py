import random

z = random.randint(0,100)
g = 0
versuche = 0

print("Gesucht ist eine Zahl von 0 bis 100.")
while g == 0:
    versuche += 1
    x = int(input("Rate eine Zahl:"))
    if x == z:
        print("Gewonnen!")
        print("Versuche: ", versuche)
        g = 1
    elif x < z:
        print("Deine Zahl ist zu klein.")
        print("Versuche es nochmal!")
    else:
        print("Deine Zahl ist zu groß.")
        print("Versuche es nochmal!")
    
