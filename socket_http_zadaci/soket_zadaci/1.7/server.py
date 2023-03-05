'''Zadatak 1.7  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server vraća string Da ako se poslati string završava karakterom tačka, Ne ukoliko se ne završava.
Potrebno je string odgovora vratiti klijentu
Klijent ispisuju string odgovora'''

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
with server:
    print("server is listening...{}".format(server.getsockname()))
    while True:
        conn,addr = server.accept()
        msg = conn.recv(HEADER).decode(FORMAT)
        print(f"[SERVER] The client at {addr},originally sent {repr(msg)}")
        msg = str(msg)
        if msg.endswith("."):
            reply = "YES" 
            #reply = conn.sendall(bytes("Yes",encoding=FORMAT))
        else:
            reply = "NO"
            #reply = conn.sendall(bytes("No",encoding=FORMAT))
        conn.sendall(bytes(str(reply),encoding=FORMAT))
        print("[TCP-SERVER] Reply sent,closing client's socket.")   