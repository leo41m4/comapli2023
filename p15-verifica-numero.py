# Verifica si un numero es positivo, negativo o cero

import os
os.system("cls")

print("Verifica si un numero es positivo, negativo o cero\n")
numero = int(input("Dame un numero "))

if numero > 0:
    print("El numero es Positivo")
if numero < 0:
    print("El numero es Negativo")
if numero == 0:
    print("El numero es Cero")

print("\nProceso Terminado")