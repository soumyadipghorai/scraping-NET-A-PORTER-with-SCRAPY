# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class CliffPipeline:

    def __init__(self) : 

        # connection
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        # creating database
        db = self.conn['ghorai']

        # collection
        self.collection = db['net-a-porter-products']

    def process_item(self, item, spider):
        
        # insert data
        self.collection.insert_one(dict(item))
        
        return item
