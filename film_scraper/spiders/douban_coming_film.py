# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.spiders import Request
from film_scraper.items import DoubanComingFilmItem
from film_scraper.utils import string_util

COMING_DATE = '上映日期'
COMING_FILM_NAME = '片名'
COMING_FILM_TYPE = '类型'
COMING_FILM_REGION = '制片国家 / 地区'
COMING_FILM_WISH = '想看'


class DoubanComingFilm(Spider):
    name = 'douban_coming_film'
    start_urls = ['https://movie.douban.com/coming']
    __coming_table_header = []

    def parse(self, response):
        coming_list = response.xpath('//table[@class="coming_list"]')
        self.__coming_table_header = coming_list.xpath('.//th//text()').extract()

        coming_film = DoubanComingFilmItem()
        for table_row in coming_list.xpath('./tbody//tr'):
            film_detail_url = table_row.xpath('.//@herf').extract()
            film_info = table_row.xpath('.//text()').extract()
            film_info = list(map(str.strip, film_info))
            film_info = list(filter(string_util.is_valid_string, film_info))

            for url in film_detail_url:
                yield Request(url, callback=self.parse)

            coming_film['wish_watch_count'] = self.__row_value(film_info, COMING_FILM_WISH)
            coming_film['play_date'] = self.__row_value(film_info, COMING_DATE)
            coming_film['name'] = self.__row_value(film_info, COMING_FILM_NAME)

            yield coming_film

    def __row_value(self, table_row, row_str):
        row_index = self.__coming_table_header.index(row_str)
        if len(table_row) > row_index:
            return table_row[row_index]
