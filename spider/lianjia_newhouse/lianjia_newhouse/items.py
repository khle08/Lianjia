# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewhouseItem(scrapy.Item):
    loupan = scrapy.Field()
    city = scrapy.Field()
    loupan_url = scrapy.Field()
    wuye_type = scrapy.Field()
    sale_status = scrapy.Field()
    img_url = scrapy.Field()
    location = scrapy.Field()
    huxing = scrapy.Field()
    area = scrapy.Field()
    main_price = scrapy.Field()
    main_price_desc = scrapy.Field()
    second_price = scrapy.Field()
    tag = scrapy.Field()
    crawl_time = scrapy.Field()
