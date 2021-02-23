# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import json

class AssignmentPipeline:
    #def process_item(self, item, spider):
        #print("Pipeline :" +items['product_name'][0])
        #return item
    def __init__(self):
        self.create_connection()
        self.create_table()
        self.ids_seen = set()
    
    def create_connection(self):
        self.conn = sqlite3.connect('books.db')
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_DB""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS books_DB( 
            product_name text,
            product_author text,
            product_price text,
            product_imagelink text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
       
    
    def store_db(self,item):
        self.curr.execute("""insert into faculty_tb values(?,?,?,?)""",
                          (item['product_name'],
                           item['product_author'],
                           item['product_price'],
                           item['product_imagelink'][0]))
        self.conn.commit()

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
    
