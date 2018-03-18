# -*- coding: utf-8 -*-

from scrapy import cmdline
import os

local_splash_url = 'http://localhost:8050'
local_mongo_url = 'mongodb://localhost:27017'

if __name__ == '__main__':
    docker_cmd = 'docker container start film_scraper_mongodb'
    os.system(docker_cmd)

    name = 'douban_coming_film'
    cmd = 'scrapy crawl {0} -s MONGO_URI={1} '.format(name, local_mongo_url)
    cmdline.execute(cmd.split())
