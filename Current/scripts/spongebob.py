import requests 
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_SpongeBob_SquarePants_episodes"
headers ={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

url2= 'https://en.wikipedia.org/wiki/List_of_SpongeBob_SquarePants_episodes_(seasons_1%E2%80%9310)#Season_1_(1999%E2%80%932001)'

resp = requests.get(url, headers=headers)
# print(resp.text)
resp2 = requests.get(url2, headers=headers)

soup= BeautifulSoup(resp.text, "html.parser") 
soup2= BeautifulSoup(resp2.text, "html.parser")
season1_table = soup2.select_one(".wikitable.plainrowheaders.wikiepisodetable")

cell_values=[]

for row in season1_table.find_all("tr")[1:]:
    cells = row.find_all("td")
    for cell in cells:
        cell_values.append(cell.get_text())
print("; ".join(cell_values))
