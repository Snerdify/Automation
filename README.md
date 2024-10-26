# Automation

**Python Automation Projects**


Executing Python automation projects based on level of difficulty .

# Basic projects

## 1. **Clipboard-Automater** 
Creating a program to read , update and save the data from the clipboard directly to a 
json file . Lib used : paperclip/clipboard

## 2. **Weather-Report-Generator** 
Use the openweatherapi(https://openweathermap.org/api) to get the API key and use it to 
send request to a specific base url that fetches the current weather data for any major city in the world. Weather data will be loaded in json format which can be further manipulated to get the desired fields. 
Get the api key by creating a free account on openweatherapi.

## 3. **Email-Automater**  

## 4. **Website-Automater** :
 Helps users to store a list of urls they want automaticaly to load depending on the kind of mood they are in (ex. work or fun).
Lets user run one line of code to open a list of urls corresponding to the domains.

## 5. **Youtube Transcripts using Selenium** - 
use selenium to access the chrome browser,search for a user selected YT url, get the transcript for that url and store it in csv format. 

<sub> Level 2 Projects under the folder Current. </sub>

Under folder current -
1. Crawler is a web crawler built  using scrapy
2. Proxifing folder contains the logic for rotating proxies
3. Scripts  

            - contains python code used for static website scraping using httpx , requests , bs4 / selectolax. 

            - The script for bypassing cloudfare security is in progress and is developed using selenium

            - mail.py - script for scraping dynamic websites containing js rendered projects 





Site investigating tips:
1. Network tab : Shows network activity from the server to the browser and often contains the API endpoint for easy access
2. View Source : Check what HTTP request object is actually seeing 
3. Inspect Element : DOM and Inspect element tool show what the browser is interpreting. Useful for finding elements with the data that  we want 
4. HTML : Plain HTML might still exist is modern applications. Check for its presence , could be the best way to extract data 

Parse data locally :
Save a copy of HTML , JSON data on local harddrive - this speeds up parsing and prevents from getting blocked. This can be accomplished using the requests library. 

Use markdown files to store pseudocode 

write func and classes for scraping - keep it simple 
If the data is coming from an API endpoint , then you can skip parsing all together . 
Chromium browser - ? 
async - requests 
lib to do a lot of requests in one go - ? 

Sitemaps -> XML format(use bs4) , map of all the links in a site 

What are headers : 
present in both request and response 
additional text that is used to provide info about request that informs all parties as to how to deal with that data 

Request Headers : 
4 most popular headers and the values sent with them :
METHODS 
1. GET - python send req to server to get data  
HOST:
USER-AGENT: identifies os and versions - who has sent the request (most imp)
Accept :
Accept-Language:
Accept-Encoding :
Referer: refers to url that sent us to the site 
DNT: Do not track - if we req privacy or more personalised content or could be a setting in the browser 
Cookie: Helps to keep some data persistent throughout multiple req , like server activity , cart details and authentication details . 

2. POST- send data to the server 

HEADERS : dict in python 
(header img )

