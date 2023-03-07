
# Imprime la tabla de multiplicar deseada del 1 al n 
import os

while(True):

    os.system('cls')

    n = int(input('Las tablas desde la tabla del 1 hasta la del n ? '))
    m = int(input('Desde 1 hasta m ? ')) 
    
    t=1
    while( t <= n):
        print(f'Tabla del {t}') 
        
        c=1
        while c <= m:
            print(f"{t} x {c} = {c*t} ")
            c += 1

        print("\n")
        t +=1

    res=input('Deseas Continuar(S/N)? ') 
    if res.upper()=='N':
        break

print("\nProceso Terminado...")
