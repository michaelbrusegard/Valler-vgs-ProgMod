def f(a):
    return a + feilMargin

def f_derivert(a):
    return a * f(a)

def eulersMetode(a):
    return f(a) + f_derivert(a) * feilMargin

tall = 3
feilMargin = 1
punkter = []

for i in range(1, 8):
    punkter.append((tall, eulersMetode(tall)))
    tall = f(tall)

print(punkter)