# Innlevering 1
# Oppgave 1
# Her definerer jeg funksjonen fotballresultat
def fotballresultat(hjemmeLag, borteLag, hjemmeMål, borteMål):
    # Hvis hjemmeMål er større enn borteMål så returnerer jeg hjemmeLag
    if hjemmeMål > borteMål:
        return hjemmeLag
    # Hvis hjemmeMål er mindre enn borteMål så returnerer jeg borteLag
    elif hjemmeMål < borteMål:
        return borteLag
    # Ellers returnerer jeg "Uavgjort"
    else:
        return "Uavgjort"


# Oppgave 2
# a)
# Her definerer jeg funksjonen erIListe
def erIListe(element, liste):
    # Hvis element er i Liste returnerer jeg True
    if element in liste:
        return True
    # Ellers returnerer jeg False
    else:
        return False


# b)
# Her definerer jeg funksjonen erIListe
def frekvensListe(element, liste):
    # Definerer x før for-løkken
    x = 0
    # Sjekker hva a er fra 0 til lengden av listen
    for a in range(0, len(liste)):
        # Sjekker hvis element er det samme som a i liste
        if element == liste[a]:
            # Legger til 1 på x for hver gang den finner element i liste
            x += 1
    return x


# Oppgave 3
# a)
# Finner a for 1 til 6
for a in range(1, 7):
    # Finner b for 1 til 6
    for b in range(1, 7):
        # Printer først a og så b for hver gang de øker med 1
        print(a, b)
# b)
# Finner a for 1 til 6
for a in range(1, 7):
    # Finner at b er 7 - a for alle a verdi
    b = 7 - a
    # Printer alle mulighetene for at a + b = 7
    print(a, b)

# Oppgave 4
# a) & b)
# Legger til tkinter packagen
from tkinter import *
# Lager et vinduelement
window = Tk()
# Henviser til en tittel på vinduet
window.title("Michael! Fancy!")
# Her setter jeg inn en tekst til å komme opp i vinduet
text = Label(window, text="Gi deg! Var det så lett?")
# Forteller hvor tekstem skal være
text.grid(column=0, row=0)
#Løkke som holder vinduet åpent til brukeren stanser det
window.mainloop()

# c)
def beregning():
    m=int(Entry.get(E1)) #Input
    a=int(Entry.get(E2)) #Input
    F=m*a #Beregning
    Entry.insert(E3,0,F) #Erstatter med svar
    print(F) #Viser Svaret

vindu = Tk()
vindu.title("Et_eksempelprogram!_Yay!")

L1 = Label(vindu, text="F=ma").grid(row=0,column=1)
L2 = Label(vindu, text="Masse_(kg)").grid(row=1,column=0)
L3 = Label(vindu, text="Akselerasjon_(m/s^2)").grid(row=2,column=0)
L4 = Label(vindu, text="Kraft_(Joule)").grid(row=3,column=0)

E1 = Entry(vindu, bd=5)
E1.grid(row=1,column=1)
E2 = Entry(vindu, bd=5)
E2.grid(row=2,column=1)
E3 = Entry(vindu, bd=5)
E3.grid(row=3,column=1)
B=Button(vindu, text ="Submit",command = beregning).grid(row=5,column=1,)
# Koden fungerer greit etter at jeg har lagt til at den skal holde vinduet åpent
vindu.mainloop()

# d)
window= Tk()
window.title("Calculator")

T1 = Entry(window, bd=1)
T1.grid(row=0,column=4)
T1.insert(0,str())

multiplication = 0
division = 0
addition = 0
subtraction = 0

def reset():
    Entry.delete(T1,0,END)

def table():
    a = Entry.get(T1)
    a = float(a)
    a *= -1
    a = str(a)
    Entry.delete(T1, 0, END)
    T1.insert(END, a)
    return a

def precentage():
    a = Entry.get(T1)
    a = float(a)
    a /= 100
    a = str(a)
    Entry.delete(T1, 0, END)
    T1.insert(END, a)
    return a

def divide():
    global a
    global division
    a = Entry.get(T1)
    a = float(a)
    Entry.delete(T1, 0, END)
    division = 1
    return division, a

def multiply():
    global a
    global multiplication
    a = Entry.get(T1)
    a = float(a)
    Entry.delete(T1, 0, END)
    multiplication = 1
    return multiplication, a

def subtract():
    global a
    global subtraction
    a = Entry.get(T1)
    a = float(a)
    Entry.delete(T1, 0, END)
    subtraction = 1
    return subtraction, a

def add():
    global a
    global addition
    a = Entry.get(T1)
    a = float(a)
    Entry.delete(T1, 0, END)
    addition = 1
    return addition, a

def equals():
    global a
    global division
    global multiplication
    global subtraction
    global addition
    if division == 1:
        b = Entry.get(T1)
        b = float(b)
        a /= b
        a = str(a)
    if multiplication == 1:
        b = Entry.get(T1)
        b = float(b)
        a *= b
        a = str(a)
    if subtraction == 1:
        b = Entry.get(T1)
        b = float(b)
        a -= b
        a = str(a)
    if addition == 1:
        b = Entry.get(T1)
        b = float(b)
        a += b
        a = str(a)
    Entry.delete(T1, 0, END)
    T1.insert(END, a)
    return a



def syv():
    Entry.insert(T1,END,"7")
def åtte():
    Entry.insert(T1,END,"8")
def ni():
    Entry.insert(T1,END,"9")
def fire():
    Entry.insert(T1,END,"4")
def fem():
    Entry.insert(T1,END,"5")
def seks():
    Entry.insert(T1,END,"6")
def tre():
    Entry.insert(T1,END,"3")
def to():
    Entry.insert(T1,END,"2")
def en():
    Entry.insert(T1,END,"1")
def null():
    Entry.insert(T1,END,"0")
def komma():
    Entry.insert(T1,END,".")

Kreset=Button(window, text="AC",command=reset).grid(row=1,column=0) #Skal resete kalkulatoren
Ktable=Button(window, text="+/-",command=table).grid(row=1,column=1) #Skal endre fortegn (gange med -1)
Kprecentage=Button(window, text="%",command=precentage).grid(row=1,column=2) #Skal gjøre til prosent (dele på 100)

M1=Button(window, text="÷",command=divide).grid(row=1,column=3)
M2=Button(window, text="×",command=multiply).grid(row=2,column=3)
M3=Button(window, text="-",command=subtract).grid(row=3,column=3)
M4=Button(window, text="+",command=add).grid(row=4,column=3)
M5=Button(window, text="=",command=equals).grid(row=5,column=3)


B7=Button(window, text="7",command=syv).grid(row=2,column=0)
B8=Button(window, text="8",command=åtte).grid(row=2,column=1)
B9=Button(window, text="9",command=ni).grid(row=2,column=2)
B4=Button(window, text="4",command=fire).grid(row=3,column=0)
B5=Button(window, text="5",command=fem).grid(row=3,column=1)
B6=Button(window, text="6",command=seks).grid(row=3,column=2)
B1=Button(window, text="1",command=en).grid(row=4,column=0)
B2=Button(window, text="2",command=to).grid(row=4,column=1)
B3=Button(window, text="3",command=tre).grid(row=4,column=2)
B0=Button(window, text="0",command=null).grid(row=5,column=0)
Bdecimal=Button(window, text=",",command=komma).grid(row=5,column=1)

window.mainloop()
#Abdul jeg fikk ikke til at man kan bruke kalkulatoren om og om igjen. Så den fungerer bare én gang etter at den er startet. Jeg fikk til de fire regneartene ved å legge til global på alle sammen.