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

url = "https://www.scrapingcourse.com/javascript-rendering"
driver.get(url)

# wait for product grid to load 
# the grid has id - product-grid 
# and the first item in the grid has class product-item
WebDriverWait(driver , 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR , "#product-grid .product-item"))
)


# after the js is rendered - print HTML 
print(driver.page_source)



# CSS SELECTOR STRATEGY 

driver.quit()