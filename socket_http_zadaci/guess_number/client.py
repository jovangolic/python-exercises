import socket
HEADER = 64; FORMAT = 'utf-8'
IP = 'localhost';PORT = 8006
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.send(bytes(input('Enter number: '),FORMAT))
print(client.recv(HEADER).decode(FORMAT))