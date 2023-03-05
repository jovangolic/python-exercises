'''Zadatak 1.10 Napraviti server I client program preko UDP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server prima ovaj podatak I vraća string sa svim velikim slovima. 
Ovaj podatak server šalje nazad klijentu.
Klijent ispisuje promenjen string
Na ekranu se ispisuje vreme pre slanja poruke serveru I vreme posle stizanja odgovora sa servera.\
Koristiti neku od biblioteka za vreme'''

import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
with server:
    print("[SERVER] is listening ... {}".format(server.getsockname()))
    while True:
        msg,adresa = server.recvfrom(HEADER)
        msg = str(msg)
        odg = ""
        for i in msg:
            if i.islower():
                odg += i.upper()

        print(f"[SERVER] The client at {adresa},originally sent {repr(msg)}")
        server.sendto(bytes(str(odg),encoding=FORMAT),adresa)    