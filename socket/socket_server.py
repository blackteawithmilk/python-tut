import socket

sock_server = socket.socket()
sock_server.bind(('127.0.0.1', 8001))
print("Server started...\n")

sock_server.listen(1)

while True:
    conn, addr = sock_server.accept()
    print("Client from "+str(addr[0])+":"+str(addr[1])+" connected\n")
    while True:
        recv_data = conn.recv(1024).decode()
        if not recv_data:
            print("Client disconnected\n")
            break
        print("Server Recv: "+recv_data)
        conn.send("connection checked".encode().upper())

sock_server.close()