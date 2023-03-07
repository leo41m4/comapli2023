# Dado un nunmero entero entre 1 y 7, se desea mostrar con letra el dia de la semana.

import os
os.system("cls")

print("Dado un numero entero entre 1 y 7, se desea mostrar con letra el dia de la semana.\n")
numero=int(input("Dame un numero entero entre 1 y 7: "))

if numero==1:
    print(f"\nDomingo ")
elif numero==2:
    print(f"\nLunes")
elif numero==3:
    print(f"\nMartes")
elif numero==4:
    print(f"\nMiercoles")
elif numero==5:
    print(f"\nJueves")
elif numero==6:
    print(f"\nViernes")
elif numero==7:
    print(f"\nSabado")
else:
    print("\nNúmero fuera de rango")
    
print("\nProceso terminado")