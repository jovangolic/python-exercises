import requests
r = requests.get("http://localhost:8080",params={"key":"b"})
print("request method: GET, response status_code: {}, response text: {}".format(r.status_code,r.text))
r = requests.get("http://localhost:8080",params={"key":"v"})
print("request method: GET, response status_code: {}, response text: {}".format(r.status_code,r.text))
r = requests.post("http://localhost:8080",params={"key":"e","values":"E"})
print("request method: POST, response status_code: {}, response text: {}".format(r.status_code,r.text))
r = requests.post("http://localhost:8080",params={"key":"f","values":"F"})
print("request method: POST, response status_code: {}, response text: {}".format(r.status_code,r.text))

