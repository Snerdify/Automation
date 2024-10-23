# import asyncio
# from crawl4ai import AsyncWebCrawler
# import base64


# async def main():
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         result = await crawler.arun("https://books.toscrape.com/index.html")
#         print(result.markdown[:500])
        

# async def screenshot():
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         result = await crawler.arun("https://books.toscrape.com/index.html", screenshot=True)
#         # open the file in binary mode
#         with open("screenshot.png","wb") as file:
#             file.write(base64.b64decode(result.screenshot))
#         print("Screenshot saved as screenshot.png")



# if __name__ =="__main__":
#     asyncio.run(screenshot())

import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # We'll add our crawling code here
        pass

if __name__ == "__main__":
    asyncio.run(main())
    