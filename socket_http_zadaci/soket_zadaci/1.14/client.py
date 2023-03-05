import socket,pickle
HEADER=1024;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR=(IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
with client:
    dct = {'hello':"World",
        'socket':'Server',
        'received':'Data'}
    d = pickle.dumps(dct)
    client.sendall(d)