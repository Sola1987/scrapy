import scrapy

class MySpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['www.github.com']
    start_urls = ['https://github.com/china-testing/python-api-tesing/blob/master/books.md/']

    def parse(self, response):
        yield {
            'book': response.xpath('//*[@id="readme"]/article/p[7]/a')
        }