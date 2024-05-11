def mol(masse,molmasse):
    return masse/molmasse

stoff = input("Hvilket stoff vil du finne antall mol til?: ")
masse = float(input("Skriv inn massen (gram): "))
molmasse = float(input("Skriv inn molmassen (gram/mol): "))
mol = mol(masse,molmasse)
print("Stoffet",stoff,"består av",mol,"mol.")