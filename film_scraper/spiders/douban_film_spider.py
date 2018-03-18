# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from film_scraper.items import DoubanFilmItem
from film_scraper.utils import string_util

FILM_DIRECTOR = '导演'
FILM_WRITER = '编剧'
FILM_ACTOR = '主演'


class DoubanFilmSpider(Spider):
    name = 'douban_film_spider'
    allow_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/6390825/']

    def parse(self, response):
        self.parse_item(response)

    def parse_item(self, response):
        film_item = DoubanFilmItem()

        # film rating 评分
        rating_response = response.xpath('//div[@class="rating_self clearfix"]')
        rating = rating_response.xpath('./strong[@class="ll rating_num"]/text()').extract()
        rating_sum = rating_response.xpath('.//div[@class="rating_sum"]//text()').extract()
        rating_sum = list(filter(string_util.valid_positive_number, rating_sum))

        # film info 信息
        film_name = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item_info_response = response.xpath('//div[@class="subject clearfix"]')
        image_src = item_info_response.xpath('.//img/@src').extract()
        self.film_response_info_parse(item_info_response.xpath('.//div[@id="info"]'), film_item)

        film_item['name'] = film_name
        film_item['post_img_url'] = image_src
        film_item['rate'] = rating
        film_item['rate_sum'] = rating_sum
        film_item['detail_url'] = response.url
        film_item['id'] = response.xpath('.//a/@share-id').extract()[0]

        yield film_item

    @staticmethod
    def film_response_info_parse(response, film_item):
        for info_response in response.xpath('./span'):
            info_type = info_response.xpath('./span[@class="pl"]/text()').extract()

            if FILM_DIRECTOR in info_type:
                director = info_response.xpath('.//span[@class="attrs"]//text()').extract()
                film_item['director'] = director
            elif FILM_WRITER in info_type:
                writer = info_response.xpath('.//span[@class="attrs"]//text()').extract()
                writer = list(filter(string_util.valid_name, writer))
                film_item['writer'] = writer
            elif FILM_ACTOR in info_type:
                actor = info_response.xpath('.//span[@class="attrs"]//text()').extract()
                actor = list(filter(string_util.valid_name, actor))
                film_item['actor'] = actor
