import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8005))
with client: 
    print("server said: ",client.recv(1024).decode("utf-8"))
    while True:
        msg = input('msg: ')
        client.send(bytes(msg,"utf-8"))
        print("server said: ",client.recv(1024).decode("utf-8"))