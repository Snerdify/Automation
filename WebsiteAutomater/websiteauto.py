# use the webbrowser library from python to automate the process of opening a website

import webbrowser
import sys

# url = 'https://docs.python.org/'
#  Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url)
#  Open URL in new window, raising the window if possible.
# webbrowser.open_new(url)


# experimenting with different sets of urls 
URLS={
    "work":["https://www.google.com/","https://www.youtube.com/", "https://github.com/Snerdify/Automation"],
    "fun":["https://www.netflix.com/","https://www.hulu.com/","https://www.amazon.com/"],}


# create a function that can open a list of urls
# the function should take a list of urls as an argument
# it loops over these urls and opens them using webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

# calling the function to open certain types of urls from VS code 
#open_urls(URLS["fun"])

# create a function that lets user decide what type of urls to open
if __name__ == "__main__":
    set_name = sys.argv[1]
    if set_name in URLS:
        open_urls(URLS[set_name])
    else:
        print("Set not found")
    
   


   

