# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    vol = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    pic_url = scrapy.Field()
    current_url = scrapy.Field()