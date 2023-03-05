""""Zadatak 1.3 Napraviti server I client program preko UDP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server prima ovaj podatak i broji koliko ima razmaka I brojeva u stringu. 
Ovaj string server šalje nazad klijentu.
Klijent ispisuje koliko razmaka I brojeva ima string"""

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
while True:
    msg,address = server.recvfrom(HEADER)
    msg = str(msg)
    razmak,brojevi = 0,0
    povratni_str = ""
    for i in range(len(msg)):
        if msg[i].isspace():
            razmak += 1
        elif msg[i].isdigit():
            brojevi += 1  
    povratni_str = str(razmak)+" "+str(brojevi)
    print(f"[CLIENT] The client at {address}, originally sent {repr(msg)}")
    server.sendto(bytes(str(povratni_str),encoding=FORMAT),address)     