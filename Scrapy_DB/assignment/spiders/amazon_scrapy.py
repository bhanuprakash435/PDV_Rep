import scrapy
from ..items import AssignmentItem

class AmazonScrapySpider(scrapy.Spider):
    name = 'amazon_scrapy'
    start_urls = [
            'https://www.amazon.com/s?bbn=6960520011&rh=n%3A283155%2Cn%3A%212334088011%2Cn%3A%212334119011%2Cn%3A6960520011%2Cp_n_condition-type%3A1294423011&dc&fst=as%3Aoff&qid=1608306267&rnid=1294421011&ref=lp_6960520011_nr_p_n_condition-type_0'
            ]

    def parse(self, response):
        items = AssignmentItem()
        
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.sg-col-12-of-20 .sg-col-12-of-20 .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()
                            
        for mybooks in zip(product_name, product_author, product_price, product_imagelink):      
            items['product_name'] = mybooks[0]
            items['product_author'] = mybooks[1]
            items['product_price'] = mybooks[2]
            items['product_imagelink'] = mybooks[3]
        
        yield items
