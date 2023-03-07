# Dado tres numeros enteros, verificar cual es el mayor (n1,n2,n3=n>).

import os
os.system("cls")

print("Dado tres numeros enteros, verificar cual es el mayor (n1,n2,n3=n>)\n")
print("Dame 3 números separados por Enter: \n")

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 > n2 and n3:
    print(f"\nEl numero mayor es {n1} ")
elif n2 > n3 and n1:
     print(f"\nEl numero mayor es {n2} ")
elif n3 > n2 and n1:
     print(f"\nEl numero mayor es {n3} ")
else:
    print("\nError ningun numero es mayor (todos son iguales)")

print("\nProceso Terminado")
