#  Imprimir los pares de 2 a n y su suma.

n = int(input("Dame numero: "))
s=0
print('\nImprimir los pares de 2 a n y su suma.\n') 

for x in range(2,n+1,2):
    print(x,end=' ')
    s+=x
print("\n\nSuma de pares:",s)

print('\nGracias por utilizar este programa')