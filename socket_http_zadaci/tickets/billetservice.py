import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
while True:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    input("press enter to get a ticket code:")
    client.send(f"GET/ insert HTTP/1.1\r\n\r\n".encode(FORMAT))
    parts = client.recv(HEADER).decode(FORMAT).splitlines()
    opis = parts[0].split(" ")
    status_code = opis[1]
    if status_code != "200":
        print("invalid server response")
    else:
        ticketTocken = parts[len(parts)-1]
        print(f"your ticket code: {ticketTocken}")
    client.close()        