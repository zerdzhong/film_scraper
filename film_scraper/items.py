# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import  Item, Field


class DoubanMovieItem(Item):
    # ID
    id = Field()
    # 名称
    name = Field()
    # 缩略图地址
    post_img_url = Field()
    # 详情地址
    detail_url = Field()
    # 评分
    rate = Field()