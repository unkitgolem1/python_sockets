import socket

# Crear un socket TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección y puerto
serversocket.bind(('0.0.0.0', 12345))
serversocket.listen(1)

print("Servidor escuchando en el puerto 12345...")

clientsocket, addr = serversocket.accept()
print(f"Conexión establecida con {addr}")

try:
    while True:
        data = clientsocket.recv(1024)
        if not data:
            break  # Salir si no hay datos (el cliente cerró la conexión)
        print(f"Cliente: {data.decode()}")

        message = input("Servidor: ")
        if message.lower() == "exit":
            print("Cerrando servidor...")
            break  # Salir del bucle si se recibe "exit"
        
        clientsocket.sendall(message.encode())
except KeyboardInterrupt:
    print("\nCerrando servidor...")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    clientsocket.close()
    serversocket.close()
