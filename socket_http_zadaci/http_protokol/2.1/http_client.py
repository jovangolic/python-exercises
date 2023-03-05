import requests 
r = requests.get("http://localhost:8080",params={"name":"Pera"})
print("response method: GET, response stats_code: {}, response data: {}".format(r.status_code,r.text))    
r = requests.post("http://localhost:8080",params={"name":"Perica","last_name":"Nikolic"})
print("response method: POST, response status_code: {}, response data: {}".format(r.status_code,r.text)) 