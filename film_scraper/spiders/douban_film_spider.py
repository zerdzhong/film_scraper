# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy_splash import SplashRequest

def _valid_string(s):
    return s and s.strip()

class DoubanFilmSpider(Spider):
    name = 'douban_film_spider'
    start_urls = ['https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0']


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for film_item in response.xpath('//a[@class="item"]'):
            post_image_src = film_item.xpath('.//img[@alt]/@src').extract()
            film_name = film_item.xpath('.//p/text()').extract()
            film_name = list(filter(_valid_string,film_name))
            film_name = list(map(str.strip,film_name))
            print(film_name,post_image_src)

    
