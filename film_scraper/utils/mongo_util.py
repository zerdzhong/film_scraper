# -*- coding:utf-8 -*-

"""
@author: zhongzhendong
@file: .py
@time: 2018/3/18 下午3:45
"""
import pymongo
from film_scraper.items import DoubanComingFilmItem
from film_scraper.items import DoubanFilmItem


class MongoUtil(object):
    film_collection_name = 'film'
    chart_collection_name = 'chart'
    coming_collection_name = 'coming_films'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.film_collection.create_index('id', unique=True)
        self.coming_collection.create_index('detail_url', unique=True)

    def setup(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self):
        self.client.close()

    @property
    def film_collection(self):
        return self.db[self.film_collection_name]

    @property
    def coming_collection(self):
        return self.db[self.coming_collection_name]

    def upsert_item(self, item):
        if isinstance(item, DoubanComingFilmItem):
            self.coming_collection.update_one({'detail_url': item['detail_url']}, {'$set': dict(item)}, True)
        elif isinstance(item, DoubanFilmItem):
            self.film_collection.update_one({'id': item['id']}, {'$set': dict(item)}, True)
