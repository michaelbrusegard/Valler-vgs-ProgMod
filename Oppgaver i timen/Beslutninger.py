#Oppgave 1 & 2
"""brus = input(str("Har du lyst på brus?"))

if brus == "ja" or brus == "Ja":
    print("Her har du en brus!")
elif brus == "nei" or brus == "Nei":
    print("Den er grei.")
else:
    print("Det forsto jeg ikke helt.")"""

#Oppgave 5
poengsum = 0
a = input("Hva er hovedstaden i Norge?")

if a == "Oslo" or "oslo":
    poengsum += 1

b = input("Hva er nasjonalretten i Norge?")

if b == "Fårikål" or "fårikål":
    poengsum += 1

c = input("Bruker vi olje til å lage asfalt?")

if c == "Ja" or "ja":
    poengsum += 1

print("Du fikk:", poengsum, "riktige svar.")
