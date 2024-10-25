# reason - httpx is asynchronous. more modern than requests, httpx is an alternative for requests
#  import httpx
import requests
# selectolax - alternative for BeautifulSoup
# from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
import csv
import json
import time
import pandas as pd
  

url = "https://www.scrapingcourse.com/ecommerce/"

# headers to be sent with the request to the server 
headers= {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

response = requests.get(url, headers=headers)
# content attribute of the response object holds HTML data in raw bytes 
# hence response.content is much better to decode that text representation in response.text
# content also helps avoid issues in character encoding
soup = BeautifulSoup(response.content , "html.parser")

# html = HTMLParser(response.content)

# get the title text 

# products = html.css("ul#product-list li")
# print(products)

# for product in products:
#     print(html.css_first("li a.woocommerce-LoopProduct-link woocommerce-loop-product__link h2.product-name woocommerce-loop-product__title"))

#     # h2.product-name woocommerce-loop-product__title"

# print(html.title.text)

# search for "Search Products" and u will come across an input field with id : woocommerce-product-search-field-0
# select the product search element 
# find() - func enables you to select single HTML element from DOM
product_search = soup.find(id="woocommerce-product-search-field-0")
# print(product_search)
# other ways to selecting elements - find("h1") , class_= " " , soup.find(attrs ={"name":"value"})

# handling none objects 

if product_search is None:
    placehoder_string = product_search['placeholder']

# how to fetch nested elements 
# 1. select the parent element 
# 2. call bs4 search funcs on parent element 
# 3. this limits the scope to only the children of the parent element


# here the li tag which contains the product info doesnt have an id , 
# select the parent element 
product_parent = soup.find(class_="post-246")
# lets print the price of the product- 69$
price = product_parent.select_one(".price").get_text()

# print(price)

# product-name woocommerce-loop-product__title - class of name of next product

# product class here is post-1864
parent2 = soup.find(class_ = "post-1864")
name = parent2.select_one(".woocommerce-loop-product__title").get_text()

# print(name)

url2= "https://www.scrapingcourse.com/ecommerce/product/abominable-hoodie/"

resp2= requests.get(url2,headers=headers)
#print(resp2.text)

soup2 = BeautifulSoup(resp2.content , "html.parser")
# print(soup2.prettify())

# parent
additional_info = soup2.select_one(".woocommerce-Tabs-panel--additional_information")

# print(additional_info.prettify())
# find the table element from the addtional info parent 
table = additional_info.find("table")
# print(table )

for row in table.find_all('tr') :
    category= row.find('th').get_text()
    cat_value = row.find('td').get_text()
    # print(category,cat_value)

# when iterating over multiple products store the data in a dict
# products=[]

# # fetch a list of products off of the website :
# product_elements = soup.select("li.product")
# for product_element in product_elements :
#     name = product_element.find("h2").get_text()
#     price= product_element.select_one(".amount").get_text()

#     new_product = {
#     "name": name , 
#     "price ": price , 
#     }


#     products.append(new_product)

# print(products)


# HERE PAGINATION LOGIC CAN BE IMPLEMENTED - GET PRODUCT DATA FROM ALL PAGES 
# url for 2nd page is - https://www.scrapingcourse.com/ecommerce/page/2/
products=[]
for x in range(1,13):

    url3 = " https://www.scrapingcourse.com/ecommerce/page/" + str(x) +"/"
    response3 = requests.get(url3, headers=headers)
    soup = BeautifulSoup(response.content , "html.parser")
   

# fetch a list of products off of the website :
    product_elements = soup.select("li.product")
    for product_element in product_elements :
        name = product_element.find("h2").get_text()
        price= product_element.select_one(".amount").get_text()

        new_product = {
        "name": name , 
        "price ": price , 
        }


        products.append(new_product)
    print(len(products))
    time.sleep(2)

# print(products)



# create a csv to store data of all 12 pages 

df = pd.DataFrame(products)
# print(df.head())

df.to_csv('products.csv')


# this is for single page file saving
# # export info to csv
# # 1. create products_csv file
# file = open('products_csv',"w", encoding = 'utf-8' , newline="")

# # 2. initialize a writer for your file

# writer = csv.writer(file)

# # convert product element to csv 
# for product in products:
#     writer.writerow(product.values())


# file.close()

# # json logic
# json_file = open("products_json","w")

# json.dump(products, json_file)

# json_file.close()
