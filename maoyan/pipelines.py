# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient()
collections = client["film"]["maoyan"]

class MaoyanPipeline(object):
    def process_item(self, item, spider):
        item["actor_name"] =",".join([i.strip() for i in item["actor_name"]])
        item["score"] = "".join([i.strip() for i in item["score"]])
        item["film_detail"] = [i.strip() for i in item["film_detail"]]
        item["film_detail"] = [i for i in item["film_detail"] if len(i)>0]
        item = dict(item)
        collections.insert_one(item)
        print(item)
