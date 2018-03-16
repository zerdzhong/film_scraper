# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DoubanFilmBaseItem(Item):
    # ID
    id = Field()
    # 名称
    name = Field()


class DoubanFilmItem(DoubanFilmBaseItem):
    # 导演
    director = Field()
    # 编剧
    writer = Field()
    # 演员
    actor = Field()
    # 缩略图地址
    post_img_url = Field()
    # 详情地址
    detail_url = Field()
    # 评分
    rate = Field()
    # 评分人数
    rate_sum = Field()


class DoubanComingFilmItem(DoubanFilmBaseItem):
    # 想看
    wish_watch_count = Field()
    # 上映日期
    play_date = Field()
    # 详情地址
    detail_url = Field()
