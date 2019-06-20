import scrapy

class superSpider(scrapy.Spider):

    name = "superspider"
    allowed_domains = []
    start_urls = []

    def parse(self, response):
        # get next page's url and download it with scrapy
        pass