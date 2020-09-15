import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    # allowed_domains = ['amazon.com']
    search_item = input('Wich item are you looking for?:\n')
    search_item = search_item.replace(' ','+')
    start_urls = [
        'https://www.amazon.com/'+'s?k='+search_item
    ]
    custom_settings = {'FEED_FORMAT':'json',
                        'FEED_URI':'resultados.json',
                        'FEED_EXPORT_ENCODING': 'utf-8',
                        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                        'DEPTH_LIMIT':5
                        }
    
    def parse(self, response):    
        """
        Funcion principal para obtener los elemntos de cada página de Amazon
        """  
        # Listado item
        item_list = response.xpath('//div[@class="sg-col-inner"]//a[@class="a-link-normal a-text-normal"]/@href').getall()
        
        for item in item_list:
            yield response.follow(item, callback = self.parse_item)
        # Link siguiente pagina
        next_page = response.xpath('//div[@class="a-section a-spacing-none a-padding-base"]//li[@class="a-last"]/a/@href').get()
        if next_page is not None:# and AmazonSpiderSpider.page_number <= 10:
            yield response.follow(next_page,callback=self.parse)
         
    
    def parse_item(self, response):
        """
        Funcion que obtiene el nombre y el precio de los productos dentro de cada página
        """
        items = AmazonItem()
        product_name = response.xpath('//h1[@id="title"]/span/text()').get()
        if product_name is not None:
            product_name = product_name.strip()
        else:
            product_name = "Name Not Found"

        product_price = response.xpath('//div[@id="price"]//span[@id="priceblock_ourprice"]/text()').get()
        if product_price is not None:
            product_price = product_price
        else:
            product_price = "Price Not Found"
       
        items['product_name']={product_name, product_price} 
        yield items
