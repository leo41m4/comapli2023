# Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. 
# Se especifica: tipo de usuario, paquete y cantidad.

# Tipo de usuario: (1) Alumno $100, (2) Trabajador $200, (3) Docente $500
# Tipo de paquete: (1) Solo conferencias $600, (2) Con eventos sociales $800, (3) Con kit de acceso $900.

# Se debe calcular un subtotal de la venta, sumando el precio del tipo de usuario más el precio 
# de tipo de paquete, y multiplicando por la cantidad solicitada.

# Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente:

# Es Alumno 20%
# Es Trabajador un 10%
# Es Docente un 5%

# Al final mostrar un resumen con los datos calculados de la venta.

# Al terminar de procesar las ventas mostrar el total de ventas del día:

import os

imptotal =float(0)

while(True):
    
    os.system("cls")
    
    print("Universidad Patito S.A. de C.V.         ")
    print("Sistema de Inscripcion Congreso de Sistemas \n")

    ent =int(input("Tipo de Usuario: (1) Alumno: $100, (2) Trabajador: $200 (3) Docente:$500: "))
    
    if ent ==1:
        usuario = "Alumno"
        pre =100
        desc =20
    elif ent ==2:
        usuario = "Trabajador"
        pre =200
        desc =10
    else:
        usuario = "Docente"
        pre =500
        desc =5

    tipaq = int(input("\nTipo de Paquete: (1) Solo Conferencias: $600, (2) Con Eventos Sociales: $800, (3) Con Kit de Acceso: $900: "))

    if tipaq ==1:
        paquete = "Solo Conferencias"
        pack =600
    elif tipaq ==2:
        paquete = "Con Eventos Sociales"
        pack =800
    else:
        paquete = "Con Kit de Acceso"
        pack =900
    
    c = int(input("\nCantidad: "))
    subtotal =(pre + pack) * c
    descuento =float(subtotal * desc)/100
    total =float(subtotal - descuento)

    imptotal =imptotal + total

    print(f"\nTu pedido fue: {c}, Tipo de Usuario: {usuario}, Tipo de Paquete: {paquete}")
    
    print(f"\nSubtotal: ${subtotal}, Descuento de: : ${descuento} ({desc}%), Total de: ${total}")
        
    x = True
    while(x ==1):
        print("\nDeseas continuar (S/N) ? ", end= ' ')
        res = input()
        if res.upper() == "S" or res.upper() == "N":
            x =False
    if res.upper()=="N":
            break

print(f"\nImporte Total de la Venta: ${imptotal:.2f}")

print("\nProceso terminado ...")
