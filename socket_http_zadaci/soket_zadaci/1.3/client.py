import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(ADDR)
unos = "Welcome to the 2021 year and how are you"
client.sendto(bytes(unos,encoding=FORMAT),ADDR)
povratni_str,address = client.recvfrom(HEADER)
lista = str(povratni_str).split(" ")
print(lista)
print(f"[SERVER] Response from server {address} is: \n")
print(f"Ukupno razmaka {lista[0]} i brojeva {lista[1]}")