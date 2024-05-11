def Veiformel2(tid,startfart,akkselerasjon):
    strekning=tid*startfart+0.5*akkselerasjon*tid**2
    return strekning
def Tidløsformel(startfart,akkselerasjon,strekning):
    fart=(startfart**2+2*akkselerasjon*strekning)**0.5
    return fart

variabel = input("Hva vil du finne ut? (strekning eller fart)")
if variabel == "strekning":
    a = float(input("Hva er tiden i sekunder:"))
    b = float(input("Hva er startfarten i meter per sekund:"))
    c = float(input("Hva er akkselerasjonen i meter per sekund i annen:"))
    print(Veiformel2(a,b,c))
elif variabel == "fart":
    a = float(input("Hva er startfarten i meter per sekund:"))
    b = float(input("Hva er akkselerasjonen i meter per sekund i annen:"))
    c = float(input("Hva er strekningen i meter?"))
    print(Tidløsformel(a,b,c))
else:
    print("Du skrev ikke riktig.")