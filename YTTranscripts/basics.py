# contains all the basic selenium code 

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# loading a website using selenium
driver.get("https://www.google.com")
# using selenium to search on google - locating elements

time.sleep(10)
driver.quit()


