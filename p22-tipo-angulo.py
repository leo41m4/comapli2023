# Muestra el tipo de angulo
# < 90° agudo, = 90° recto, > 90° y < 180° obtuso, = 180° llano, > 180° y < 260° concavo

import os
os.system("cls")

print("Muestra el tipo de Angulo (de 0 a 360°):\n")
angulo=int(input("Dame un angulo: "))

if angulo >=0 and angulo <=360:
    print(f"\nEl angulo es ", end="")
    if angulo <90:      #Anidaciones de ifs
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo >90 and angulo <180:
        print("Obtuso")
    elif angulo == 180:
        print("Llano")
    elif angulo >180 and angulo <360:
         print("Concavo")
    else:
         print("Completo")
else:
    print("\nAngulo fuera de rango")

print("\nProceso terminado")