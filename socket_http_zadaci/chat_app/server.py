#Potrebno je napraviti chat aplikaciju. Aplikacija ima klijentski i serverski deo.
#Aplikacija podrzava vise klijenata (ne sme biti chat 1:1)

import socket,selectors
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
server.setblocking(False)
users = {}

def broadcast(msg,sender=None):
    for user in users:
        if sender and user == sender:
            continue
        user.send(msg.encode(FORMAT))
def accept(sock):
    conn,addr = sock.accept()
    conn.setblocking(True)
    username = conn.recv(HEADER).decode(FORMAT)
    conn.setblocking(False)
    users[conn] = username
    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room",conn)
    sel.register(conn,selectors.EVENT_READ,read)
def read(sock):
    msg = sock.recv(HEADER).decode(FORMAT)
    username = users[sock]   
    print(f"User {username} say {msg}")
    if msg == "/exit":
        del users[sock]
        sock.close()
        broadcast(f"User {username} left the room")
        print(f"User {username} left")
    else:
        broadcast(f"{username}: {msg}")    
sel = selectors.DefaultSelector()
sel.register(server,selectors.EVENT_READ,accept)
print("Server is running...")
while True:
    events = sel.select()
    for key,mask in events:
        key.data(key.fileobj)