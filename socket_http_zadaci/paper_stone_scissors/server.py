#Napraviti mrezni program papir,kamen, makaze. Server i klijent biraju predmet.
#Klijent salje predmet serveru, a server vraca klijentu poruku koji predmet je zamislio,
#kao i informaciju o tome ko je pobedio

import socket,random
predmeti = {1:'Paper',2:'Stone',3:'Scissors'}
izabrani = random.randint(1,3)
izabrani_predmeti = predmeti[izabrani]
print(f"I selected {izabrani_predmeti}")
HEADER = 64; FORMAT = "utf-8";IP = 'localhost';PORT = 8006
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
conn,addr = server.accept()
for i in predmeti:
    msg = f"{i} = {predmeti[i]}\n"
    conn.send(bytes(msg,FORMAT))
client_selection = int(conn.recv(HEADER))
client_selection_objects = predmeti[client_selection]
print(f"Player selected {client_selection_objects}")
conn.send(bytes(f"You selected {client_selection_objects}\n",FORMAT))
conn.send(bytes(f"I select {izabrani_predmeti}\n",FORMAT))
if client_selection == izabrani:
    conn.send(b"Nereseno\n")
    print("Nereseno")
elif client_selection-1 == izabrani or (client_selection == 1 and izabrani == 3):
    conn.send(b"I won game\n")
    print("I won game")    
else:
    conn.send(b"You won\n")
    print("You won")     