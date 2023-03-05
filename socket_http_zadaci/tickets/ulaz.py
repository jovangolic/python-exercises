import socket
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
while True:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    ulaz = input("Scan or enter ticket code: ")
    client.send(f"POST /checkout HTTP/1.1\r\n\r\n{ulaz}".encode(FORMAT))
    parts = client.recv(HEADER).decode(FORMAT).splitlines()
    opis = parts[0].split(" ")
    status_code = opis[1]
    if status_code != "200":
        print("invalid server response")
    else:
        body = parts[len(parts)-1]
        if body == "1":
            print("Ticket is valid..open the door")
        else:
            print("Ticket is not valid, do not open the door.")        