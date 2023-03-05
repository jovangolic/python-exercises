import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
with client: 
    while True:
        val = input("Enter number: ")
        if val == "":
            client.send("-".encode(FORMAT))
            print(client.recv(HEADER).decode(FORMAT))
            break
        else:
            client.send(val.encode(FORMAT))