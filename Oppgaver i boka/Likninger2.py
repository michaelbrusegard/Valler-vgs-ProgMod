import matplotlib.pyplot
import math

def y_derivert(x, y):
    return 1/2 * y + 8 * x ** 2 + 2

def defMengde(deltaX):
    return 0, 2 * int(10 ** -math.log10(deltaX))

def plottSvar(x_verdier, y_verdier):
    matplotlib.pyplot.plot(x_verdier, y_verdier)
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()

def eulersMetode(x, y, deltaX):
    x_verdier = []
    y_verdier = []
    for i in range(defMengde(deltaX)[0], defMengde(deltaX)[1]):
        y_verdier.append(y)
        x_verdier.append(x)
        y = y + y_derivert(x, y) * deltaX 
        x += deltaX
    plottSvar(x_verdier, y_verdier)

eulersMetode(5, 1, 0.001)