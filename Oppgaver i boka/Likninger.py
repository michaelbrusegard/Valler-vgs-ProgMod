feilMargin = 1      # Hvor feilmarginen er mengden x skal øke med før det skal gjøres en ny utregning
x = 0       # Intialbetingelsen sier at x = 0
y = 2       # og y er 2
punkter = []        # Liste med punktene den har regnet ut

def y_derivert(x, y):
    return 1 + x * y        # Den oppgitte funksjonen for den deriverte

def eulersMetode(x, y):
    return y + y_derivert(x, y) * feilMargin        # Eulers metode

for i in range(1, 8):
    punkter.append((x, y))      # Legger til de utregnete punktene i en liste
    y = eulersMetode(x, y)      # Setter den nye y-verdien
    x += feilMargin     # Finner den neste x-verdien å regne ut for

print(punkter)