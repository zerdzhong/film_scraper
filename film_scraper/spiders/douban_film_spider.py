# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
import logging

class DoubanFilmSpider(Spider):
    name = 'douban_film_spider'
    start_urls = ['https://movie.douban.com']

    def parse(self, response):
        titles = response.xpath('//a[@class="item"]')
        for title in titles:
            print(title.strip())

    
