# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    house_url = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    xiaoqu_url = scrapy.Field()
    xiaoqu_name = scrapy.Field()
    huxing = scrapy.Field()
    position_info = scrapy.Field()
    position = scrapy.Field()
    position_url = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    crawl_time = scrapy.Field()
    # follow_info = scrapy.Field()
