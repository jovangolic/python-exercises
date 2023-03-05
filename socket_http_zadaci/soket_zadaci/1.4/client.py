import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
with client:
    unos = "Danas je bas lep dan, zar ne?"
    client.sendto(bytes(unos,encoding=FORMAT),ADDR)
    povratni_str,address = client.recvfrom(HEADER)
    print(f"[CLIENT] Response from server {address}, is: \n")
    print("Ukupno pojavljivanje 'a' karaktera je: {}".format(povratni_str))
