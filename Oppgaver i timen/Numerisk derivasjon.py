import matplotlib.pyplot
import math
import os

x_aksen = []
y_aksen = []

"""def f(a):
    return a ** 2

def f_derivert(a):
    delta_x = - 0.00000000001
    return (f(a + delta_x) - f(a)) / delta_x

for i in range(1, 100):
    x_aksen.append(i)
    y_aksen.append(f_derivert(i))


matplotlib.pyplot.grid()
matplotlib.pyplot.title("f'")
matplotlib.pyplot.plot(x_aksen, y_aksen)
matplotlib.pyplot.show()

print(f(3), f_derivert(3))"""

#Oppgave 1

"""def favorittfunksjon(x):
    return ((x + 2) ** 2 // 45) * x ** 3 + math.log2(x) - math.sin(x * 45 / 3) * math.tan(x + 80)

def favoritt_derivert(x):
    delta_x = - 0.00000000001
    return (favorittfunksjon(x + delta_x) - favorittfunksjon(x)) / delta_x

""""""grafen til den deriverte
for i in range(1, 5):
    b = i * 2
    x_aksen.append(b)
    y_aksen.append(favoritt_derivert(b))"""

"""grafen til favorittfunksjonen  """"""
for i in range(1, 5):
    b = i * 2
    x_aksen.append(b)
    y_aksen.append(favorittfunksjon(b))


matplotlib.pyplot.grid()
matplotlib.pyplot.title("f")
matplotlib.pyplot.plot(x_aksen, y_aksen)
matplotlib.pyplot.show()

print(favoritt_derivert(124))

f = open(os.path.join('Oppgaver i timen', 'Tekster'), "favoritt_derivert.txt","w")
f.write(str(y_aksen))"""

"""def f(a):
    return 3 * a ** 2

def fDerivert(a, deltaX):
    return ((f(a + deltaX)) - f(a)) / deltaX

xVerdier = []
funksjonsverdier = []
deriverteverdier = []

fil = open("os.path.join('Oppgaver i timen', 'Tekster'), funksjon.txt", "w+")
fil.write(str(funksjonsverdier))

for i in range(0, 9, 2):
    xVerdier.append(i)
    funksjonsutregning = f(i)
    funksjonsverdier.append(funksjonsutregning)
    deriverteverdier.append(fDerivert(i, 0.0001))
    fil.write(str(funksjonsutregning))

fil.write(str(funksjonsutregning))
fil.close()

matplotlib.pyplot.grid()
matplotlib.pyplot.plot(xVerdier, funksjonsverdier)
matplotlib.pyplot.show()"""

#Oppgave 2
#a) Dette er det samme som å derivere vanlig siden når b --> a så er b - a det samme som deltaX
#b) h er deltaX
#c) h er deltaX men den dobbles

#Oppgave 4
# Du finner vekstfarten til et interval som er så lite som et punkt som er gjennomsnitlig vekst i det punktet

def f(a):
    return 3 * a ** 2

def dobbeltDerivert(x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2

def fDerivert(a, deltaX):
    return ((f(a + deltaX)) - f(a)) / deltaX

import numpy
import scipy.io.wavfile
fs, DATATEST = scipy.io.wavfile.read(os.path.join('Oppgaver i timen','Lyder', "so1.wav"))

x = []
y = []
xderivert = []
yderivert = []

for i in range(1, 44100):
    x.append(numpy.array(DATATEST[i][0], dtype=float))
    y.append(numpy.array(DATATEST[i][1], dtype=float))
    xderivert.append(numpy.array(fDerivert((DATATEST[i][0]), 0.001)))
    yderivert.append(numpy.array(fDerivert((DATATEST[i][1]), 0.001)))

matplotlib.pyplot.grid()
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(xderivert, yderivert)
matplotlib.pyplot.show()

DATATEST = fDerivert(DATATEST, 0.001)

data = numpy.random.uniform(-30000, 30000, 44100) # 44100 random samples between -1 and 1
scaled = numpy.int16(data/numpy.max(numpy.abs(DATATEST)) * 32767)
scipy.io.wavfile.write(os.path.join('Oppgaver i timen', 'Lyder', 'out1.wav'), 44100, DATATEST)


"""
print("Lydfil:\n", DATATEST)"""

"""mim = fDerivert(DATATEST, 0.1)
mam = dobbeltDerivert(DATATEST, 0.1)
print("Derivert:\n", mim)
print("DobbeltDerivert:\n", mam)

scipy.io.wavfile.write(os.path.join('Oppgaver i timen', 'Lyder', 'test.wav'), 44100, mim)

""""""matplotlib.pyplot.grid()
matplotlib.pyplot.plot(DATATEST, y_aksen)
matplotlib.pyplot.show()""""""

data = numpy.random.uniform(-30000, 30000, 44100) # 44100 random samples between -1 and 1
scaled = numpy.int16(data/numpy.max(numpy.abs(data)) * 32767)"""