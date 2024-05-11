#[Skjæringsetningen] Hvis f(a) og f(b) har ulike fortegn og f er kontinuerlig, da har f minst et nullpunkt når x = {a, b}
#[Halveringsmetoden] Hvis f(a) og f(b) har ulike forteg  let etter nullpunktet. Regne ut f((a + b) / 2 ). Hvis f((a + b) / 2 ) = 0, da er vi ferdige. Eller, fortsett

#Input
feilmargin = 0.001
definisjonsmengde = [-100, 100]

#Variabler
a = 0
b = 0
entRun = True
nullpunkt = []

#Funksjon
def f(x):
    return x ** 5 + 3 * x ** 2 - 1

while entRun:
    #Finner a og b
    for i in range(definisjonsmengde[0], definisjonsmengde[1] + 1):
        p = f(i)
        if p < 0:
            a = i

    for i in range(definisjonsmengde[1], a, -1):
        p = f(i)
        if p > 0:
            b = i

    if f(a) * f(b) >= 0 and f(b) != 0 and f(a) != 0:
        for i in range(definisjonsmengde[1], definisjonsmengde[0] - 1, -1):
            p = f(i)
            if p > 0:
                b = i

    if f(a) * f(b) > 0:
        entRun = False
        if not nullpunkt:
            print("Funksjonen har ingen nullpunkter i definisjonsmengden:", str(definisjonsmengde[0]) + ",", str(definisjonsmengde[1]) + ".")

    else:
        m = (a + b) / 2

        while abs(f(m)) - feilmargin > 0 or f(m) == 0:
            if f(m) > 0:
                b = m
            else:
                a = m
            m = (a + b) / 2

        nullpunkt.append(m)

        if a > b:
            definisjonsmengde[1] = int(b - 1)
        else:
            definisjonsmengde[1] = int(a - 1)

nullpunkt.sort()
print("Funksjonen har nullpunktet", str(nullpunkt), "i definisjonsmengden:", str(definisjonsmengde[0]) + ",", str(definisjonsmengde[1]) + ".")








#LÆRER FORKLARING GREIE

def gjennomsnitt(a, b):
    return (a + b) / 2

c = gjennomsnitt(a, b)

def halveringsmetoden(a, b, feilMargin):

    while abs(f(c)) > feilMargin or f(c) == 0:

        #Tilfelle 1: f(a) og f(c) har ulike fortegn.
        #Tilfelle 2: f(a) og f(c) har like fortegn.

        if f(a) * f(c) < 0:
            b = c

        else:
            a = c

        c = gjennomsnitt(a, b)

    return c

