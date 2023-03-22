# Calcular el area de un circulo
import math

#Entrada de datos
print("Calcular el area de un circulo\n")
radio=float(input("Dame el radio: "))

#Proceso
area=math.pi *math.pow(radio,2)
print(math.pi)
#Salida
print(f"El circulo de radio {radio} tiene un area de: {area:.2f}")

