'''Zadatak 2.3 Napraviti HTTP klijent i server skriptu gde server sadrži rečnik malih I velikih slova\
nazvan slova_dict, a klijent pokušava ili da dobavi veliko slovo za dat mali karakter (GET)\
ili da doda nove vrednosti tom rečniku (POST) koristeći upitne stringove\
ili da izbriše par koristeći (DELETE). '''
from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import parse_qs
slova_dict = {'a':'A','b':'B','c':'C', 'd':'D'}
class Requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("incoming GET request")
        try:
            slovo = parse_qs(self.path[2:])["key"][0]
            self.sesnd_response_to_client(200,slova_dict[slovo])
            return
        except:
            self.sesnd_response_to_client(404,"incorrect paramteres")
            self.log_message("incorrect parameters")
        if slovo in slova_dict:
            self.sesnd_response_to_client(200,slova_dict[slovo])
        else:
            self.sesnd_response_to_client(404,"Key not found")
            self.log_message("key not found")    
    def do_POST(self):
        self.log_message("incoming POST request")
        data = parse_qs(self.path[2:])
        try:
            slova_dict[data['key'][0]] = data["values"][0]
            self.sesnd_response_to_client(200,slova_dict)
        except KeyError:
            self.sesnd_response_to_client(404,"incorrect parameters")
            self.log_message("incorrect parameteres")    
    def do_DELETE(self):
        self.log_message("incoming DELETE request")
        try:
            slovo = parse_qs(self.path[2:])['key'][0]
        except:
            self.sesnd_response_to_client(404,"incorrect parametes")
            self.log_message("incorrect parameters")
            return
        if slovo in slova_dict.keys():
            slova_dict.pop(slovo)
            self.sesnd_response_to_client(200,slova_dict)
        else:
            self.sesnd_response_to_client(404,"not found")
            self.log_message("not found")
    def sesnd_response_to_client(self,status_code,data):
        self.send_response(status_code)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(str(data).encode("utf-8"))
http_address = ("localhost",8080)
http_server = HTTPServer(http_address,Requesthandler)
http_server.serve_forever()