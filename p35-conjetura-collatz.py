# Calcula los numeros de la conjetura de Collatz 

import os
while(True):

    os.system("cls")
    num=int(input("Dame un numero entero positivo:  "))

    while num!=1:
        print(num, end=" " )
        if num % 2== 0:
            num=num //2
        else:
            num= num*3+1
    print(num)

    res=input("\nDeseas continuar (S/N)? ")
    if res.upper()=='N':
        break


print("Proceso Terminado...")