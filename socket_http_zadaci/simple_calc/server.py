#Napraviti mrezni program za sabiranje brojeva.
#Klijent unosi dva broja, a server vraca rezultat operacije
import socket
HEADER = 64;FORMAT='utf-8';IP='localhost';PORT=8006
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
print('Server is listening....')
conn,addr = server.accept()
conn.send(b"Enter number 1: ")
num1 = int(conn.recv(HEADER).decode(FORMAT))
conn.send(b"Enter number 2: ")
num2 = int(conn.recv(HEADER).decode(FORMAT))
rez = format(num1 + num2)
conn.send(bytes(rez,FORMAT))