import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8007
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print("Choose object:")
client.recv(HEADER).decode(FORMAT)
selected = input("Your selection: ")
client.send(bytes(selected,FORMAT))
print(client.recv(HEADER).decode(FORMAT))