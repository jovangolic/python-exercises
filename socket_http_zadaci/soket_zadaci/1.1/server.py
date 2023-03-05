#Zadatak 1.1 Napraviti server I klijent preko UDP protokola tako da:
#Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
#Server prima ovaj podataka I mala slova pretvara u velika a velika u mala, razmake u zvezdice
#Potrebno je taj promenjen string vratiti klijentu
#Klijent ispisuju promenjen string

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
while True:
    msg,addr = server.recvfrom(HEADER)
    msg = str(msg)
    string = ""
    for i in msg:
        if i.isupper():
            string += i.lower()
        elif i.islower():
            string += i.upper()
        elif i.isspace():
            string += "*"
    string = str(string)            
    print("[SERVER] the client at {}, originally sent: {}".format(addr,repr(msg)))
    server.sendto(bytes("server is sending back: {}".format(string),encoding=FORMAT),addr)
