# selenium is a open source tool used for browser automation and testing 
# selenium imports 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# initialize the headless chrome driver - runs in the background without opening a window 
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service , options=options)


url = "https://www.scrapingcourse.com/javascript-rendering"
driver.get(url)

# wait for product grid to load 
# the grid has id - product-grid 
# and the first item in the grid has class product-item
WebDriverWait(driver , 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR , "#product-grid .product-item"))
)


# after the js is rendered - print HTML 
html = driver.page_source

soup = BeautifulSoup(html ,"html.parser")
# print(html)
# print(soup.title.text)
# note - get_text() - only works on find() and doesnt work on find_all()
product_list = []
products  = soup.find_all('div', class_='product-item')

for product in products:
    name  = product.select_one('span', class_= 'product-name').get_text()
    price = product.select_one('span', class_ ='product-price').get_text()

    new_product = {
        'name' : name  ,
        'price' : price ,

    }
    product_list.append(new_product)

print(product_list)




# CSS SELECTOR STRATEGY 
driver.quit()