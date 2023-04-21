import os;os.system('cls')

a=[]
b=[]
c=[]

n=int(input('Cuantos elementos?'))

print('\nDame los elementos de la lista 1: ')
for i in range (n):
    x=int(input(f'Lista 1 elemento {i+1} : '))
    a.append(x)
print(a)

print('\nDame los elementos de la lista 2: ')
for i in range (n):
    x=int(input(f'Lista 1 elemento {i+1} : '))
    b.append(x)
print(b)

print('\nCalculando la suma de la la lista 1 + la lista 2 ')
for i in range (n):
    x= a [i] + b[i]
    c.append(x)
print(c)

