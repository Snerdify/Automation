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
import random
import json


url ="https://www.mailmodo.com/pricing/"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.67 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]


def fetch_page(url):
    # Select a random user-agent from the list
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
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
                row_data.append(f"{cell_text} : Feature not available ")
            else:
                main_text = cell.get_text(strip=True)
                b_tag = cell.find('b')
                # get the b tag text 
                if b_tag and b_tag.get_text(strip=True):
                    b_text = b_tag.get_text(strip=True) 
                    if "credits" in main_text.lower():  # Check for email credits feature
                        main_text = "Email Sending Credits"
                        b_text = "4,000"
                    elif "events" in main_text.lower():  # Check for custom events feature
                        main_text = "Custom Events"
                        b_text = "20,000"
                else: 
                    ""

                if b_text:
                    main_text =  main_text.replace(b_text , "").strip()
                    row_data.append(f"{b_text} : {main_text}")
                else:
                    row_data.append(main_text) 

                
                  # Get cleaned text without surrounding whitespace
        cell_values.append(row_data)

    print(cell_values)

    json_file = open("lite_pricing_json","w")

    json.dump(cell_values, json_file)

    json_file.close()

fetch_page("https://www.mailmodo.com/pricing/")



    # after the js is rendered - print HTML 
    # print(driver.page_source)



