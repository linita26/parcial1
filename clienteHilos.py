from socket import socket
import funcionesservidor

def main():
    server = socket()
    server.connect(('localhost', 9090))

    while True:

        mensajecliente = raw_input("Ingrese su nombre") #el clien te envia al servidor


        if mensajecliente:
            try:
                server.send(mensajecliente)

                mensajecliente = funcionesservidor.crear2()

            except TypeError:
                server.send(bytes(mensajecliente, "utf-8"))

        mensaje_servidor = server.recv(1024)
        if mensaje_servidor:

            print mensaje_servidor  # si recibe una respuesta del servidor imprime


if __name__ == '__main__':
    main()