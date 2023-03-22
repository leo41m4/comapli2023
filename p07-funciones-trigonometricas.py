#Calcular las funciones trigonometricas básicas de un ángulo en radianes

import math

print('Calcula las funciones trigonometricas básicas de un ángulo en radianes:\n')
angulo = int(input('Dame un angulo en radianes: '))

seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
grados = math.degrees(angulo)

salida = (f'Resumen de funciones trigonometricas\n'
f'EL seno es : {seno:.3f}\n'
f'El coseno es: {cos:.3f}\n'
f'La tangente : {tan:.3f}\n'
f'El angulo {angulo:.3f} en radianes equivale a {grados:.3f} grados\n'
)

print(salida)