import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(ADDR)
unos = 'Hello, my name is Charlie Chaplin'
client.sendto(bytes(unos,encoding=FORMAT),ADDR)
povratni_str,addr = client.recvfrom(HEADER)
print("Client response from server {}, is: {}".format(addr,str(povratni_str.decode(FORMAT))))