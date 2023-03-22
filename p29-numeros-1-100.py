# Imprime numeros de 1 al 100

import os
os.system("cls")

print("Imprime numeros del 1 al 100")
n= int(input("Hasta donde: "))
m= int(input("Salto: "))

c=1 #variable de control
while c <= n:
    print(c, end= " ")
    c=c + m

print("\n\nProceso terminado...")

