from time import sleep
r = 0
sv = 0
ap = 0
sp = 0
mdg = 0
krf = 0
v = 0
h = 0
frp = -100
navn = input("Skriv inn fornavnet ditt:")
print("Hei,", navn, "så hyggelig at du ville prøve denne valgautomaten. Det partiet du får er det du burde stemme på i valget hvis du er smart. Lykke til!")
sleep(5)
print("På hvert spørsmål vil du få flere valg, for å svare velger du bokstaven knyttet til alternativet du syns passer best. (A, B, C, D, E, osv...)")
sleep(5)
print("La oss starte...")
sleep(2)

startS1PåNytt = True
startS2PåNytt = True
startS3PåNytt = True
startS4PåNytt = True

while startS1PåNytt == True:
    s1 = input("Liker du Erna solberg?\n""A) Ja, veldig godt.\n""B) Litt.\n""C) Liker hun ikke.\n""D) Hater hun.\n")
    if s1 == "a" or s1 == "A":
        h += 20
        frp += 10
        r -= 10
        sv -= 10
        ap -= 5
        mdg -= 15
        v += 7
        krf += 3
        sp -= 12
        startS1PåNytt = False
    elif s1 == "b" or s1 == "B":
        r -= 7
        sv -= 5
        ap -= 2.5
        sp -= 5
        mdg -= 7
        krf += 0
        v += 3
        h += 10
        frp +=5
        startS1PåNytt = False
    elif s1 == "c" or s1 == "C":
        r += 2
        sv += 1
        ap += 2.5
        sp += 2
        mdg += 7
        krf += 0
        v -= 3
        h -= 10
        frp -= 5
        startS1PåNytt = False
    elif s1 == "d" or s1 == "D":
        h -= 20
        frp -= 10
        r += 10
        sv += 10
        ap += 5
        mdg += 15
        v -= 7
        krf -= 3
        sp += 8
        startS1PåNytt = False
    else:
        print("Det er ikke et gyldig svar, prøv på nytt.")
        sleep(4)

    while startS2PåNytt == True:
        s2 = input("Hva tenker du om flyktninger?\n""A) Hjelpe dem der de er.\n""B) Gi beskytelse til de som har behov for det, og returnere de som ikke har et slikt behov. \n""C) Ta i mot alle flyktninger, spesielt ivareta de yngre.\n""D) Oprette et felles eurpopeisk system.\n""E) Ta i mot flere flyktninger i større mengder.\n")
        if s2 == "a" or s2 == "A":
            h += 5
            frp += 30
            r -= 10
            sv -= 10
            ap -= 10
            mdg -= 10
            v += 0
            krf += 0
            sp -= 10
            startS2PåNytt = False
        elif s2 == "b" or s2 == "B":
            r += 10
            sv += 5
            ap += 15
            sp += 5
            mdg -= 7
            krf += 4
            v += 3
            h += 15
            frp -= 10
            startS2PåNytt = False
        elif s2 == "c" or s2 == "C":
            r += 25
            sv += 20
            ap += 10
            sp += 15
            mdg += 8
            krf -= 5
            v -= 3
            h -= 5
            frp -= 20
            startS2PåNytt = False
        elif s2 == "d" or s2 == "D":
            h -= 10
            frp -= 5
            r += 5
            sv += 20
            ap += 5
            mdg += 15
            v -= 7
            krf -= 3
            sp += 20
            startS2PåNytt = False
        elif s2 == "e" or s2 == "E":
            h -= 15
            frp -= 25
            r += 10
            sv += 10
            ap -= 5
            mdg -= 10
            v += 5
            krf -= 10
            sp += 10
            startS2PåNytt = False
        else:
            print("Det er ikke et gyldig svar, prøv på nytt.")
            sleep(4)

while startS3PåNytt == True:
    s3 = input("Hva skal navnet på religions og etikk faget være?\n""A) Bare kristendom fordi det er den viktigste religionen.\n""B) KRLE, Alt er like mye verdt, men kristendom er litt mer viktig.\n""C) RLE, like mye om alle religioner og livssyn.\n""D) LE, fuck religion...\n""E) Bare etikk, religioner og livssyn tilhører fortiden.\n")
    if s3 == "a" or s3 == "A":
        h += 10
        frp += 15
        r -= 10
        sv -= 10
        ap -= 10
        mdg -= 10
        v += 0
        krf += 30
        sp -= 10
        startS3PåNytt = False
    elif s3 == "b" or s3 == "B":
        r -= 10
        sv -= 10
        ap += 0
        sp += 5
        mdg -= 10
        krf += 5
        v += 5
        h += 15
        frp += 10
        startS3PåNytt = False
    elif s3 == "c" or s3 == "C":
        r += 10
        sv += 15
        ap += 5
        sp += 0
        mdg += 10
        krf += -5
        v += 0
        h += -5
        frp += -10
        startS3PåNytt = False
    elif s3 == "d" or s3 == "D":
        h += -10
        frp += -15
        r += 0
        sv += 10
        ap += 5
        mdg += 10
        v += 15
        krf += -30
        sp += 5
        startS3PåNytt = False
    elif s3 == "e" or s3 == "E":
        h += -10
        frp += -20
        r += 10
        sv += 5
        ap += 0
        mdg += 5
        v += -10
        krf += -30
        sp += -5
        startS3PåNytt = False
    else:
        print("Det er ikke et gyldig svar, prøv på nytt.")
        sleep(4)

while startS4PåNytt == True:
    s4 = input("Hvor mye er mennesket verdt?\n""A) 100kr.\n""B) Alle er like mye verdt.\n""C) De som har høyest lønn er mest verdt.\n""D) Nyrer og blod.\n""E) Relgiøse ledere er mer verdt.\n")
    if s4 == "a" or s4 == "A":
        h += 10
        frp += 15
        r -= 10
        sv -= 10
        ap -= 10
        mdg -= 10
        v += 0
        krf += 30
        sp -= 10
        startS4PåNytt = False
    elif s4 == "b" or s4 == "B":
        r += 10
        sv += 5
        ap += 15
        sp += 5
        mdg -= 7
        krf += 4
        v += 3
        h += 15
        frp -=10
        startS4PåNytt = False
    elif s4 == "c" or s4 == "C":
        r += 25
        sv += 20
        ap += 10
        sp += 15
        mdg += 8
        krf -= 5
        v -= 3
        h -= 5
        frp -= 20
        startS4PåNytt = False
    elif s4 == "d" or s4 == "D":
        h -= 10
        frp -= 5
        r += 5
        sv += 20
        ap += 5
        mdg += 15
        v -= 7
        krf -= 3
        sp += 20
        startS4PåNytt = False
    elif s4 == "e" or s4 == "E":
        h -= 15
        frp -= 25
        r += 10
        sv += 10
        ap -= 5
        mdg -= 10
        v += 5
        krf -= 10
        sp += 10
        startS4PåNytt = False
    else:
        print("Det er ikke et gyldig svar, prøv på nytt.")
        sleep(4)

print("Er du spendt på hvilket parti som passer deg best...")
sleep(2)
print("drumroll...")
sleep (2)
print("det er...")
sleep(1)
if h >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Høyre")
elif frp >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Fremskritspartiet")
elif r >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Rødt")
elif sv >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Sosialistisk venstreparti")
elif ap >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Arbeiderpartiet")
elif mdg >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Miljøpartiet de grønne")
elif v >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Venstre")
elif krf >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Kristlig folkeparti")
elif sp >= max(h, frp, r, sv, ap, mdg, v, krf, sp):
    print("Senterpartiet")



