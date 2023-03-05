import pickle,socket
HEADER = 6400;FORMAT = "utf-8";IP = "localhost";PORT = 8005;ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(ADDR)
with client:
    ulaz = {1:"a",2:"b",3:"c"}
    d = pickle.dumps(ulaz)
    client.sendto(bytes(d),ADDR)
    poruka,adresa = client.recvfrom(HEADER)
    print("[CLIENT] Response from server {} is: {}".format(adresa,poruka))