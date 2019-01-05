# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #car_name = scrapy.Field()
    #car_id = scrapy.Field()
    #car_text_info = scrapy.Field()
    car = scrapy.Field()
    pass

