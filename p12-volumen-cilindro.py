# Calcular el volumen de un cilindro dado su radio y altura, usando la siguiente formula: 
# Volumen = PI * (Radio * Radio) * Altura

import math
import os
os.system("cls")

print("Dame el valor del radio y altura del cilindro separados por un espacio:\n")
radio, altura = input().split()
radio, altura = [float(radio), float(altura)]

volumen = 3.1416 * (radio * radio) * altura
print(f"El volumen del cilindro es: {volumen:.3f} ")
