# Calcular la paga total de un trabajador

print("Calcular la paga total de un trabajador\n") #Entrada
nombre=input("Dame tu Nombre    : ") #Teclado
horas = int(input("Horas trabajadas : "))
paga=float(input("Paga por hora   : "))

tasa=0.3 #Asignada
#Calculados
pagabruta= horas*paga
impuesto=pagabruta*tasa
paganeta=pagabruta-impuesto

#Salida 7 variables
print("\nResumen de pagos\n")
print(f"El trabajador {nombre} trabajo {horas} horas con una paga de {paga} pesos ")
print(f"Paga bruta : {pagabruta}")
print(f"Impuesto   : {impuesto}")
print(f"Paga Neta  : {paganeta}")