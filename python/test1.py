import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['10000recipe.com']
    start_urls = ['http://10000recipe.com/']

    def parse(self, response):
        pass
