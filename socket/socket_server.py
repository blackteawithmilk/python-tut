import socket

sock_server = socket.socket()
sock_server.bind(('localhost', 8001))

sock_server.listen(1)

conn, addr = sock_server.accept()
while True:
    recv_data = conn.recv(1024).decode()
    print(recv_data)
    conn.send("connection checked".encode().upper())

sock_server.close()