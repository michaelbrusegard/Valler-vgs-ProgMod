
def f(x):
    return x ** 2 - 5

nullpunkt = []
u = True
d_f = [int(input("Minste x-verdi ")), int(input("Største x-verdi "))]

while u:
    a = 0
    b = 0

    for i in range(d_f[0], d_f[1] + 1):
        p = f(i)
        if p < 0:
            a = i

    for i in range(d_f[1], a, -1):
        p = f(i)
        if p > 0:
            b = i

    l = f(a)
    k = f(b)

    if l * k >= 0 and k != 0 and l != 0:
        for i in range(d_f[1], d_f[0] - 1, -1):
            p = f(i)
            if p < 0:
                a = i

        for i in range(d_f[0], a):
            p = f(i)
            if p > 0:
                b = i

    elif l == 0 or k == 0:
        if l == 0:
            nullpunkt.append(a)
        else:
            nullpunkt.append(b)

    if f(a) * f(b) > 0:
        u = False
        if not nullpunkt:
            print("Funksjonen har ingen nullpunkter i definisjonsmengden:", str(d_f[0]) + ",", str(d_f[1]) + ".")

    else:
        n = (a + b) / 2

        while abs(f(n)) - 0.0001 > 0 or f(n) == 0:
            n = (a + b) / 2
            if f(n) > 0:
                b = n
            else:
                a = n

        nullpunkt.append(n)

        if a > b:
            d_f[1] = int(b) - 1
        else:
            d_f[1] = int(a) - 1

nullpunkt.sort()
print("Funksjonen har nullpunktet", str(nullpunkt), "i definisjonsmengden:", str(d_f[0]) + ",", str(d_f[1]) + ".")