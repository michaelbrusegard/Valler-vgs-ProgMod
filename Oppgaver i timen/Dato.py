#Oppgave 1 & 2
måned_1 = int(input("Skriv en måned:"))
dag_1 = int(input("Skriv en dag:"))
måned_2 = int(input("Skriv en måned til:"))
dag_2 = int(input("Skriv en dato til:"))

if måned_1<måned_2:
    if dag_1<dag_2:
        print("Riktig rekkefølge!")
elif måned_1==måned_2:
    if dag_1==dag_2:
        print("Samme dato!")
else:
    print("Feil rekkerfølge!")