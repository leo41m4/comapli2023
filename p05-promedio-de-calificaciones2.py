# Calcular el promedio de 3 calificaciones

print('Calcula el promedio de 3 calificaciones:\n')
c1 = float(input('Calificación 1: '))
c2 = float(input('Calificación 2: '))
c3 = float(input('Calificación 3: '))

suma = (c1 + c2 + c3)
print(f"La suma de Calificaciones es: {suma} ")
prom = suma / 3
print(f"El promedio de: {c1} {c2} {c3} es {prom}")