x = float(input("Hva vil du ha kvadratroten til:"))
k = 1
if x == 2:
    print("Dette er et irrasjonelt tall. Kvadratroten din er omtrent: 1,414213562373039")
elif x > 0 and x != 2:
    while k != x**0.5:
        k = (k+x/k)/2
    print("Her er kvadratroten din:", k)
elif x == 0:
    print("Kan ikke ta kvadratroten til null.")
else:
    print("Det er et negativt tall, kan ikke ta kvadratroten.")



# funksjon
"""def kvadratrot(x,k, feilmargin):
    while feilmargin < abs(k*k-x):
        k = (k + x / k) / 2
        return k
        
print(kvadratrot(12,3,0.00001))"""
