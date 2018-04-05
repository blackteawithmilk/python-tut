import socket

sock_client = socket.socket()
sock_client.connect(('localhost', 8001))

sock_client.send("checking connection.".encode())
recv_data = sock_client.recv(1024)
print(recv_data)

sock_client.close()