import os;os.system('cls')

materias =['Fisica','Quimica','Matematicas','Geografia','Estadistica']
califs = [10,9,8,7.5,6]

notas=dict(zip(materias,califs))

print(notas,len(notas),'\n')

notas.update({'Ingles':10,'Programacion':7})

print(notas,len(notas),'\n')

notas.pop('Fisica')
print(notas,len(notas),'\n')

notas.popitem()
print(notas,len(notas),'\n')

notas.update({'Quimica':10, 'Matematicas':10})
print(notas,len(notas),'\n')

s=0
print('Materia\t\tCalificacion')
for m,c in notas.items():
    print(f'{m:<12} - {c:5}')
    s=s+c

print()
print('Suma:',s)
print('Promedio:',s/len(notas))

print('\nProceso terminado...')

