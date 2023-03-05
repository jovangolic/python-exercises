import socket,datetime,time
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(ADDR)
with client:
    '''unos = "Hello, my name is Charlie Chaplin"
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S:%f")
    print(formatted_time)
    client.sendto(bytes(unos,encoding=FORMAT),ADDR)
    povratni_str,adresa = client.recvfrom(HEADER)
    print("[CLIENT] response from server is: {}\n".format(adresa))
    print("Izmenje string je {}".format(povratni_str))
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S:%f")
    print(formatted_time)'''
    unos = "Hello, my name is Charlie Chaplin"
    pre_slanja = time.time()
    print(pre_slanja)
    client.sendto(bytes(unos,encoding=FORMAT),ADDR)
    poruka,adresa = client.recvfrom(HEADER)
    print("[CLIENT] Response from server is {}\n".format(adresa))
    print("izmenjeni string je {}".format(poruka))
    posle_slanja = time.time()
    print(posle_slanja)