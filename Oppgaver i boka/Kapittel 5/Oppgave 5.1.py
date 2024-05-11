fotballspillere = ["Lionel Messi","Christiano Ronaldo", "Pique","Martin Ødegaard", "Zlatan Ibrahimovitz"]
tvSerier = ["The office", "Family Guy", "The 100", "Breaking Bad", "Vampire Diaries"]

lister = fotballspillere + tvSerier
print(lister)

lister.pop(0)
lister.pop(1)
print(lister)

print(lister.index("The office"))

nyliste = lister[1:5]
print(nyliste)

print(nyliste.index("Family Guy"))
nyliste.pop(3)
print(nyliste)

nyliste.reverse()
print(nyliste)