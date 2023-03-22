# Verificar si la suma de dos numeros es igual a un tercero
# n1=4, n2=5, n3=9  n1+n2=n3   n2+n3=n1   n1+n3=n2

import os
os.system("cls")

print("Verificar si la suma de dos numeros es igual a un tercero\n")
print("Dame tres numeros enteros separados por espacio:\n")

n1, n2, n3 = input().split() #leer la cadena y tomar los elementos por un espacio
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n1+n2==n3:
    print("\nn1 + n2 = n3")
elif n2+n3 ==n1:
    print("\nn2 + n3 = n1")
elif n1+n3==n2:
    print("\nn1 +n3 = n2")
else:
    print("\nNo hay sumas factibles")

print("\nProceso Terminado")
