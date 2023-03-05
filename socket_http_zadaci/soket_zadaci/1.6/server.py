"""Zadatak 1.6  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server prima ovaj podataka I obrće string
Potrebno je taj promenjen string vratiti klijentu
Klijent ispisuju promenjen string"""

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen() 
with server:
    print(f'server is listening....{server.getsockname()}')  
    while True:
        conn,addr = server.accept()
        msg = conn.recv(HEADER).decode(FORMAT)
        print(f"[SERVER] The client at {addr},originally sent {repr(msg)}")
        msg = str(msg)
        reply = msg[::-1]
        conn.sendall(bytes(str(reply),encoding=FORMAT))
        print ("[TCP_SERVER] Reply sent, closing client's socket.")   