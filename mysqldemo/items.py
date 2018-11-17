# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysqldemoItem(scrapy.Item):
    # define the fields for your item here like:
    mingyan = scrapy.Field()
    zuoze = scrapy.Field()
    ctime = scrapy.Field()
    uid = scrapy.Field()
    pass
