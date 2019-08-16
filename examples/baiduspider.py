import scrapy

class BaiduComSpider(scrapy.Spider):
    name = 'baidu.com'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        yield {
            'title': response.xpath('//title/text()').extract_first()
        }