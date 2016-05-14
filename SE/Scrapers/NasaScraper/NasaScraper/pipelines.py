import pymongo
from scrapy.conf import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class NasascraperPipeline(object):
    def __init__(self):
    	connection = pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

	
    def process_item(self, item, spider):
    	self.collection.insert(dict(item))
        log.msg("Question added to MongoDB database!",level=log.DEBUG, spider=nasaspider)

        return item
