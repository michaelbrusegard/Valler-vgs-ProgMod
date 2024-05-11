#Oppgave 19
def summen(feilMargin):
    svar = 0
    e = 1
    while svar <= 1 - feilMargin:
        svar += 1 / 2 ** e
        e += 1
    return svar

print(summen(0.0001))

#Oppgave 18
def fortegn(n):
    if n < 0:
        return -1
    else:
        return 1

ListeTall = [-1, 2, 3, 0]