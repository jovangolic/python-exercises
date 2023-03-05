'''Zadatak 1.12 Napraviti server I klijent preko UDP protokola tako da:
Klijent šalje rečnik koji izgleda ovako  input_s = {1:'a',2:'b',3:'c'}
Server prima ovaj podatak I dodaje četvrti par, koji je 4:'d'.
Potrebno je taj promenjen rečnik vratiti klijentu
Klijent ispisuju promenjen rečnik'''


import socket,pickle
HEADER=6400;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
while True:
    msg,adresa = server.recvfrom(HEADER)
    load_msg = pickle.loads(msg)
    load_msg[4]="d"
    print(f"[SERVER] The client at {adresa}, originally sent {repr(msg)}")
    server.sendto(bytes('Server is sending back: "{}".'.format(load_msg), encoding=FORMAT), adresa)