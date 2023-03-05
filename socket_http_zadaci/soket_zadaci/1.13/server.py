'''Zadatak 1.13 Napraviti server I klijent preko UDP protokola tako da:
Klijent šalje listu koja ima za elemente cele brojeve
Server prima ovaj podatak I izbacuje duplikate
Potrebno je tu promenjenu listu vratiti klijentu
Klijent ispisuju promenjenu listu'''
import pickle,socket

HEADER=64;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR) 
while True:
    msg,adresa = server.recvfrom(HEADER)
    load_msg = pickle.loads(msg)
    lst = []
    for i in load_msg:
        if i not in lst:
            lst.append(i)
    print("[SERVER] The client at {}, originally sent {}".format(adresa,repr(msg)))
    server.sendto(bytes("no duplicates list is: {}".format(lst),encoding=FORMAT),adresa)  