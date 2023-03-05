#Kreirati jednostavan http server koji procesira zahtev tako sto klijentu u odgovoru vraca naziv trazenog 
#fajla (ne fajl, nego samo naziv). Testirati server pomocu web pregledaca

import socket,selectors
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)

def connection(sock):
    conn,addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)
def read(sock):
    zahtev = sock.recv(HEADER).decode(FORMAT)
    parts = zahtev.split("\r\n")
    opis = parts[0].split(" ")
    file_name = opis[1].replace("/","")
    code = "200 OK"    
    if not file_name:
        body = "this page is not valid"
        code = "404 Not Found"
    else:
        body = file_name
    protocol = "HTTP/1.1"
    sock.send(f"{protocol} {code}\r\nContent-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode(FORMAT))
    sock.close()
    sel.unregister(sock)        
sel = selectors.DefaultSelector()
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,connection)

while True:
    events = sel.select()
    for key,mask in events:
        key.data(key.fileobj)