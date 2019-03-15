import socket

IP = "10.108.33.23"
PORT = 8083

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((IP, PORT))
    print("Conexión enlazada")
except OSError:
    print("Problemas con el sistema")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

message = input("Introduzca un numero: ")
send_bytes = str.encode(message)
s.send(send_bytes)
print("Mensaje enviado")

condition = True
while condition:
    respuesta = s.recv(2048).decode("utf-8")
    print (respuesta)
    if respuesta == '¡Acertaste!':
        condition = False
    else:
        message = input('Vuelve a intentarlo: ')
        send_bytes = str.encode(message)
        s.send(send_bytes)

s.close()
