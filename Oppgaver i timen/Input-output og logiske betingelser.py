import random
import math
#03 - Input-output og logiske betingelser
#Oppgave 1
"""subjekt = ["Du", "Jeg", "Vi", "Dere", "Michael"]
verbal = ["spiser", "programmerer", "regner", "tenker"]
direkte_objekt = ["ofte", "dårlig", "sakte", "stygt"]
x = subjekt[random.randint(0,len(subjekt)-1)]
y = verbal[random.randint(0,len(verbal)-1)]
z = direkte_objekt[random.randint(0,len(direkte_objekt)-1)]
print(x, y, z+".")"""

#Oppgave 2
"""m = float(input("Hva er massen?"))
c = float(input("Hva er  hastigheten?"))
E = m*(c**2)
print("Energien er,", E, "Joule.")

v = float(input("Hva er farten?"))
t = float(input("Hva er tiden?"))
s = v*t
print("Strekningen er:", s, "meter.")

a = float(input("Hva er a?"))
b = float(input("Hva er b?"))
c = float(input("Hva er c?"))
c = float(input("Hva er x?"))
y = (a*x**2+b*x+c)
print("y er:", y+".")"""

#Oppgave 3
"""liste = []
mat = input("Hva vil du spise i dag?")
liste.append(mat)
mat = input("Hva vil du spise i dag?")
liste.append(mat)
mat = input("Hva vil du spise i dag?")
liste.append(mat)
print(liste, len(liste))"""

#Oppgave 4
"""n = float(input("Skriv inn et tall: "))
if n > 0 and n != 1337:
    print("Positivt tall!")
elif n == 1337:
    print("Favoritt tall!")
elif n == 0:
    print("Dette er null.")
else:
    print("Negativt tall!")"""

"""a=float(input("Skriv inn ett tall:"))
b=float(input("Skriv inn ett til tall:"))
if a == b:
    print("Tallene er like.")
else:
    print("Tallene er ikke like.")"""

#Oppgave 8
"""a = float(input("Hva er a:"))
b = float(input("Hva er b:"))
c = float(input("Hva er c:"))
z = float((b**2-4*a*c))
x_1 = -b +z**0.5/2*a
x_2 = -b -z**0.5/2*a
if z<0:
    print("Ingen løsning.")
elif z==0:
    print("En løsning:", "x="+str(x_1))
else:
    print("To løsninger:", "x="+str(x_1), "V", "x="+str(x_2))"""

#Oppgave 9
"""a = float(input("Hvor mange oksonionioner er det?"))
a = math.log(1/a)
if a<7:
    print(str(a)+"pH", "Væsken er sur.")
elif a==7:
    print(str(a)+"pH", "Væsken er nøytral.")
else:
    print(str(a)+"pH", "Væsken er basisk.")"""


