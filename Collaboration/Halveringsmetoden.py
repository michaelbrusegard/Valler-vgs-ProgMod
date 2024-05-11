"""
Notater:

Funksjonen er x ** 2 - 36.

Positiv = 200
negativ = -2
"""

def f(x):
    return x ** 2 - 36

def gjennomsnitt(P, N):
    return (P + N) / 2

def halveringsMetoden(pos, neg, h):
    a = 0
    while abs(f(a)) > h:
        a = gjennomsnitt(pos, neg)
        if f(a) < 0 :
            neg=a
        else :
            pos=a
    return a

print(round(halveringsMetoden(200, -2, 0.001), 2))