import skimage.io #Importer f.eks. denne modulen.
import IPython.core.display
from PIL import Image
import os

"""rad1 = [1, 2, 3]
rad2 = [0, 1, 0]
rad3 = [2, 4, 7]
rad4 = [8, 9, 2]
matrise = [rad1, rad2]
matrise2 = [rad3, rad4]
dobbelmatrise = [matrise, matrise2]

print(dobbelmatrise)"""

n = 1
deltaen = 0.0000001
matriseBilde = skimage.io.imread(os.path.join('Oppgaver i timen','Bilder',"sg" + str(n) + ".jpeg"))
print("RGB verdien til første rad, første kolonne er:", matriseBilde[0,0])
print("Størrelsen til bildet er:", len(matriseBilde), "x", len(matriseBilde[0])), IPython.core.display.Image(url="sg.jpeg", width=200, height=200)

def f(a):
    return a ** 2

def fDerivert(a, deltaX):
    return ((f(a + deltaX)) - f(a)) / deltaX

for i in range(len(matriseBilde)):
    for j in range(len(matriseBilde[0])):
        p_1 = fDerivert(matriseBilde[i][j][0], deltaen)
        p_2 = fDerivert(matriseBilde[i][j][1], deltaen)
        p_3 = fDerivert(matriseBilde[i][j][2], deltaen)
        matriseBilde[i][j] = [p_1, p_2, p_3]
        #Lagrer til en ny fil.
img = Image.fromarray(matriseBilde, 'RGB')
img.save(os.path.join('Oppgaver i timen','Bilder',"out" + str(n) + ".jpeg"))