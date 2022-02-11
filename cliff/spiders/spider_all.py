from numpy import product
import scrapy
from ..items import CliffItem

# spider class
class PostsSpider(scrapy.Spider) : 

    name = 'both'

    start_urls = ['https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber='+ str(i) for i in range(1,29)] + ['https://www.net-a-porter.com/en-in/shop/shoes?pageNumber='+ str(i) for i in range(1,29)]

    # parse method 
    def parse(self, response) : 

        items = CliffItem()
 
        title = response.css('h1.Header6__title::text').extract_first() #? to match the product category 
        main_div_clothes = response.css('div.ProductGrid52')

        product_link = main_div_clothes.css('a::attr(href)').extract()
        product_div = main_div_clothes.css('div.ProductItem24__p')

        #* used i to get the link as well --> as the length of product_div and product_link should be same 
        for i in range(len(product_div)) :  
            
            product_page_url = 'https://www.net-a-porter.com' + product_link[i]
            brand = product_div[i].css('span.ProductItem24__designer::text').extract()
            name = product_div[i].css('span.ProductItem24__name::text').extract()
            original_price = product_div[i].css('div.PriceWithSchema9 span.PriceWithSchema9__value span::text').extract()
            image_url = product_div[i].css('img::attr(src)').extract()
            
            if len(image_url) == 0 : 
                image_url = product_div[i].css('img::attr(src)').extract_first()

            items['name'] = name[0]
            items['brand'] = brand[0]

            #? handles the price if there is a , in it 
            try :
                items['original_price'] = float(original_price[0][1:])
                items['sale_price'] = float(original_price[0][1:])

            except : 
                items['original_price'] = float(original_price[0][1:].replace(',', ''))
                items['sale_price'] = float(original_price[0][1:].replace(',', ''))

            #? if couldn't find image url
            try :
                items['image_url'] = 'https:' + image_url[0]
            except : 
                items['image_url'] = image_url

            items['product_page_url'] = product_page_url

            # ?to match the title with category
            if title == 'Shoes' : 
                items['product_category'] = 'footwear' 
            else : 
                items['product_category'] = 'topwear'

            yield items
