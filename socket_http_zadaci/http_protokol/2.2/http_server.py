'''Zadatak 2.2 Napraviti HTTP klijent i server skriptu gde server sadrži rečnik malih I velikih slova nazvan
slova_dict, a klijent pokušava ili da dobavi veliko slovo za dat mali karakter (GET)\
ili da doda nove vrednosti tom rečniku (POST) koristeći upitne stringove.           '''


from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import parse_qs
slova_dict = {'a':'A','b':'B','c':'C','d':'D'}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("incomig GET request")
        try:
            slovo = parse_qs(self.path[2:])["key"][0]
            self.send_response_to_client(200,slova_dict[slovo])
        except:
            self.send_response_to_client(404,"incorrect parameters")
            self.log_message("incorrect parameters")
            return
        if slovo in slova_dict:
            self.send_response_to_client(200,slova_dict[slovo])
        else:
            self.send_response_to_client(404,"name/key not found")
            self.log_message("name/key not found")    
    def do_POST(self):
        self.log_message("incoming POST request")
        data = parse_qs(self.path[2:])
        try:
            slova_dict[data["key"][0]] = data["values"][0]
            self.send_response_to_client(200,slova_dict)
        except KeyError:
            self.send_response_to_client(404,"incorrect parameters")
            self.log_message("incorrect parameters")                    
    def send_response_to_client(self,status_code,data):
        self.send_response(status_code)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(str(data).encode("utf-8"))
http_address = ("localhost",8080)
http_server = HTTPServer(http_address,RequestHandler)
http_server.serve_forever()