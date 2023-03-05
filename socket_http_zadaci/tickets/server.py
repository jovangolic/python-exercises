import socket,selectors,filehandler
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
def connection(sock):
    conn,addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)
def read(sock):
    response = sock.recv(HEADER).decode(FORMAT)
    parts = response.split("\r\n")
    bodyData = parts[len(parts)-1]
    opis = parts[0].split(" ")
    filename = opis[1].replace("/","")
    method = opis[0]
    code = "200 OK" 
    if not filename:
        body = "This is not a valid page"
        code = "404 not found"
    else:
        if filename == "insert":
            body = filehandler.insertticket()   
        elif filename == "checkout":
            if method.lower() != "post":
                body = "you must use post method on this page"
                code = "405 method not allowed"
            elif not bodyData:
                body = "not a valid body"
                code = "400 bad request"
            else:
                ticket_id = -1
                print(f"validating ticket {bodyData}")
                try:
                    ticket_id = int(bodyData)
                except:
                    body = "not a valid ticket code"
                    code = "400 bad request"
                if ticket_id == -1:
                    body = "not a valid ticket code"
                    code = "400 bad request"
                else:
                    body = int(filehandler.checkout(ticket_id))
        else:
            body = "not ta valid command"
            code = "400 bad request"                                   
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