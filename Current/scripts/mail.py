import requests
from bs4 import BeautifulSoup  

url ="https://www.mailmodo.com/pricing/"



headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=headers)
# print(resp.text)

soup = BeautifulSoup(resp.content, "html.parser")
# print(soup.prettify())

print(soup.title.text)


