# Imprimir la secuencia de números mostrados, el numero de renglones que el usuario desee.

n=int(input('Dame un numero:  '))
print('\nImprimir la secuencia de números mostrados, el numero de renglones que el usuario desee.\n')
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,end=' ')
    print('\r')

print('\nProceso Terminado')