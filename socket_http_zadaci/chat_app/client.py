import socket,sys,threading
HEADER = 64;FORMAT = "utf-8";IP = "localhost";PORT = 8005
ADDR = (IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
class Listener(threading.Thread):
    username = ""
    def __init__(self,username):
        super().__init__()
        self.username = username
    def run(self):
        client.connect(ADDR)
        client.send(self.username.encode(FORMAT))
        while True:
            res = client.recv(HEADER).decode(FORMAT)
            if res != "":
                print(res)
username = input("Enter username: ")
chat = Listener(username)
chat.daemon = True
chat.start()
while True:
    print("Enter message: ")
    msg = input()
    client.send(msg.encode(FORMAT))
    if msg == "/exit":
        print("bye")
        sys.exit()
        #break                    