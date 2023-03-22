# Imprimir numeros del 1 a n o de n a 1 segun lo decida el usuario

import os
while(True):
    os.system('cls')

    print('Imprimir los números de 1 a n o de n a 1\n')
    print('[1] Números de 1 a n ')
    print('[2] Números de n a 1 ')
    op = int( input('\nElige una opción ? ') ) 
    n = int(input('\nLimite n ? '))

    if op==1:
        print(f'\nImprimiendo los numeros de 1 a {n}\n') 
        for v in range(1,n+1,1):
            print(v,end=' ')
    elif op==2:
        print(f'\nImprimiendo los numeros de {n} hasta 1\n') 
        for r in range(n,0,-1):
            print(r,end=' ')
    else:
        print("\nOpcion invalida")

    res = input('\n\nDeseas continuar (S/N) ? ').upper() 
    if res=='N': break

print('Gracias por utilizar este programa')