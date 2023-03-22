# Cuenta numeros, los suma, cuenta positivos, cuenta negativos y ceros, hasta salir con 999

import os
os.system("cls")
print("Cuenta numeros, los suma, cuenta positivos, cuenta negativos y ceros, hasta salir con 999")

cuenta=0
suma=0
cp=cn=cz=0

while True:
    num=float(input("numero:"))
    if num !=999:
        cuenta = cuenta + 1
        suma=suma+num
        if num>0:
            cp=cp+1
        elif num<0:
            cn=cn+1
        else:
            cz=cz+1
    else:
        break

print("\nResumen:")
print(f"\nSe capturaron {cuenta} números")
print(f"\nla suma es: {suma}")
print(f"\nEl promedio es: {suma/cuenta} ")
print(f"\nPositivos: {cp}\n Negativos: {cn}\n Ceros: {cz}")