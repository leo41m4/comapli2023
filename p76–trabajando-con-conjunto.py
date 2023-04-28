
import os; os.system('cls')

municipios= {'Zacatecas','Guadalupe','Jerez','Fresnillo','Fresnillo'}

print(municipios)
print(len(municipios))
print(type(municipios),'\n')

for n in municipios:
    print('Tu vives en',n,'\n' )

print('Zacatecas' in municipios, '\n')

municipios.add(('Teul'))
print(municipios,len(municipios),'\n')

otros= {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
municipios.update(otros)
print(municipios, len(municipios),'\n')

municipios.remove('Zacatecas')
print(municipios, len(municipios), '\n')

municipios.discard('Ojocaliente')
print(municipios, len(municipios), '\n')

municipios.pop()
print(municipios, len(municipios),'\n' )

municipios.clear()
print(municipios, len(municipios),'\n' )

print('Proceso terminado...')