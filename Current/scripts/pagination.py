# reason - httpx is asynchronous. more modern than requests, httpx is an alternative for requests
#  import httpx
import requests
# selectolax - alternative for BeautifulSoup
# from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
  

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

print(name)