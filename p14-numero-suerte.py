# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte
# Mostrar los dígitos individuales y el número de la suerte.

import math
import os
os.system("cls")

an = int(input("Digita el año de nacimiento: "))
mil = an //1000
centenas = ( an - (mil * 1000) ) // 100
decenas = ( an - (mil * 1000) - (centenas * 100) ) // 10
unidades = an - centenas*100 - mil*1000 - decenas*10

print("Los digitos individuales son:")
print("Millar "   ,mil)
print("Centenas " ,centenas)
print("Decenas "  ,decenas)
print("Unidades " ,unidades)

numerosuerte = mil + centenas + decenas + unidades

print(f"\nTu numero de la suerte es: {numerosuerte}")