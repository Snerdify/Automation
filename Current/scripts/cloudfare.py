from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# instance of options
options = Options()
# headless browser argument 
options.add_argument("--headless")

# initialize webdriver
driver = webdriver.Chrome(options=options)


# get the url
driver.get("https://www.datacamp.com/users/sign_in")
# wait for 15 sec for page to load 
time.sleep(20)

driver.take_screenshot("screenshot.png")

driver.close()






