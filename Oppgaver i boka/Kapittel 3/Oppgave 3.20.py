def f(x):
    return 1/(2*x) + 1
print("f(x) =",f(4))


from math import cos, radians
def g(x):
    return 3*x + cos(radians(x))

y = float(input("Skriv inn verdi for x:"))
print("g(x) =",g(y))

def G(t):
    a = t**2 - 2
    return a

t = 1
print(G(t))

