# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    film_name = scrapy.Field()
    film_href = scrapy.Field()
    score = scrapy.Field()
    film_detail = scrapy.Field()
    actor_name = scrapy.Field()
    film_introduction = scrapy.Field()

