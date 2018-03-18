# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from film_scraper.utils.mongo_util import MongoUtil


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_util = MongoUtil(mongo_uri, mongo_db)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'))

    def open_spider(self, spider):
        self.mongo_util.setup()

    def close_spider(self, spider):
        self.mongo_util.close()

    def process_item(self, item, spider):
        self.mongo_util.upsert_item(item)
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
