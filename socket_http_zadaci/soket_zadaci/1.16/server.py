'''Zadatak 1.16  Napraviti server I klijent preko TCP protokola tako da:
Klijent šalje listu celih brojeva
Server prima ovaj podatak računa da li ima više pozitivnih, negativnih ili isti broj.
Potrebno je da se taj string vrati klijentu
Klijent ispisuju string'''

import pickle,socket
HEADER=1024; FORMAT="utf-8"; IP="localhost"; PORT=8005; ADDR=(IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
while True:
    conn,addr = server.accept()
    print("[TCP-SERVER] is listening at {}\{}".format(conn.getsockname(),conn.getpeername()))
    msg = conn.recv(HEADER)
    loads_msg = pickle.loads(msg)
    pozitivni,negativni = 0,0
    for i in loads_msg:
        if i >= 0:
            pozitivni +=1
        else:
            negativni +=1
    if pozitivni > negativni:
        odg = "pozitivnih ima vise"
    elif pozitivni < negativni:
        odg = "negativnih ima vise"
    elif pozitivni == negativni:
        odg = "ima ih isto" 
    modified = str(odg)    
    print("[TCP-SERVER] The client at {},originally sent {}".format(addr,repr(msg)))
    #conn.sendall(bytes(str([pozitivni,negativni,odg]),encoding=FORMAT))
    conn.sendall(bytes(modified,encoding=FORMAT))