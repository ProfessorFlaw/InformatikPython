import random

n = 10
Zufallsliste = []
for i in range(n):
    Zufallsliste.append(random.randint(100,999))
print(Zufallsliste)
schluessel = int(input("Schlüssel: ")) 
i = 0
gefunden = False

while not gefunden and i < n:
    if schluessel == Zufallsliste[i]:
        gefunden = True
    else:
        i += 1
if gefunden:
    print("Gefunden an der Stelle ", i, ", also der ", i+1," Eintrag auf der Liste")
else:
    print("Element nicht im Suchbereich.")