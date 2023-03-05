'''Zadatak 1.15  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje string serveru
Server prima ovaj podatak I pravi rečnik tako da su ključevi rečnika karakteri stringa a vrednosti su\
broj pojavljivanja karaktera u stringu
Potrebno je taj rečnik vratiti klijentu
Klijent ispisuju rečnik'''


import socket,pickle
HEADER=1024; FORMAT="utf-8"; IP="localhost"; PORT=8005; ADDR=(IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
while True:
    conn,addr = server.accept()
    print("[TCP-SERVER] is listenning at {}\n{}".format(conn.getsockname(),conn.getpeername()))
    msg = conn.recv(HEADER)
    loads_msg = pickle.loads(msg)
    d = dict()
    for i in loads_msg:
        #key = d.keys()
        #if i in key:
        #    d[i]+=1
        if i in d:
            d[i]+=1
        else:
            d[i]=1  
    dumps_msg = d
    print("[TCP-SERVER] The client at {},originally sent {}".format(addr,repr(msg)))
    conn.sendall(bytes(str(dumps_msg),encoding=FORMAT))  
    print ("[TCP_SERVER] Reply sent, closing client's socket.")  