# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import json
import uuid

class GlassonsPipeline:
    def __init__(self):
        self.connection = mysql.connector.connect(user='saqlain', password='saqlain123',
                                        host='shopra2.cx9mmdexfpd7.us-west-1.rds.amazonaws.com',
                                        database='shopra')
        self.cursor = self.connection.cursor()
    def process_item(self, item, spider):
        rand_db_id = uuid.uuid4().hex
        values = (rand_db_id,item['product_name'],item['product_url'],item['product_price'],item['product_old_price'],item['product_description'],json.dumps(item['product_image_list']),item['product_seller'],item['product_gender'],item['product_video'],item['bad_product'],item['product_gender_id'],item['product_type_id'])
        # If Item Exist Update Values
        self.cursor.execute(f'''
                               SELECT * FROM giga_table_test 
                               WHERE product_seller = '{item['product_seller']}' 
                               AND 
                               product_url = '{item['product_url']}'
                               ''')
        val = [x for x in self.cursor]
        
        if(val != []):
            self.cursor.execute(f'''
                                UPDATE giga_table_test
                                SET product_name = '{item['product_name']}',
                                product_price = '{item['product_price']}',
                                product_old_price = '{item['product_old_price']}',
                                product_description = '{item['product_description']}',
                                product_image_list = '{item['product_image_list']}',
                                product_gender = '{item['product_gender']}',
                                product_video = '{item['product_video']}',
                                bad_product = '{item['bad_product']}',
                                product_gender_id = '{item['product_gender_id']}',
                                product_type_id = '{item['product_type_id']}',
                                WHERE product_seller = '{item['product_seller']}'
                                AND 
                                product_url = '{item['product_url']}'
                                ''')
        # Else Store Values
        else:
            sql = 'INSERT INTO giga_table_test(rand_db_id,product_name,product_url,product_price,product_old_price,product_description,product_image_list,product_seller,product_gender,product_video,bad_product,product_gender_id,product_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql,values)
            self.connection.commit()
        return item
