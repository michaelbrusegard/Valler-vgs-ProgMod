"""
Notater:
tangenter

funksjon = f(x) = x ** 4 + 10 x ** 3 - 15 x ** 2 - 21
Startx er 24
"""

def f(x):
    return x ** 4 + 10 * x ** 3 - 15 * x ** 2 - 21

def derivert(x, h):
    return (f(x+h)-f(x))/h

def newtonsMetode(x, h):
    while abs(f(x)) > h:
        x = x - f(x) / derivert(x, h)
    return x

print(round(newtonsMetode(24, 0.0001), 2))