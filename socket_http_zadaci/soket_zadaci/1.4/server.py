'''Zadatak 1.4 Napraviti server I client program preko UDP protokola tako da:
Klijent šalje tip podatka string zadat u promenljivoj ’input_s’
Server prima ovaj podatak i broji koliko pojavljivanja karaktera ’a’  ili ’A’ se nalazi primljenom stringu
Ovaj podatak server šalje nazad klijentu.
Klijent ispisuje koliko pojavljivanja karaktera ’a’ se nalazi u poslatom stringu.
'''
import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
while True:
    msg,address = server.recvfrom(HEADER)
    msg = str(msg)
    word = 0
    for i in range(len(msg)):
        if msg[i].count('a') or msg[i].count('A'):
            word += 1
    #for i in msg:
    #    if i == "a" or i == "A":
    #        word+=1                
    print(f"[SERVER] The client at {address}, originally sent {repr(msg)}")
    server.sendto(bytes(str(word),encoding=FORMAT),address)