# Convertir una temperatura de grados Celcius a grados Farenheit y viceversa.
# Formulas: centigrados = (farenheit - 32) * 5 / 9
#           farenheit = ( centigrados * 9 / 5 ) + 32

import os
os.system("cls")
print("Convertir una temperatura de grados Celcius a grados Farenheit y viceversa.\n")
opcion = str.upper(input("Seleccionar [C]elcius o [F]arenheit para convertir: "))

if opcion == "C":
    print("\nConvertir a Celcius")
    temp = float(input("Teclee grados Farenheit: "))
    res = (temp-32)*5/9
    print(f"{temp} grados Farenheit, equivalen a {res} grados Celcius")
else:
    print("\nConvertir a Farenheit")
    temp = float(input("Teclee grados Celcius: "))
    res = (temp*9/5)+32
    print(f"{temp} grados Celcius, equivalen a {res:.2f} grados Farenheit")