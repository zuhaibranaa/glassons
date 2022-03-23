# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassonsItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_url = scrapy.Field()
    product_price = scrapy.Field()
    product_old_price = scrapy.Field()
    product_description = scrapy.Field()
    product_image_list = scrapy.Field()
    product_seller = scrapy.Field()
    product_gender = scrapy.Field()
    product_video = scrapy.Field()
    bad_product = scrapy.Field()
    product_gender_id = scrapy.Field()
    product_type_id = scrapy.Field()
    pass
