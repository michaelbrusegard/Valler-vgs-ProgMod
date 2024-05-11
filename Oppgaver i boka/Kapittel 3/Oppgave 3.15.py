godteritype = input("sur sild, melkesjokolade eller potetgull? Skriv den du vil ha:")
penger = float(input("Hvor mye penger har du?"))

if godteritype == "sur sild":
    rest = penger % 16
    antall = (penger - rest) / 16

elif godteritype == "melkesjokolade":
    rest = penger % 25
    antall = (penger - rest) / 25

elif godteritype == "potetgull":
    rest = penger % 20.5
    antall = (penger - rest) / 20.5

else:
    print("Illegitim godteritype.")
print("Du får", antall, "av", godteritype, "med", rest, "kr i rest.")