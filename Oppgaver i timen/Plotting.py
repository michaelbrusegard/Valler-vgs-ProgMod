import matplotlib.pyplot as plt
from pylab import *

"""x = []
y = []

for i in range(-1000, 1000):
    x.append(i)
    y.append(i**99)

print(x)
print(y)

plt.plot(x, y)
plt.show()"""

#Oppgave 1
"""# x^2 + 2
x = []
y = []

for i in range(-10000, 10000):
    x.append(i)
    y.append(i**2 + 2)

plt.plot(x, y)
plt.grid()
plt.title("Helt ærlig, dette er kult!")
plt.show()"""

"""fag = ["R2","S2","Fysikk 2","Kjemi 2", "Biologi 2"]
antall = [90,45,57,56,23]
antall_min = sort(antall)

pie(antall,labels=fag)
show()
bar(fag,antall)
show()"""

#Oppgave 2
"""karakter = ["6","5","4","3","2","1"]
antall = [10,12,23,45,15,377]
pie(antall,labels=karakter)
show()
bar(karakter,antall)
show()
#Oppgave 3
summen = 0

for i in range(len(karakter)):
    s = antall[i]*int(karakter[1])
    summen = summen + s

print(summen/sum(antall))"""