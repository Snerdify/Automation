# crawlspider - most common spider for crawling websites
# conveninet mech for following links based on certain rules
# is mostly applicable on most generic websites 
# rule is used to define rules 
from scrapy.spiders import CrawlSpider ,Rule
# linkectractor is used to extract links from the page
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name ="mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    # from the above start_urls we will extract the rules acc to rules 
    rules = (
        # extracts links matching - catalogue/category
        # crawling
        Rule(LinkExtractor(allow=(r"catalogue/category/"))),
        # scraping 
        Rule(LinkExtractor(allow=(r"catalogue",),deny=(r"category")), callback="parse_item"),
)
    
    # define what the function will do here 
    def parse_item(self,response):
        # title , price and availability
        # use yield to generate 
        




