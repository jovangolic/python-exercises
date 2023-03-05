#prosta komunikacija sa jednim klijentom
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("localhost",8005))
server.listen()
with server:
    conn,addr = server.accept()
    while True:
        conn.send(b"hello and welcome")
        print("client said: ",conn.recv(1024).decode("utf-8"))
        conn.send(b"continue")