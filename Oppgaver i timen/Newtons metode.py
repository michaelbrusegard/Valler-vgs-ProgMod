# Using Newtons Method to find where x is null

"""
Hvis vi har en tangentlinje til en funksjon i et punkt (x^1, f(x^1))
og (x, y) er et tilfeldig punkt på tangenten, da er :
# y - f(x^1) = f'(x^1) (x - x^1)

Bevis: Her er:
a = Δy / Δx = (y - f(x^1)) / (x - x^1)
Siden tangent, er a = f'(x^1). Dette gjør f'(x^1) = (y - f(x^1)) / (x - x^1) ⇒ y - f(x^1) = f'(x^1) (x - x^1)

La f(x) = x^2 - 11, når x = {3, 4}
Tangent  når x = 7
y - f(7) = f'(7) * (x - 7)
y = 14x - 60

Finner nullpunktet til tangent:
y = 0
14x = 60
x = 30 / 7

GJENTA ALT DETTE, ved å bytte 7 med 30 / 7

"""

# variables
D_f = [-100, 100]
decimals = 3
roots = []
failMargin = 10 ** - decimals
n = D_f[1]
run = True


# function
def f(x):
    return x ** 5 - x + 1


def f_derived(x):
    return (f(x + failMargin) - f(x)) / failMargin


while run:
    while abs(f(n)) > failMargin:
        n = n - f(n) / f_derived(n)
    roots.append(n)

    for i in range(0, len(roots)):
        round(roots[i], decimals)
    print(roots)
    run = False
