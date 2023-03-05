'''Zadatak 1.11 Napraviti server I klijent preko UDP protokola tako da:
Klijent šalje tip podatka int zadat u promenljivoj ’input_s’
Server prima ovaj podatak I umnožava ga.
Potrebno je taj promenjen objekat vratiti klijentu
Klijent ispisuju promenjen objekat'''

import socket,pickle
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR) 
while True:
    msg,adresa = server.recvfrom(HEADER)
    load_msg = pickle.loads(msg)
    load_msg *= load_msg
    dump_msg = pickle.dumps(load_msg)
    print(f"[SERVER] The client at {adresa}, originally sent {repr(msg)}")
    server.sendto(bytes(dump_msg),adresa)  