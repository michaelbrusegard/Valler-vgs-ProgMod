def tid(strekning,fart):
    return strekning/fart
a = float(input("Skriv inn en strekning:"))
b = float(input("Skriv inn en fart:"))
print("Du bruker", tid(a,b), "sekunder.")
