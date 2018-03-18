# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.exceptions import DropItem
from film_scraper.items import DoubanComingFilmItem
from film_scraper.items import DoubanFilmItem


class MongoPipeline(object):
    film_collection_name = 'film'
    chart_collection_name = 'chart'
    coming_collection_name = 'coming_films'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.film_collection_name].create_index('id', unique=True)
        self.db[self.coming_collection_name].create_index('detail_url', unique=True)
        self.saved_films = set()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, DoubanComingFilmItem):
            self.db[self.coming_collection_name].update_one({'detail_url': item['detail_url']}, {'$set': dict(item)}, True)
        elif isinstance(item, DoubanFilmItem):
            if item['id'] in self.saved_films:
                raise DropItem("Duplicate item found: %s" % item) 
            else:
                self.saved_films.add(item['id'])
                self.db[self.film_collection_name].update_one({'id': item['id']}, {'$set': dict(item)}, True)
                return item
