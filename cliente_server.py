import socket
import random
PORT = 8083
IP = "10.108.33.23"

numero_aleatorio =random.random()*99
numero_aleatorio = int(numero_aleatorio)
print (numero_aleatorio)

def conexion_cliente(clientsocket):
    print(clientsocket)
    condition = True

    while condition:
        a = (clientsocket.recv(2048).decode("utf-8"))
        print(a)
        a = int(a)

        if a == numero_aleatorio:
            mensaje='FELICIDADES'
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = False

        elif numero_aleatorio - 10 <= a <= numero_aleatorio + 10:
            b = "Caliente Caliente"
            send_bytes = str.encode(b)
            clientsocket.send(send_bytes)
            condition = True

        elif a > numero_aleatorio + 10:
            c = "Frío Frío por arriba"
            send_bytes = str.encode(c)
            clientsocket.send(send_bytes)
            condition = True

        elif a < n_aleatorio - 10:
            d = "Frío Frío por abajo"
            send_bytes = str.encode(d)
            clientsocket.send(send_bytes)
            condition = True

    clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = IP

try:
    serversocket.bind((HOST, PORT))

    while True:
        # permite conexiones
        print("Esperando a compañerxs %s %i" % (HOST, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas con el puerto %i. ¿Tienes permiso?" % PORT)

except KeyboardInterrumpt:
    print('Hubo algún error en el sistema')
