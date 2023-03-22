# Imprimir pares e impares y su suma segun lo decida el usuario

import os

while (True):
    os.system('cls')

    print('[P]ares de 1 a n y su suma\n[I]mpares de 1 a n y su suma')
    op = input('\nElige una opción ? ').upper()
    n=int(input("Hasta donde ? "))

    s=0

    if op=="P":
        print(f'\nNumeros pares de 1 a {n} y su suma\n') 
        for i in range(2,n+1,2):
            print(i,end=' ')
            s+=i
        print("\n\nSuma de pares:",s) 
    elif op=="I":
        print(f'\nNumeros impares de 1 a {n} y su suma\n') 
        for i in range(1,n+1,2):
            print(i,end=' ')   
            s+=i
        print("\n\nSuma de impares:",s)
    else:
            print("\nOpcion invalida")

    res = input('\n\nDeseas continuar (S/N) ? ').upper() 
    if res=='N': break

print('\nGracias por utilizar este programa')