#Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados, con la siguiente formula:
#Formula hipotenusa=raizcuadrada(longlado1+longlado1 * longlado2+longlado2)

import math
import os
os.system("cls")

print("Dame el valor de los 2 lados separados por un espacio:\n")
longlado1, longlado2=input().split()
longlado1, longlado2=[float(longlado1), float(longlado2)]

hipotenusa =math.sqrt((longlado1 * longlado1)+(longlado2 * longlado2))
print(f"La hipotesusa del triangulo rectangulo es: {hipotenusa}")