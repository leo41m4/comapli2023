# Dado un número entre 1 y 10, muestre su equivalente en número romano.

import os
os.system("cls")

print("Dado un numero entero entre 1 y 10, muestre su equivalente en número romano.\n")
numero=int(input("Dame un numero entero: "))

if numero==1:
    print(f"\nI ")
elif numero==2:
    print(f"\nII")
elif numero==3:
    print(f"\nIII")
elif numero==4:
    print(f"\nIV")
elif numero==5:
    print(f"\nV")
elif numero==6:
    print(f"\nVI")
elif numero==7:
    print(f"\nVII")
elif numero==8:
    print(f"\nVIII")
elif numero==9:
    print(f"\nIX")
elif numero==10:
    print(f"\nX")
else:
    print("\nNúmero fuera de rango")
    
print("\nProceso terminado")