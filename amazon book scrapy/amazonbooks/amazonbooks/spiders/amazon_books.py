import scrapy
from ..items import AmazonbooksItem


class AmazonBooksSpider(scrapy.Spider):
    name = 'amazon_books'
    page_number = 2

    start_urls = [
        'https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684820031&dc&fst=as%3Aoff&qid=1605055605&rnid=2684818031&ref=lp_976389031_nr_p_n_publication_date_1'
        ]

    def parse(self, response):
        
        items = AmazonbooksItem()
        
        book_name = response.css('.a-color-base.a-text-normal::text').extract()
        book_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        book_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        book_imagelink = response.css('.s-image::attr(src)').extract()
        
        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['book_imagelink'] = book_imagelink
        
        yield items
        
        next_page = 'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684820031&dc&page='+ str(AmazonBooksSpider.page_number)  +'&fst=as%3Aoff&qid=1605065126&rnid=2684818031&ref=sr_pg_2'
        
        
        if AmazonBooksSpider.page_number <= 3:
            yield response.follow(next_page, callback = self.parse)
            AmazonBooksSpider.page_number += 1