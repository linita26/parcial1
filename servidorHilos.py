from socket import socket , error
from threading import Thread
import funcionesservidor





#Clase para crear los hilos

class Cliente(Thread):
    def __init__(self, conex , dire):
        Thread.__init__(self)
        self.conexion = conex
        self.direccion = dire

    def run (self):
        while True: #recibe un mensaje
            try:
                 mensajecliente = self.conexion.recv(1024)


                 if mensajecliente == "administrador":
                     print "Usuario Administrador"
                     mensajecliente = funcionesservidor.menu()
                 if mensajecliente == "cliente":
                     print "Usuario Cliente"
                     mensajecliente = funcionesservidor.menu2()



                     #para poderse conectar y permita recibir mensajes
            except error:
                    print ("[%s] Eroor de Lectura" %self.name)
                    break
            else:
                if mensajecliente:
                 self.conexion.send(mensajecliente)


def main():
    server = socket() #variable server con la conexion
    server.bind(('localhost',9090))
    server.listen(1)

    while True:
        conex,dire = server.accept()
        hilo = Cliente(conex, dire)
        hilo.start()
        print ("%s:%d conexion de" %dire)


if __name__ == "__main__":
    main()

