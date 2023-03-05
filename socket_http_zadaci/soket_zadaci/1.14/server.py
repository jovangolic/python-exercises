'''Zadatak 1.14  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje rečnik serveru
Server prima ovaj podatak ispisuje ga'''


import socket,pickle
HEADER=1024;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR=(IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
while True:
    print("server is listening at {}".format(server.getsockname()))
    conn,addr = server.accept()
    msg = conn.recv(HEADER)
    modified = pickle.loads(msg)
    print("[TCP-SERVER] The client at {},originally sent {}".format(conn.getpeername(),repr(msg)))
    for key,value in modified.items():
        print(key,value)