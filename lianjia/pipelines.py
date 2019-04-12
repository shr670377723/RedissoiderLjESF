# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class LianjiaPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.lianjia = self.client.plianjia.shujv
    def process_item(self, item, spider):
        # print(type(item))
        self.lianjia.insert(dict(item))
        return item
    def close_spider(self,spider):
        self.client.close()
