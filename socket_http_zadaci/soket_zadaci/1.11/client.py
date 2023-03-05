import socket,pickle
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(ADDR)
with client:
    ulaz = 12
    d = pickle.dumps(ulaz)
    client.sendto(bytes(d),ADDR)
    poruka,adresa = client.recvfrom(HEADER)
    modified = pickle.loads(poruka)
    print("[CLIENT] Response from server {}, is: {}, type of modified message is {}".format(adresa,modified,type(modified)))