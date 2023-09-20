from typing import Any, Optional
import scrapy  
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls =["https://books.toscrape.com"]
    allowed_domains = ["books.toscrape.com"]
    
    # FOR EXCEL COLUMNS
    # cols = ["Title", "Price"]

    def __init__(self):
        super().__init__()
        self.page_count = 0

    def parse(self,response):
        print("[Our Response]")
        self.page_count += 1
        ebooks = response.css("article.product_pod")


        for ebook in ebooks:
            print("*********OUTPUT***********")
            # loader = ItemLoader(item = EbookItem())
            # loader.add_value('title', ebook.css("h3 a").attrib['title'])
            # loader.add_value('price', ebook.css("p.price_color::text").get())
            
            # # title = ebook.css("h3 a::attr(title)").get()
            
            loader = ItemLoader(item=EbookItem(), selector=ebook)
            loader.add_css('title', 'h3 a::attr(title)')
            loader.add_css('price', 'p.price_color::text')
           
            
            yield loader.load_item()
        
        print("[PAGE COUNT]:", self.page_count)

        next_btn = response.css("li.next a")
        if next_btn:
            next_page = response.urljoin(next_btn.attrib['href'])
            yield scrapy.Request( url = next_page)
       
        # print("[NEXT PAGE URL]:", self.start_urls[0] +"/" + next_btn.attrib["href"])
        

        