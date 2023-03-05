'''Zadatak 1.5  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server prima ovaj podataka I mala slova pretvara u velika a velika u mala, razmake u zvezdice
Potrebno je taj promenjen string vratiti klijentu
Klijent ispisuju promenjen string'''

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP, PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
with server:
    print("server is listening...")
    while True: 
        conn,addr = server.accept()
        msg = conn.recv(HEADER).decode(FORMAT)
        print(f"[SERVER] The client at {addr},originally sent {repr(msg)}")
        msg = str(msg)
        razmak = ""
        for i in range(len(msg)):
            if msg[i].isupper():
                razmak += msg[i].lower()
            elif msg[i].islower():
                razmak += msg[i].upper()
            elif msg[i].isspace():
                razmak += "*"
        razmak = str(razmak)
        conn.sendall(bytes(razmak, encoding=FORMAT))
        print("Reply sent, closing client's socket")    