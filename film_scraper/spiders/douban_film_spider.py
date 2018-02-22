# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from film_scraper.items import DoubanMovieItem


def _valid_string(s):
    return s and s.strip()


class DoubanFilmSpider(Spider):
    name = 'douban_film_spider'
    start_urls = ['https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        movie_item = DoubanMovieItem()
        for film_item in response.xpath('//a[@class="item"]'):
            detail_url = film_item.xpath('./@href').extract()
            post_image_src = film_item.xpath('.//img[@alt]/@src').extract()
            film_name = film_item.xpath('.//p/text()').extract()
            film_name = list(filter(_valid_string, film_name))
            film_name = list(map(str.strip, film_name))

            movie_item['name'] = film_name[0]
            movie_item['post_img_url'] = post_image_src[0]
            movie_item['detail_url'] = detail_url[0]

            yield movie_item
