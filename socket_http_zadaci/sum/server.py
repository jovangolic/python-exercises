#Korisnik se konektuje na server i unosi brojeve. Kada unese prazan string,
#svi uneti brojevi se sabiraju

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
with server:
    while True:
        conn,addr = server.accept()
        total = 0
        while True:
            val = conn.recv(HEADER).decode(FORMAT)
            if val == "-":
                conn.send(f"{total}".encode(FORMAT))
                break
            else:
                total += int(val)