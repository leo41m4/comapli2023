# Imprime la tabla de multiplicar que el usuario pida.

import os

while True:
    os.system("cls")
    t=int(input('Que tabla quieres ?  '))
    n=int(input('Hasta donde       ?  '))

    for i in range (1, n+1):
        print(f"{t} x {i} = {t*i}")

    res = input('\n\nDeseas continuar (S/N) ? ').upper() 
    if res=='N': break

print('\nProceso Terminado')
    
