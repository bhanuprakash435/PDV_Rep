import scrapy
from ..items import AmazonMobileDetailsItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&page=1']
    page_number=2

    def parse(self, response):
        items = AmazonMobileDetailsItem()

        # Extracting details
        name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        ratings = response.css('.a-icon-alt').css('::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        dtype = response.css('.s-align-children-center span').css('::text').extract()

        # Passing it to items dictionary
        '''
        items['name'] = name
        items['review'] = review
        items['price'] = price
        items['dtype'] = dtype
        '''
        
        for amz in zip(name, ratings, price, dtype):
            items['name'] = amz[0].strip()
            items['ratings'] = amz[1].strip()
            items['price'] = amz[2].strip()
            items['dtype'] = amz[3].strip()
            yield items
            
        next_page='https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&page='+ str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <=10:
            AmazonSpiderSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)