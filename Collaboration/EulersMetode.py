"""
Notater:
f'(x) = (f(x+h)+f(x))/h

f(x+h)-f(x) = h*f'(x)
f(x+h) = h*f'(x)+f(x)

y' = 1 + x * y

Vi skal finne punkter å tegne en grad til at innitialbetingelsen er f(5) = 1, og funksjonen til den deriverte er y'= 1/2 * y + 8x ** 2 + 2 x + 1
x = 5
y = 1
h = 0.001
"""

import math

def y_derivert(x, y):
    return (0.5 * y ** 2 - 50 * 9.81) / 50

def eulersMetode(x, y, h, punkter):
    x_list = []
    y_list = []
    for i in range(punkter * int(10 ** - math.log10(h))):
        x_list.append(x)
        y_list.append(y)
        y = h * y_derivert(x, y) + y
        x += h
    return x_list, y_list

eulersMetode(0, 0, 0.001, 100)