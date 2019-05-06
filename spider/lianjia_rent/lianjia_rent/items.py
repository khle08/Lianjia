# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaRentItem(scrapy.Item):
    # define the fields for your item here like:
    house = scrapy.Field()
    zufang_url = scrapy.Field()
    city = scrapy.Field()
    district_multi = scrapy.Field()
    brand = scrapy.Field()
    img_url = scrapy.Field()
    price = scrapy.Field()
    post_time = scrapy.Field()
    tag = scrapy.Field()
    crawl_time = scrapy.Field()
