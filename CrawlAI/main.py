import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun("https://books.toscrape.com/index.html")
        print(result.markdown[:500])
        

async def screenshot():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun("https://books.toscrape.com/index.html", screenshot=True)
        

if __name__ =="__main__":
    asyncio.run(main())