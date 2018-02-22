# -*- coding: utf-8 -*-

from scrapy import cmdline

local_splash_url = 'http://localhost:8050'

name = 'douban_film_spider'
cmd = 'scrapy crawl {0} -s SPLASH_URL={1}'.format(name, local_splash_url)
cmdline.execute(cmd.split())
