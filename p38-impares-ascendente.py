# Imprime los numeros impares de forma ascendente desde 1 hasta el numero que el usuario decida.

import os

while(True):
    os.system("cls")

    print("Imprime los numeros impares de forma ascendente desde 1 hasta el numero que el usuario decida.")
    n= int(input("\nHasta donde: "))
    c=1
    s=0

    while c <=n:
        if c % 2 == 1:
            print(c, end=" ")        
            s=s+c
            c=c+2
        
    print(f"\n\nLa suma de los números impares es: {s} ")

    res=input('\nDeseas Continuar (S/N): ') 
    if res.upper()=='N':
        break

print("\nProceso terminado...")