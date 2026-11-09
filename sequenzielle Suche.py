n = 10
bereich = [364,872,569,832,569,543,149,672,729,637]
schluessel = input("Schlüssel: ")
i = 0
gefunden = False

while not gefunden and i < n:
    if schluessel == bereich[i]:
        gefunden = True
    else:
        i += 1
if gefunden:
    print("Gefunden an der Stelle ", i)
else:
    print("Element nicht im Suchbereich.")