import socket

sock_client = socket.socket()
sock_client.connect(('localhost', 8001))

while True:
    sock_client.send("checking connection.".encode())
    recv_data = sock_client.recv(1024).decode()
    print(recv_data)

sock_client.close()