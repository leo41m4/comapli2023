
import os; os.system('cls')

nuromanos = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X', 11:'XI', 12:'XII', 13:'XIII', 14:'XIV', 15:'XV', 16:'XVI', 17:'XVII', 18:'XVIII', 19:'XIX', 20:'XX'}

while True:
    nromano = int(input('Digite un número arabigo entre 1 y 20: '))
    if nromano > 0 and nromano < 21:
        print(f'El Número Romano es: {nuromanos[nromano]}')
        break
    else:
        print('Numero Invalido')

print('\nProceso Terminado')