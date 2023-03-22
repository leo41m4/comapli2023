# Imprime numeros del 100 al 1

import os
os.system("cls")

print("Imprime numeros del 100 a 1:\n")
n=int(input("Desde donde: "))
m=int(input("Salto: "))
c=n

while c >= 0:
    print(c, end= ' ')
    c=c -m

print("\n\nProceso terminado...")