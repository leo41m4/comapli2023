# Cambiar los elementos de una lista 
import os; os.system('cls')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5] 
print(f'Todos: {califs} - {len(califs)} \n') 
califs[0]=7
califs[1]=7
print(f'modificar 0 y 1 : {califs}\n') 
califs[2:5] = [9,9,9]
print(f'modificar 2:5 - : {califs}\n')