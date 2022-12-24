import socket
import zlib
import threading
from colored import fg, bg, attr

host = "127.0.0.1"
port = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    clients.append(client)
    while True:
        try:
            response = client.recv(1024).decode("UTF-8", errors="replace")
            rSplit = response.splitlines()
            content = rSplit[10].encode("ascii")
            if client in clients:
                clients.remove(client)
            broadcast(content)
        except Exception as e:
            #print(f'{fg("white")}{bg("red")}ERROR: {e}, disconnecting client.')
            clients.remove(client)
            client.close()
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"{bg('black')}{fg('blue')}{address} {fg('green')}connected.")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f"{fg('red')}R{fg('white')}T{fg('magenta')}D{fg('white')} ({fg('red')}Roblox {fg('white')}to {fg('magenta')}Discord{fg('white')}) Server v1.0.0")
print(f"Server started on address {host} and port {str(port)}")
recieve()