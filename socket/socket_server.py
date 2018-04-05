import socket

sock_server = socket.socket()
sock_server.bind(('localhost', 8001))

sock_server.listen()

sock_conn, addr = sock_server.accept()

recv_data = sock_conn.recv(1024)
print(recv_data)
sock_conn.send("connection checked".encode().upper())

sock_server.close()