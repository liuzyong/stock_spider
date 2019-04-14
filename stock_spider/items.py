# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StockItem(scrapy.Item):
    # define the fields for your item here like:
    names = scrapy.Field()
    code = scrapy.Field()
    today_open = scrapy.Field()
    yes_close = scrapy.Field()

    pass