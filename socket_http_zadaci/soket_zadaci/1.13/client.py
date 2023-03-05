import pickle,socket
HEADER=64;FORMAT="utf-8";IP="localhost";PORT=8005;ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
client.connect(ADDR)
with client:
    lst = [1,5,6,3,4,8,0,3,2,5]
    d = pickle.dumps(lst)
    client.sendto(bytes(d),ADDR)
    poruka,adresa = client.recvfrom(HEADER)
    print("[CLIENT] response from server {} is: {}".format(adresa,poruka))