# Dada una temperatura en grados Celcius, obtener su equivalente en grados Farenheit, usando la formula:
# Formula Farenheit =(celcius × 9/5)+32

import math
import os
os.system("cls")

celcius = float(input("Dame la temperatura en grados Celcius:\n"))
farenheit = (celcius * 9/5) + 32
print(f"La temperatura en grados Farenheit es: {farenheit} ")