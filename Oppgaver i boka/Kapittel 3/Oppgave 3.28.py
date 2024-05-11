from math import log10

def ph(konsentrasjon):
    return -1*log10(konsentrasjon)

h3o = float(input("skriv inn konsentrasjonen av H3O+:"))
ph = ph(h3o)
print(ph)