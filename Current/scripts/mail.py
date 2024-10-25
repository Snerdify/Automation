# import requests
# from bs4 import BeautifulSoup  

# url ="https://www.mailmodo.com/pricing/"



# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
# }

# resp = requests.get(url,headers=headers)
# # print(resp.text)

# soup = BeautifulSoup(resp.content, "html.parser")
# # print(soup.prettify())

# print(soup.title.text)

# selenium is a open source tool used for browser automation and testing 
# selenium imports 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize the headless chrome driver - runs in the background without opening a window 
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service , options=options)

url = "https://www.mailmodo.com/pricing/"
driver.get(url)

# wait for product grid to load 
# the grid has id - product-grid 
# and the first item in the grid has class product-item
WebDriverWait(driver , 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR , ".styles_prices__s2LRD"))
)


# after the js is rendered - print HTML 
print(driver.page_source)

driver.quit()


