import requests
r = requests.get("http://localhost:8080",params={"key":"a"})
print("request method: GET, response status_code: {}, response text: {}".format(r.status_code,r.text))
r = requests.post("http://localhost:8080",params={"key":"g","values":"G"})
print("request method: GET, response status_code: {}, response text: {}".format(r.status_code,r.text))
r = requests.delete("http://localhost:8080",params={"key":"a"})
print("request method: GET, response status_code: {}, response text: {}".format(r.status_code,r.text))
