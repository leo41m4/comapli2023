
import os; os.system('cls')

empleados = []

print('\nMueblerias Dico')
print('Sistema de Procesamiento de Empleados')
print('\nCaptura de datos de los empleados * para terminar:')


while True:
    empleado = {}
    nombre = input('\nNombre\t\t : ')
    if nombre == '*':
        break
    else:
        empleado['Nombre'] = nombre
        empleado['Edad'] = int(input('Edad\t\t : '))
        
        while True:
            sexo = input('Sexo (h/m)\t: ').upper()
            if sexo == 'H' or sexo == 'M':
                empleado['Sexo (h/m)'] = sexo
                break
            else:
                print('\nError de captura:')
                            
        empleado['Sueldo'] = int(input('Sueldo\t\t : $'))
        empleados.append(empleado)

print('\nLos datos como se guardan:')
print('')
print(empleados)

print('\nTabla de datos ')
print('')
print("Nombre\tEdad\tSexo\tSalario")

for empleado in empleados: 
    for i in empleado.keys(): 
        if i != 'sueldo':
            print(f'{empleado[i]}\t', end= '')
        else:
            print(f'{format(empleado[i],",.2f")}\t', end= '')
    print('\r')

sumamujeres = 0
for k in empleados:
    if k['Sexo (h/m)'] == 'm' or k['Sexo (h/m)'] == 'M':
        sumamujeres = sumamujeres + 1

sumahombres = 0
for l in empleados:
    if l['Sexo (h/m)'] == 'h' or l['Sexo (h/m)'] == 'H':
        sumahombres = sumahombres + 1

sumaEdad = 0
promedioEdad = 0
for n in empleados:
    sumaEdad = sumaEdad + n['Edad']
promedioEdad = sumaEdad/len(empleados)


sumaSueldos = 0
promedioSueldos = 0
for o in empleados:
    sumaSueldos = sumaSueldos + o['Sueldo']
promedioSueldos = sumaSueldos/len(empleados)

print('\n\nResumen ')
print('')
print(f'Empleados : {len(empleados)}')
print(f'Mujeres   : {sumamujeres}')
print(f'Hombres   : {sumahombres}')
print(f'Edad Suma  :\t{sumaEdad},\t\tPromedio: \t{promedioEdad}')
print(f'Sueldo Suma:\t{format(sumaSueldos,".2f")},\tPromedio:\t{format(promedioSueldos,".2f")}')