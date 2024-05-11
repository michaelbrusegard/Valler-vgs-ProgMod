from math import log2, log10
x = float(input("Skriv inn et tall:"))
a = float(input("Skriv inn et tall a:"))
a = log10(x)/log10(a)
x = log2(x)
print(x)
print(a)