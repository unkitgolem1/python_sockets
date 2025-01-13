import socket

# Crear un socket TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor (reemplazar 'IP_DEL_SERVIDOR' con la IP del servidor)
clientsocket.connect(('IP_DEL_SERVIDOR', 12345))

try:
    while True:
        message = input("Cliente: ")
        if message.lower() == "exit":
            print("Cerrando cliente...")
            break  # Salir del bucle si se recibe "exit"
        
        clientsocket.sendall(message.encode())

        # Recibir respuesta del servidor
        data = clientsocket.recv(1024)
        print(f"Servidor: {data.decode()}")
except KeyboardInterrupt:
    print("\nCerrando cliente...")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    clientsocket.close()
