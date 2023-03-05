#Server bira broj od 1 do 5. Klijent unosi broj u konzoli.
#Broj se salje na server. Server odgovara da li je broj pogodjen ili ne.

import random,socket
HEADER = 64; FORMAT = 'utf-8'
IP = 'localhost';PORT = 8006
ADDR = (IP,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDR)
server.listen()
print('server is listening...\nIzaberi broj od 1 do 5')
conn,addr = server.accept()
num = random.randint(1,5)
data = int(conn.recv(HEADER).decode(FORMAT))
if data == num:
    print("Nice! I guessed that number",)
else:
    print(f"Wrong! I guessed {num} and you typed {data}")    