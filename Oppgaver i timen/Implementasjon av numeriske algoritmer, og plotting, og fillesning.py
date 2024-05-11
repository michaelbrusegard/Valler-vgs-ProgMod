#Oppgave 1
"""def sumNaturligeTall(n):
    k = n
    for x in range (1, n):
        k += n - 1
        n -= 1
    return k

print(sumNaturligeTall(3))"""

#Oppgave 2
"""def sumKubikker(n):
    k = n**3
    for x in range(1, n):
        k += (n - 1)**3
        n -= 1
    return k

print(sumKubikker(2))"""

#Oppgave 3
"""def leibnizPi(e):
    pi = 0
    n=1
    t=1
    for i in range(1, e):
        pi += t/n
        t *= -1
        n += 2
    return pi*4
print(leibnizPi(300000000))"""

#Oppgave 4
"""def randisko(a):
    t = 3
    n = 4
    s = 1
    for i in range(1, a):
        s *= t/n
        if i % 3 == 0:
            t += 4
        else:
            t += 2
        if (i+2) % 3 != 0:
            n += 4
    return s
print(randisko(5))
#Nærmer seg mot null"""

#Innlevering 4
#Oppgave 1
"""def minKuleFunksjon(N) :
    Svar = 0
    for i in range(0,N+1):
        Svar += 2**i
    return Svar

print(minKuleFunksjon(10))"""

#Oppgave 2
"""import math
def eulerTallet(feilMargin) :
    n = 1000
    while abs(math.e-(1+1/n)**n) > feilMargin :
        n *= 10
        e = (1 + 1 / n)**n
    return e

print(eulerTallet(0.001))"""

