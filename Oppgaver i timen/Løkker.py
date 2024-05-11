"""for i in range(0,25):
    print("Michael")"""

"""passord = "JegErKul1"
tekst = input("Skriv inn passordet: ")
feilsvar=0
while tekst != passord and feilsvar<5:
    feilsvar += 1
    tekst = input("Feil passord. Prøv igjen:")
    if feilsvar == 3:
        print("Hint: Første bokstav er J.")

print("Du har knekket passordet.")"""

#Oppgave 1
"""for m in range(0,1000):
    print("Michael")
    a=0
for t in range (0,101):
    print(a)
    a += 1"""

#Oppgave 2
"""tall = str(69)
tekst = input("Gjett et tall mellom 0 og 100 ellers blir jeg sur:")
while tekst != tall:
    tekst = input("Feil svar. Prøv på nytt hihi:")
print("Du vet hvorfor du har riktig.")"""

#Oppgave 3
""""(a). Det var lurt å bruke en for-løkke i oppgave 1 fordi det er noe som skal gjenta seg 1000 ganger.
(b). Jeg brukte while-løkke i oppgave 2 fordi da vil den gjenta spørsmålet helt til svaret er riktig.
(c). Den store forskjellen på for og while er at med for må du definere et område."""

#Oppgave 4
"""for i in range (0,101):
    print(2*i)
for u in range (0, 51):
    print((u)**0.5)"""

#Oppgave 5
"""n = int(input("Skriv inn n:"))
if n == 0:
    print("0! er 1.")
elif n == 1:
    print("1! er 1.")
else:
    produkt = 1
    for i in range(1, n+1):
        produkt *= i
    print("n! er", produkt)"""

"""for x in range(-100,100,1):
    print("f("+str(x)+")="+str(x**3-1))"""
#Lekse
elevid = int(input("Skriv din ElevID:"))

if elevid <= 1 or elevid >= 999:
    print()
elif elevid == 444 or elevid == 666:
    print("Sensur! Denne ElevID-en er ikke tillatt.")
else:
    print("Dette er din Elev ID:", elevid)

kjæledyr = ["hund", "katt", "hest", "hamster"]

for x in range (0,4):
     print(kjæledyr[2])

a = int(input("Tast inn et heltall!"))
if a < 10:
    print( str(a) + "hei")