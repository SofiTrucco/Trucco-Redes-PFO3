import socket

HOST = "localhost"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

while True:
    texto = input("Ingrese un texto (o 'salir'): ")
    cliente.send(texto.encode())

    if texto.lower() == "salir":
        break

    respuesta = cliente.recv(1024).decode()

    print("\nResultado:")
    print(respuesta)

cliente.close()