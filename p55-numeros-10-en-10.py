# Imprimir los números de 1 a n de 10 en 10.

n = int(input("Dame numero: "))

print('\nImprimir los números de 1 a n de 10 en 10\n') 

for x in range(1,n+1,10):
    print(x,end=' ')

print('\n\nGracias por utilizar este programa')
