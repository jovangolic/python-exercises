import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
unos = 'abcdefABCDEF'
client.sendto(bytes(unos,encoding=FORMAT),ADDR)
poruka,adresa = client.recvfrom(HEADER)
print ('[CLIENT] Response from server {}, is: \n'.format(adresa))
print("Izmenjen string: {}".format(poruka))
client.close()