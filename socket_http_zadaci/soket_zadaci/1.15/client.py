import socket,pickle
HEADER=1024;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR=(IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
with client:
    s="Hellooooo OOO"
    d = pickle.dumps(s)
    client.sendall(d)
    poruka = client.recv(HEADER)
    print("[CLIENT] Response from server is: {}\n".format(poruka.decode(FORMAT)))