# this is a script that generates custom user agents for us that prevent us from getting errors 

import requests

resp = requests.get('http://google.com')

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# print(resp.status_code)
print(resp.request.headers)

