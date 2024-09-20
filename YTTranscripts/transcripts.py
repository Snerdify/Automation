# https://www.youtube.com/watch?v=ErnWZxJovaM&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI
# script 1 - using youtube_dl
# script 2 - using selenium and pandas 
# generate using gemini and chatgpt, transformers (gen ai solution )- 
# another way - azure open and whisper model 
# automate shorts making process
# automate video making process - like a make a complete video

#Selenium supports automation of all the major browsers in the 
# market through the use of WebDriver.
import pandas as pd
import os
from time import sleep
from selenium import webdriver



#  func3 = get the transcript
# func 4= convert transcript to pdf
# func5 = convert transcript to csv

# func1 = open_url_in_chrome
# mode = headed -> Opens the browser with a visible window. 
# mode = headless -> Opens the browser without a visible window.-> runs on server
def open_url_in_chrome(url , mode ):
    if mode=='headed' :
        driver = webdriver.Chrome()
    elif mode == 'headless':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome('chromedriver.exe', options= options)
    driver.get(url)
    return driver


# func2 = accept terms and conditions
def accept_terms_and_conditions(driver):
    # step 1: click on the no thanks button 
    # doing this will click on no thanks when the user is prompted to sign in
    


 














