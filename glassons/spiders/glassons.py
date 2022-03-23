import json
import scrapy
from ..items import GlassonsItem
from .product_type_id import get_product_type

class GlassonsSpider(scrapy.Spider):
    name = 'glassons'
    start_urls = ['https://www.glassons.com/us/c/clothing?s=SORT_RELEVANCE&p=1']

    def parse(self, response):
        pattern = r'\s+window.category\s*=\s*(\{.*?\})\s*;\s*\n'
        json_data = response.css(' main script')
        json.loads(json_data[-1].re_first(pattern))
        links = response.css('link[rel=next]::attr(href)').get()
        for item in json.loads(json_data[-1].re_first(pattern))['items']:
            it = GlassonsItem()
            it['product_name'] = item['description']
            it['product_url'] = 'https://www.glassons.com/us/p/'+item['stylecolour']['urlkey']
            it['product_price'] = item['stylecolour']['variants'][0]['gadata']['price']
            it['product_old_price'] = 0
            it['product_description'] = None
            it['product_image_list'] = [i['src'] for i in item['stylecolour']['images']]
            it['product_seller'] = 'glassons'
            it['product_gender'] = 'female' 
            it['product_video'] = None
            it['bad_product'] = 0
            it['product_gender_id'] = 1
            it['product_type_id'] = get_product_type(it['product_name'])[1]
            yield it
        yield scrapy.Request(
                    response.urljoin(links),
                    callback=self.parse
                )
