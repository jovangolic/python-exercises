'''Zadatak 1.2 Napraviti server I klijent preko UDP protokola tako da:
•	Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
•	Server prima ovaj podataka sortira string
•	Potrebno je taj promenjen string vratiti klijentu
•	Klijent ispisuju promenjen string'''


import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)      
while True:
    msg,adresa = server.recvfrom(HEADER)
    msg = str(msg)
    lista = sorted(msg)
    sortirani_str = "".join(lista)
    print ('[SERVER] The client at {}, originally sent: {}'.format(adresa, repr(msg)))
    server.sendto(bytes(str(sortirani_str),encoding=FORMAT),adresa)