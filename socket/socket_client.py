import socket

sock_client = socket.socket()
sock_client.connect(('localhost', 8001))

while True:
    msg = input("input>>").strip()
    if len(msg) == 0:
        break
    sock_client.send("checking connection.".encode().upper())
    sock_client.send(msg.encode())
    recv_data = sock_client.recv(1024).decode()
    print("Client Recv: "+recv_data)

sock_client.close()