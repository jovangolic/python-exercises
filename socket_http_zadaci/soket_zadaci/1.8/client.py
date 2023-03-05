import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
with client:
    unos = "Devojcica Ana"
    client.sendall(bytes(unos,encoding=FORMAT))
    reply = client.recv(HEADER)
    print("[CLIENT] Response from server is: {}\n".format(reply))
    print(client.recv(HEADER).decode(FORMAT))