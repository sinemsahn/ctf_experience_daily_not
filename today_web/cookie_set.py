import requests

r=requests.get("site:port",cookies={"Who are youe title":"admin"})
print(r.text)
