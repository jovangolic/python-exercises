'''Zadatak 2.1 Napraviti HTTP klijent i server skriptu gde server sadrži rečnik imena i prezimena nazvan names_dict,\
a klijent pokušava ili da dobavi prezime za dato ime (GET) ili da doda nove vrednosti tom rečniku (POST)\
koristeći upitne stringove.'''

from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs
names_dict = {'Pera':'Peric','Mika':'Mikic','Mihajlo':'Mihajlovic','Marko':'Markovic'}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("incoming get request...")
        try:
            name = parse_qs(self.path[2:])['name'][0]
            self.send_response_to_client(200,names_dict[name])
        except:
            self.send_response_to_client(404,"Name not found")
            self.log_message("Incorrect parameters")
            return
        if name in names_dict:
            self.send_response_to_client(200,names_dict[name])
        else:
            self.send_response_to_client(404,"Name not found") 
            self.log_message("Incorrect parameters")       
    def do_POST(self):
        self.log_message("incoming post request...")
        data = parse_qs(self.path[2:])
        try:
            names_dict[data['name'][0]] = data['last_name'][0]
            self.send_response_to_client(200,names_dict)
        except KeyError:
            self.send_response_to_client(404,"incorrect parameters")
            self.log_message("incorrect parameters")    
    def send_response_to_client(self,status_code,data):
        self.send_response(status_code)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(str(data).encode("utf-8"))
server_addr = ("localhost",8080)
http_server = HTTPServer(server_addr,RequestHandler)
http_server.serve_forever()         