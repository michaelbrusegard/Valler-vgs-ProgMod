import time
navn = input("Hva heter du?")
print("Hei,", navn + "! Gjør deg klar til å spille Hangman.")
time.sleep(1)
ord = input("Få en venn til å putte inn et hemmelig ord:")
print("")
time.sleep(1)
print("Begynn å gjett...")
time.sleep(0.5)
turer = 10
bokstaver = []

while turer > 0:
    gjettning = input("Gjett en bokstav eller et ord:")
    if gjettning == ord :
        turer = 0
        print("Du vant.")
    elif gjettning in list(ord):
        bokstaver.append(gjettning)
        if()
