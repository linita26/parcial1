import json
def menu():

    lista =['1.Crear_Pelicula','2.eliminar_Pelicula','3.Listar_Pelicula','Ver_Vendidas','Sillas_Disponibles']
    cadena = json.dumps(lista)
    return cadena



def menu2():

    lista =['1.Listar Peliculas','2.Comprar Entrada','3.Ver mi Pelicula']
    cadena = json.dumps(lista)
    return cadena


def crear():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 1):
        pelicula = raw_input("Ingrese Nombre Pelicula")  # envia el mensaje al cliente

        costo = raw_input("Ingrese Costo de la Pelicula")

        sillas = raw_input("Ingrese Cantidad de Sillas")

        hora = raw_input("Ingrese Hora de la Pelicula")

        print ("Pelicula Creada")


def crear2():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 2):
        pelicula = raw_input("Ingrese Nombre Pelicula")  # envia el mensaje al cliente

        costo = raw_input("Ingrese nombre Cliente")

        sillas = raw_input("Cedula Cliente")

        hora = raw_input("Hora cliente")



