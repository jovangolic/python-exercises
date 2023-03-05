import socket
HEADER = 64;FORMAT='utf-8';IP='localhost';PORT=8006
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
num1 = input(client.recv(HEADER).decode(FORMAT))
client.send(bytes(num1,FORMAT))
num2 = input(client.recv(HEADER).decode(FORMAT))
client.send(bytes(num2,FORMAT))
print('Result is: ',client.recv(HEADER).decode(FORMAT))