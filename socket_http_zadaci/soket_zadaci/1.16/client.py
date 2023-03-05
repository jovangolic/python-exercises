import pickle,socket
HEADER=1024; FORMAT="utf-8"; IP="localhost";PORT=8005; ADDR=(IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
with client:
    lista = [1,-4,5,2,-5,3,9,-7]
    d = pickle.dumps(lista)
    client.sendall(d)
    reply = client.recv(HEADER).decode(FORMAT)
    print("[CLIENT] Response from server is {}\n".format(reply))