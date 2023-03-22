# Dado tres numeros enteros, verificar si son consecutivos (n1,n2,n3).

import os
os.system("cls")

print("Dado tres numeros enteros, verificar si son consecutivos (n1,n2,n3)\n")
print("Dame 3 números separados por Enter: \n")
n1, n2, n3 = int(input()), int(input()), int(input())

if n2-n1 == 1 and n3-n2 == 1:
    print("\nLos tres numeros dados son consecutivos")
else:
    print("\nError los numeros no son consecutivos")

print("\nProceso Terminado")