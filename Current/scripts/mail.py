import requests
from bs4 import BeautifulSoup 
# selenium is a open source tool used for browser automation and testing 
# selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time 

url ="https://www.mailmodo.com/pricing/"
headers = {
     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
     
}
time.sleep(3)
resp = requests.get(url,headers=headers)
time.sleep(2)
soup = BeautifulSoup(resp.content, "html.parser")

# initialize the headless chrome driver - runs in the background without opening a window 
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service , options=options)
# here i commented out the driver as it was getting blocked by the website 
# driver.get(url)
# # wait for product grid to load 
# the grid has id - product-grid 
# and the first item in the grid has class product-item
# WebDriverWait(driver , 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR , ".styles_prices__s2LRD"))
# )


pricing_data =  soup.find('div' , class_ = "features_component__SE_Xi").get_text()
# print(pricing_data)


lite_plan = soup.find('div' , class_= "styles_pricecard__QJVmR").get_text()
# print(lite_plan)


# cell_values = []
# table = soup.find('table')
# for column in table.find_all('tr'):
#     column_data = []
#     for cell in column.find_all('td'):
#         icon = cell.find('img')
#         if icon:
#             icon.decompose()
#             # column_data.append("- Feature not available")
#         column_data.append(cell.get_text(strip=True))

#     cell_values.append(column_data)
#     time.sleep(2)
# print(cell_values)
cell_values = []
table = soup.find('table')
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        icon = cell.find('img')  # Update with the actual icon tag if different
        if icon:
            icon.decompose()  # Remove only the icon
            cell_text = cell.get_text(strip=True)  # Retain text after the icon
            row_data.append(f"- Feature not available: {cell_text}")
        else:
            row_data.append(cell.get_text(strip=True))  # Get cleaned text without surrounding whitespace
    cell_values.append(row_data)


# after the js is rendered - print HTML 
# print(driver.page_source)

driver.quit()


