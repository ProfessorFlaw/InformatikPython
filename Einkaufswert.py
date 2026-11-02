einkaufswert = float(input("Bitte geben Sie den Einkaufswert ein: "))
betrag = 0
if einkaufswert > 100:
    if einkaufswert > 500:
        betrag = einkaufswert * 0.9
    else:
        betrag = einkaufswert * 0.95
print(betrag)