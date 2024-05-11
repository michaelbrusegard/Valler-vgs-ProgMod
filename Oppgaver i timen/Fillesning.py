import os
"""f = open(os.path.join('Oppgaver i timen', 'Tekster'), "operasjon.txt","w+")
f.write("Her er noe nytt")
liste = ["iskrem", "kake", "trening", "fotball"]
for x in liste:
    f.write(x+"/n")
f.close()

f = open(os.path.join('Oppgaver i timen', 'Tekster'), "operasjon.txt","r")
data = f.readlines()
f.close()

print(data[0])"""

#Oppgave 1
#a) Det er nødvendig å lagre data til en fil for at et program skal kunne vite hva som har skjedd etter at det er lukket til neste gang du starter det igjen.
#b) I alle applikasjoner og spill hvor du ønsker å lagre progresjonen.

#Oppgave 2
"""f = open(os.path.join('Oppgaver i timen', 'Tekster'), "minFeteFil.txt", "w+")
#b) Det blir laget en txt fil som heter minFeteFil
#c) Bytter jeg ut navnet så vil den lage en ny txt med det nye navnet
f.write("Her er noe tekst til filen min..")
f.write("Enda mer tekst..!")
f.close()"""
#g) Teksten blir lagt til i tekstfilen.
"""import math
def eulerTallet(feilMargin) :
    n = 1000
    while abs(math.e-(1+1/n)**n) > feilMargin :
        n *= 10
        e = (1 + 1 / n)**n
    return e
k = eulerTallet(0.001)

t = open(os.path.join('Oppgaver i timen', 'Tekster'), "Eulertallet.txt", "w+")
t.write(str(k))"""

#Oppgave 3
"""f = open(os.path.join('Oppgaver i timen', 'Tekster'), "hvorErFilaMi.txt", "w+")
f.write("Michael er kul.")
f.close()

f = open(os.path.join('Oppgaver i timen', 'Tekster'), "hvorErFilaMi.txt", "r")
data = f.read()
print(data)"""