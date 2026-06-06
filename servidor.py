import socket
import threading
import queue

HOST = "localhost"
PORT = 5000

cola_tareas = queue.Queue()


def procesar_texto(texto):
    mayusculas = texto.upper()
    palabras = len(texto.split())
    caracteres = len(texto)

    resultado = (
        f"Texto original: {texto}\n"
        f"Mayúsculas: {mayusculas}\n"
        f"Palabras: {palabras}\n"
        f"Caracteres: {caracteres}"
    )
    return resultado


def worker(id_worker):
    while True:
        cliente_socket, texto = cola_tareas.get()
        try:
            resultado = (
                f"Procesado por Worker {id_worker}\n\n"
                + procesar_texto(texto)
            )
            cliente_socket.send(resultado.encode())
        except Exception as e:
            print(f"Error enviando resultado: {e}")
        finally:
            cola_tareas.task_done()


def manejar_cliente(cliente_socket):
    while True:

        texto = cliente_socket.recv(1024).decode()

        if not texto:
            break

        if texto.lower() == "salir":
            break

        cola_tareas.put((cliente_socket, texto))

    cliente_socket.close()


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PORT}")

    for i in range(3):
        hilo_worker = threading.Thread(
            target=worker,
            args=(i + 1,),
            daemon=True
        )
        hilo_worker.start()

    while True:
        cliente_socket, direccion = servidor.accept()
        print(f"Cliente conectado: {direccion}")

        hilo_cliente = threading.Thread(
            target=manejar_cliente,
            args=(cliente_socket,)
        )
        hilo_cliente.start()

if __name__ == "__main__":
    iniciar_servidor()

