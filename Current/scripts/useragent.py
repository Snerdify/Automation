# this is a script that generates custom user agents for us that prevent us from getting errors 

import requests

url = 'https://httpbin.org/headers'



# method 1 to get ur headers 
'''
url = "http://google.com"
resp =  requests.get(url)
print(resp.request.headers)
'''

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept-Language":'en-GB,en;q=0.5',
    "Referer": 'https://google.com',
    "DNT":'1',
 }
resp = requests.get(url, headers=headers )

# print(resp.status_code)
# just printing the text out without passing in the headers to the resp object gives the following user-agent : "python-requests/2.32.3",
print(resp.text)

# Script to write custom agents 


