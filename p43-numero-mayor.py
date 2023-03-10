# Calcular el número mayor de una serie de numeros introducidos por el usuario, hasta salir con 0.

import os
while True:
    os.system('cls')
    print('Calcular el número mayor de una serie de numeros introducidos por el usuario, hasta salir con 0.\n')

    x=True   
    nmax = 0

    while x==True:

        n = int(input("Número: "))

        if nmax < n:
            nmax = n
        if n == 0:
            print(f"\nEl Número mayor es: {nmax}")
            x=False

    res = input("\nDeseas continuar (S/N): ")
    if res.upper()=="N":
        break

print('\nProceso terminado ...')